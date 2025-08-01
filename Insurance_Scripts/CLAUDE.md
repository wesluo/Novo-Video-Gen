# CLAUDE.md - Novo Insurance Video Script Generation Project Memory

## Project Context & Vision

This system is part of the Multi-Product Video Generation Platform, specifically focused on Novo Insurance's social media marketing. Built around Novo's mission: "Transform car insurance by rewarding safe driving and empowering customers with technology."

**Multi-Product Context**: This Insurance_Scripts system serves as the foundation for the broader platform that includes Crypto_Scripts and App_Scripts, all sharing the same core road safety mission but with different product messaging.

## Key Design Decisions

### 1. Real Content Over Templates
**Decision**: Use actual high-engagement Reddit stories instead of generic templates
**Rationale**: Authenticity drives virality - real stories with verified engagement perform better
**Implementation**: 90-story database with actual upvote counts and Reddit sources

### 2. Multiple Format Support
**Decision**: Support 6 different viral video formats instead of one-size-fits-all
**Rationale**: Different stories work better in different formats (comedy vs. educational vs. transformation)
**Implementation**: Format mapping in database + specialized generation functions

### 3. Natural Brand Integration
**Decision**: Weave Novo messaging naturally into scripts rather than forced CTAs
**Rationale**: Authentic brand integration feels less promotional and more trustworthy
**Implementation**: Contextual brand messages that relate to each story's lesson

### 4. Organized Script Storage
**Decision**: All generated scripts saved to `output/sample_scripts.md` in dedicated subfolder
**Rationale**: Clean project organization with output files separated from source code
**Implementation**: Auto-save functions in script generator tool with output folder structure

### 5. 30-Second Format Standardization
**Decision**: Standardize all video scripts to exactly 30 seconds
**Rationale**: 30-second content has highest completion rates and algorithm favorability on social platforms
**Implementation**: Updated all existing scripts and set generator tool to default to 30-second format

## Development History

### Phase 1: Research & Planning
- Analyzed 3 source files with 245+ driving safety stories
- Identified viral video formats from successful templates
- Created comprehensive project plan with user approval

### Phase 2: Database Creation
- Extracted 90 highest-engagement stories from sources
- Added metadata: themes, emotions, suggested formats
- Structured as JSON for programmatic access

### Phase 3: Script Generator Tool
- Built Python tool with 6 format generation methods
- Implemented dynamic content creation (no placeholders)
- Added Novo brand messaging integration
- Created file saving functionality

### Phase 4: Sample Generation
- Generated 8 sample scripts across different formats
- Demonstrated variety: comedy, educational, transformation, etc.
- Included Arizona regional variant for geographic targeting

### Phase 5: Documentation & Organization
- Consolidated all scripts into single master file in output folder
- Created comprehensive documentation system
- Built auto-update slash command for maintenance
- Organized project with clean output folder structure

### Phase 6: Maturity & Automation
- Project reached 500+ lines of production Python code
- Implemented automated documentation maintenance system
- Enhanced file organization with dedicated output structure
- Created self-maintaining documentation ecosystem

### Phase 7: Format Optimization
- **30-Second Standardization**: All scripts updated to 30-second format
- **Rationale**: Maximizes engagement on TikTok, Instagram Reels, YouTube Shorts
- **Data-Driven**: Shorter content has higher completion rates and algorithm preference
- **Implementation**: Updated all existing scripts and generator defaults

### Phase 8: Comprehensive Tracking System
- **Full Progress Tracking**: Added status, completion dates, and file locations to all 90 stories
- **Analytics Dashboard**: Built `tracking_dashboard.py` with real-time progress monitoring
- **Auto-Tracking**: Script generator automatically updates completion status on generation
- **Smart Suggestions**: Algorithm recommends next stories based on engagement + theme diversity
- **Current Status**: 7/90 stories completed (7.8% completion rate)
- **Data-Driven Insights**: Analytics show theme distributions, format preferences, and optimal story selection

### Phase 9: Multi-Product Platform Evolution (Latest)
- **System Restructure**: Moved from single "Story Scripting" to dedicated "Insurance_Scripts"
- **Shared Resources**: Created common Story Bank accessible across all product systems
- **Product Cloning**: Created Crypto_Scripts and App_Scripts as identical starting points
- **Architecture Documentation**: Established decision log and multi-product governance
- **Independent Tracking**: Each product maintains separate progress tracking
- **Foundation Role**: Insurance system serves as proven foundation for other products

## Technical Architecture

### Core Components
1. **story_database.json**: Structured data with 90 stories + metadata + tracking fields
2. **script_generator.py**: Main tool with 6 format generators + auto-tracking
3. **tracking_dashboard.py**: Analytics and progress monitoring system
4. **output/sample_scripts.md**: Master repository of generated scripts
5. **update-docs.md**: Slash command for documentation maintenance

### Data Flow
```
Source Stories → Database → Generator Tool → Formatted Scripts → Master File
                    ↓              ↓              ↓
               Tracking Fields → Auto-Update → Analytics Dashboard
```

### Quality Assurance Pipeline
- Real engagement verification
- Format structure validation
- Novo brand alignment check
- Production readiness review
- **Automated progress tracking and validation**

## Success Metrics

### Engagement Verification
- Stories range from 5K to 160K+ upvotes
- All sources include comment counts
- Themes mapped to audience interests

### Format Diversity
- 6 different viral video formats supported
- **30-second standardized duration** for maximum engagement
- Optimized for TikTok, Instagram Reels, YouTube Shorts

### Brand Integration
- 8 different Novo messaging variations
- Natural contextual placement
- Mission-aligned content themes

## Lessons Learned

### What Worked Well
1. **Real story approach**: Authenticity beats templates
2. **Format variety**: Different stories need different treatments
3. **Metadata richness**: Themes and emotions guide format selection
4. **Organized storage**: Output folder keeps generated files separate and clean
5. **Comprehensive tracking**: Full visibility into project progress and intelligent story selection

### Challenges Overcome
1. **Source consolidation**: 245+ stories → 90 highest-engagement
2. **Format mapping**: Manual curation to match stories to formats
3. **Brand integration**: Natural messaging without forced promotion
4. **File organization**: Implemented clean output folder structure
5. **Progress visibility**: Built comprehensive tracking system for project management

## Current Project Status (Auto-Updated)

### Project Metrics
- **Codebase**: 800+ lines of Python (script_generator.py + tracking_dashboard.py)
- **Database**: 1,200+ lines of JSON with 90 verified stories + tracking fields
- **Scripts**: 7 completed scripts in output folder (375+ lines)
- **Progress**: 7.8% completion rate with 83 stories pending
- **Documentation**: 14 files totaling 3,500+ lines
- **Automation**: Self-maintaining documentation + tracking system active

### System Health
✅ **All documentation synchronized** with current codebase  
✅ **Output folder structure** implemented and functional  
✅ **Auto-save capabilities** working in script generator  
✅ **Brand integration** consistent across all scripts  
✅ **Quality assurance** maintained throughout  
✅ **Comprehensive tracking system** operational with analytics dashboard  
✅ **Auto-progress updates** functional in script generation workflow

## Future Development Notes

### Immediate Opportunities
- Convert high-engagement pending stories (160K+ upvotes available)
- Balance theme diversity using dashboard suggestions
- Add more story themes (winter driving, teen drivers, etc.)
- Create regional variants for different states  
- Develop format-specific optimization
- Add A/B testing capabilities
- Implement performance tracking for generated scripts

### Scaling Considerations
- Database could grow to 200+ stories
- Additional video formats could be added
- Brand messaging could be customized by audience
- Performance tracking could inform story selection

### Technical Improvements
- Add story freshness scoring
- Implement engagement prediction
- Create automated story sourcing
- Build performance analytics
- Enhance tracking dashboard with time-series data
- Add completion goal setting and deadline tracking

## Key Files & Responsibilities

### Core Files
- `story_database.json`: Single source of truth for all story data + tracking
- `script_generator.py`: Main generation engine, handles all formats + auto-tracking
- `tracking_dashboard.py`: Analytics, progress monitoring, and smart suggestions
- `output/sample_scripts.md`: Master script repository, updated by tool
- `README.md`: User-facing documentation and setup instructions

### Documentation Files
- `Video Script Generation Plan.md`: Complete process documentation
- `CLAUDE.md`: This file - project memory and context
- `update-docs.md`: Slash command for documentation maintenance

### Source Material
- `Story Bank/`: Original research files (3 sources)
- Maintained for reference, not used directly in generation

## Brand Alignment

### Novo Mission Integration
Every script connects to Novo's core messages:
- Rewarding safe driving behavior
- Empowering drivers with technology
- Transforming insurance through innovation
- Creating corridors of care on roads

### Content Strategy
- Educational content that helps drivers
- Emotional stories that resonate personally  
- Community-building through shared experiences
- Technology appreciation without being pushy

## Quality Standards

### Script Requirements
- ✅ No placeholder content - all actual stories
- ✅ Verified engagement numbers from sources
- ✅ Time markers for production efficiency
- ✅ Visual directions for each segment
- ✅ Natural Novo brand integration
- ✅ Optimized CTAs for social platforms

### Documentation Standards
- Keep all docs current with code changes
- Maintain single source of truth approach
- Use clear, actionable language
- Include examples and usage patterns

---

*This project successfully transforms authentic driving safety stories into production-ready viral video content that authentically represents Novo's mission and values.*