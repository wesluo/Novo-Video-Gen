# Novo Insurance Video Script Generation System

Part of the Multi-Product Video Generation Platform - specialized for insurance product messaging and Novo Insurance branding.

## 🎯 Purpose

Transform driving safety stories from Reddit and other sources into compelling, viral video scripts that align with Novo's mission of rewarding safe driving and empowering customers with technology.

## 📁 Insurance Scripts Structure

```
Insurance_Scripts/                     # This insurance-focused system
├── README.md                          # This file
├── CLAUDE.md                         # Project memory and context  
├── Video Script Generation Plan.md   # Complete process documentation
├── story_database.json              # 90+ stories with insurance focus
├── script_generator.py              # Novo Insurance branding
├── tracking_dashboard.py            # Insurance-specific analytics
├── update-docs.md                   # Slash command for documentation
├── output/                          # Generated insurance scripts
│   ├── sample_scripts.md           # All generated video scripts
│   └── arizona_variant_script.md   # Regional variant example
└── [other insurance-specific files]
```

**Part of Multi-Product Platform:**
```
../                                   # Parent directory
├── Insurance_Scripts/               # This system
├── Crypto_Scripts/                  # Cryptocurrency product system
├── App_Scripts/                     # Mobile app product system  
├── Shared_Resources/                # Common story research
│   └── Story_Bank/                 # Original research materials
└── README.md                        # Multi-product overview
```

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- JSON support (built-in)

### Installation
1. Navigate to the `Insurance_Scripts` directory from the parent multi-product system
2. Ensure `story_database.json` exists in this directory (insurance-specific stories)
3. Shared resources are available in `../Shared_Resources/Story_Bank/`

### Basic Usage

```python
from script_generator import VideoScriptGenerator

# Initialize the generator
generator = VideoScriptGenerator('story_database.json')

# Generate a specific script
script = generator.generate_script(story_id=1)
print(script)

# Generate by theme
road_rage_script = generator.generate_random_script(theme='road_rage')

# Generate and auto-save to output/sample_scripts.md (automatically tracks completion)
generator.generate_and_save_script(story_id=25, format_override='comedy')
```

### Tracking & Analytics

```python
from tracking_dashboard import TrackingDashboard

# View project progress
dashboard = TrackingDashboard('story_database.json')
dashboard.print_dashboard()

# Get suggestions for next stories to convert
suggestions = dashboard.get_next_story_suggestions(5)
```

Or run the dashboard directly:
```bash
python3 tracking_dashboard.py
```

## 📝 Script Formats Available

- **Educational Hook**: "This trick could save your life" format
- **Comedy/Relatable**: Humorous take on driving situations  
- **Transformation**: Before/after format showing change
- **Storytelling**: Emotional narrative with lesson
- **POV**: Point-of-view perspective scripts
- **Challenge**: Interactive format encouraging participation

## 📊 Database Contents

- **90 verified stories** from Reddit and YouTube
- **Engagement range**: 5,000 - 160,000+ upvotes
- **12 thematic categories**: Road rage, safety features, hero drivers, etc.
- **6 format mappings**: Each story suggests optimal video format
- **Complete metadata**: Source links, engagement metrics, themes
- **Progress tracking**: Status, completion dates, and file locations

## 🎬 Generated Scripts Include

- ✅ **Actual content** (no placeholders)
- ✅ **30-second format** optimized for maximum social media engagement
- ✅ **Visual directions** for production
- ✅ **Novo brand integration** naturally woven in
- ✅ **Engagement CTAs** optimized for social media
- ✅ **Source verification** with Reddit metrics

## 🔧 Key Features

### Story Database
- Comprehensive collection of viral driving safety content
- Verified engagement metrics from original posts
- Thematic categorization for easy filtering
- Format suggestions based on content analysis

### Script Generator
- Multiple viral video formats supported
- Natural Novo brand message integration
- Dynamic content generation (no templates)
- Automatic file saving to `output/sample_scripts.md`
- **Auto-tracking**: Completion status updated automatically

### Tracking Dashboard
- Real-time progress monitoring (7/90 stories completed - 7.8%)
- Theme and format completion breakdowns
- Smart story selection suggestions based on engagement and diversity
- Export capabilities for pending story lists

### Quality Assurance
- All scripts use real story content
- Engagement numbers verified from sources
- Brand messaging aligned with Novo mission
- Production-ready with timing and visuals

## 📈 Sample Output

View complete examples in `output/sample_scripts.md`:
- 8 different format demonstrations
- Real engagement numbers (44K+ upvotes)
- Professional video script structure
- Novo brand integration examples

## 🎯 Novo Brand Integration

Every script naturally incorporates Novo's key messages:
- "Technology and safe driving go hand in hand with Novo"
- "This is why Novo rewards safe drivers"
- "Novo believes in turning roads into corridors of care"
- "Every safe decision matters - that's the Novo way"

## 🔄 Workflow

1. **Story Selection**: Choose from 90+ verified high-engagement stories
2. **Progress Tracking**: Check dashboard for completion status and suggestions
3. **Format Matching**: Select optimal video format for the story
4. **Script Generation**: Create complete video script with timing
5. **Brand Integration**: Natural weaving of Novo messaging
6. **Auto-Tracking**: System automatically records completion and metadata
7. **Quality Check**: Verify content, timing, and CTAs
8. **Production Ready**: Scripts include all visual directions

## 📋 Usage Guidelines

- Scripts are production-ready for 9:16 vertical video
- **30-second standardized duration** for optimal social media performance
- Visual directions included for each segment
- CTAs optimized for TikTok, Instagram Reels, YouTube Shorts
- All content verified for authenticity and engagement

## 🔄 Updates & Maintenance

### Automatic Documentation Updates
Use the `/update-docs` command to automatically refresh all documentation when code changes are made:
- Detects modifications in code files and project structure
- Updates README, CLAUDE.md, and process documentation
- Maintains consistency across all project files
- Generates update reports with change summaries

### Recent Updates
- **Comprehensive Tracking System**: Full story completion tracking with dashboard analytics
- **Smart Story Suggestions**: Algorithm recommends next stories based on engagement and theme diversity
- **Auto-Progress Updates**: Script generation automatically updates completion status
- **Project Analytics**: Real-time statistics, theme breakdowns, and completion rates (7.8% done)
- **30-Second Format**: All scripts standardized to 30 seconds for maximum engagement
- **File Organization**: Implemented clean `output/` folder structure for generated scripts
- **Enhanced Generator**: Added automatic file saving and script management
- **Documentation System**: Created comprehensive auto-update slash command
- **Project Scale**: 500+ lines of Python code, 90-story database, 8+ sample scripts

## 📞 Support

For questions about script generation, refer to:
- `Video Script Generation Plan.md` - Complete process documentation
- `output/sample_scripts.md` - Format examples and structure
- `CLAUDE.md` - Project context and development notes
- `tracking_dashboard.py` - Run for progress analytics and story suggestions
- `../README.md` - Multi-product system overview
- `../ARCHITECTURE_DECISIONS.md` - System evolution and decisions

---

*Built for Novo Insurance to transform driving safety stories into viral video content that rewards safe driving and empowers customers with technology.*