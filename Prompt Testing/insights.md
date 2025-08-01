# Project Insights: Novo Video Generation Prompt Testing

## Current Status: Testing Phase

This repository represents an **experimental approach** to AI video generation prompt creation for Novo Insurance's social media content. The project combines Reddit-sourced driving incident stories with animated pigeon characters to create educational safety content.

## Current Methodology

### Brute Force Approach
The current process appears to be a **brute force combination** of:
1. **Raw Scripts** (`scripts/` folder) - High-engagement Reddit posts from r/IdiotsInCars and r/GenZ
2. **Character Definitions** (`SamplePrompt.md`) - Basic appearance and personality traits for three pigeon characters
3. **LLM Generation** - AI-generated prompts without structured guidelines

### Workflow Observation
```
Reddit Posts → Raw Scripts → [LLM Processing] → Character-Based Video Prompts
```

## Key Findings

### Strengths
- **Proven Content**: Scripts sourced from viral Reddit posts (5K-137K upvotes) with demonstrated audience engagement
- **Consistent Structure**: Generated prompts follow a reliable 6-stage format (Hook → Exclusivity → Benefit → Reveal → Proof → CTA)
- **Character-Format Matching**: Each pigeon character consistently assigned to appropriate video formats

### Critical Issues Identified

#### 1. Script Readiness Gap
**Problem**: Raw scripts may not be optimized for prompt generation
- Scripts contain Reddit-specific language and context
- Inconsistent formatting across different source posts
- Missing key elements needed for video generation (visual cues, timing, transitions)

**Impact**: Requires significant LLM processing to transform raw content into video-ready prompts

#### 2. Insufficient Prompt Guidelines
**Problem**: `SamplePrompt.md` contains only character descriptions
- No prompt engineering best practices
- No video generation tool specifications
- No brand voice guidelines beyond character personalities
- Missing technical requirements (aspect ratios, duration constraints, etc.)

**Impact**: Inconsistent prompt quality and effectiveness for AI video generation tools

#### 3. Unguided LLM Generation
**Problem**: Prompt creation relies entirely on LLM interpretation
- No structured templates or frameworks
- No quality control mechanisms
- No examples of successful vs. unsuccessful prompts
- No feedback loop for prompt optimization

**Impact**: Unpredictable output quality and potential brand consistency issues

## Understanding Areas

### Script Preprocessing Considerations
- Standardization of script formatting across sources
- Extraction of key story elements (characters, conflict, resolution)
- Addition of visual description requirements
- Translation from Reddit context to video context

### Prompt Engineering Framework Needs
- Video generation tool requirements and capabilities
- Brand voice and safety messaging standards
- Technical specifications (duration, format, aspect ratio)
- Character-specific template structures

### Quality Control Aspects
- Prompt completeness verification
- Brand alignment assessment
- Technical requirement validation
- Consistency across character types and formats

### Optimization Considerations
- Performance tracking with AI video generation tools
- Engagement metrics on generated content
- Pattern recognition in successful prompts
- Common failure mode identification

## Risk Assessment

**High Risk**: Current brute force approach may produce inconsistent results unsuitable for production use

**Medium Risk**: Lack of guidelines could lead to brand voice inconsistencies or inappropriate content

**Low Risk**: Character concepts are well-defined and source material has proven engagement

## Documentation Updates

- **README.md**: Updated project structure and added testing phase status
- **CLAUDE.md**: Created comprehensive project instructions and methodology analysis
- **insights.md**: This analysis document for understanding current approach

---

*Generated: 2025-07-31*  
*Status: Testing Phase - Not Production Ready*