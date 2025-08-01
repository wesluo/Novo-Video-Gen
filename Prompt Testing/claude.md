# CLAUDE.md - Novo Video Generation Prompt Testing

## Project Overview

This is a **testing environment** for generating AI video prompts that combine:
- High-engagement Reddit driving incident stories (r/IdiotsInCars, r/GenZ)
- Animated pigeon characters representing Novo Insurance
- Educational safety messaging for social media

**Current Status**: Experimental testing phase - not production ready

## Project Structure Understanding

### Source Material (`scripts/` folder)
- **Origin**: Viral Reddit posts with 5K-137K upvotes
- **Content**: Real driving incidents adapted as video scripts
- **Format**: Raw, unprocessed content with Reddit-specific context
- **Issues**: Inconsistent formatting, missing visual cues, requires significant processing

### Character Definitions (`SamplePrompt.md`)
Three pigeon characters with distinct personalities:
- **Sir Reginald Featherstone III**: Aristocratic, dramatic flair
- **Lil' Beak**: Street-smart, witty, sarcastic  
- **Professor Plume**: Wise, observant, educational

### Generated Prompts (`script*_prompt.md`)
AI video generation prompts following consistent structure:
- **Hook** (0-3s) í **Exclusivity/Setup** (3-8s) í **Benefit** (8-12s) í **Reveal/Lesson** (12-22s) í **Proof** (22-27s) í **CTA + Novo** (27-30s)

## Current Methodology Analysis

**Workflow**: `Reddit Posts í Raw Scripts í [LLM Processing] í Character-Based Video Prompts`

**Approach**: Brute force combination without structured guidelines

**Strengths**:
- Proven viral content source material
- Consistent 6-stage video structure in outputs
- Character-format matching (Professor = Educational, Lil' Beak = POV/Comedy, Sir Reginald = Dramatic)

**Critical Issues** (see `insights.md`):
1. **Script Readiness Gap**: Raw scripts not optimized for prompt generation
2. **Insufficient Guidelines**: Only character descriptions, no prompt engineering framework
3. **Unguided Generation**: No templates, quality control, or optimization feedback

## Working with This Project

### When Analyzing Content
- Scripts contain Reddit-specific language requiring translation to video context
- Character assignments follow patterns but lack explicit rules
- Generated prompts show consistency despite lack of structured templates

### When Creating New Prompts
- Reference existing successful patterns in current prompts
- Maintain 30-second duration with 6-stage structure
- Match character personality to appropriate video format
- Include specific visual, animation, and audio details

### When Identifying Issues
- Look for inconsistencies in brand voice or messaging
- Check for technical completeness (timing, visual cues, etc.)
- Assess whether scripts translate effectively to video format
- Verify character personality alignment with content

## Testing Considerations

This is a **proof-of-concept environment** for understanding:
- How raw Reddit content can be transformed into branded video prompts
- Whether pigeon characters can effectively deliver safety messaging
- What prompt structures work best for AI video generation tools
- Where quality control and optimization are needed

**Not suitable for production use** without addressing identified framework gaps.

## File Relationships

```
Reddit Source í scripts/script*.md í [LLM] í script*_prompt.md
                     ë                           ì
               SamplePrompt.md êí Character matching logic
```

The `insights.md` file provides detailed analysis of this workflow and its limitations.