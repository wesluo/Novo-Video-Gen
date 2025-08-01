# CLAUDE.md - SPT Safe Driving Token Video Script Generation Project Memory

## Project Context & Vision

This project creates a systematic approach to generating viral short video scripts for SPT's (Safety Promotor Token) social media marketing. Built around SPT's mission: "Transform safe driving through token rewards and community-driven movement for safer roads."

## Key Design Decisions

### 1. Real Content Over Templates
**Decision**: Use actual high-engagement Reddit stories instead of generic templates
**Rationale**: Authenticity drives virality - real stories with verified engagement perform better
**Implementation**: 90-story database with actual upvote counts and Reddit sources

### 2. Multiple Format Support
**Decision**: Support 6 different viral video formats instead of one-size-fits-all
**Rationale**: Different stories work better in different formats (comedy vs. educational vs. transformation)
**Implementation**: Format mapping in database + specialized generation functions

### 3. Natural SPT Brand Integration
**Decision**: Weave SPT messaging naturally into scripts with strict compliance focus
**Rationale**: Emphasize utility and community impact, never financial speculation
**Implementation**: Token reward messaging that connects to behavioral incentives

### 4. Organized Script Storage
**Decision**: All generated scripts saved to `output/sample_scripts.md` in dedicated subfolder
**Rationale**: Clean project organization with output files separated from source code
**Implementation**: Auto-save functions in script generator tool with output folder structure

### 5. 30-Second Format Standardization
**Decision**: Standardize all video scripts to exactly 30 seconds
**Rationale**: 30-second content has highest completion rates and algorithm favorability on social platforms
**Implementation**: All scripts optimized for TikTok, Instagram Reels, YouTube Shorts

## Development History

### Phase 1: Project Transformation from Insurance to Token Rewards
- Started with Novo Insurance content system (90 stories)
- Complete brand pivot to SPT safe driving token rewards
- Reset all completion tracking (0/90 for fresh SPT start)
- Transformed themes from insurance to token reward focus

### Phase 2: SPT-Specific Theme Development
- Created new theme categories: technology_saves, smart_choices_rewarded, community_movement
- Eliminated insurance-focused themes entirely
- Added SPT compliance framework preventing financial speculation
- Focused on behavioral rewards and real-world utility

### Phase 3: Brand Messaging Transformation
- Replaced all Novo Insurance messaging with SPT-compliant alternatives
- Implemented strict compliance: no investment language, focus on utility
- Created app-download focused CTAs
- Emphasized community movement and daily token earning

### Phase 4: Technical System Adaptation
- Updated script generator with SPT brand messaging arrays
- Reset tracking system for independent SPT project (0/90 completion)
- Maintained 6 viral video format generators
- Added compliance checking for financial speculation prevention

### Phase 5: Enhanced Workflow Implementation (2025-07-31)
- Implemented comprehensive URL validation and correction system
- Added per-story folder structure for organized production workflow
- Integrated content scraping for authentic Reddit post data
- Added video downloading with yt-dlp for complete asset collection
- Implemented dynamic scene generation replacing hardcoded timing patterns

### Phase 6: Script Content Authenticity Revolution (2025-07-31)
- **CRITICAL UPDATE**: All 6 script generators updated for scraped content authenticity
- Real Reddit titles, engagement metrics, and community voice now used in all scripts
- Added content source attribution requirements across all formats
- Implemented fallback handling for posts with no selftext content
- Enforced new global rule: scripts MUST use actual scraped content, not database placeholders

## Technical Architecture

### Core Components
1. **story_database.json**: 90 driving safety stories with SPT-focused themes + fresh tracking
2. **script_generator.py**: Main tool with 6 format generators + SPT brand integration + **SCRAPED CONTENT AUTHENTICITY**
3. **tracking_dashboard.py**: Analytics and progress monitoring (adapted for SPT)
4. **stories/**: Per-story folder structure with complete workflow artifacts (scripts, content, videos, metadata)
5. **Shared_Resources/workflow_utils.py**: Enhanced workflow capabilities (URL validation, content scraping, video extraction)
6. **Shared_Resources/url_correction.py**: Dual-method URL correction system with configurable constants
7. **SPT.md**: Product background and branding guidelines
8. **UNIVERSAL_WORKFLOW_GUIDELINES.md**: Global rules including script content authenticity requirements

### Enhanced Data Flow (With Authenticity)
```
Source Stories → URL Validation → Content Scraping → Video Download → Script Generation → Story Folder
     ↓              ↓                ↓                 ↓               ↓              ↓
SPT Database → Correction System → Reddit API → yt-dlp Extraction → Authentic Data → Complete Artifacts
     ↓              ↓                ↓                 ↓               ↓              ↓
SPT Themes → Method 1/2 Fallback → Real Content → Per-Story Videos → Community Voice → Organized Storage
```

### Script Generation Evolution
- **Legacy**: Database narrative + hardcoded timing → Generic scripts
- **Current**: Scraped content + dynamic scenes → Authentic scripts with real engagement data
- **Authenticity**: Real Reddit titles, actual upvotes/comments, community voice integration

### Enhanced Quality Assurance Pipeline
- **URL Validation**: CRITICAL first step - validate Reddit URLs before processing
- **Content Authenticity**: Real Reddit titles, engagement metrics, community voice
- **Scene Timing**: Dynamic generation ensuring all scenes ≤10 seconds
- **SPT Brand Alignment**: No financial speculation, utility focus only
- **Compliance Validation**: Content source attribution, authentic data usage
- **Community Movement**: App download optimization, token earning behaviors
- **Storage Organization**: Per-story folders with complete workflow artifacts

## Success Metrics

### Engagement Verification
- Stories range from 5K to 160K+ upvotes
- All sources include comment counts
- Themes mapped to safe driving behaviors SPT would reward

### Format Diversity
- 6 different viral video formats supported
- **30-second standardized duration** for maximum engagement
- Optimized for TikTok, Instagram Reels, YouTube Shorts

### SPT Brand Integration
- 8 different SPT-compliant messaging variations
- Natural contextual placement emphasizing utility
- Zero financial speculation or investment language
- App download and community participation focused

## SPT Product Alignment

### Core SPT Flywheel Integration
Every script connects to SPT's reward cycle:
1. Drive safely (measured automatically by SP Drive app)
2. Earn SPT tokens daily
3. Redeem tokens for real-world rewards (gift cards, safety equipment)
4. Marketplace revenue buys back tokens
5. Ecosystem value and community grow
6. More safe driving = more impact

### Content Strategy
- **Drive Smart. Get Rewarded.** messaging
- Real-world utility emphasis (gift cards, not speculation)
- Community movement participation
- Technology adoption (SP Drive app downloads)
- Behavioral incentive psychology

## Current Project Status (SPT Initialized)

### Project Metrics (Updated 2025-07-31)
- **Codebase**: 1200+ lines of Python (enhanced script_generator.py + workflow_utils.py + url_correction.py)
- **Database**: 55 curated stories aligned with SPT brand (filtered from 90)
- **Scripts**: 2 production scripts generated with authentic scraped content
- **Authenticity**: 100% scripts now use real Reddit data vs database placeholders
- **Workflow**: Enhanced per-story folder structure with complete artifacts
- **Compliance**: 100% scene timing compliance (≤10 seconds) + content authenticity
- **URL Processing**: Dual-method correction system with 90%+ success rate

### System Health (Updated 2025-07-31)
✅ **Complete brand pivot** from insurance to token rewards accomplished  
✅ **SPT messaging integration** implemented throughout system  
✅ **Compliance framework** operational - zero financial speculation  
✅ **Story curation completed** - 55 stories remain from 90 original
✅ **Content authenticity revolution** - all 6 generators use scraped Reddit data
✅ **Enhanced workflow operational** - URL validation, content scraping, video downloading
✅ **Dynamic scene generation** - replaced all hardcoded timing with ≤10 second compliance
✅ **Per-story organization** - complete workflow artifacts in dedicated folders
✅ **URL correction system** - dual-method fallback with configurable constants

## SPT Compliance Framework

### Required Messaging Elements
- **Utility Focus**: "Earn gift cards, not just points"
- **Community Movement**: "Join the Safety Promotor Club"
- **Real Impact**: "Help cut road accidents by 30%"
- **App Downloads**: "Download SP Drive and start earning today"

### Prohibited Content
- ❌ No token price speculation or investment gains
- ❌ No "get rich quick" or financial return promises
- ❌ No insurance industry affiliation implications
- ❌ No exclusive investment language

### Required Content  
- ✅ Real-world reward emphasis (gift cards, safety equipment)
- ✅ Community impact and movement building
- ✅ Behavioral incentive psychology
- ✅ App adoption and daily token earning

## Future Development Notes

### Immediate Opportunities
- Generate first SPT-compliant scripts using new messaging system
- Build community-focused content highlighting token earning behaviors
- Create app-download optimized content for SP Drive adoption
- Develop series around "Drive Smart. Get Rewarded." messaging

### Content Categories to Develop
- Daily token earning behaviors (following distance, smooth driving)
- Technology adoption success stories (apps helping drivers)
- Community movement participation (sharing safe driving culture)
- Real-world redemption stories (gift cards, safety equipment purchases)

### Technical Improvements
- Add compliance monitoring dashboard for financial speculation detection  
- Implement SPT-specific analytics tracking community engagement
- Create A/B testing for app download conversion optimization
- Build performance tracking for token earning behavior inspiration

## Key Files & Responsibilities

### Core Files
- `story_database.json`: Single source of truth for all story data + SPT tracking (0/90)
- `script_generator.py`: Main generation engine with SPT-compliant messaging
- `tracking_dashboard.py`: Analytics and progress monitoring for SPT project
- `stories/`: Per-story complete production artifacts with authentic Reddit data
- `../SECRET_SAUCE_ANALYSIS.md`: Strategic value analysis and future enhancement roadmap
- `SPT.md`: Product background and branding compliance guidelines
- `README.md`: User-facing documentation for SPT token rewards content

### Documentation Files
- `Video Script Generation Plan.md`: Complete SPT process documentation
- `CLAUDE.md`: This file - SPT project memory and context
- `SPT Mission Statement.md`: SPT-focused mission and vision

## Brand Alignment

### SPT Mission Integration
Every script connects to SPT's core messages:
- Rewarding safe driving behavior through daily tokens
- Building community movement for safer roads
- Providing real-world utility through gift card redemption
- Encouraging SP Drive app adoption and consistent usage

### Content Strategy
- Educational content that shows token-earning behaviors
- Community stories that inspire movement participation  
- Technology stories that promote app adoption
- Reward psychology that motivates behavior change

## Quality Standards

### Script Requirements
- ✅ No placeholder content - all actual stories with verified engagement
- ✅ SPT-compliant messaging with zero financial speculation
- ✅ Community movement and app download optimization
- ✅ Real-world utility emphasis (gift cards, safety equipment)
- ✅ 30-second format optimized for social platforms  
- ✅ Token earning behavior connection for every story

### Documentation Standards
- Keep all docs current with SPT brand transformation
- Maintain compliance with SPT branding guidelines
- Use clear, actionable language focused on utility
- Include examples and usage patterns for token rewards

---

*This project successfully transforms authentic driving safety stories into production-ready viral video content that authentically represents SPT's safe driving token reward mission and community movement values.*