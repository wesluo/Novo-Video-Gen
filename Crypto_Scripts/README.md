# SPT Safe Driving Token Video Script Generation System

Complete viral video script generation platform for SPT (Safety Promotor Token) - the web3 rewards ecosystem that incentivizes safe driving through daily token rewards.

> **Status**: ✅ **Fully Operational** - Complete SPT brand integration with compliance-focused messaging for token reward community building.

## 🎯 Purpose

Transform authentic driving safety stories into compelling, viral video scripts that inspire safe driving behavior and promote SPT's token reward ecosystem. Target safe driving app users who value community, rewards, and technology-enabled safety.

## 📁 SPT Scripts Structure

```
Crypto_Scripts/                       # SPT token reward system
├── README.md                         # This file
├── CLAUDE.md                        # SPT project memory
├── SPT.md                           # Product background & branding guidelines
├── SPT Mission Statement.md         # Vision and values
├── Video Script Generation Plan.md  # Process documentation
├── story_database.json             # 55 curated stories with SPT themes
├── script_generator.py             # 🆕 Enhanced with scraped content authenticity
├── tracking_dashboard.py           # SPT-specific analytics
├── stories/                        # 🆕 Per-story complete workflow artifacts
│   └── story_###_title/            # Individual story folders
│       ├── script.md               # Generated script with authentic data
│       ├── original_post.md        # Scraped Reddit content
│       ├── video.mp4               # Downloaded video assets
│       ├── metadata.json           # Complete workflow information
│       └── generation_log.txt      # Process execution logs
├── output/                         # Legacy script repository
│   └── sample_scripts.md          # Master SPT script repository
└── ../Shared_Resources/            # 🆕 Enhanced workflow capabilities
    ├── workflow_utils.py           # URL validation, content scraping, video extraction
    └── url_correction.py           # Dual-method URL correction system
```

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- JSON support (built-in)
- **🆕 Enhanced Dependencies:**
  - `requests` - Web scraping and API calls
  - `yt-dlp` - YouTube video downloading
  - `beautifulsoup4` - HTML parsing
  - `praw` - Reddit API access (optional)

### Installation
1. Navigate to the `Crypto_Scripts` directory
2. Ensure `story_database.json` exists with SPT themes
3. Review `SPT.md` for branding compliance guidelines

### Basic Usage
```python
from script_generator import VideoScriptGenerator

# Initialize the SPT generator with URL validation
generator = VideoScriptGenerator('story_database.json')

# Enhanced script generation with URL validation and content scraping
script = generator.generate_enhanced_script(story_id=1)
print(script)

# Generate and save with auto-tracking (includes URL validation)
result = generator.generate_and_save_script(story_id=1, format_override='educational_hook')

# View analytics dashboard with failure tracking
from tracking_dashboard import TrackingDashboard
dashboard = TrackingDashboard('story_database.json')
dashboard.print_dashboard()  # Shows failed stories and completion rates
```

## 🛡️ **Enhanced Workflow Features (2025-07-31)**

### 🔍 URL Validation & Correction System
- **Pre-Processing Validation**: Checks story URLs before any script generation
- **STOP IMMEDIATELY**: Invalid URLs halt processing and mark stories as failed
- **Dual-Method Correction**: Automatic URL fixing with Reddit API + scraping fallback
- **Failure Tracking**: Failed stories are logged with specific reasons
- **Dashboard Visibility**: Analytics show failed stories separately from active ones

### 📄 Content Scraping & Authenticity
- **Real Reddit Data**: Scripts use actual post titles, engagement metrics, community voice
- **Content Source Attribution**: All scripts labeled with authentic content sources
- **Community Integration**: Top comments included in script metadata
- **Fallback Handling**: Posts with no selftext use top comments and video context

### 🎬 Video Asset Management
- **Automatic Download**: YouTube videos extracted and saved per story
- **Complete Archives**: Each story folder contains all production assets
- **Metadata Tracking**: Video duration, resolution, view counts captured
- **yt-dlp Integration**: Professional-grade video downloading capabilities

### ⏱️ Dynamic Scene Generation
- **No More Hardcoding**: All scene timing generated dynamically
- **≤10 Second Compliance**: Every scene respects global timing rules
- **Format-Specific Structure**: Each video format has optimized scene templates
- **Timing Display**: Clear scene markers like "HOOK (0-3 seconds)"

## 📊 Strategic Value Analysis

### 🎯 System Value Proposition
This system transforms **generic template-based content creation** into **authentic, community-verified viral content production** with proven engagement metrics. See `../SECRET_SAUCE_ANALYSIS.md` for comprehensive analysis.

**Key Differentiators:**
- **Authenticity at Scale**: Real Reddit data with 10K+ upvote validation
- **Complete Production Packages**: Scripts + content + videos + metadata
- **Template-Based Intelligence**: Future roadmap for proven sample libraries
- **Digital Persona Filtering**: Potential market segment optimization

### SPT-Focused Script Generation
```python
# Generate community movement content
community_script = generator.generate_script(
    story_id=1,  # "Technology saves story"
    format_override='educational_hook'
)
# Output: "This smart choice could have earned them SPT tokens"

# Generate app download content
app_script = generator.generate_random_script(theme='smart_choices_rewarded')
# Focuses on SP Drive app adoption and daily token earning
```

## 🎁 SPT Brand Integration

### Core Messaging Framework
- **Drive Smart. Get Rewarded.** - Primary tagline
- **Every Safe Mile Counts** - Community impact focus
- **Real Rewards for Real Safety** - Utility emphasis
- **Join the SPT Movement** - Community building

### Compliance Requirements
✅ **Allowed**: Utility focus, gift card rewards, community impact, app downloads  
❌ **Prohibited**: Token price speculation, investment gains, financial returns

### Target Audience
- SP Drive app users seeking daily token rewards
- Safe driving community members
- Technology-forward drivers interested in gamification
- Community-minded individuals building safer roads

## 📊 Current Status (SPT Initialized)

- **Total Stories**: 55 curated SPT-aligned stories (filtered from 90)
- **Completed Scripts**: 0 (ready for production generation)
- **Pool Status**: ✅ Curated and transformed for SPT alignment
- **Brand Messaging**: ✅ 100% SPT-compliant, zero financial speculation
- **Story Focus**: ✅ Token earning behaviors and community building
- **Sample Scripts**: 2 production-ready examples generated

## 🎬 SPT Script Examples

### Before/After Transformation:

**Technology Saves Story**
- **Before**: "Dashcam evidence is invaluable for proving fault"
- **SPT Version**: "Technology like dashcams rewards smart drivers with evidence and protection - earn SPT tokens for using SP Drive"

**Smart Choices Story**
- **Before**: "Road rage can escalate quickly - stay calm"
- **SPT Version**: "Staying calm and documenting incidents shows the smart driving that SPT rewards - join thousands earning daily tokens"

## 🔄 Script Format Options

### 6 Viral Video Formats Available:
1. **Educational Hook** - "This SPT token earning tip..."
2. **Transformation** - "From risky driving to rewarded safety"
3. **Storytelling** - "How SPT movement changes lives"
4. **POV** - "Your daily SPT token earning moment"
5. **Comedy** - "When safe driving pays off (literally)"
6. **Challenge** - "Join the SPT Safe Driving Challenge"

All formats optimized for:
- ✅ 30-second duration (TikTok, Instagram Reels, YouTube Shorts)
- ✅ SPT brand compliance (no financial speculation)
- ✅ App download optimization
- ✅ Community movement building

## 📈 SPT Tracking & Analytics

### Progress Monitoring
- Individual story completion tracking
- SPT theme distribution analysis
- Compliance monitoring (zero speculation content)
- Community engagement optimization

### Theme Categories
- `technology_saves`: Apps and tech helping drivers
- `smart_choices_rewarded`: Decisions SPT would reward
- `community_movement`: Drivers building safer roads together
- `defensive_success`: Proactive safety preventing incidents
- `habit_formation`: Building consistent safe driving
- `daily_rewards_earned`: Behaviors earning daily tokens

## 🛠️ Advanced Features

### Compliance Framework
Built-in checking for:
- ❌ Financial speculation language
- ❌ Investment return promises
- ❌ Token price discussions
- ✅ Utility and real-world rewards focus
- ✅ Community impact messaging
- ✅ App adoption encouragement

### Community Building Tools
- Movement-focused messaging
- App download CTAs
- Token earning behavior connections
- Safety culture reinforcement

## 📞 Support & Development

### Project Files:
- `SPT.md` - Complete product background and branding guidelines
- `SPT Mission Statement.md` - Vision, values, and commitments
- `CLAUDE.md` - Comprehensive project memory and context
- `story_database.json` - 55 curated stories with SPT alignment verified

### Success Metrics:
- ✅ Real story authenticity (5K-160K+ Reddit upvotes)
- ✅ SPT brand alignment (100% compliance)
- ✅ Community building potential
- ✅ App download optimization
- ✅ Token earning behavior inspiration

### Quality Standards:
- Zero placeholder content
- Verified engagement numbers
- 30-second social-optimized format
- Natural SPT integration
- Movement building focus

---

**Drive Smart. Get Rewarded. Build Community.**

*Transform authentic driving safety stories into SPT community content that inspires safe driving behavior, promotes app adoption, and builds the movement for safer roads through token rewards.*