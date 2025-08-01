# Multi-Product Video Generation System

A comprehensive suite of tools for generating viral short video scripts from high-engagement stories across multiple product brands, all focused on road safety messaging.

## ✨ **Enhanced with Universal Workflow Guidelines**

All projects now include advanced video production capabilities:
- **URL Validation**: Critical pre-processing validation that stops invalid URLs immediately
- **Failure Tracking**: Stories with invalid URLs are marked as failed and excluded from completion rates
- **Video Extraction**: Automatic extraction of embedded videos from Reddit posts
- **Content Scraping**: Original post content retrieval for authentic storytelling  
- **Scene Optimization**: ≤10 second scene timing for optimal production workflow
- **Production Assets**: Organized video/ and post/ folders for each project

## 🎯 Overview

This system evolved from a single-product (Novo Insurance) video script generator into a multi-product platform supporting:

- **Insurance Products**: Claims prevention, risk reduction messaging
- **Cryptocurrency Products**: Digital security meets road safety
- **Mobile App Products**: Real-time safety alerts and features

All products share the same core road safety mission while targeting different audiences and use cases.

## 📁 Project Structure

```
Novo Video Generation/
├── README.md                      # This overview file
├── ARCHITECTURE_DECISIONS.md      # Decision log and rationale
├── UNIVERSAL_WORKFLOW_GUIDELINES.md # Workflow standards for all projects
├── CLAUDE_WORKFLOW_INSTRUCTIONS.md # Claude Code instruction templates
├── Shared_Resources/              # Common utilities and assets
│   ├── workflow_utils.py          # Video extraction & content scraping utilities
│   └── Story Bank/                # Original research materials
├── Insurance_Scripts/             # Insurance product system
│   ├── story_database.json        # 90 stories with insurance focus
│   ├── script_generator.py        # Enhanced with workflow capabilities
│   ├── tracking_dashboard.py      # Progress analytics
│   ├── video/                     # Extracted video assets
│   ├── post/                      # Scraped original content
│   └── output/                    # Generated scripts
├── SECRET_SAUCE_ANALYSIS.md       # Strategic value analysis & future roadmap
├── Crypto_Scripts/                # Cryptocurrency product system (SPT)
│   ├── story_database.json        # 55 curated SPT-aligned stories
│   ├── script_generator.py        # Enhanced with scraped content authenticity
│   ├── tracking_dashboard.py      # Independent tracking 
│   ├── stories/                   # Per-story complete production packages
│   ├── video/                     # Legacy extracted video assets
│   ├── post/                      # Legacy scraped original content
│   └── output/                    # SPT-specific scripts
├── App_Scripts/                   # Mobile app product system
│   ├── story_database.json        # Same stories, app perspective  
│   ├── script_generator.py        # App branding (to be customized)
│   ├── tracking_dashboard.py      # Independent tracking
│   └── output/                    # App-specific scripts
├── Shared_Resources/              # Common assets
│   └── Story_Bank/               # Original research materials
└── Prompt Testing/               # AI video generation prompts
    ├── README.md                 # Pigeon character system
    └── [prompt files]            # Character-based video prompts
```

## 🚀 Quick Start

### Choose Your Product

Each product has its own complete system:

**Insurance Scripts:**
```bash
cd Insurance_Scripts
python3 tracking_dashboard.py  # View progress
python3 script_generator.py    # Generate scripts
```

**Crypto Scripts:**
```bash
cd Crypto_Scripts  
python3 tracking_dashboard.py  # Independent tracking
python3 script_generator.py    # Crypto-focused scripts
```

**App Scripts:**
```bash
cd App_Scripts
python3 tracking_dashboard.py  # App-specific analytics
python3 script_generator.py    # App-focused scripts
```

### Current Status

- **Insurance_Scripts**: ✅ Fully operational (7/90 stories completed - 7.8%)
- **Crypto_Scripts**: 🚀 **Revolutionary upgrade complete** - Scraped content authenticity implemented
- **App_Scripts**: 🔄 Cloned system, awaiting brand customization

### Strategic Value Analysis

The **Crypto_Scripts** system now includes comprehensive strategic analysis in `SECRET_SAUCE_ANALYSIS.md`:
- **Value Proposition**: Authentic, community-verified viral content vs generic templates
- **Competitive Advantage**: Real Reddit data with 10K+ upvote validation
- **Future Roadmap**: Template-based intelligence and digital persona filtering concepts
- **Macro Pipeline**: Complete concept → video creation workflow analysis

## 🔧 System Features

### Each Product System Includes:
- **90 verified stories** from Reddit with high engagement (5K-160K upvotes)
- **6 viral video formats**: Comedy, Educational, Transformation, Storytelling, POV, Challenge
- **30-second standardized** scripts optimized for social media
- **URL validation system** that prevents processing of invalid stories
- **Failure tracking** with detailed reason logging and dashboard visibility
- **Progress tracking** with completion analytics (excluding failed stories)
- **Smart suggestions** for next stories to convert
- **Brand-specific messaging** (customizable per product)

### Shared Resources:
- **Original story research** from Reddit, YouTube sources
- **Architectural decisions** documentation
- **Template systems** for new product addition

## 📊 Analytics Dashboard

Each product maintains independent analytics with failure tracking:

```python
from tracking_dashboard import TrackingDashboard

# Product-specific dashboard
dashboard = TrackingDashboard('story_database.json')
dashboard.print_dashboard()

# View failed stories separately
failed_stories = dashboard.get_failed_stories(5)

# Get smart suggestions for next stories (excludes failed)
suggestions = dashboard.get_next_story_suggestions(5)
```

### Dashboard Features:
- **Overview Statistics**: Total, completed, pending, in-progress, and failed story counts
- **Completion Rate**: Calculated excluding failed stories from total processable
- **Failed Story Display**: Shows failure reasons and dates when stories exist
- **Theme & Format Analytics**: Breakdown by content categories
- **Smart Suggestions**: Algorithm-based recommendations for optimal story selection

## 🎬 Script Generation

### Basic Usage (Same for All Products):
```python
from script_generator import VideoScriptGenerator

# Initialize generator with URL validation capabilities
generator = VideoScriptGenerator('story_database.json')

# Enhanced script generation with URL validation
result = generator.generate_enhanced_script(story_id=25, format_override='comedy')

# Generate and save with auto-tracking (includes URL validation)
result = generator.generate_and_save_script(story_id=25, format_override='comedy')
```

### Script Generation Features:
- **URL Validation**: Automatically validates story URLs before processing
- **Immediate Failure Handling**: Stops processing and marks stories as failed if URLs are invalid
- **Enhanced Content**: Uses scraped original content when available
- **Scene Optimization**: Validates scene timing (≤10 seconds per scene)
- **Auto-Tracking**: Updates completion status and failure tracking automatically

## 🔄 Customization Workflow

### Current Phase: System Cloning ✅
- Insurance system serves as proven foundation
- Crypto and App systems are identical clones
- All systems immediately functional

### Next Phase: Brand Customization 🔄
*Awaiting brand guidelines for crypto and app products*

1. **Update Brand Messaging**: Customize `script_generator.py` messaging arrays
2. **Story Adaptation**: Modify story lessons and focus for each product
3. **Theme Customization**: Adapt themes and categorizations  
4. **Story Pruning**: Remove irrelevant stories, add product-specific ones

## 📋 Development Guidelines

### Adding New Products:
1. Clone `Insurance_Scripts` to `New_Product_Scripts`
2. Update brand messaging in `script_generator.py`
3. Customize stories in `story_database.json`
4. Update product documentation
5. Add entry to this master README

### Shared Resources:
- Use `Shared_Resources/Story_Bank/` for new story research
- Document decisions in `ARCHITECTURE_DECISIONS.md`
- Keep template files in shared location

## 📞 Support & Documentation

### Product-Specific Documentation:
- `Insurance_Scripts/README.md` - Insurance system details
- `Crypto_Scripts/README.md` - Crypto system details (to be customized)
- `App_Scripts/README.md` - App system details (to be customized)

### System Documentation:
- `ARCHITECTURE_DECISIONS.md` - Decision rationale and evolution
- `Shared_Resources/Story_Bank/` - Original research materials
- Each product's `CLAUDE.md` - Development context and history

## 🎯 Road Safety Mission

Despite different products, all systems share the core mission:
> "Transform road safety awareness into engaging, viral content that saves lives while naturally promoting product benefits"

Each product approaches this mission through their unique value proposition:
- **Insurance**: Risk reduction and claims prevention
- **Crypto**: Digital security parallels with physical safety  
- **App**: Technology solutions for real-time safety

---

## 🔄 Current Project Status

| Product | Stories | Scripts | Completion | Status |
|---------|---------|---------|------------|---------|
| Insurance | 90 | 7 | 7.8% | ✅ Active Production |
| Crypto | 90 | 7* | 7.8%* | 🔄 Awaiting Customization |
| App | 90 | 7* | 7.8%* | 🔄 Awaiting Customization |

*\*Cloned data - will be customized per brand guidelines*

---

*Built to transform authentic road safety stories into viral video content across multiple products, all united by the mission of making roads safer for everyone.*