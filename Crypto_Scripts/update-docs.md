# Auto-Documentation Update Slash Command

You are an expert documentation maintainer for the SPT Safe Driving Token Video Script Generation project. Your job is to automatically update all documentation files whenever code changes are detected.

## Primary Responsibilities

1. **Scan for Changes**: Detect modifications in code files, scripts, and project structure
2. **Update Documentation**: Refresh README files, CLAUDE.md, and other docs
3. **Maintain Consistency**: Ensure all documentation reflects current project state
4. **Preserve Context**: Keep existing documentation structure while updating content

## Files to Monitor and Update

### Code Files to Watch:
- `script_generator.py` - Main script generation tool
- `story_database.json` - Story database structure
- `output/sample_scripts.md` - Generated video scripts
- `output/` folder contents - All generated script files
- Any new Python files or JSON data files

### Documentation Files to Update:
- `README.md` (create if missing)
- `CLAUDE.md` - Project memory and context
- `Video Script Generation Plan.md` - Process documentation
- Any other .md files in the project

## Update Process

### Step 1: Analyze Current State
- Read all code files to understand functionality
- Check project structure and new additions
- Identify what has changed since last documentation update

### Step 2: Update Documentation
For each documentation file:

#### README.md:
- Project overview and purpose
- Installation/setup instructions
- Usage examples
- Feature list
- File structure explanation

#### CLAUDE.md:
- Project context and goals
- Key decisions and rationale
- Development history
- Important notes for future development

#### Process Documentation:
- Workflow explanations
- Tool usage instructions
- Best practices

### Step 3: Maintain Quality
- Ensure all code examples work
- Update any outdated information
- Keep documentation clear and concise
- Add new features and capabilities

## Usage Instructions

Run this slash command after making any significant code changes:
- After adding new functions to script_generator.py
- After updating the story database
- After generating new sample scripts
- After changing project structure

## Output Format

The command should:
1. List what changes were detected
2. Show which documentation files were updated
3. Provide a summary of major updates made
4. Suggest any manual review needed

## Example Usage

```
/update-docs
```

This command will automatically:
- Scan the project for changes
- Update all relevant documentation
- Ensure consistency across all files
- Provide a report of updates made

## Quality Standards

- All documentation must be accurate and current
- Code examples must be functional
- File references must be correct
- Markdown formatting must be proper
- Links must work correctly

---

*This slash command helps maintain professional, up-to-date documentation for the SPT Safe Driving Token Video Script Generation project.*