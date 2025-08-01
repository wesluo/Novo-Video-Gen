# Universal Video Generation Workflow Guidelines

**Version**: 1.0  
**Date**: July 30, 2025  
**Applies to**: Insurance_Scripts, Crypto_Scripts, App_Scripts

---

## Overview

These universal guidelines establish standardized workflows for video content extraction, original post scraping, and scene timing optimization across all video generation projects. Every project should implement these capabilities to enhance video production quality and efficiency.

## Core Workflow Guidelines

### 0. URL Validation & Correction (CRITICAL) ⚠️

#### **Purpose**
Validate that story URLs point to actual Reddit posts with content before attempting any processing. If URLs are invalid, attempt automatic correction using verified methods.

#### **Enhanced Process**
1. **Primary Validation**: Check if current URL is valid Reddit post URL
2. **Automatic Correction**: If invalid, attempt URL correction using fallback system:
   - **Method #1**: Reddit API Search (fast, effective)
   - **Method #2**: Enhanced Content Scraping (slower, edge cases)
3. **Database Update**: Update story with corrected URL and video links if found
4. **Failure Tracking**: Mark as correction failed if both methods fail
5. **Data Consistency**: Clear previous failure markers when story succeeds after correction

#### **Validation Rules**
1. **Reddit URL Format**: Must be valid Reddit URL (https://reddit.com/...)
2. **Specific Post Path**: Must contain `/comments/` path indicating a specific post
3. **Not Subreddit**: Must not be just a subreddit link (e.g., reddit.com/r/IdiotsInCars)
4. **Accessible Content**: URL should lead to accessible post content

#### **Correction Methods**
**Method #1: Reddit API Search**
- Uses story title and subreddit to search for matching posts
- High success rate for stories with distinctive titles
- Fast execution, preferred method

**Method #2: Enhanced Content Scraping**
- Fallback method with broader search terms
- More lenient matching criteria
- Handles edge cases where Method #1 fails

#### **Implementation Requirements**
- **Automatic Correction**: Attempt URL fixing before marking as failed
- **Database Integration**: Save corrected URLs and metadata
- **Method Tracking**: Record which correction method succeeded
- **Video Extraction**: Extract video links during correction process
- **Failure Categories**: Categorize correction failures for analytics
- **Data Cleanup**: Remove failure_reason, failed_date fields when story succeeds after correction

#### **Quality Control**
- ✅ URL validation attempts correction before failing
- ✅ Both correction methods attempted with fallback
- ✅ Corrected URLs saved to database with metadata
- ✅ Video links extracted when possible
- ✅ Correction statistics tracked in dashboards
- ✅ Failed corrections categorized for improvement

---

### 1. Video Extraction & Storage 📹

#### **Purpose**
Extract existing video content from Reddit posts to use as foundation footage for final video production, reducing production time and costs.

#### **Process**
1. **Identify Video Sources**: Check each story's Reddit URL for embedded videos
2. **Common Video Types**: 
   - YouTube links (most common)
   - Direct video files (.mp4, .webm, etc.)
   - Video hosting platforms (Streamable, v.redd.it, etc.)
3. **Extract & Store**: Download or save to dedicated story folder within `stories/` directory
4. **Correlate**: Link video files to their source stories in database

#### **Storage Structure**
```
[Project]_Scripts/
├── stories/
│   ├── story_001_dashcam_crash/
│   │   ├── script.md                 # Generated video script
│   │   ├── original_post.md          # Scraped Reddit content
│   │   ├── video.mp4                 # Downloaded video file
│   │   ├── metadata.json             # Complete story metadata
│   │   └── generation_log.txt        # Process execution log
│   ├── story_002_road_rage/
│   │   ├── script.md
│   │   ├── original_post.md
│   │   ├── video.webm
│   │   ├── metadata.json
│   │   └── generation_log.txt
│   └── video_links.json              # URLs that couldn't be downloaded (global)
```

#### **Implementation Requirements**
- Create per-story folders using `story_###_clean_title/` naming convention
- Save all story artifacts in dedicated folder for organized production workflow
- Include comprehensive unified `metadata.json` with complete workflow information:
  - Story information (ID, title, theme, engagement metrics)
  - Workflow execution status (content scraped, video downloaded, timestamps)
  - Video metadata (duration, resolution, source URL, file path)
  - Content scraping results and engagement data
  - Files created and processing logs
- Use consistent generic filenames within each story folder:
  - `video.mp4` or `video.webm` (based on source format)
  - `original_post.md` for scraped Reddit content
  - `script.md` for generated video script
  - `metadata.json` for complete story metadata
  - `generation_log.txt` for process execution logs
- Maintain story ID correlation through folder naming (story_###_title) rather than individual filenames

---

### 2. Original Post Content Scraping 📄

#### **Purpose**
Scrape authentic original Reddit post content to use as foundation for script writing, ensuring accuracy and authenticity in storytelling.

#### **Two Scenarios**

##### **Scenario A: Direct Reddit URLs**
- Story database contains direct Reddit post URL
- Scrape content directly from the provided URL
- Extract: title, post text, top comments, engagement metrics

##### **Scenario B: Reddit Topic with Tags/Terms**
- Story database contains subreddit + search terms
- Navigate to Reddit board (e.g., r/IdiotsInCars)
- Search using provided tags/terms
- Find matching story and scrape content

#### **Content to Scrape**
- **Post Title**: Original Reddit post title
- **Post Body**: Full text content of original post
- **Top Comments**: 3-5 highest upvoted comments for context
- **Engagement**: Upvotes, comments count, awards
- **Metadata**: Date posted, author, subreddit

#### **Storage Structure**
Content is stored within the per-story folder structure outlined in Section 1, with unified metadata tracking all workflow components:
```
[Project]_Scripts/
├── stories/
│   ├── story_001_dashcam_crash/
│   │   ├── original_post.md          # Scraped Reddit content in markdown
│   │   ├── metadata.json             # Unified metadata with content, video, and execution info
│   │   └── generation_log.txt        # Detailed process execution logs
```

#### **Implementation Requirements**
- Save scraped content as `original_post.md` within each story's dedicated folder
- Format content in readable markdown with proper headers and structure
- Include engagement metrics, author info, and top comments in the content file
- Handle Reddit rate limiting gracefully with retry logic
- Log scraping success/failure details in generation_log.txt for debugging
- Maintain story ID correlation through folder organization

---

### 3. Scene Timing Optimization ⏱️

#### **Purpose**
Optimize video scenes for better production workflow and platform engagement by keeping each scene ≤ 10 seconds.

#### **Current vs. New Structure**

##### **Current Structure (30-second blocks)**
```
HOOK (0-3 seconds)
SETUP (3-10 seconds)  
LESSON (10-22 seconds)
CTA (22-30 seconds)
```

##### **New Structure (≤10 second scenes)**
```
HOOK (0-3 seconds)
SETUP (3-6 seconds)
CONTEXT (6-9 seconds)
LESSON_PART_1 (9-12 seconds)
LESSON_PART_2 (12-15 seconds)
IMPACT (15-18 seconds)
CTA_SETUP (18-21 seconds)
CTA_MAIN (21-24 seconds)
CTA_CLOSE (24-27 seconds)
OUTRO (27-30 seconds)
```

#### **Scene Design Principles**
1. **Maximum 10 seconds per scene**
2. **Minimum 3 seconds per scene** (for readability)
3. **Clear scene transitions** with visual/audio cues
4. **Single focus per scene** (one main message/visual)
5. **Maintain overall 30-second duration**

#### **Implementation Requirements**
- Update all format generators to use ≤10 second scenes
- Provide specific visual directions for each scene
- Include transition suggestions between scenes
- Maintain story pacing and engagement flow

---

## Technical Implementation

### Required Dependencies
```python
# Add to requirements for projects implementing these guidelines
import requests          # For web scraping
import yt_dlp           # For YouTube video downloading  
import beautifulsoup4   # For HTML parsing
import praw             # For Reddit API access
import json             # For metadata storage
import os               # For folder creation
import re               # For URL parsing
from urllib.parse import urlparse  # For URL validation
```

### URL Validation Implementation
```python
class URLValidator:
    @staticmethod
    def validate_reddit_url(url: str) -> Dict[str, Any]:
        """
        Validate Reddit URL format and structure.
        Returns dict with 'valid' boolean and error details.
        """
        result = {
            'valid': False,
            'error': '',
            'url_type': 'unknown',
            'cleaned_url': url
        }
        
        # Check for protocol
        if not url.startswith(('http://', 'https://')):
            if url.startswith('reddit.com'):
                url = 'https://' + url
                result['cleaned_url'] = url
            else:
                result['error'] = 'Invalid URL format - must be Reddit URL'
                return result
        
        # Parse URL structure
        try:
            parsed = urlparse(url)
            if 'reddit.com' not in parsed.netloc:
                result['error'] = 'URL is not a Reddit URL'
                return result
            
            # Check for specific post (contains /comments/)
            if '/comments/' in parsed.path:
                result['url_type'] = 'post'
                result['valid'] = True
            elif '/r/' in parsed.path and len(parsed.path.split('/')) <= 3:
                result['error'] = 'URL points to subreddit, not specific post'
            else:
                result['error'] = 'URL does not point to a specific Reddit post'
                
        except Exception as e:
            result['error'] = f'URL parsing error: {str(e)}'
            
        return result
```

### Folder Creation Function
```python
def ensure_workflow_folders(base_path: str):
    """Create video/ and post/ subfolders if they don't exist"""
    video_path = os.path.join(base_path, 'video')
    post_path = os.path.join(base_path, 'post')
    
    os.makedirs(video_path, exist_ok=True)
    os.makedirs(post_path, exist_ok=True)
    
    return video_path, post_path
```

### Error Handling Standards
- Graceful failure when videos can't be downloaded
- Rate limiting respect for Reddit API
- Timeout handling for slow connections
- Fallback to URL storage when download fails

---

## Quality Control Standards

### Video Extraction Validation
- ✅ Video file successfully downloaded or URL saved
- ✅ Metadata captured (duration, resolution, source)
- ✅ Story correlation maintained in database
- ✅ File naming convention followed

### Content Scraping Validation  
- ✅ Original post content successfully retrieved
- ✅ Engagement metrics captured accurately
- ✅ Content saved in readable format
- ✅ Story correlation maintained

### Scene Timing Validation
- ✅ No scene exceeds 10 seconds
- ✅ No scene under 3 seconds  
- ✅ Total duration remains ~30 seconds
- ✅ Clear transitions between scenes
- ✅ Single focus maintained per scene

---

## Claude Code Integration

### Standard Workflow Prompt Template
```
When generating video scripts, follow the Universal Workflow Guidelines:

0. CRITICAL FIRST STEP: Validate story URL
   - Check that URL points to specific Reddit post (contains /comments/)
   - If URL is invalid, STOP IMMEDIATELY and mark story as failed
   - Do not proceed with any processing if URL validation fails

1. SECOND: Extract any embedded videos from the story's Reddit URL
   - Check for YouTube links, direct videos, etc.
   - Save to video/ subfolder with story correlation
   
2. THIRD: Scrape original Reddit post content  
   - Extract full post text, comments, engagement metrics
   - Save to post/ subfolder in markdown format
   
3. FOURTH: Generate script using ≤10 second scenes
   - Break content into scenes of 3-10 seconds each
   - Maintain 30-second total duration
   - Provide clear scene transitions

4. FIFTH: Reference scraped content as foundation
   - Use original post text for authenticity
   - Incorporate actual engagement numbers
   - Maintain story accuracy and context
   
5. CRITICAL: Script generation MUST use scraped content
   - Use actual Reddit title (not database title)
   - Use real-time engagement metrics (upvotes, comments)
   - Incorporate top comments for community voice
   - For posts with no text content, use top comments and video context
   - Label content source transparently (e.g., "Based on actual Reddit post")
   - Include community reactions in script metadata
```

### Quality Control Prompt
```
Before finalizing any script generation:

✅ CRITICAL: Verify URL validation passed (story not marked as failed)
✅ Verify video extraction attempted and logged
✅ Confirm original content scraping completed  
✅ Validate all scenes are ≤10 seconds
✅ Check total duration ~30 seconds
✅ Ensure story accuracy from scraped content
✅ Verify script uses actual Reddit data (title, upvotes, comments)
✅ Confirm authentic content integration (not generic database text)
✅ Check content source attribution is present
✅ IMPLEMENTATION STATUS: All 6 script generators updated (2025-07-31)
✅ VERIFIED WORKING: Educational, Comedy, Transformation, Storytelling, POV, Challenge formats
✅ Confirm brand messaging appropriate for project
✅ Check that failed stories are excluded from completion rates
```

---

## Project-Specific Adaptations

### Insurance_Scripts
- **Brand Integration**: Novo Insurance messaging in scenes
- **Audience**: Insurance buyers focused on safety and savings
- **Tone**: Professional, trustworthy, educational

### Crypto_Scripts  
- **Brand Integration**: SPT token reward messaging
- **Audience**: Tech-savvy drivers interested in earning tokens
- **Tone**: Community-driven, innovative, reward-focused

### App_Scripts
- **Brand Integration**: Mobile app download and usage
- **Audience**: Mobile-first users seeking convenience
- **Tone**: Tech-forward, user-friendly, convenience-focused

---

## Success Metrics

### Video Extraction Success
- **Target**: 80% of stories have extractable video content
- **Measure**: Video files or URLs successfully captured
- **Quality**: Videos directly relevant to story content

### Content Scraping Accuracy
- **Target**: 95% successful content retrieval  
- **Measure**: Complete original posts with engagement data
- **Quality**: Content matches story database information

### Scene Timing Compliance
- **Target**: 100% scenes ≤10 seconds
- **Measure**: No scenes exceed timing limits
- **Quality**: Maintains story flow and engagement

---

## Troubleshooting & Common Issues

### Video Extraction Issues
- **Issue**: Video unavailable or deleted
- **Solution**: Save URL and metadata, note unavailability
- **Fallback**: Use story description for visual direction

### Content Scraping Issues  
- **Issue**: Reddit post deleted or private
- **Solution**: Use cached/archived versions if available
- **Fallback**: Use story database information as foundation

### Scene Timing Challenges
- **Issue**: Complex stories hard to fit in ≤10 second scenes
- **Solution**: Break into multiple focused scenes
- **Approach**: Prioritize key message per scene

---

## Implementation Checklist

### For Each Project Implementation:
- [ ] Implement URL validation as FIRST step in processing
- [ ] Add failure tracking with status='failed' and failure_reason
- [ ] Update tracking dashboard to show failed stories
- [ ] Exclude failed stories from completion rate calculations
- [ ] Create `video/` and `post/` subfolders
- [ ] Add video extraction capabilities to script generator
- [ ] Add content scraping capabilities to script generator  
- [ ] Update scene timing in all format generators
- [ ] Update project documentation with new capabilities
- [ ] Test workflow with sample stories
- [ ] Verify quality control standards met

---

**These guidelines ensure consistent, high-quality video content generation across all projects while leveraging existing authentic content and optimizing for modern video production workflows.**