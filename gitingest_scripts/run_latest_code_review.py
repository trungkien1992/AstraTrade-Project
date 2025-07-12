#!/usr/bin/env python3
"""
Latest Code Review Digest Script

This script generates a focused code review digest containing only the files 
that have been modified in the current working session or since a specified time.
It's designed for efficient code review by highlighting recent changes.

Usage:
    python run_latest_code_review.py [options]
    
Options:
    --since HOURS    Only include files modified in the last N hours (default: 24)
    --staged         Only include staged files for commit
    --branch BRANCH  Compare against specific branch (default: main)
    --output FILE    Output file name (default: latest_code_review.md)
    --format FORMAT  Output format: markdown, txt, or json (default: markdown)
"""

import os
import sys
import argparse
import subprocess
import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Set, Tuple
import hashlib

# Add the parent directory to the path to import gitingest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from gitingest import ingest
    GITINGEST_AVAILABLE = True
except ImportError:
    GITINGEST_AVAILABLE = False
    print("Warning: gitingest not available. Using basic file reading instead.")


class LatestCodeReviewDigester:
    """Generates focused code review digests for recently modified files."""
    
    def __init__(self, repo_path: str = "."):
        self.repo_path = Path(repo_path).resolve()
        self.git_available = self._check_git_availability()
        
    def _check_git_availability(self) -> bool:
        """Check if git is available and we're in a git repository."""
        try:
            result = subprocess.run(
                ["git", "rev-parse", "--git-dir"],
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                check=True
            )
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False
    
    def get_recently_modified_files(self, since_hours: int = 24) -> List[str]:
        """Get list of files modified in the last N hours."""
        if not self.git_available:
            return self._get_files_by_mtime(since_hours)
        
        try:
            # Get files modified since N hours ago
            since_time = datetime.now() - timedelta(hours=since_hours)
            since_str = since_time.strftime("%Y-%m-%d %H:%M:%S")
            
            cmd = [
                "git", "log", 
                f"--since={since_str}",
                "--name-only", 
                "--pretty=format:", 
                "--diff-filter=AM"  # Added or Modified files only
            ]
            
            result = subprocess.run(
                cmd,
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                check=True
            )
            
            files = [f.strip() for f in result.stdout.split('\n') if f.strip()]
            # Remove duplicates while preserving order
            return list(dict.fromkeys(files))
            
        except subprocess.CalledProcessError:
            print("Warning: Failed to get git log. Falling back to filesystem timestamps.")
            return self._get_files_by_mtime(since_hours)
    
    def get_staged_files(self) -> List[str]:
        """Get list of staged files ready for commit."""
        if not self.git_available:
            return []
        
        try:
            result = subprocess.run(
                ["git", "diff", "--cached", "--name-only"],
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                check=True
            )
            return [f.strip() for f in result.stdout.split('\n') if f.strip()]
        except subprocess.CalledProcessError:
            return []
    
    def get_diff_against_branch(self, branch: str = "main") -> List[str]:
        """Get files that differ from the specified branch."""
        if not self.git_available:
            return []
        
        try:
            result = subprocess.run(
                ["git", "diff", f"{branch}..HEAD", "--name-only"],
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                check=True
            )
            return [f.strip() for f in result.stdout.split('\n') if f.strip()]
        except subprocess.CalledProcessError:
            return []
    
    def _get_files_by_mtime(self, since_hours: int) -> List[str]:
        """Fallback method to get files by modification time."""
        cutoff_time = datetime.now() - timedelta(hours=since_hours)
        modified_files = []
        
        # Focus on main code directories
        code_dirs = ['lib', 'src', 'test', 'tests', 'docs']
        
        for dir_name in code_dirs:
            dir_path = self.repo_path / dir_name
            if dir_path.exists():
                for file_path in dir_path.rglob('*'):
                    if file_path.is_file():
                        mtime = datetime.fromtimestamp(file_path.stat().st_mtime)
                        if mtime > cutoff_time:
                            rel_path = file_path.relative_to(self.repo_path)
                            modified_files.append(str(rel_path))
        
        return modified_files
    
    def filter_code_files(self, files: List[str]) -> List[str]:
        """Filter to only include relevant code files."""
        code_extensions = {
            '.dart', '.py', '.js', '.ts', '.jsx', '.tsx', 
            '.java', '.kt', '.swift', '.cpp', '.c', '.h',
            '.rs', '.go', '.rb', '.php', '.cs', '.scala',
            '.md', '.yml', '.yaml', '.json', '.toml'
        }
        
        filtered_files = []
        for file_path in files:
            path = Path(file_path)
            
            # Skip certain directories
            if any(part in ['.git', 'node_modules', '.dart_tool', 'build', 'dist'] 
                   for part in path.parts):
                continue
                
            # Include files with relevant extensions
            if path.suffix.lower() in code_extensions:
                filtered_files.append(file_path)
            # Include important config files without extensions
            elif path.name in ['Dockerfile', 'Makefile', 'pubspec.lock']:
                filtered_files.append(file_path)
        
        return filtered_files
    
    def get_file_stats(self, file_path: str) -> Dict:
        """Get statistics about a file."""
        full_path = self.repo_path / file_path
        if not full_path.exists():
            return {}
        
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            stats = {
                'size_bytes': len(content.encode('utf-8')),
                'line_count': len(content.splitlines()),
                'char_count': len(content),
                'modification_time': datetime.fromtimestamp(full_path.stat().st_mtime).isoformat()
            }
            
            # Get git info if available
            if self.git_available:
                try:
                    # Get last commit info for this file
                    result = subprocess.run(
                        ["git", "log", "-1", "--pretty=format:%h|%an|%ad", "--date=iso", file_path],
                        cwd=self.repo_path,
                        capture_output=True,
                        text=True
                    )
                    if result.stdout:
                        commit_hash, author, date = result.stdout.split('|', 2)
                        stats.update({
                            'last_commit': commit_hash,
                            'last_author': author,
                            'last_commit_date': date
                        })
                except subprocess.CalledProcessError:
                    pass
            
            return stats
        except Exception as e:
            return {'error': str(e)}
    
    def read_file_content(self, file_path: str) -> str:
        """Read and return file content with error handling."""
        full_path = self.repo_path / file_path
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                return f.read()
        except UnicodeDecodeError:
            try:
                with open(full_path, 'r', encoding='latin-1') as f:
                    return f"[Binary or non-UTF8 file content - {full_path.suffix} file]"
            except Exception:
                return "[Unable to read file content]"
        except Exception as e:
            return f"[Error reading file: {e}]"
    
    def generate_markdown_digest(self, files: List[str], title: str = "Latest Code Review") -> str:
        """Generate a markdown-formatted code review digest."""
        
        output = [f"# {title}\n"]
        output.append(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        output.append(f"Repository: {self.repo_path}\n")
        output.append(f"Files analyzed: {len(files)}\n")
        
        if not files:
            output.append("## No files found matching the criteria.\n")
            return '\n'.join(output)
        
        # Summary section
        output.append("## Summary\n")
        total_lines = 0
        total_size = 0
        file_types = {}
        
        for file_path in files:
            stats = self.get_file_stats(file_path)
            if 'line_count' in stats:
                total_lines += stats['line_count']
            if 'size_bytes' in stats:
                total_size += stats['size_bytes']
            
            ext = Path(file_path).suffix or 'no extension'
            file_types[ext] = file_types.get(ext, 0) + 1
        
        output.append(f"- **Total lines of code**: {total_lines:,}")
        output.append(f"- **Total size**: {total_size:,} bytes ({total_size/1024:.1f} KB)")
        output.append(f"- **File types**: {dict(sorted(file_types.items()))}\n")
        
        # File list with stats
        output.append("## Modified Files\n")
        for file_path in files:
            stats = self.get_file_stats(file_path)
            output.append(f"### {file_path}")
            
            if stats:
                if 'line_count' in stats:
                    output.append(f"- **Lines**: {stats['line_count']}")
                if 'size_bytes' in stats:
                    output.append(f"- **Size**: {stats['size_bytes']} bytes")
                if 'last_author' in stats:
                    output.append(f"- **Last author**: {stats['last_author']}")
                if 'last_commit_date' in stats:
                    output.append(f"- **Last modified**: {stats['last_commit_date']}")
            
            output.append("")  # Empty line
        
        # Full content section
        output.append("## File Contents\n")
        for file_path in files:
            output.append(f"### File: `{file_path}`\n")
            
            content = self.read_file_content(file_path)
            if content.startswith('[') and content.endswith(']'):
                output.append(content)  # Error message or binary file note
            else:
                # Determine language for syntax highlighting
                ext = Path(file_path).suffix.lower()
                lang_map = {
                    '.py': 'python', '.dart': 'dart', '.js': 'javascript',
                    '.ts': 'typescript', '.json': 'json', '.yml': 'yaml',
                    '.yaml': 'yaml', '.md': 'markdown', '.sh': 'bash'
                }
                lang = lang_map.get(ext, '')
                
                output.append(f"```{lang}")
                output.append(content)
                output.append("```")
            
            output.append("\n---\n")  # Separator between files
        
        return '\n'.join(output)
    
    def generate_json_digest(self, files: List[str]) -> str:
        """Generate a JSON-formatted code review digest."""
        digest_data = {
            'metadata': {
                'generated_at': datetime.now().isoformat(),
                'repository_path': str(self.repo_path),
                'total_files': len(files)
            },
            'files': []
        }
        
        for file_path in files:
            file_data = {
                'path': file_path,
                'stats': self.get_file_stats(file_path),
                'content': self.read_file_content(file_path)
            }
            digest_data['files'].append(file_data)
        
        return json.dumps(digest_data, indent=2, ensure_ascii=False)


def main():
    parser = argparse.ArgumentParser(
        description="Generate code review digest for recently modified files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    
    parser.add_argument(
        '--since', 
        type=int, 
        default=24, 
        help='Include files modified in the last N hours (default: 24)'
    )
    
    parser.add_argument(
        '--staged', 
        action='store_true',
        help='Only include staged files ready for commit'
    )
    
    parser.add_argument(
        '--branch',
        type=str,
        default='main',
        help='Compare against specific branch (default: main)'
    )
    
    parser.add_argument(
        '--output',
        type=str,
        default='latest_code_review.md',
        help='Output file name (default: latest_code_review.md)'
    )
    
    parser.add_argument(
        '--format',
        choices=['markdown', 'txt', 'json'],
        default='markdown',
        help='Output format (default: markdown)'
    )
    
    parser.add_argument(
        '--repo-path',
        type=str,
        default='.',
        help='Path to repository (default: current directory)'
    )
    
    args = parser.parse_args()
    
    # Initialize digester
    digester = LatestCodeReviewDigester(args.repo_path)
    
    # Get list of files based on criteria
    if args.staged:
        files = digester.get_staged_files()
        title = "Staged Files Code Review"
    else:
        files = digester.get_recently_modified_files(args.since)
        title = f"Latest Code Review (Last {args.since} hours)"
    
    # Filter to code files only
    files = digester.filter_code_files(files)
    
    print(f"Found {len(files)} files to analyze:")
    for file_path in files:
        print(f"  - {file_path}")
    
    if not files:
        print("No files found matching the criteria.")
        return
    
    # Generate digest based on format
    if args.format == 'json':
        content = digester.generate_json_digest(files)
    else:  # markdown or txt
        content = digester.generate_markdown_digest(files, title)
    
    # Write output
    output_path = Path(args.output)
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"\nCode review digest generated successfully!")
        print(f"Output saved to: {output_path.absolute()}")
        print(f"File size: {len(content.encode('utf-8'))} bytes")
        
    except Exception as e:
        print(f"Error writing output file: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())