# GitIngest Scripts for AstraTrade Project

This directory contains scripts for generating code digests and reviews from the AstraTrade project repository.

## Scripts Overview

### 1. `run_ingest.py` 
**Original full repository digest**
- Processes the entire repository using gitingest
- Includes Python and Markdown files
- Generates complete project overview
- Best for: Initial project analysis, comprehensive documentation

```bash
python run_ingest.py
# Output: digest.txt
```

### 2. `run_session_review.py` ⭐ **NEW**
**Current session focused review**
- Analyzes files modified in the last 2 hours
- Focuses on Dart/Flutter files and configs
- Perfect for immediate code review
- Best for: Quick session summaries, immediate feedback

```bash
python run_session_review.py
# Output: session_review.md
```

### 3. `run_latest_code_review.py` ⭐ **NEW**
**Advanced latest changes digest**
- Configurable time window (default: 24 hours)
- Multiple output formats (Markdown, JSON, TXT)
- Git integration for accurate change tracking
- Comprehensive file statistics and metadata
- Best for: Detailed code reviews, change documentation

```bash
# Basic usage - last 24 hours
python run_latest_code_review.py

# Custom time window
python run_latest_code_review.py --since 8

# Only staged files
python run_latest_code_review.py --staged

# JSON output
python run_latest_code_review.py --format json --output review.json

# Compare against specific branch
python run_latest_code_review.py --branch develop
```

### 4. `auto_digest_task.py` 🤖 **NEW**
**Automatic task completion digests**
- Runs automatically after each Claude Code task
- Smart change detection using git history
- Lightweight with minimal performance impact
- JSON and Markdown output formats
- Best for: Seamless development documentation

```bash
# Setup automatic digests
python setup_claude_hooks.py --enable

# Manual digest generation
python auto_digest_task.py

# Custom time window
python auto_digest_task.py --window 60

# Check status
python setup_claude_hooks.py --status
```

## Usage Scenarios

### 🔄 Daily Development Workflow

1. **One-time setup**: Enable auto-digest with `python setup_claude_hooks.py --enable`
2. **Start of session**: Use `run_session_review.py` to see what was worked on recently
3. **During development**: Work with Claude Code - digests are automatically generated
4. **Review progress**: Check `.claude_digests/` directory for automatic task summaries
5. **Before commit**: Use `run_latest_code_review.py --staged` to review staged changes

### 🤖 Automated Development Tracking

1. **Enable auto-digest**: `python setup_claude_hooks.py --enable`
2. **Work normally**: Use Claude Code for development tasks
3. **Automatic documentation**: Each task completion generates a digest file
4. **Review history**: Browse `.claude_digests/` for development progress
5. **Weekly cleanup**: Old digests are automatically removed

### 📋 Code Review Process

1. **For PR reviews**: `run_latest_code_review.py --branch main`
2. **For specific timeframe**: `run_latest_code_review.py --since 48`
3. **For comprehensive analysis**: `run_ingest.py` (full repository)

### 🎯 Project Documentation

- **Project overview**: `run_ingest.py`
- **Recent changes summary**: `run_latest_code_review.py --since 168` (1 week)
- **Feature development tracking**: `run_latest_code_review.py --format json`

## File Filtering

The scripts intelligently filter files to focus on relevant code:

**Included:**
- Dart source files (`.dart`)
- Configuration files (`pubspec.yaml`, `analysis_options.yaml`)
- Documentation (`.md`)
- Build configs (`.yml`, `.yaml`, `.json`)

**Excluded:**
- Generated files (`.g.dart`, `.freezed.dart`)
- Build directories (`build/`, `.dart_tool/`)
- Version control (`.git/`)
- Dependencies (`node_modules/`, etc.)

## Output Examples

### Session Review Output
```markdown
# 🔍 Current Session Code Review
**Generated**: 2024-01-15 14:30:00
**Session Period**: Last 2 hours
**Files Modified**: 3

## 📊 Session Summary
- **Dart source files**: 2
- **Test files**: 1
- **Total lines modified**: ~150

## 🔄 Modified Files
### ⚡ `lib/services/game_service.dart`
- **Lines**: 583 | **Size**: 18.2 KB | **Modified**: 14:25:00
- **Changes**: +45/-12
```

### Latest Code Review Output
```markdown
# Latest Code Review (Last 24 hours)
Generated on: 2024-01-15 14:30:00
Repository: /path/to/AstraTrade-Project
Files analyzed: 5

## Summary
- **Total lines of code**: 1,250
- **Total size**: 45,678 bytes (44.6 KB)
- **File types**: {'.dart': 4, '.md': 1}
```

## Requirements

- Python 3.7+
- Git (for accurate file tracking)
- gitingest package (for `run_ingest.py`)

```bash
pip install gitingest
```

## Advanced Configuration

### Custom File Patterns

Edit the scripts to include additional file patterns:

```python
# In run_latest_code_review.py
code_extensions = {
    '.dart', '.py', '.js', '.ts',  # Add your extensions
    '.cpp', '.h', '.rs'            # System languages
}
```

### Custom Time Windows

```bash
# Last hour (great for quick checks)
python run_latest_code_review.py --since 1

# Last week (for weekly reviews)
python run_latest_code_review.py --since 168

# Last month (for milestone reviews)  
python run_latest_code_review.py --since 720
```

### Integration with CI/CD

Add to your workflow:

```yaml
# .github/workflows/code-review.yml
- name: Generate Code Review
  run: |
    python gitingest_scripts/run_latest_code_review.py --format json
    # Upload or process the generated review
```

## Troubleshooting

### Git Not Available
The scripts gracefully fall back to filesystem timestamps when Git is not available.

### No Files Found
- Check if you're in the correct repository
- Verify the time window (`--since` parameter)
- Ensure files have been actually modified

### Large Output Files
- Use `--format json` for structured data
- Filter specific file types by editing the filter functions
- Reduce the time window with `--since`

## Future Enhancements

- Integration with GitHub/GitLab APIs
- Automatic detection of feature branches
- Code complexity metrics
- Change impact analysis
- Team collaboration features

---

*These scripts are designed to enhance the AstraTrade development workflow by providing focused, actionable code review materials.*