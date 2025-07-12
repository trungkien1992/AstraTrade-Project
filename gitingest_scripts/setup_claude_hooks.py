#!/usr/bin/env python3
"""
Claude Code Auto-Digest Setup Script

This script helps configure Claude Code to automatically generate task completion
digests by setting up the appropriate hooks in the Claude Code configuration.

Usage:
    python setup_claude_hooks.py [--enable|--disable|--status]
"""

import json
import os
import sys
from pathlib import Path
import argparse
import shutil


class ClaudeHookSetup:
    """Manages Claude Code hook configuration for auto-digest generation."""
    
    def __init__(self):
        self.claude_config_path = Path.home() / '.claude.json'
        self.script_dir = Path(__file__).parent
        self.hook_script = self.script_dir / 'claude_task_hook.sh'
        
    def load_claude_config(self) -> dict:
        """Load existing Claude Code configuration."""
        try:
            if self.claude_config_path.exists():
                with open(self.claude_config_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            else:
                return {}
        except Exception as e:
            print(f"Warning: Could not load Claude config: {e}")
            return {}
    
    def save_claude_config(self, config: dict) -> bool:
        """Save Claude Code configuration."""
        try:
            # Create backup
            if self.claude_config_path.exists():
                backup_path = self.claude_config_path.with_suffix('.json.backup')
                shutil.copy2(self.claude_config_path, backup_path)
            
            # Save new config
            with open(self.claude_config_path, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
            
            return True
        except Exception as e:
            print(f"Error saving Claude config: {e}")
            return False
    
    def is_hook_configured(self, config: dict) -> bool:
        """Check if auto-digest hook is already configured."""
        hooks = config.get('hooks', {})
        stop_hooks = hooks.get('Stop', [])
        
        for hook_group in stop_hooks:
            if isinstance(hook_group, dict) and 'hooks' in hook_group:
                for hook in hook_group['hooks']:
                    if (isinstance(hook, dict) and 
                        hook.get('type') == 'command' and
                        'claude_task_hook.sh' in str(hook.get('command', ''))):
                        return True
        
        return False
    
    def add_auto_digest_hook(self) -> bool:
        """Add the auto-digest hook to Claude Code configuration."""
        config = self.load_claude_config()
        
        # Check if already configured
        if self.is_hook_configured(config):
            print("✅ Auto-digest hook is already configured!")
            return True
        
        # Ensure hooks structure exists
        if 'hooks' not in config:
            config['hooks'] = {}
        
        if 'Stop' not in config['hooks']:
            config['hooks']['Stop'] = []
        
        # Add our hook
        auto_digest_hook = {
            "hooks": [
                {
                    "type": "command",
                    "command": str(self.hook_script.absolute())
                }
            ]
        }
        
        config['hooks']['Stop'].append(auto_digest_hook)
        
        # Save configuration
        if self.save_claude_config(config):
            print("✅ Auto-digest hook added successfully!")
            print(f"📁 Hook script: {self.hook_script}")
            print(f"⚙️  Configuration: {self.claude_config_path}")
            return True
        else:
            print("❌ Failed to save Claude Code configuration")
            return False
    
    def remove_auto_digest_hook(self) -> bool:
        """Remove the auto-digest hook from Claude Code configuration."""
        config = self.load_claude_config()
        
        if not self.is_hook_configured(config):
            print("ℹ️  Auto-digest hook is not configured")
            return True
        
        # Remove hook
        hooks = config.get('hooks', {})
        stop_hooks = hooks.get('Stop', [])
        
        # Filter out our hook
        filtered_hooks = []
        for hook_group in stop_hooks:
            if isinstance(hook_group, dict) and 'hooks' in hook_group:
                filtered_inner_hooks = []
                for hook in hook_group['hooks']:
                    if not (isinstance(hook, dict) and 
                           hook.get('type') == 'command' and
                           'claude_task_hook.sh' in str(hook.get('command', ''))):
                        filtered_inner_hooks.append(hook)
                
                if filtered_inner_hooks:
                    hook_group['hooks'] = filtered_inner_hooks
                    filtered_hooks.append(hook_group)
            else:
                filtered_hooks.append(hook_group)
        
        config['hooks']['Stop'] = filtered_hooks
        
        # Clean up empty structure
        if not config['hooks']['Stop']:
            del config['hooks']['Stop']
        if not config['hooks']:
            del config['hooks']
        
        # Save configuration
        if self.save_claude_config(config):
            print("✅ Auto-digest hook removed successfully!")
            return True
        else:
            print("❌ Failed to save Claude Code configuration")
            return False
    
    def show_status(self) -> None:
        """Show current hook configuration status."""
        config = self.load_claude_config()
        
        print("🔍 Claude Code Auto-Digest Hook Status")
        print("=" * 50)
        
        # Configuration file
        if self.claude_config_path.exists():
            print(f"✅ Configuration file: {self.claude_config_path}")
        else:
            print(f"❌ Configuration file not found: {self.claude_config_path}")
        
        # Hook script
        if self.hook_script.exists():
            print(f"✅ Hook script: {self.hook_script}")
        else:
            print(f"❌ Hook script not found: {self.hook_script}")
        
        # Hook configuration
        is_configured = self.is_hook_configured(config)
        print(f"{'✅' if is_configured else '❌'} Hook configured: {is_configured}")
        
        # Show current hooks
        hooks = config.get('hooks', {})
        if hooks:
            print(f"\n📋 Current hooks configuration:")
            for event, event_hooks in hooks.items():
                print(f"  - {event}: {len(event_hooks)} hook(s)")
        else:
            print("\n📋 No hooks currently configured")
        
        # Auto-digest directory
        digest_dir = self.script_dir.parent / '.claude_digests'
        if digest_dir.exists():
            digest_files = list(digest_dir.glob('task_digest_*.json'))
            print(f"\n📁 Digest directory: {digest_dir}")
            print(f"   {len(digest_files)} digest files found")
        else:
            print(f"\n📁 Digest directory: {digest_dir} (will be created)")
    
    def test_hook(self) -> bool:
        """Test the hook script execution."""
        print("🧪 Testing hook script...")
        
        if not self.hook_script.exists():
            print(f"❌ Hook script not found: {self.hook_script}")
            return False
        
        try:
            import subprocess
            result = subprocess.run([str(self.hook_script)], 
                                  cwd=self.script_dir.parent,
                                  capture_output=True, 
                                  text=True, 
                                  timeout=30)
            
            if result.returncode == 0:
                print("✅ Hook script executed successfully")
                
                # Check if digest was created
                digest_dir = self.script_dir.parent / '.claude_digests'
                if digest_dir.exists():
                    recent_digests = list(digest_dir.glob('task_digest_*.json'))
                    if recent_digests:
                        print(f"📄 Found {len(recent_digests)} digest files")
                
                return True
            else:
                print(f"❌ Hook script failed with exit code {result.returncode}")
                if result.stderr:
                    print(f"   Error: {result.stderr}")
                return False
                
        except Exception as e:
            print(f"❌ Failed to test hook script: {e}")
            return False


def main():
    """Main CLI interface."""
    parser = argparse.ArgumentParser(
        description='Setup Claude Code auto-digest hooks',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python setup_claude_hooks.py --enable     # Enable auto-digest
    python setup_claude_hooks.py --disable    # Disable auto-digest  
    python setup_claude_hooks.py --status     # Show current status
    python setup_claude_hooks.py --test       # Test hook execution
        """
    )
    
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--enable', action='store_true', help='Enable auto-digest hook')
    group.add_argument('--disable', action='store_true', help='Disable auto-digest hook')
    group.add_argument('--status', action='store_true', help='Show current status')
    group.add_argument('--test', action='store_true', help='Test hook execution')
    
    args = parser.parse_args()
    
    setup = ClaudeHookSetup()
    
    if args.enable:
        success = setup.add_auto_digest_hook()
        if success:
            print("\n💡 The auto-digest hook will now run after each Claude Code task!")
            print("   Digests will be saved to .claude_digests/ directory")
        return 0 if success else 1
        
    elif args.disable:
        success = setup.remove_auto_digest_hook()
        return 0 if success else 1
        
    elif args.test:
        success = setup.test_hook()
        return 0 if success else 1
        
    else:
        # Default to showing status
        setup.show_status()
        print("\n💡 Use --enable to activate auto-digest generation")
        return 0


if __name__ == '__main__':
    sys.exit(main())