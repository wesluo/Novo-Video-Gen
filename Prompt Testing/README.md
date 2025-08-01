# Novo Video Generation Prompt Testing

This repository contains AI video generation prompts for Novo Insurance's social media content, featuring animated pigeon characters delivering safety messages.

## Project Structure

```
.
├── README.md                           # This file
├── SamplePrompt.md                     # Character descriptions  
├── claude.md                           # Project instructions
├── insights.md                         # Analysis of current approach and issues
├── scripts/                            # Source material folder
│   ├── sample_scripts.md              # Master list of all 8 scripts
│   └── script[1-8]_*.md               # Individual script files
└── script[1-8]_*_prompt.md            # Generated AI video prompts (8 files)
```

## Characters

Three pigeon characters from `SamplePrompt.md`:

1. **Sir Reginald Featherstone III** - Aristocratic pigeon with monocle and top hat
2. **Lil' Beak** - Street-smart pigeon with gold chain and backward cap  
3. **Professor Plume** - Elderly wise pigeon with spectacles and tweed vest

## Generated Prompts

Each prompt file adapts the pigeon characters to deliver safety messages from the original scripts:

| File | Character(s) | Format | Topic |
|------|-------------|---------|--------|
| script1_semi_truck_prompt.md | Professor Plume | Educational | Dashcam importance |
| script2_driver_violence_prompt.md | Lil' Beak | POV | Road rage incident |
| script3_bruise_saved_life_prompt.md | Sir Reginald | Dramatic | Seatbelt saves life |
| script4_good_samaritans_prompt.md | All Three | News Report | Rescue story |
| script5_alabama_roundabout_prompt.md | Professor Plume | Documentary | Traffic confusion |
| script6_jeep_thing_prompt.md | Lil' Beak | Comedy | Overconfidence fail |
| script7_boring_safe_driver_prompt.md | Sir Reginald | Challenge | Safe driving is cool |
| script8_arizona_uturn_prompt.md | Professor Plume | Educational | Michigan Left explanation |

## Prompt Structure

Each generated prompt includes:

- **Character Details**: Appearance and personality traits
- **Video Style**: Format and visual approach
- **Scene Breakdown**: Timed sections (30 seconds total)
- **Visual Elements**: Specific animation and effects
- **Tone**: Character-appropriate delivery style
- **Audio**: Sound effects and music suggestions

## Usage

These prompts are designed for AI video generation tools to create engaging 30-second social media videos that:
- Maintain Novo Insurance's safety messaging
- Leverage character personalities for engagement
- Adapt real driving incidents into educational content
- Balance entertainment with important safety lessons

## Source Material

All scripts based on high-engagement Reddit posts from r/IdiotsInCars and r/GenZ, with engagement ranging from 5,000 to 137,802 upvotes.

## Project Status

⚠️ **Testing Phase**: This project is currently in experimental testing mode. See `insights.md` for detailed analysis of the current approach, identified issues, and considerations for improvement.

**Key Limitations**:
- Brute force combination of scripts and character definitions
- No structured prompt engineering guidelines
- Unguided LLM generation without quality control
- Scripts may require preprocessing for optimal prompt generation

## Files Overview

| File Type | Purpose | Status |
|-----------|---------|--------|
| `scripts/*.md` | Source Reddit posts adapted as video scripts | Raw material |
| `script*_prompt.md` | AI video generation prompts with pigeon characters | Generated |
| `SamplePrompt.md` | Character definitions only | Basic |
| `insights.md` | Project analysis and issue identification | Analysis |