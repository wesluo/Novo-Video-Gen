# Claude Code Workflow Instructions

**Version**: 1.0  
**Date**: July 30, 2025  
**For**: Insurance_Scripts, Crypto_Scripts, App_Scripts

---

## Overview

This document provides standardized Claude Code instruction templates for implementing the Universal Workflow Guidelines across all video generation projects. Use these templates to ensure consistent, high-quality results when working with video extraction, content scraping, and scene optimization.

---

## Standard Workflow Generation Prompt

### **Primary Generation Prompt Template**

```
You are working with a video generation project that follows Universal Workflow Guidelines. When generating video scripts, you MUST follow this exact sequence:

## STEP 1: VIDEO EXTRACTION
First, extract any embedded videos from the story's Reddit URL:
- Check for YouTube links, direct videos, hosting platforms
- Save video metadata to video/ subfolder with story correlation
- Use the extract_story_videos(story_id) method
- Log success/failure for debugging

## STEP 2: CONTENT SCRAPING  
Second, scrape original Reddit post content:
- Extract full post text, top comments, engagement metrics
- Save content to post/ subfolder in readable markdown format
- Use the scrape_story_content(story_id) method
- Use scraped data as foundation for authentic storytelling

## STEP 3: SCENE OPTIMIZATION
Third, generate script using ≤10 second scenes:
- Break content into scenes of 3-10 seconds each
- Maintain 30-second total duration
- Provide clear scene transitions and visual directions
- Validate timing using scene optimizer

## STEP 4: BRAND INTEGRATION
Fourth, apply project-specific brand messaging:
- **Insurance_Scripts**: Novo Insurance messaging (rewards, safety, technology)
- **Crypto_Scripts**: SPT token rewards messaging (compliance-focused, utility)
- **App_Scripts**: Mobile app download and convenience messaging

## STEP 5: QUALITY VALIDATION
Finally, validate the complete workflow:
- Confirm video extraction attempted and logged
- Verify original content scraping completed successfully
- Check all scenes are ≤10 seconds with clear transitions
- Ensure brand messaging appropriate for target project
- Add workflow metadata to final script output

Use the generate_enhanced_script() method when available, or call workflow methods individually.
```

---

## Project-Specific Generation Prompts

### **Insurance_Scripts Generation**

```
Generate a video script for Insurance_Scripts project following these guidelines:

PROJECT CONTEXT: Novo Insurance - rewards safe drivers, technology-enabled insurance
AUDIENCE: Insurance buyers focused on safety and savings  
BRAND TONE: Professional, trustworthy, educational
COMPLIANCE: Emphasize safety rewards and technology benefits

WORKFLOW REQUIREMENTS:
1. Extract videos from Reddit post using extract_story_videos(story_id)
2. Scrape original content using scrape_story_content(story_id)  
3. Generate script with ≤10 second scenes
4. Use Novo brand messaging: "This is why Novo rewards safe drivers"
5. Include CTAs: "Get a quote from Novo Insurance", "Safe drivers save with Novo"

SCENE TIMING STRUCTURE (≤10 seconds each):
- HOOK (0-3s): Attention grabber
- CREDIBILITY (3-6s): Engagement numbers  
- SETUP (6-9s): Story context
- LESSON_1 (9-12s): First learning point
- LESSON_2 (12-15s): Second learning point
- PROOF (15-18s): Community validation
- BRAND_CONNECTION (18-21s): Novo messaging
- CTA (21-24s): Insurance call-to-action
- SAFETY_MESSAGE (24-27s): Final safety tip
- CLOSING (27-30s): Novo branding

Generate using: generator.generate_enhanced_script(story_id, use_scraped_content=True)
```

### **Crypto_Scripts (SPT) Generation**

```
Generate a video script for Crypto_Scripts (SPT) project following these guidelines:

PROJECT CONTEXT: SPT (Safety Promotor Token) - rewards safe driving with daily tokens
AUDIENCE: Tech-savvy drivers interested in earning cryptocurrency rewards
BRAND TONE: Community-driven, innovative, reward-focused  
COMPLIANCE: ZERO financial speculation - focus on utility and real rewards only

WORKFLOW REQUIREMENTS:
1. Extract videos from Reddit post using extract_story_videos(story_id)
2. Scrape original content using scrape_story_content(story_id)
3. Generate script with ≤10 second scenes
4. Use SPT messaging: "Drive smart, get rewarded - join the SPT movement"
5. Include CTAs: "Download SP Drive app", "Join the SPT Safe Driving movement"

COMPLIANCE REQUIREMENTS:
- NO token price speculation or investment language
- Focus on UTILITY: gift cards, safety equipment rewards
- Emphasize COMMUNITY movement and app adoption
- Connect stories to daily token earning behaviors

SCENE TIMING STRUCTURE (≤10 seconds each):
- HOOK (0-3s): Token reward angle hook
- EXCLUSIVITY (3-6s): Engagement validation
- STORY_SETUP (6-9s): Incident context
- LESSON_PART_1 (9-12s): First safety lesson
- LESSON_PART_2 (12-15s): Complete safety lesson
- PROOF (15-18s): Community confirmation
- SPT_CONNECTION (18-21s): Token earning connection
- CTA_MAIN (21-24s): App download CTA
- OUTRO (24-27s): Movement participation
- CLOSING (27-30s): "Drive Smart. Get Rewarded."

Generate using: generator.generate_enhanced_script(story_id, use_scraped_content=True)
```

### **App_Scripts Generation**

```
Generate a video script for App_Scripts project following these guidelines:

PROJECT CONTEXT: Novo Mobile App - convenient, tech-forward driving safety
AUDIENCE: Mobile-first users seeking convenience and technology solutions
BRAND TONE: Tech-forward, user-friendly, convenience-focused
COMPLIANCE: Emphasize app features and mobile convenience

WORKFLOW REQUIREMENTS:
1. Extract videos from Reddit post using extract_story_videos(story_id)
2. Scrape original content using scrape_story_content(story_id)
3. Generate script with ≤10 second scenes  
4. Use app messaging: "Get the Novo app for instant access to safety tools"
5. Include CTAs: "Download the Novo app", "Available on iOS and Android"

SCENE TIMING STRUCTURE (≤10 seconds each):
- HOOK (0-3s): Mobile-first hook
- ENGAGEMENT (3-6s): Social validation
- SCENARIO (6-9s): Real-world context
- APP_SOLUTION_1 (9-12s): How app helps
- APP_SOLUTION_2 (12-15s): Additional app benefits
- USER_BENEFIT (15-18s): Personal value
- APP_FEATURES (18-21s): Key app capabilities
- DOWNLOAD_CTA (21-24s): App store CTAs
- CONVENIENCE (24-27s): Easy usage message
- CLOSING (27-30s): App branding

Generate using: generator.generate_enhanced_script(story_id, use_scraped_content=True)
```

---

## Quality Control Prompts

### **Pre-Generation Validation**

```
Before generating any video script, validate these requirements:

STORY VALIDATION:
- Story ID exists in database: ✓ / ✗
- Story has valid Reddit URL: ✓ / ✗  
- Story theme aligns with project brand: ✓ / ✗
- Story contains appropriate content (no extreme violence): ✓ / ✗

WORKFLOW SETUP:
- Video/ and post/ folders exist: ✓ / ✗
- Workflow utilities imported correctly: ✓ / ✗
- Project-specific brand messaging loaded: ✓ / ✗
- Scene optimizer initialized: ✓ / ✗

If any validation fails, address the issue before proceeding with script generation.
```

### **Post-Generation Quality Check**

```
After generating a video script, validate these quality standards:

WORKFLOW COMPLETION:
- Video extraction attempted and logged: ✓ / ✗
- Content scraping completed successfully: ✓ / ✗  
- Original content used as script foundation: ✓ / ✗
- All workflow metadata included in output: ✓ / ✗

SCENE TIMING VALIDATION:
- All scenes ≤10 seconds duration: ✓ / ✗
- Total script duration ~30 seconds: ✓ / ✗
- Clear transitions between scenes: ✓ / ✗
- Visual directions provided for each scene: ✓ / ✗

BRAND COMPLIANCE:
- Project-appropriate messaging used: ✓ / ✗
- No conflicting brand messages: ✓ / ✗
- Compliance requirements met (especially SPT): ✓ / ✗
- CTAs match project goals: ✓ / ✗

PRODUCTION READINESS:
- Script includes time markers: ✓ / ✗
- Visual directions are clear and actionable: ✓ / ✗
- Engagement numbers are authentic: ✓ / ✗
- Story source properly attributed: ✓ / ✗

If any quality check fails, revise the script before saving.
```

---

## Batch Processing Prompts

### **Multiple Story Processing**

```
For batch processing multiple stories, follow this systematic approach:

BATCH SETUP:
1. Load project database and identify pending stories
2. Prioritize by engagement (highest upvotes first)
3. Balance theme diversity using tracking dashboard suggestions
4. Set target batch size (recommended: 5-10 stories per session)

PROCESSING WORKFLOW:
For each story in batch:
1. Run story validation checks
2. Execute complete workflow (extract videos + scrape content + generate script)
3. Validate quality before moving to next story
4. Log results and update tracking database
5. Save generated script to project output folder

BATCH COMPLETION:
1. Review overall batch quality and consistency
2. Update project tracking dashboard
3. Generate batch summary report
4. Identify any stories that need rework

Use this code pattern:
```python
for story_id in batch_story_ids:
    result = generator.generate_enhanced_script(story_id)
    if "⚠️ Issues found" not in result:
        generator.generate_and_save_script(story_id)
        print(f"✅ Story {story_id} completed successfully")
    else:
        print(f"⚠️ Story {story_id} needs review")
```

---

## Troubleshooting Prompts

### **Video Extraction Issues**

```
If video extraction fails, troubleshoot systematically:

COMMON ISSUES:
1. Reddit post deleted or private → Check URL accessibility
2. No embedded videos found → Verify post contains video content  
3. Network/API errors → Check internet connection and retry
4. Unsupported video platform → Add platform to supported list

TROUBLESHOOTING STEPS:
1. Manually visit Reddit URL to confirm post exists
2. Check if video is still available on source platform
3. Review video extraction logs for specific error messages
4. Use fallback: save story information for manual video sourcing

FALLBACK STRATEGY:
- Continue with content scraping if video extraction fails
- Use story description for visual direction placeholders
- Mark in workflow metadata that video needs manual sourcing
- Generate script with [VIDEO PLACEHOLDER] markers
```

### **Content Scraping Issues**

```
If content scraping fails, troubleshoot systematically:

COMMON ISSUES:
1. Reddit rate limiting → Implement delays between requests
2. Post content deleted → Use story database as fallback
3. JSON parsing errors → Check Reddit API response format
4. Network timeouts → Increase timeout values and retry

TROUBLESHOOTING STEPS:
1. Check Reddit API accessibility (add .json to URL manually)
2. Verify story database contains sufficient information for fallback
3. Review scraping logs for specific error details
4. Test with different story URLs to isolate issue

FALLBACK STRATEGY:
- Use story database narrative and metadata as foundation
- Generate script based on available information
- Mark in workflow metadata that content needs verification
- Include note about using database fallback vs. scraped content
```

---

## Success Metrics & Validation

### **Workflow Success Criteria**

```
Measure workflow success using these criteria:

VIDEO EXTRACTION SUCCESS:
- Target: 70% of stories have extractable video content
- Measure: Video files or URLs successfully captured
- Quality: Videos directly relevant to story content

CONTENT SCRAPING SUCCESS:
- Target: 90% successful content retrieval
- Measure: Complete original posts with engagement data  
- Quality: Content matches story database information

SCENE TIMING COMPLIANCE:
- Target: 100% scenes ≤10 seconds
- Measure: No scenes exceed timing limits
- Quality: Maintains story flow and engagement

BRAND MESSAGING QUALITY:
- Target: 100% appropriate brand integration
- Measure: No conflicting or off-brand messages
- Quality: Natural, contextual brand placement

PRODUCTION READINESS:
- Target: 95% scripts production-ready without revision
- Measure: Clear visual directions, accurate timing, proper formatting
- Quality: Scripts can be used immediately for video production
```

---

## Usage Examples

### **Single Story Generation**

```python
# Complete workflow for single story
from script_generator import VideoScriptGenerator

generator = VideoScriptGenerator('story_database.json')

# Generate with full workflow
result = generator.generate_enhanced_script(
    story_id=1, 
    use_scraped_content=True
)

print(result)
```

### **Production Batch Processing**

```python
# Batch process multiple stories for production
from script_generator import VideoScriptGenerator
from tracking_dashboard import TrackingDashboard

generator = VideoScriptGenerator('story_database.json')
dashboard = TrackingDashboard('story_database.json')

# Get smart suggestions for next stories
suggestions = dashboard.get_next_story_suggestions(5)

for item in suggestions:
    story_id = item['story']['id']
    
    # Generate with full workflow
    result = generator.generate_enhanced_script(story_id)
    
    # Save if quality checks pass
    if "✅ Valid" in result:
        generator.generate_and_save_script(story_id)
        print(f"✅ Story {story_id}: {item['story']['title'][:30]}...")
    else:
        print(f"⚠️ Story {story_id} needs review")
```

---

**These instruction templates ensure consistent, high-quality video script generation across all projects while maintaining brand compliance and production readiness.**