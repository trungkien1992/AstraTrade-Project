#!/usr/bin/env python3
"""
Interactive Review Menu

A convenient wrapper script that helps users choose and run the appropriate
code review script based on their needs.
"""

import subprocess
import sys
from pathlib import Path


def print_banner():
    """Print the application banner."""
    print("=" * 60)
    print("🔍 AstraTrade Code Review Menu")
    print("=" * 60)
    print()


def print_menu():
    """Print the main menu options."""
    options = [
        ("1", "🚀 Current Session Review", "Files modified in last 2 hours"),
        ("2", "📅 Latest Changes (24h)", "All changes in last 24 hours"),
        ("3", "📋 Staged Files Review", "Only staged files ready for commit"),
        ("4", "🌿 Branch Comparison", "Compare against main/develop branch"),
        ("5", "📚 Full Repository Digest", "Complete project overview"),
        ("6", "⚙️  Custom Time Range", "Specify custom hours"),
        ("7", "📊 JSON Export", "Export latest changes as JSON"),
        ("q", "❌ Quit", "Exit the menu")
    ]
    
    print("Choose a review type:")
    print()
    
    for code, title, description in options:
        print(f"  {code}. {title}")
        print(f"     {description}")
        print()


def run_command(cmd, description):
    """Run a command and handle errors."""
    print(f"🏃 Running: {description}")
    print(f"Command: {' '.join(cmd)}")
    print("-" * 40)
    
    try:
        result = subprocess.run(cmd, cwd=Path(__file__).parent.parent, check=True)
        print()
        print("✅ Command completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Command failed with exit code {e.returncode}")
        return False
    except FileNotFoundError:
        print("❌ Script not found. Make sure you're in the correct directory.")
        return False


def get_user_input(prompt, default=None):
    """Get user input with optional default."""
    if default:
        response = input(f"{prompt} [{default}]: ").strip()
        return response if response else default
    else:
        return input(f"{prompt}: ").strip()


def main():
    """Main interactive menu."""
    print_banner()
    
    scripts_dir = Path(__file__).parent
    repo_dir = scripts_dir.parent
    
    # Check if scripts exist
    required_scripts = [
        "run_session_review.py",
        "run_latest_code_review.py", 
        "run_ingest.py"
    ]
    
    missing_scripts = []
    for script in required_scripts:
        if not (scripts_dir / script).exists():
            missing_scripts.append(script)
    
    if missing_scripts:
        print("❌ Missing required scripts:")
        for script in missing_scripts:
            print(f"  - {script}")
        print("\nPlease ensure all scripts are in the gitingest_scripts directory.")
        return 1
    
    while True:
        print_menu()
        
        choice = input("Enter your choice (1-7, q): ").strip().lower()
        print()
        
        if choice == 'q':
            print("👋 Goodbye!")
            break
            
        elif choice == '1':
            # Current session review
            cmd = ["python", str(scripts_dir / "run_session_review.py")]
            run_command(cmd, "Current Session Review")
            
        elif choice == '2':
            # Latest changes (24h)
            cmd = ["python", str(scripts_dir / "run_latest_code_review.py")]
            run_command(cmd, "Latest Changes (24 hours)")
            
        elif choice == '3':
            # Staged files
            cmd = ["python", str(scripts_dir / "run_latest_code_review.py"), "--staged"]
            run_command(cmd, "Staged Files Review")
            
        elif choice == '4':
            # Branch comparison
            branch = get_user_input("Enter branch to compare against", "main")
            cmd = ["python", str(scripts_dir / "run_latest_code_review.py"), "--branch", branch]
            run_command(cmd, f"Branch Comparison (against {branch})")
            
        elif choice == '5':
            # Full repository digest
            print("⚠️  This will process the entire repository and may take a while.")
            confirm = get_user_input("Continue? (y/n)", "y").lower()
            if confirm in ['y', 'yes']:
                cmd = ["python", str(scripts_dir / "run_ingest.py")]
                run_command(cmd, "Full Repository Digest")
            else:
                print("Operation cancelled.")
                
        elif choice == '6':
            # Custom time range
            try:
                hours = int(get_user_input("Enter number of hours to look back", "8"))
                output = get_user_input("Output filename", f"review_{hours}h.md")
                cmd = [
                    "python", str(scripts_dir / "run_latest_code_review.py"),
                    "--since", str(hours),
                    "--output", output
                ]
                run_command(cmd, f"Custom Review ({hours} hours)")
            except ValueError:
                print("❌ Invalid number of hours.")
                
        elif choice == '7':
            # JSON export
            hours = get_user_input("Hours to look back", "24")
            output = get_user_input("JSON output filename", "code_review.json")
            cmd = [
                "python", str(scripts_dir / "run_latest_code_review.py"),
                "--since", hours,
                "--format", "json",
                "--output", output
            ]
            run_command(cmd, f"JSON Export ({hours} hours)")
            
        else:
            print("❌ Invalid choice. Please try again.")
        
        print()
        input("Press Enter to continue...")
        print("\n" + "=" * 60 + "\n")
    
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\n👋 Interrupted by user. Goodbye!")
        sys.exit(0)