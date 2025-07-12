#!/usr/bin/env python3
"""
Session Code Review Script

A focused script to quickly generate code review materials for the current
working session. This script identifies and processes only the most recently
modified files, perfect for immediate code review or session summaries.

Usage:
    python run_session_review.py

This script will:
1. Find files modified in the last 2 hours (current session)
2. Focus on Dart/Flutter files and configuration files
3. Generate a clean, readable markdown report
4. Include file statistics and modification details
"""

import os
import subprocess
import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict


class SessionReviewGenerator:
    """Generates code review for current working session."""
    
    def __init__(self):
        self.repo_path = Path('.').resolve()
        self.session_hours = 2  # Look at last 2 hours for current session
        
    def get_recent_files(self) -> List[str]:
        """Get files modified in the current session."""
        try:
            # Get files modified in the last 2 hours
            since_time = datetime.now() - timedelta(hours=self.session_hours)
            since_str = since_time.strftime("%Y-%m-%d %H:%M:%S")
            
            result = subprocess.run([
                "git", "log", 
                f"--since={since_str}",
                "--name-only", 
                "--pretty=format:",
                "--diff-filter=AM"
            ], capture_output=True, text=True, check=True)
            
            files = [f.strip() for f in result.stdout.split('\n') if f.strip()]
            return list(dict.fromkeys(files))  # Remove duplicates
            
        except subprocess.CalledProcessError:
            # Fallback to filesystem timestamps
            return self._get_files_by_mtime()
    
    def _get_files_by_mtime(self) -> List[str]:
        """Fallback: get files by modification time."""
        cutoff_time = datetime.now() - timedelta(hours=self.session_hours)
        modified_files = []
        
        # Focus on main directories
        for pattern in ['lib/**/*', 'test/**/*', '*.md', '*.yaml', '*.yml']:
            for file_path in self.repo_path.glob(pattern):
                if file_path.is_file():
                    mtime = datetime.fromtimestamp(file_path.stat().st_mtime)
                    if mtime > cutoff_time:
                        rel_path = file_path.relative_to(self.repo_path)
                        modified_files.append(str(rel_path))
        
        return modified_files
    
    def filter_important_files(self, files: List[str]) -> List[str]:
        """Filter to most important files for review."""
        priority_patterns = [
            'lib/**/*.dart',      # Main Dart code
            'test/**/*.dart',     # Tests
            '*.md',               # Documentation
            'pubspec.yaml',       # Flutter config
            'analysis_options.yaml'  # Linting config
        ]
        
        filtered = []
        for file_path in files:
            path = Path(file_path)
            
            # Skip build and generated files
            if any(part in str(path) for part in ['.dart_tool', 'build/', '.g.dart']):
                continue
            
            # Include Dart files, docs, and configs
            if (path.suffix == '.dart' or 
                path.suffix == '.md' or
                path.name in ['pubspec.yaml', 'pubspec.lock', 'analysis_options.yaml']):
                filtered.append(file_path)
        
        return filtered
    
    def get_file_info(self, file_path: str) -> Dict:
        """Get concise file information."""
        full_path = self.repo_path / file_path
        if not full_path.exists():
            return {}
        
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            lines = content.splitlines()
            
            return {
                'lines': len(lines),
                'size_kb': round(len(content.encode('utf-8')) / 1024, 1),
                'modified': datetime.fromtimestamp(full_path.stat().st_mtime).strftime('%H:%M:%S')
            }
        except Exception:
            return {}
    
    def get_git_changes(self, file_path: str) -> str:
        """Get brief git change summary."""
        try:
            result = subprocess.run([
                "git", "diff", "HEAD~1", "HEAD", "--numstat", file_path
            ], capture_output=True, text=True)
            
            if result.stdout.strip():
                parts = result.stdout.strip().split('\t')
                if len(parts) >= 2:
                    added, removed = parts[0], parts[1]
                    return f"+{added}/-{removed}"
            
            return "new file"
        except subprocess.CalledProcessError:
            return "modified"
    
    def read_file_safely(self, file_path: str) -> str:
        """Read file content with error handling."""
        full_path = self.repo_path / file_path
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            return f"[Error reading file: {e}]"
    
    def generate_session_review(self, files: List[str]) -> str:
        """Generate a focused session review."""
        
        # Header
        output = [
            "# 🔍 Current Session Code Review",
            f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"**Session Period**: Last {self.session_hours} hours",
            f"**Files Modified**: {len(files)}",
            ""
        ]
        
        if not files:
            output.extend([
                "## ✅ No Recent Changes",
                "No files have been modified in the current session.",
                ""
            ])
            return '\n'.join(output)
        
        # Quick Summary
        output.extend([
            "## 📊 Session Summary",
            ""
        ])
        
        total_lines = 0
        dart_files = 0
        test_files = 0
        
        for file_path in files:
            info = self.get_file_info(file_path)
            if 'lines' in info:
                total_lines += info['lines']
            
            if file_path.endswith('.dart'):
                if 'test/' in file_path:
                    test_files += 1
                else:
                    dart_files += 1
        
        output.extend([
            f"- **Dart source files**: {dart_files}",
            f"- **Test files**: {test_files}",
            f"- **Total lines modified**: ~{total_lines}",
            ""
        ])
        
        # File Changes Overview
        output.extend([
            "## 🔄 Modified Files",
            ""
        ])
        
        for file_path in files:
            info = self.get_file_info(file_path)
            changes = self.get_git_changes(file_path)
            
            # File icon based on type
            if file_path.endswith('.dart'):
                icon = "🎯" if 'test/' in file_path else "⚡"
            elif file_path.endswith('.md'):
                icon = "📝"
            else:
                icon = "⚙️"
            
            output.append(f"### {icon} `{file_path}`")
            
            if info:
                output.append(f"- **Lines**: {info['lines']} | **Size**: {info['size_kb']} KB | **Modified**: {info['modified']}")
            
            output.append(f"- **Changes**: {changes}")
            output.append("")
        
        # Full File Contents
        output.extend([
            "---",
            "",
            "## 📄 File Contents",
            ""
        ])
        
        for file_path in files:
            output.append(f"### File: `{file_path}`")
            output.append("")
            
            content = self.read_file_safely(file_path)
            
            # Syntax highlighting
            if file_path.endswith('.dart'):
                lang = 'dart'
            elif file_path.endswith('.md'):
                lang = 'markdown'
            elif file_path.endswith(('.yaml', '.yml')):
                lang = 'yaml'
            else:
                lang = ''
            
            output.append(f"```{lang}")
            output.append(content)
            output.append("```")
            output.append("")
            output.append("---")
            output.append("")
        
        return '\n'.join(output)


def main():
    """Main function to generate session review."""
    print("🔍 Generating current session code review...")
    
    generator = SessionReviewGenerator()
    
    # Get recent files
    files = generator.get_recent_files()
    print(f"Found {len(files)} recently modified files")
    
    # Filter to important files
    files = generator.filter_important_files(files)
    print(f"Filtered to {len(files)} important files for review")
    
    if files:
        for f in files:
            print(f"  - {f}")
    
    # Generate review
    review_content = generator.generate_session_review(files)
    
    # Save to file
    output_file = "session_review.md"
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(review_content)
        
        print(f"\n✅ Session review generated: {output_file}")
        print(f"📏 Review size: {len(review_content.encode('utf-8'))} bytes")
        
    except Exception as e:
        print(f"❌ Error saving review: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())