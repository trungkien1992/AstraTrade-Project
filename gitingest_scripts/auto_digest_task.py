#!/usr/bin/env python3
"""
Auto Task Digest Generator for Claude Code

This script automatically generates a digest of code changes after each Claude Code task.
It's designed to be called by Claude Code hooks to provide automatic documentation
of what was changed, added, or removed during each development session.

Features:
- Detects files modified in the last task session
- Generates concise change summaries
- Creates timestamped digest files
- Integrates with git for accurate change tracking
- Minimal performance impact
"""

import os
import sys
import json
import subprocess
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Optional
import hashlib


class AutoDigestGenerator:
    """Generates automatic task completion digests for Claude Code."""
    
    def __init__(self, repo_path: str = None):
        # Auto-detect if we're in AstraTrade project
        current_path = Path.cwd()
        if repo_path:
            self.repo_path = Path(repo_path).resolve()
        elif 'AstraTrade-Project' in str(current_path):
            # Navigate to project root
            self.repo_path = current_path
            while self.repo_path.name != 'AstraTrade-Project' and self.repo_path.parent != self.repo_path:
                self.repo_path = self.repo_path.parent
        else:
            self.repo_path = current_path
        
        self.digest_dir = self.repo_path / '.claude_digests'
        self.digest_dir.mkdir(exist_ok=True)
        
        # Task session window (look for changes in last 30 minutes)
        self.task_window_minutes = 30
        
    def get_recent_changes(self) -> Dict[str, List[str]]:
        """Get files that were recently changed, categorized by change type."""
        changes = {
            'modified': [],
            'added': [],
            'deleted': []
        }
        
        try:
            # Get recent changes using git
            since_time = datetime.now() - timedelta(minutes=self.task_window_minutes)
            since_str = since_time.strftime("%Y-%m-%d %H:%M:%S")
            
            # Get file changes with status
            result = subprocess.run([
                'git', 'log', 
                f'--since={since_str}',
                '--name-status',
                '--pretty=format:',
                '--no-merges'
            ], cwd=self.repo_path, capture_output=True, text=True, check=True)
            
            # Parse git output
            for line in result.stdout.strip().split('\n'):
                if not line.strip():
                    continue
                    
                parts = line.strip().split('\t')
                if len(parts) >= 2:
                    status, filepath = parts[0], parts[1]
                    
                    # Filter to important files only
                    if self._is_important_file(filepath):
                        if status == 'A':
                            changes['added'].append(filepath)
                        elif status == 'M':
                            changes['modified'].append(filepath)
                        elif status == 'D':
                            changes['deleted'].append(filepath)
            
            # Remove duplicates while preserving order
            for category in changes:
                changes[category] = list(dict.fromkeys(changes[category]))
                
        except subprocess.CalledProcessError:
            # Fallback to filesystem timestamps if git fails
            changes = self._get_changes_by_mtime()
        
        return changes
    
    def _get_changes_by_mtime(self) -> Dict[str, List[str]]:
        """Fallback method using file modification times."""
        changes = {'modified': [], 'added': [], 'deleted': []}
        
        cutoff_time = datetime.now() - timedelta(minutes=self.task_window_minutes)
        
        # Check important directories
        for pattern in ['lib/**/*.dart', 'test/**/*.dart', '*.md', '*.yaml', '*.yml']:
            for file_path in self.repo_path.glob(pattern):
                if file_path.is_file():
                    mtime = datetime.fromtimestamp(file_path.stat().st_mtime)
                    if mtime > cutoff_time:
                        rel_path = file_path.relative_to(self.repo_path)
                        changes['modified'].append(str(rel_path))
        
        return changes
    
    def _is_important_file(self, filepath: str) -> bool:
        """Check if a file is important enough to include in digest."""
        path = Path(filepath)
        
        # Skip build and generated files
        skip_patterns = [
            '.dart_tool/', 'build/', '.git/', 'node_modules/',
            '.g.dart', '.freezed.dart', '.mocks.dart'
        ]
        
        for pattern in skip_patterns:
            if pattern in str(path):
                return False
        
        # Include important file types
        important_extensions = {'.dart', '.py', '.md', '.yaml', '.yml', '.json', '.sh'}
        important_files = {'Dockerfile', 'Makefile', 'pubspec.lock'}
        
        return (path.suffix in important_extensions or 
                path.name in important_files)
    
    def get_change_summary(self, changes: Dict[str, List[str]]) -> Dict[str, any]:
        """Generate a summary of changes with statistics."""
        total_files = sum(len(files) for files in changes.values())
        
        if total_files == 0:
            return {
                'total_files': 0,
                'summary': 'No significant changes detected in the last task.',
                'changes': changes
            }
        
        # Categorize by file type
        file_types = {}
        for category, files in changes.items():
            for filepath in files:
                ext = Path(filepath).suffix or 'config'
                if ext not in file_types:
                    file_types[ext] = {'modified': 0, 'added': 0, 'deleted': 0}
                file_types[ext][category] += 1
        
        # Generate summary text
        summary_parts = []
        if changes['added']:
            summary_parts.append(f"{len(changes['added'])} files added")
        if changes['modified']:
            summary_parts.append(f"{len(changes['modified'])} files modified")
        if changes['deleted']:
            summary_parts.append(f"{len(changes['deleted'])} files deleted")
        
        summary = f"Task completed: {', '.join(summary_parts)}"
        
        return {
            'total_files': total_files,
            'summary': summary,
            'file_types': file_types,
            'changes': changes,
            'primary_language': self._get_primary_language(changes)
        }
    
    def _get_primary_language(self, changes: Dict[str, List[str]]) -> str:
        """Determine the primary language of changes."""
        all_files = []
        for files in changes.values():
            all_files.extend(files)
        
        if any(f.endswith('.dart') for f in all_files):
            return 'Dart/Flutter'
        elif any(f.endswith('.py') for f in all_files):
            return 'Python'
        elif any(f.endswith('.md') for f in all_files):
            return 'Documentation'
        else:
            return 'Configuration'
    
    def generate_digest(self) -> Optional[str]:
        """Generate the complete task digest."""
        timestamp = datetime.now()
        
        # Get recent changes
        changes = self.get_recent_changes()
        summary = self.get_change_summary(changes)
        
        # Skip if no changes
        if summary['total_files'] == 0:
            return None
        
        # Create digest content
        digest = {
            'metadata': {
                'timestamp': timestamp.isoformat(),
                'session_id': self._generate_session_id(timestamp),
                'repo_path': str(self.repo_path),
                'claude_code_version': self._get_claude_version()
            },
            'summary': summary['summary'],
            'statistics': {
                'total_files_changed': summary['total_files'],
                'primary_language': summary['primary_language'],
                'file_types': summary['file_types']
            },
            'changes': changes,
            'files_detail': self._get_file_details(changes)
        }
        
        # Save digest
        digest_filename = f"task_digest_{timestamp.strftime('%Y%m%d_%H%M%S')}.json"
        digest_path = self.digest_dir / digest_filename
        
        try:
            with open(digest_path, 'w', encoding='utf-8') as f:
                json.dump(digest, f, indent=2, ensure_ascii=False)
            
            # Also create a human-readable summary
            self._create_readable_summary(digest, digest_path.with_suffix('.md'))
            
            return str(digest_path)
            
        except Exception as e:
            print(f"Error saving digest: {e}", file=sys.stderr)
            return None
    
    def _get_file_details(self, changes: Dict[str, List[str]]) -> Dict[str, Dict]:
        """Get detailed information about changed files."""
        details = {}
        
        for category, files in changes.items():
            for filepath in files:
                full_path = self.repo_path / filepath
                
                file_info = {
                    'category': category,
                    'size_bytes': 0,
                    'lines': 0
                }
                
                if full_path.exists() and category != 'deleted':
                    try:
                        with open(full_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                            file_info['size_bytes'] = len(content.encode('utf-8'))
                            file_info['lines'] = len(content.splitlines())
                    except Exception:
                        pass  # Skip files we can't read
                
                details[filepath] = file_info
        
        return details
    
    def _create_readable_summary(self, digest: Dict, output_path: Path):
        """Create a human-readable markdown summary."""
        content = [
            f"# 🤖 Claude Code Task Digest",
            f"**Generated**: {digest['metadata']['timestamp']}",
            f"**Session**: {digest['metadata']['session_id']}",
            "",
            f"## 📋 Summary",
            digest['summary'],
            "",
            f"**Primary Language**: {digest['statistics']['primary_language']}",
            f"**Total Files**: {digest['statistics']['total_files_changed']}",
            ""
        ]
        
        # File type breakdown
        if digest['statistics']['file_types']:
            content.extend([
                "## 📊 File Types",
                ""
            ])
            
            for ext, counts in digest['statistics']['file_types'].items():
                total = counts['added'] + counts['modified'] + counts['deleted']
                content.append(f"- **{ext}**: {total} files")
                details = []
                if counts['added']: details.append(f"{counts['added']} added")
                if counts['modified']: details.append(f"{counts['modified']} modified") 
                if counts['deleted']: details.append(f"{counts['deleted']} deleted")
                if details:
                    content.append(f"  - {', '.join(details)}")
            content.append("")
        
        # Changed files list
        for category, files in digest['changes'].items():
            if files:
                icon = {'added': '➕', 'modified': '📝', 'deleted': '🗑️'}[category]
                content.extend([
                    f"## {icon} {category.title()} Files",
                    ""
                ])
                
                for filepath in files:
                    content.append(f"- `{filepath}`")
                    
                    # Add file details if available
                    if filepath in digest['files_detail']:
                        detail = digest['files_detail'][filepath]
                        if detail['lines'] > 0:
                            content.append(f"  - {detail['lines']} lines, {detail['size_bytes']} bytes")
                
                content.append("")
        
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(content))
        except Exception:
            pass  # Fail silently for readable summary
    
    def _generate_session_id(self, timestamp: datetime) -> str:
        """Generate a unique session ID."""
        session_data = f"{timestamp.strftime('%Y%m%d_%H%M')}{self.repo_path.name}"
        return hashlib.md5(session_data.encode()).hexdigest()[:8]
    
    def _get_claude_version(self) -> str:
        """Try to get Claude Code version."""
        try:
            result = subprocess.run(['claude', '--version'], 
                                  capture_output=True, text=True, timeout=3)
            return result.stdout.strip() if result.returncode == 0 else 'unknown'
        except:
            return 'unknown'
    
    def cleanup_old_digests(self, keep_days: int = 7):
        """Clean up digest files older than specified days."""
        cutoff_time = datetime.now() - timedelta(days=keep_days)
        
        for digest_file in self.digest_dir.glob('task_digest_*.json'):
            try:
                if datetime.fromtimestamp(digest_file.stat().st_mtime) < cutoff_time:
                    digest_file.unlink()
                    # Also remove corresponding .md file
                    md_file = digest_file.with_suffix('.md')
                    if md_file.exists():
                        md_file.unlink()
            except Exception:
                continue  # Skip files we can't process


def main():
    """Main function for CLI usage."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate automatic task digest for Claude Code')
    parser.add_argument('--repo-path', help='Repository path (auto-detected if not provided)')
    parser.add_argument('--window', type=int, default=30, help='Time window in minutes (default: 30)')
    parser.add_argument('--cleanup', type=int, help='Clean up digests older than N days')
    parser.add_argument('--quiet', action='store_true', help='Suppress output')
    
    args = parser.parse_args()
    
    generator = AutoDigestGenerator(args.repo_path)
    generator.task_window_minutes = args.window
    
    if args.cleanup:
        generator.cleanup_old_digests(args.cleanup)
        if not args.quiet:
            print(f"Cleaned up digests older than {args.cleanup} days")
        return 0
    
    # Generate digest
    digest_path = generator.generate_digest()
    
    if digest_path:
        if not args.quiet:
            print(f"✅ Task digest generated: {digest_path}")
        return 0
    else:
        if not args.quiet:
            print("ℹ️  No significant changes detected - no digest generated")
        return 0


if __name__ == '__main__':
    sys.exit(main())