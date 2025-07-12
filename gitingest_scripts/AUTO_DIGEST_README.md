# 🤖 Claude Code Auto-Digest System

Automatically generate digests of code changes after each Claude Code task completion. This system provides seamless documentation of development progress without manual intervention.

## 🌟 Features

- **Automatic Execution**: Runs after every Claude Code task completion
- **Smart Change Detection**: Uses git history to accurately track modifications
- **Minimal Impact**: Lightweight scripts with fast execution
- **Comprehensive Logging**: Detailed file change tracking and statistics
- **Flexible Time Windows**: Configurable task session detection
- **Multiple Output Formats**: JSON for automation, Markdown for humans
- **Automatic Cleanup**: Removes old digests to prevent disk bloat

## 🚀 Quick Setup

### 1. Enable Auto-Digest

```bash
# Navigate to your project
cd /path/to/AstraTrade-Project

# Enable the auto-digest hook
python gitingest_scripts/setup_claude_hooks.py --enable
```

### 2. Verify Setup

```bash
# Check configuration status
python gitingest_scripts/setup_claude_hooks.py --status

# Test the hook manually
python gitingest_scripts/setup_claude_hooks.py --test
```

### 3. Start Coding!

The system is now active. After each Claude Code task completion, a digest will automatically be generated in the `.claude_digests/` directory.

## 📁 Generated Files

### Digest Directory Structure
```
.claude_digests/
├── task_digest_20240115_143022.json    # Machine-readable digest
├── task_digest_20240115_143022.md      # Human-readable summary  
├── task_digest_20240115_150815.json
├── task_digest_20240115_150815.md
├── hook.log                            # Hook execution log
└── .last_cleanup                       # Cleanup tracking
```

### JSON Digest Format
```json
{
  "metadata": {
    "timestamp": "2024-01-15T14:30:22.123456",
    "session_id": "a1b2c3d4",
    "repo_path": "/path/to/AstraTrade-Project",
    "claude_code_version": "1.0.0"
  },
  "summary": "Task completed: 2 files modified, 1 file added",
  "statistics": {
    "total_files_changed": 3,
    "primary_language": "Dart/Flutter",
    "file_types": {
      ".dart": {"modified": 2, "added": 1, "deleted": 0}
    }
  },
  "changes": {
    "modified": ["lib/services/game_service.dart"],
    "added": ["lib/api/new_client.dart"],
    "deleted": []
  },
  "files_detail": {
    "lib/services/game_service.dart": {
      "category": "modified",
      "size_bytes": 15420,
      "lines": 425
    }
  }
}
```

### Markdown Summary Format
```markdown
# 🤖 Claude Code Task Digest
**Generated**: 2024-01-15T14:30:22.123456
**Session**: a1b2c3d4

## 📋 Summary
Task completed: 2 files modified, 1 file added

**Primary Language**: Dart/Flutter
**Total Files**: 3

## 📊 File Types
- **.dart**: 3 files
  - 2 modified, 1 added

## 📝 Modified Files
- `lib/services/game_service.dart`
  - 425 lines, 15420 bytes

## ➕ Added Files  
- `lib/api/new_client.dart`
  - 120 lines, 3450 bytes
```

## ⚙️ Configuration

### Task Detection Window

By default, the system looks for changes in the last 30 minutes. You can customize this:

```bash
# Custom time window (60 minutes)
python gitingest_scripts/auto_digest_task.py --window 60
```

### File Filtering

The system automatically filters to important files:

**Included:**
- Dart source files (`.dart`)
- Python scripts (`.py`)
- Documentation (`.md`)
- Configuration files (`.yaml`, `.yml`, `.json`)
- Build files (`Dockerfile`, `Makefile`)

**Excluded:**
- Generated files (`.g.dart`, `.freezed.dart`)
- Build directories (`build/`, `.dart_tool/`)
- Version control (`.git/`)
- Dependencies (`node_modules/`)

### Cleanup Configuration

Old digests are automatically cleaned up:

```bash
# Manual cleanup (keep last 7 days)
python gitingest_scripts/auto_digest_task.py --cleanup 7

# Custom retention period (keep last 30 days)
python gitingest_scripts/auto_digest_task.py --cleanup 30
```

## 🔧 Advanced Usage

### Manual Digest Generation

```bash
# Generate digest for current session
python gitingest_scripts/auto_digest_task.py

# Custom time window
python gitingest_scripts/auto_digest_task.py --window 120

# Specific repository path
python gitingest_scripts/auto_digest_task.py --repo-path /path/to/repo

# Quiet mode (no output)
python gitingest_scripts/auto_digest_task.py --quiet
```

### Integration with CI/CD

Add to your workflow:

```yaml
# .github/workflows/digest.yml
- name: Generate Development Digest
  run: |
    python gitingest_scripts/auto_digest_task.py --window 1440  # Last 24 hours
    # Process or upload the generated digest
```

### Hook Management

```bash
# Check current status
python gitingest_scripts/setup_claude_hooks.py --status

# Enable auto-digest
python gitingest_scripts/setup_claude_hooks.py --enable

# Disable auto-digest  
python gitingest_scripts/setup_claude_hooks.py --disable

# Test hook execution
python gitingest_scripts/setup_claude_hooks.py --test
```

## 🛠️ Troubleshooting

### Common Issues

#### Hook Not Executing
```bash
# Check if hook is configured
python gitingest_scripts/setup_claude_hooks.py --status

# Verify script permissions
ls -la gitingest_scripts/claude_task_hook.sh

# Test hook manually
python gitingest_scripts/setup_claude_hooks.py --test
```

#### No Digests Generated
1. **Check time window**: Default is 30 minutes - ensure you've made changes recently
2. **Verify git repository**: System requires git for accurate change detection
3. **Check file types**: Only important files are included (see filtering rules)

#### Large Digest Files
```bash
# Reduce retention period
python gitingest_scripts/auto_digest_task.py --cleanup 3

# Check current disk usage
du -sh .claude_digests/
```

### Debug Mode

Enable detailed logging:

```bash
# Check hook execution log
tail -f .claude_digests/hook.log

# Manual execution with full output
python gitingest_scripts/auto_digest_task.py --window 60
```

### Performance Considerations

- **Execution Time**: ~100-500ms per hook execution
- **Disk Usage**: ~2-5KB per digest file
- **Git Operations**: Minimal impact, uses efficient git log queries
- **Memory Usage**: <10MB peak during execution

## 🔄 Integration Examples

### Development Workflow

```bash
# Morning: Check what was done yesterday
ls -la .claude_digests/task_digest_$(date -d yesterday '+%Y%m%d')*.md

# During development: Work normally with Claude Code
# (Digests are generated automatically)

# Evening: Review the day's changes
cat .claude_digests/task_digest_$(date '+%Y%m%d')*.md
```

### Team Collaboration

```bash
# Share daily progress
cp .claude_digests/task_digest_$(date '+%Y%m%d')_*.md daily_reports/

# Weekly summary
python gitingest_scripts/auto_digest_task.py --window 10080  # 7 days
```

### Project Documentation

```bash
# Generate milestone summary
python gitingest_scripts/auto_digest_task.py --window 4320  # 3 days
mv task_digest_*.md docs/milestones/
```

## 🔮 Advanced Features

### Custom Hook Events

You can extend the system to hook into other Claude Code events:

```json
{
  "hooks": {
    "Start": [{"hooks": [{"type": "command", "command": "start_session.sh"}]}],
    "Stop": [{"hooks": [{"type": "command", "command": "claude_task_hook.sh"}]}]
  }
}
```

### Integration with External Tools

```bash
# Send digest to Slack
cat latest_digest.json | jq '.summary' | slack-cli send

# Commit digest to git
git add .claude_digests/task_digest_*.json
git commit -m "Auto: Task completion digest"

# Generate weekly reports
find .claude_digests -name "*.json" -mtime -7 | xargs jq -s '.'
```

## 📚 Related Documentation

- [GitIngest Scripts Overview](README.md)
- [Claude Code Hooks Documentation](https://docs.anthropic.com/en/docs/claude-code/hooks)
- [Session Review Scripts](README.md#2-run_session_reviewpy)

## 🤝 Contributing

To extend the auto-digest system:

1. **Fork the script**: Copy `auto_digest_task.py` as a starting point
2. **Modify detection logic**: Update `get_recent_changes()` for custom file detection  
3. **Enhance output format**: Extend `generate_digest()` for additional data
4. **Add new hooks**: Create additional hook scripts for different events

---

*The auto-digest system seamlessly captures your development progress, ensuring no important changes go undocumented.*