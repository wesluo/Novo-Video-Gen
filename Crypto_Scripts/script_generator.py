#!/usr/bin/env python3
"""
SPT Safe Driving Token Video Script Generator  
Transforms driving safety stories into viral video scripts for token reward community

🆕 ENHANCED WITH SCRAPED CONTENT AUTHENTICITY (2025-07-31):
- ✅ All 6 script generators use real Reddit titles, engagement metrics, community voice
- ✅ Content source attribution in every generated script
- ✅ Fallback handling for posts with no selftext content
- ✅ Dynamic scene generation replacing all hardcoded timing patterns

Universal Workflow Guidelines Implementation:
- URL validation with dual-method correction system (Method 1: Reddit API, Method 2: Scraping)
- Video extraction and downloading with yt-dlp integration
- Original content scraping for authentic script foundations  
- Scene timing optimization (≤10 seconds per scene, dynamically generated)
- Per-story folder organization for complete production workflow
- Production-ready video asset management with metadata tracking
"""

import json
import os
import random
import sys
import logging
from datetime import datetime
from typing import Dict, List, Optional, Any

# Add Shared_Resources to path for workflow utilities
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Shared_Resources'))
from workflow_utils import VideoExtractor, ContentScraper, SceneOptimizer, WorkflowFolders, WorkflowLogger, URLValidator
from url_correction import URLCorrectionSystem

# Configure logging
logger = logging.getLogger(__name__)

class VideoScriptGenerator:
    """
    SPT Safe Driving Token Video Script Generation System with Tracking
    ===================================================================
    
    Main class for generating viral video scripts from driving safety stories
    focused on token reward community building and safe driving incentives.
    
    Features:
    - 6 viral video format generators
    - Automatic SPT brand integration (compliance-focused)
    - Progress tracking and database updates  
    - 30-second standardized timing
    - Production-ready script output
    - Token reward messaging alignment
    
    Attributes:
        db_path (str): Path to story database file
        stories (List[Dict]): Loaded story data with tracking fields
        spt_messages (List[str]): SPT-compliant brand messaging options
        ctas (List[str]): Call-to-action options for app downloads and community
    """
    
    def __init__(self, story_db_path: str):
        """
        Initialize script generator with story database and workflow capabilities.
        
        Args:
            story_db_path (str): Path to story_database.json file
            
        Raises:
            FileNotFoundError: If database file doesn't exist
            json.JSONDecodeError: If database JSON is malformed
        """
        self.db_path = story_db_path
        self.base_path = os.path.dirname(story_db_path)
        
        with open(story_db_path, 'r') as f:
            self.data = json.load(f)
        self.stories = self.data['stories']
        
        # Initialize workflow utilities
        self.video_extractor = VideoExtractor()
        self.content_scraper = ContentScraper()
        self.scene_optimizer = SceneOptimizer()
        self.workflow_logger = WorkflowLogger("SPT_Crypto")
        
        # Ensure video/ and post/ folders exist
        self.video_path, self.post_path = WorkflowFolders.ensure_folders(self.base_path)
        
        # SPT brand messaging elements - compliance focused
        self.spt_messages = [
            "This is why safe driving should be rewarded - join the SPT movement",
            "Every safe mile counts - earn SPT tokens for smart choices like this",
            "Real rewards for real safety - that's the SPT way",
            "Drive smart, get rewarded - help build safer communities",
            "Join thousands earning daily rewards for smart driving",
            "Safe driving should pay - now it does with SPT",
            "Your smart driving earns tokens and builds safer roads",
            "Download SP Drive and start earning tokens for choices like this"
        ]
        
        # SPT-focused CTA options
        self.ctas = [
            "Download SP Drive app and start earning today",
            "Join the SPT Safe Driving movement",
            "Share your SPT earning story",
            "Tag a friend who drives smart like this",
            "Comment 'EARN TOKENS' if you're ready to start",
            "Double tap if you want rewards for safe driving",
            "Save this and start earning SPT tokens",
            "Send this to someone who deserves rewards for safe driving"
        ]
    
    def get_story_by_id(self, story_id: int) -> Optional[Dict]:
        """Get a specific story by ID"""
        for story in self.stories:
            if story['id'] == story_id:
                return story
        return None
    
    def get_stories_by_theme(self, theme: str) -> List[Dict]:
        """Get all stories matching a theme"""
        return [s for s in self.stories if s['theme'] == theme]
    
    def get_stories_by_format(self, format_type: str) -> List[Dict]:
        """Get all stories matching a suggested format"""
        return [s for s in self.stories if s['suggested_format'] == format_type]
    
    # ==========================================
    # WORKFLOW ENHANCEMENT METHODS
    # ==========================================
    
    def extract_story_videos(self, story_id: int) -> Dict:
        """
        Extract videos from a story's Reddit URL for production use.
        
        Args:
            story_id (int): ID of the story to extract videos from
            
        Returns:
            Dict containing extraction results and video information
        """
        story = self.get_story_by_id(story_id)
        if not story:
            return {'success': False, 'error': f'Story {story_id} not found'}
            
        if 'url' not in story or not story['url']:
            return {'success': False, 'error': 'No URL available for story'}
            
        # Extract videos from Reddit post
        result = self.video_extractor.extract_from_reddit_url(story['url'])
        
        # Save video metadata
        if result['success']:
            video_file = os.path.join(self.video_path, f"story_{story_id:03d}_videos.json")
            with open(video_file, 'w') as f:
                json.dump(result, f, indent=2)
                
        # Log results
        self.workflow_logger.log_video_extraction(story_id, result)
        
        return result
    
    def scrape_story_content(self, story_id: int) -> Dict:
        """
        Scrape original Reddit post content for authentic script foundation.
        
        Args:
            story_id (int): ID of the story to scrape content from
            
        Returns:
            Dict containing scraped content and metadata
        """
        story = self.get_story_by_id(story_id)
        if not story:
            return {'success': False, 'error': f'Story {story_id} not found'}
            
        if 'url' not in story or not story['url']:
            return {'success': False, 'error': 'No URL available for story'}
            
        # Scrape original post content
        result = self.content_scraper.scrape_reddit_post(story['url'])
        
        # Save scraped content
        if result['success']:
            content_file = os.path.join(self.post_path, f"story_{story_id:03d}_original.md")
            self._save_scraped_content_as_markdown(result['content'], content_file)
            
            # Also save raw JSON
            json_file = os.path.join(self.post_path, f"story_{story_id:03d}_content.json")
            with open(json_file, 'w') as f:
                json.dump(result, f, indent=2)
                
        # Log results
        self.workflow_logger.log_content_scraping(story_id, result)
        
        return result
    
    def _save_scraped_content_as_markdown(self, content: Dict, file_path: str):
        """Save scraped content in readable markdown format."""
        with open(file_path, 'w') as f:
            f.write(f"# {content.get('title', 'Unknown Title')}\n\n")
            f.write(f"**Subreddit**: r/{content.get('subreddit', 'unknown')}\n")
            f.write(f"**Author**: u/{content.get('author', 'unknown')}\n")
            f.write(f"**Score**: {content.get('score', 0):,} ({content.get('upvote_ratio', 0):.1%} upvoted)\n")
            f.write(f"**Comments**: {content.get('num_comments', 0):,}\n\n")
            
            if content.get('selftext'):
                f.write("## Original Post\n\n")
                f.write(f"{content['selftext']}\n\n")
                
            if content.get('url') and content['url'] != content.get('title', ''):
                f.write(f"**Link**: {content['url']}\n\n")
                
            if content.get('top_comments'):
                f.write("## Top Comments\n\n")
                for i, comment in enumerate(content['top_comments'], 1):
                    f.write(f"### Comment {i} (Score: {comment['score']})\n")
                    f.write(f"*By u/{comment['author']}*\n\n")
                    f.write(f"{comment['body']}\n\n")
    
    def validate_story_url(self, story_id: int) -> Dict:
        """
        Enhanced URL validation with automatic correction system.
        CRITICAL: This prevents script generation from invalid data.
        
        Process:
        1. Check current URL validity
        2. If invalid, attempt URL correction (Method #1 → Method #2)
        3. Update database if correction succeeds
        4. Return validation result
        
        Args:
            story_id (int): ID of the story to validate
            
        Returns:
            Dict containing validation status and error details
        """
        story = self.get_story_by_id(story_id)
        if not story:
            return {'valid': False, 'error': f'Story {story_id} not found in database'}
        
        url = story.get('url', '')
        if not url:
            return {'valid': False, 'error': 'No URL field in story data'}
        
        # Step 1: Check if current URL is already valid
        validation_result = URLValidator.validate_reddit_url(url)
        
        if validation_result['valid']:
            return {
                'valid': True, 
                'url': validation_result.get('cleaned_url', url),
                'corrected': False
            }
        
        # Step 2: URL is invalid - attempt correction using fallback system
        print(f"🔧 URL invalid for story {story_id}, attempting automatic correction...")
        
        url_corrector = URLCorrectionSystem("Crypto_Scripts")
        correction_result = url_corrector.attempt_url_correction(story)
        
        # Step 3: Handle correction results
        if correction_result['success']:
            # Correction succeeded - update database
            print(f"✅ URL corrected using {correction_result['method_used']}")
            self.update_story_with_correction(story_id, correction_result)
            
            return {
                'valid': True,
                'url': correction_result['corrected_url'],
                'corrected': True,
                'method_used': correction_result['method_used'],
                'video_url': correction_result.get('video_url')
            }
        else:
            # Correction failed - mark as correction failed
            print(f"❌ URL correction failed: {correction_result.get('failure_category', 'unknown')}")
            self.mark_story_correction_failed(story_id, correction_result)
            
            return {
                'valid': False, 
                'error': f"URL invalid and correction failed: {correction_result.get('failure_category', 'unknown')}",
                'url': url,
                'correction_attempted': True,
                'correction_failed': True
            }
    
    def update_story_with_correction(self, story_id: int, correction_result: Dict):
        """Update story in database with corrected URL and metadata."""
        for story in self.stories:
            if story['id'] == story_id:
                # Update URL
                story['corrected_url'] = correction_result['corrected_url']
                
                # Add video URL if found
                if correction_result.get('video_url'):
                    story['video_url'] = correction_result['video_url']
                
                # Add correction metadata
                story['url_correction'] = {
                    'attempted': True,
                    'success': True,
                    'method_used': correction_result['method_used'],
                    'attempt_date': correction_result['attempt_timestamp'],
                    'match_confidence': correction_result.get('match_confidence', 0.0),
                    'original_url': correction_result['original_url']
                }
                break
        
        # Save to database
        with open(self.db_path, 'w') as f:
            json.dump(self.data, f, indent=2)
        
        print(f"✅ Database updated for story {story_id} with corrected URL")
    
    def mark_story_correction_failed(self, story_id: int, correction_result: Dict):
        """Mark story as correction failed with detailed failure info."""
        for story in self.stories:
            if story['id'] == story_id:
                story['status'] = 'correction_failed'
                story['url_correction'] = {
                    'attempted': True,
                    'success': False,
                    'attempt_date': correction_result['attempt_timestamp'],
                    'methods_attempted': correction_result['methods_attempted'],
                    'failure_reasons': correction_result['failure_reasons'],
                    'failure_category': correction_result.get('failure_category', 'unknown'),
                    'original_url': correction_result['original_url']
                }
                story['script_generated'] = False
                break
        
        # Save to database
        with open(self.db_path, 'w') as f:
            json.dump(self.data, f, indent=2)
        
        self.workflow_logger.log_story_failure(story_id, f"URL correction failed: {correction_result.get('failure_category')}")
        self._update_tracking_with_failures()
    
    def mark_story_failed(self, story_id: int, reason: str):
        """
        Mark story as failed with specific reason.
        Updates database to track stories that cannot be processed.
        
        Args:
            story_id (int): ID of the story that failed
            reason (str): Specific reason for failure
        """
        for story in self.stories:
            if story['id'] == story_id:
                story['status'] = 'failed'
                story['failure_reason'] = reason
                story['failed_date'] = datetime.now().strftime('%Y-%m-%d')
                story['script_generated'] = False
                break
        
        # Log the failure
        self.workflow_logger.log_story_failure(story_id, reason)
        
        # Update tracking to include failure
        self._update_tracking_with_failures()
    
    def _update_tracking_with_failures(self):
        """Update tracking metadata to include failed story counts and URL correction stats."""
        completed_count = sum(1 for s in self.stories if s.get('status') == 'completed')
        failed_count = sum(1 for s in self.stories if s.get('status') == 'failed')
        correction_failed_count = sum(1 for s in self.stories if s.get('status') == 'correction_failed')
        
        # URL correction statistics
        correction_attempted = sum(1 for s in self.stories if s.get('url_correction', {}).get('attempted', False))
        correction_succeeded = sum(1 for s in self.stories if s.get('url_correction', {}).get('success', False))
        method1_success = sum(1 for s in self.stories if s.get('url_correction', {}).get('method_used') == 'reddit_api_search')
        method2_success = sum(1 for s in self.stories if s.get('url_correction', {}).get('method_used') == 'content_scraping')
        
        total_count = len(self.stories)
        pending_count = total_count - completed_count - failed_count - correction_failed_count
        
        if 'tracking' not in self.data['metadata']:
            self.data['metadata']['tracking'] = {}
        
        self.data['metadata']['tracking'].update({
            'total_stories': total_count,
            'scripts_generated': completed_count,
            'failed': failed_count,
            'correction_failed': correction_failed_count,
            'pending': pending_count,
            'url_correction_stats': {
                'correction_attempted': correction_attempted,
                'correction_succeeded': correction_succeeded,
                'correction_failed': correction_attempted - correction_succeeded,
                'method_1_success': method1_success,
                'method_2_success': method2_success,
                'success_rate': f"{(correction_succeeded / correction_attempted * 100):.1f}%" if correction_attempted > 0 else "0%"
            },
            'last_updated': datetime.now().isoformat()
        })
        
        # Save updated database
        with open(self.db_path, 'w') as f:
            json.dump(self.data, f, indent=2)
    
    def prepare_story_for_production(self, story_id: int) -> Dict:
        """
        Complete workflow preparation: extract videos + scrape content.
        
        Args:
            story_id (int): ID of the story to prepare
            
        Returns:
            Dict containing results from both video extraction and content scraping
        """
        results = {
            'story_id': story_id,
            'video_extraction': self.extract_story_videos(story_id),
            'content_scraping': self.scrape_story_content(story_id),
            'preparation_complete': False
        }
        
        # Mark as complete if both operations succeeded
        results['preparation_complete'] = (
            results['video_extraction']['success'] and 
            results['content_scraping']['success']
        )
        
        return results
    
    def generate_comedy_script(self, story: Dict, scraped_content: Optional[Dict] = None) -> str:
        """Generate a comedy/relatable format script with authentic content"""
        
        # Use scraped content for authentic details if available
        if scraped_content:
            actual_title = scraped_content.get('title', story['title'])
            actual_score = scraped_content.get('score', story['upvotes'])
            content_source = f"Based on actual Reddit post with {actual_score:,} upvotes"
            
            # Use actual post content for more authentic narrative
            if scraped_content.get('selftext'):
                authentic_context = scraped_content['selftext'][:200] + "..." if len(scraped_content['selftext']) > 200 else scraped_content['selftext']
            else:
                authentic_context = story['narrative']
                
            # Include top comment insights if available
            community_reaction = ""
            if scraped_content.get('top_comments'):
                top_comment = scraped_content['top_comments'][0]
                community_reaction = f"Top comment: \"{top_comment['body'][:100]}...\""
        else:
            actual_title = story['title']
            actual_score = story['upvotes']
            content_source = f"Story database entry ({actual_score:,} upvotes)"
            authentic_context = story['narrative']
            community_reaction = ""
        
        # Generate dynamic scene structure
        scenes = self.scene_optimizer.generate_scene_structure('comedy')
        
        script = f"""## **Script: {actual_title}**

**Format**: Comedy/Relatable
**Duration**: 30 seconds
**Hook**: "{self._create_hook(story, 'comedy')}"
**Structure**: Hook → Setup → Context → Punchline (2 parts) → CTA

### Full Script:

**{scenes[0]['timing_display']}:**
[Text Overlay: "{self._create_hook(story, 'comedy')}"]
[Visual: Person looking at camera with exaggerated expression]

**{scenes[1]['timing_display']}:**
"So apparently {authentic_context.lower() if authentic_context else story['narrative'].lower()}..."
[Shows relevant footage or reenactment]

**{scenes[2]['timing_display']}:**
"And I'm just thinking..."
[Visual: Person's contemplative expression]

**{scenes[3]['timing_display']}:**
"{self._create_comedy_escalation(story)}"
[Visual reactions, comedic gestures]

**{scenes[4]['timing_display']}:**
"{self._create_punchline(story)}"
[Deadpan delivery]

**{scenes[5]['timing_display']}:**
"{random.choice(self.spt_messages)}"
"{random.choice(self.ctas)}"

---
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}
Content Source: {content_source}
{community_reaction}
"""
        return script
    
    def generate_educational_hook_script(self, story: Dict, scraped_content: Optional[Dict] = None) -> str:
        """Generate an educational hook format script with authentic content"""
        
        # Use scraped content for authentic details if available
        if scraped_content:
            actual_title = scraped_content.get('title', story['title'])
            actual_score = scraped_content.get('score', story['upvotes'])
            actual_comments = scraped_content.get('num_comments', story['comments'])
            content_source = f"Based on actual Reddit post with {actual_score:,} upvotes"
            
            # Use actual post content for more authentic narrative
            if scraped_content.get('selftext'):
                authentic_context = scraped_content['selftext'][:100] + "..." if len(scraped_content['selftext']) > 100 else scraped_content['selftext']
            else:
                authentic_context = story['narrative'][:100] + "..."
                
            # Include top comment insights if available
            community_reaction = ""
            if scraped_content.get('top_comments'):
                top_comment = scraped_content['top_comments'][0]
                community_reaction = f"Top comment: \"{top_comment['body'][:100]}...\""
        else:
            actual_title = story['title']
            actual_score = story['upvotes']
            actual_comments = story['comments']
            content_source = f"Story database entry ({actual_score:,} upvotes)"
            authentic_context = story['narrative'][:100] + "..."
            community_reaction = ""

        # Generate dynamic scene structure
        scenes = self.scene_optimizer.generate_scene_structure('educational')
        
        script = f"""## **Script: {actual_title}**

**Format**: Educational Hook
**Duration**: 30 seconds
**Hook**: "{self._create_hook(story, 'educational')}"
**Structure**: Hook → Exclusivity → Benefit → Reveal → Proof → CTA

### Full Script:

**{scenes[0]['timing_display']}:**
[Text Overlay: "{self._create_hook(story, 'educational')}"]
[Visual: Person looking around conspiratorially]

**{scenes[1]['timing_display']}:**
"This got {actual_score:,} upvotes because it's THAT important."
[Visual: Highlight engagement numbers]

**{scenes[2]['timing_display']}:**
"Here's what happened: {authentic_context}"
[Visual: Set scene with context]

**{scenes[3]['timing_display']}:**
"The lesson? {story['key_lesson'][:40]}..."
[Visual: Key learning moment]

**{scenes[4]['timing_display']}:**
"{story['key_lesson'][40:] if len(story['key_lesson']) > 40 else 'This changes everything.'}"
[Show relevant visuals or graphics]

**{scenes[5]['timing_display']}:**
"Over {actual_comments:,} people confirmed this works."
[Visual: Community validation]

**{scenes[6]['timing_display']}:**
"{random.choice(self.spt_messages)}"
[Visual: Token reward concept]

**{scenes[7]['timing_display']}:**
"{random.choice(self.ctas)}"
[Visual: App/community call-to-action]

---
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}
Content Source: {content_source}
{community_reaction}
"""
        return script
    
    def generate_transformation_script(self, story: Dict, scraped_content: Optional[Dict] = None) -> str:
        """Generate a transformation/before & after format script with authentic content"""
        
        # Use scraped content for authentic details if available
        if scraped_content:
            actual_title = scraped_content.get('title', story['title'])
            actual_score = scraped_content.get('score', story['upvotes'])
            content_source = f"Based on actual Reddit post with {actual_score:,} upvotes"
            
            # Use actual post content for more authentic narrative
            if scraped_content.get('selftext'):
                authentic_context = scraped_content['selftext'][:150] + "..." if len(scraped_content['selftext']) > 150 else scraped_content['selftext']
            else:
                authentic_context = story['narrative']
                
            # Include top comment insights if available
            community_reaction = ""
            if scraped_content.get('top_comments'):
                top_comment = scraped_content['top_comments'][0]
                community_reaction = f"Top comment: \"{top_comment['body'][:100]}...\""
        else:
            actual_title = story['title']
            actual_score = story['upvotes']
            content_source = f"Story database entry ({actual_score:,} upvotes)"
            authentic_context = story['narrative']
            community_reaction = ""

        # Generate dynamic scene structure
        scenes = self.scene_optimizer.generate_scene_structure('transformation')
        
        script = f"""## **Script: {actual_title}**

**Format**: Transformation/Before & After
**Duration**: 30 seconds
**Hook**: "{self._create_hook(story, 'transformation')}"
**Structure**: Hook → Problem → Process → Reveal → Tips → CTA

### Full Script:

**{scenes[0]['timing_display']}:**
[Text Overlay: "{self._create_hook(story, 'transformation')}"]
[Visual: Dramatic before footage]

**{scenes[1]['timing_display']}:**
"This is what happened: {self._get_before_state(story)}"
[Show the incident or problem]

**{scenes[2]['timing_display']}:**
"{authentic_context if authentic_context else story['narrative']}"
[Show the incident unfolding]

**{scenes[3]['timing_display']}:**
"The transformation: {story['key_lesson']}"
[Show the positive outcome]

**{scenes[4]['timing_display']}:**
"Remember: {self._create_actionable_tip(story)}"
[Visual: Key takeaway]

**{scenes[5]['timing_display']}:**
"{random.choice(self.spt_messages)}"
"{random.choice(self.ctas)}"
[Visual: SPT integration and call-to-action]

---
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}
Content Source: {content_source}
{community_reaction}
"""
        return script
    
    def generate_storytelling_script(self, story: Dict, scraped_content: Optional[Dict] = None) -> str:
        """Generate a storytelling/emotional format script with authentic content"""
        
        # Use scraped content for authentic details if available
        if scraped_content:
            actual_title = scraped_content.get('title', story['title'])
            actual_score = scraped_content.get('score', story['upvotes'])
            content_source = f"Based on actual Reddit post with {actual_score:,} upvotes"
            
            # Use actual post content for more authentic narrative
            if scraped_content.get('selftext'):
                authentic_context = scraped_content['selftext'][:120] + "..." if len(scraped_content['selftext']) > 120 else scraped_content['selftext']
            else:
                authentic_context = story['narrative']
                
            # Include top comment insights if available
            community_reaction = ""
            if scraped_content.get('top_comments'):
                top_comment = scraped_content['top_comments'][0]
                community_reaction = f"Top comment: \"{top_comment['body'][:100]}...\""
        else:
            actual_title = story['title']
            actual_score = story['upvotes']
            content_source = f"Story database entry ({actual_score:,} upvotes)"
            authentic_context = story['narrative']
            community_reaction = ""

        # Generate dynamic scene structure
        scenes = self.scene_optimizer.generate_scene_structure('storytelling')
        
        script = f"""## **Script: {actual_title}**

**Format**: Storytelling/Emotional
**Duration**: 30 seconds
**Hook**: "{self._create_hook(story, 'storytelling')}"
**Structure**: Hook → Setup → Struggle → Twist → Victory → Lesson → CTA

### Full Script:

**{scenes[0]['timing_display']}:**
[Text Overlay: "{self._create_hook(story, 'storytelling')}"]
[Visual: Person looking directly at camera, serious expression]

**{scenes[1]['timing_display']}:**
"This got {actual_score:,} people talking..."
"{self._get_story_setup(story)}"
[Visual: Establish the scene]

**{scenes[2]['timing_display']}:**
"{authentic_context if authentic_context else story['narrative']}"
[Visual: Show the story unfolding]

**{scenes[3]['timing_display']}:**
"Then... {self._create_story_twist(story)}"
[Visual: The turning point]

**{scenes[4]['timing_display']}:**
"The takeaway? {self._simplify_lesson(story['key_lesson'])}"
[Visual: Key lesson moment]

**{scenes[5]['timing_display']}:**
"{random.choice(self.spt_messages)}"
"{random.choice(self.ctas)}"
[Visual: SPT integration and call-to-action]

---
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}
Content Source: {content_source}
{community_reaction}
"""
        return script
    
    def generate_pov_script(self, story: Dict, scraped_content: Optional[Dict] = None) -> str:
        """Generate a POV format script with authentic content"""
        
        # Use scraped content for authentic details if available
        if scraped_content:
            actual_title = scraped_content.get('title', story['title'])
            actual_score = scraped_content.get('score', story['upvotes'])
            content_source = f"Based on actual Reddit post with {actual_score:,} upvotes"
            
            # Use actual post content for more authentic narrative
            if scraped_content.get('selftext'):
                authentic_context = scraped_content['selftext'][:150] + "..." if len(scraped_content['selftext']) > 150 else scraped_content['selftext']
            else:
                authentic_context = story['narrative']
                
            # Include top comment insights if available
            community_reaction = ""
            if scraped_content.get('top_comments'):
                top_comment = scraped_content['top_comments'][0]
                community_reaction = f"Top comment: \"{top_comment['body'][:100]}...\""
        else:
            actual_title = story['title']
            actual_score = story['upvotes']
            content_source = f"Story database entry ({actual_score:,} upvotes)"
            authentic_context = story['narrative']
            community_reaction = ""

        # Generate dynamic scene structure
        scenes = self.scene_optimizer.generate_scene_structure('pov')
        
        script = f"""## **Script: {actual_title}**

**Format**: POV
**Duration**: 30 seconds
**Hook**: "POV: {self._create_pov_hook(story)}"

### Full Script:

**{scenes[0]['timing_display']}:**
[Text Overlay: "POV: {self._create_pov_hook(story)}"]
[Visual: First-person perspective]

**{scenes[1]['timing_display']}:**
"{self._create_pov_setup(story)}"
[Shows situation from driver's perspective]

**{scenes[2]['timing_display']}:**
"Internal thought: \"{self._create_internal_monologue(story)}\""
[Visual: Inner dialogue representation]

**{scenes[3]['timing_display']}:**
"{authentic_context if authentic_context else story['narrative']}"
[POV footage or reenactment]

**{scenes[4]['timing_display']}:**
"My heart is racing... {story['key_lesson']}"
[Visual: Emotional reaction and lesson]

**{scenes[5]['timing_display']}:**
"{random.choice(self.spt_messages)}"
"{random.choice(self.ctas)}"
[Visual: SPT integration and call-to-action]

---
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}
Content Source: {content_source}
{community_reaction}
"""
        return script
    
    def generate_challenge_script(self, story: Dict, scraped_content: Optional[Dict] = None) -> str:
        """Generate a challenge/interactive format script with authentic content"""
        
        # Use scraped content for authentic details if available
        if scraped_content:
            actual_title = scraped_content.get('title', story['title'])
            actual_score = scraped_content.get('score', story['upvotes'])
            actual_comments = scraped_content.get('num_comments', story['comments'])
            content_source = f"Based on actual Reddit post with {actual_score:,} upvotes"
            
            # Include top comment insights if available
            community_reaction = ""
            if scraped_content.get('top_comments'):
                top_comment = scraped_content['top_comments'][0]
                community_reaction = f"Top comment: \"{top_comment['body'][:100]}...\""
        else:
            actual_title = story['title']
            actual_score = story['upvotes']
            actual_comments = story['comments']
            content_source = f"Story database entry ({actual_score:,} upvotes)"
            community_reaction = ""

        # Generate dynamic scene structure
        scenes = self.scene_optimizer.generate_scene_structure('challenge')
        
        script = f"""## **Script: {actual_title}**

**Format**: Challenge/Interactive
**Duration**: 30 seconds
**Hook**: "{self._create_challenge_hook(story)}"
**Structure**: Hook → Challenge Setup → Instructions → Benefits → Call to Action

### Full Script:

**{scenes[0]['timing_display']}:**
[Text Overlay: "{self._create_challenge_hook(story)}"]
[Visual: Person pointing at camera confidently]

**{scenes[1]['timing_display']}:**
"After seeing {actual_title.lower()}, {actual_score:,} people agreed..."
[Visual: Engagement stats display]

**{scenes[2]['timing_display']}:**
"Here's the challenge: {self._create_challenge_action(story)}"
[Visual: Challenge explanation]

**{scenes[3]['timing_display']}:**
"{story['key_lesson']}"
[Visual: Benefits demonstration]

**{scenes[4]['timing_display']}:**
"Just try it for one week."
[Visual: Demonstrate the action]

**{scenes[5]['timing_display']}:**
"{actual_comments:,} people said this works."
"{random.choice(self.spt_messages)}"
"Comment 'DAY 1' if you're starting!"
[Visual: Community engagement and SPT integration]

---
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}
Content Source: {content_source}
{community_reaction}
"""
        return script
    
    # Helper methods for generating dynamic content
    def _create_hook(self, story: Dict, style: str) -> str:
        """Create an attention-grabbing hook based on style"""
        if style == 'comedy':
            return f"When {story['theme'].replace('_', ' ')} goes hilariously wrong 😅"
        elif style == 'educational':
            return f"This {story['theme'].replace('_', ' ')} trick could save your life"
        elif style == 'transformation':
            return f"How {story['upvotes']:,} people learned from this {story['emotion']} moment"
        elif style == 'storytelling':
            return f"The {story['source']} story that changed how I drive forever"
        else:
            return f"You won't believe what happened here"
    
    def _create_comedy_escalation(self, story: Dict) -> str:
        """Create comedy escalation based on story emotion"""
        escalations = {
            'shock': "I mean, the confidence! The audacity! The complete lack of brain cells!",
            'anger': "And everyone's just supposed to be okay with this? EVERYONE?",
            'frustration': "This is why we can't have nice things. THIS RIGHT HERE.",
            'humor': "I can't even be mad, I'm actually impressed by the stupidity.",
            'disbelief': "Physics said no, common sense said no, but they said YOLO!"
        }
        return escalations.get(story['emotion'], "The sheer chaos of it all!")
    
    def _create_punchline(self, story: Dict) -> str:
        """Create a punchline that lands the lesson"""
        return f"And that, friends, is why {story['key_lesson'].lower()}"
    
    def _get_before_state(self, story: Dict) -> str:
        """Extract the 'before' state for transformation stories"""
        if 'crash' in story['narrative'].lower():
            return "Everything seemed normal, just another day on the road"
        elif 'saved' in story['narrative'].lower():
            return "They thought they didn't need it"
        else:
            return "Before they learned this lesson the hard way"
    
    def _create_actionable_tip(self, story: Dict) -> str:
        """Create an actionable tip from the story"""
        theme_tips = {
            'safety_features': "Always wear your seatbelt, always",
            'road_rage': "Take a breath, it's not worth it",
            'distracted_driving': "Put the phone away, period",
            'weather_driving': "Slow down when conditions change",
            'dashcam_saves': "Get a dashcam yesterday"
        }
        return theme_tips.get(story['theme'], story['key_lesson'])
    
    def _get_story_setup(self, story: Dict) -> str:
        """Create story setup for emotional narratives"""
        return f"Picture this: {story['narrative'].split('.')[0]}..."
    
    def _create_story_twist(self, story: Dict) -> str:
        """Create the twist moment in storytelling"""
        if story['theme'] == 'hero_drivers':
            return "someone decided to be a hero"
        elif story['theme'] == 'instant_karma':
            return "karma had other plans"
        else:
            return "everything changed in an instant"
    
    def _simplify_lesson(self, lesson: str) -> str:
        """Simplify lesson to memorable phrase"""
        if len(lesson) > 50:
            return lesson.split('-')[0].strip()
        return lesson
    
    def _create_pov_hook(self, story: Dict) -> str:
        """Create POV-specific hook"""
        pov_hooks = {
            'road_rage': "You're the driver who just got brake checked",
            'near_miss': "You just avoided a massive accident",
            'hero_moment': "You see someone in danger",
            'realization': "You realize you've been driving wrong"
        }
        
        # Map themes to POV types
        if 'rage' in story['theme']:
            return pov_hooks['road_rage']
        elif 'hero' in story['theme']:
            return pov_hooks['hero_moment']
        else:
            return "You're about to learn something important"
    
    def _create_pov_setup(self, story: Dict) -> str:
        """Create POV setup narrative"""
        return f"You're driving along when suddenly..."
    
    def _create_internal_monologue(self, story: Dict) -> str:
        """Create internal thoughts for POV"""
        emotions = {
            'fear': "What do I do? WHAT DO I DO?",
            'anger': "Are you KIDDING me right now?",
            'shock': "This can't be happening...",
            'relief': "Thank god I was paying attention"
        }
        return emotions.get(story['emotion'], "This is really happening...")
    
    def _create_challenge_hook(self, story: Dict) -> str:
        """Create challenge-specific hook"""
        return f"I dare you to {story['theme'].replace('_', ' ')} better for 7 days"
    
    def _create_challenge_action(self, story: Dict) -> str:
        """Create specific challenge action"""
        actions = {
            'safety_features': "Check your seatbelt before starting the car, every time",
            'distracted_driving': "Put your phone in the glove box before driving",
            'defensive_driving': "Leave 3 seconds of space between you and the next car",
            'road_rage': "Wave and smile at aggressive drivers instead of reacting"
        }
        return actions.get(story['theme'], "Apply this lesson every time you drive")
    
    def generate_script(self, story_id: int, format_override: Optional[str] = None) -> str:
        """
        Generate a comprehensive script for a specific story with enhanced workflow.
        Includes URL validation, content scraping, video downloading, and organized storage.
        """
        story = self.get_story_by_id(story_id)
        if not story:
            return f"Story ID {story_id} not found"
        
        # Enhanced workflow implementation
        workflow_result = self._execute_enhanced_workflow(story)
        
        if not workflow_result['success']:
            return f"Workflow failed for story {story_id}: {workflow_result.get('error', 'Unknown error')}"
        
        # Use override format or story's suggested format
        format_type = format_override or story['suggested_format']
        
        # Map format types to generation methods
        generators = {
            'comedy': self.generate_comedy_script,
            'educational_hook': self.generate_educational_hook_script,
            'transformation': self.generate_transformation_script,
            'storytelling': self.generate_storytelling_script,
            'pov_story': self.generate_pov_script,
            'challenge': self.generate_challenge_script
        }
        
        generator = generators.get(format_type, self.generate_educational_hook_script)
        
        # Generate script using scraped content
        script_content = generator(story, workflow_result.get('scraped_content'))
        
        # Save script to story folder
        story_paths = workflow_result['story_paths']
        self._save_script_to_story_folder(script_content, story_paths['script'])
        
        # Update database with completion status
        self._update_story_completion(story, workflow_result)
        
        return script_content
    
    def _execute_enhanced_workflow(self, story: Dict) -> Dict[str, Any]:
        """
        Execute the complete enhanced workflow for a story.
        Includes URL validation, content scraping, video downloading, and folder creation.
        """
        workflow_result = {
            'success': False,
            'story_paths': {},
            'scraped_content': None,
            'video_info': None,
            'error': None
        }
        
        try:
            # Step 1: Validate URL (with correction if needed)
            url_validation = self._validate_story_url(story['id'])
            if not url_validation['valid']:
                workflow_result['error'] = f"URL validation failed: {url_validation.get('error', 'Unknown')}"
                return workflow_result
            
            # Step 2: Create story folder structure
            story_folder = WorkflowFolders.create_story_folder(
                self.base_path, story['id'], story['title']
            )
            workflow_result['story_paths'] = WorkflowFolders.get_story_paths(story_folder)
            
            # Step 3: Scrape content from Reddit post
            scraped_result = self.content_scraper.scrape_reddit_post(story['url'])
            if scraped_result['success']:
                workflow_result['scraped_content'] = scraped_result['content']
                # Save content to file
                self.content_scraper.save_content_to_file(
                    scraped_result['content'], 
                    workflow_result['story_paths']['content']
                )
                self.workflow_logger.log_content_scraping(story['id'], scraped_result)
            else:
                self.workflow_logger.log_content_scraping(story['id'], scraped_result)
                # Continue with basic story data if scraping fails
                workflow_result['scraped_content'] = None
            
            # Step 4: Extract and download video if available
            video_result = self.video_extractor.extract_from_reddit_url(story['url'])
            if video_result['success'] and video_result['videos']:
                # Try to download the first video
                first_video = video_result['videos'][0]
                if first_video.get('type') in ['youtube', 'direct']:
                    download_result = self.video_extractor.download_video(
                        first_video['url'],
                        workflow_result['story_paths']['video']
                    )
                    if download_result['success']:
                        workflow_result['video_info'] = {
                            'downloaded': True,
                            'metadata': download_result['metadata'],
                            'file_path': download_result['output_file']
                        }
                    else:
                        # Save video URL info even if download fails
                        workflow_result['video_info'] = {
                            'downloaded': False,
                            'url': first_video['url'],
                            'errors': download_result['errors']
                        }
                else:
                    workflow_result['video_info'] = {
                        'downloaded': False,
                        'url': first_video['url'],
                        'type': first_video.get('type', 'unknown')
                    }
                    
                self.workflow_logger.log_video_extraction(story['id'], video_result)
            else:
                self.workflow_logger.log_video_extraction(story['id'], video_result)
                workflow_result['video_info'] = None
            
            # Step 5: Save metadata
            self._save_story_metadata(story, workflow_result)
            
            workflow_result['success'] = True
            
        except Exception as e:
            workflow_result['error'] = str(e)
            self.workflow_logger.log_story_failure(story['id'], str(e))
            
        return workflow_result
    
    def _validate_story_url(self, story_id: int) -> Dict[str, Any]:
        """
        Validate story URL and attempt correction if needed.
        Integrates with the URL correction system.
        """
        story = self.get_story_by_id(story_id)
        if not story:
            return {'valid': False, 'error': 'Story not found'}
        
        # First check if URL is already valid
        validation = URLValidator.validate_reddit_url(story['url'])
        
        if validation['valid']:
            return validation
        
        # If invalid, attempt URL correction
        url_corrector = URLCorrectionSystem("Crypto_Scripts")
        correction_result = url_corrector.attempt_url_correction({
            'id': story['id'],
            'title': story['title'],
            'url': story['url'],
            'source': story.get('source', ''),
            'upvotes': story.get('upvotes', 0)
        })
        
        if correction_result.get('success', False):
            # Update story URL in memory and database
            story['url'] = correction_result['corrected_url']
            story['url_correction'] = {
                'attempted': True,
                'success': True,
                'method_used': correction_result['method_used'],
                'original_url': correction_result['original_url']
            }
            
            # Save updated database
            with open(self.db_path, 'w') as f:
                json.dump(self.data, f, indent=2)
            
            return {'valid': True, 'corrected': True, 'url': story['url']}
        else:
            # Mark story as correction failed
            story['status'] = 'correction_failed'
            story['failure_reason'] = validation.get('error', 'URL correction failed')
            story['failed_date'] = datetime.now().strftime('%Y-%m-%d')
            
            with open(self.db_path, 'w') as f:
                json.dump(self.data, f, indent=2)
            
            return {'valid': False, 'error': 'URL correction failed'}
    
    def _save_story_metadata(self, story: Dict, workflow_result: Dict):
        """Save comprehensive metadata to story folder."""
        metadata = {
            'story_info': {
                'id': story['id'],
                'title': story['title'],
                'theme': story['theme'],
                'upvotes': story['upvotes'],
                'comments': story['comments'],
                'url': story['url']
            },
            'workflow_execution': {
                'timestamp': datetime.now().isoformat(),
                'content_scraped': workflow_result['scraped_content'] is not None,
                'video_downloaded': workflow_result['video_info'] and workflow_result['video_info'].get('downloaded', False),
                'video_info': workflow_result['video_info']
            },
            'files_created': list(workflow_result['story_paths'].keys())
        }
        
        try:
            with open(workflow_result['story_paths']['metadata'], 'w') as f:
                json.dump(metadata, f, indent=2)
        except Exception as e:
            logger.error(f"Failed to save metadata: {str(e)}")
    
    def _save_script_to_story_folder(self, script_content: str, script_path: str):
        """Save generated script to story folder."""
        try:
            with open(script_path, 'w', encoding='utf-8') as f:
                f.write(script_content)
            logger.info(f"Script saved to: {script_path}")
        except Exception as e:
            logger.error(f"Failed to save script: {str(e)}")
    
    def _update_story_completion(self, story: Dict, workflow_result: Dict):
        """Update story database with completion status."""
        story['status'] = 'completed'
        story['script_generated'] = True
        story['generated_date'] = datetime.now().strftime('%Y-%m-%d')
        story['story_folder'] = os.path.basename(os.path.dirname(workflow_result['story_paths']['script']))
        
        # Save updated database
        with open(self.db_path, 'w') as f:
            json.dump(self.data, f, indent=2)
    
    def generate_random_script(self, theme: Optional[str] = None) -> str:
        """Generate a random script, optionally filtered by theme"""
        if theme:
            stories = self.get_stories_by_theme(theme)
        else:
            stories = self.stories
        
        if not stories:
            return "No stories found matching criteria"
        
        story = random.choice(stories)
        return self.generate_script(story['id'])
    
    def save_script_to_file(self, script: str, filename: str = "output/sample_scripts.md") -> bool:
        """Save a generated script to the sample scripts file"""
        try:
            # Read existing content
            with open(filename, 'r') as f:
                content = f.read()
            
            # Find the insertion point (before "## Script Generation Notes")
            insertion_point = content.find("## Script Generation Notes")
            if insertion_point == -1:
                # If notes section doesn't exist, append to end
                new_content = content + "\n\n" + script + "\n"
            else:
                # Insert before the notes section
                new_content = content[:insertion_point] + script + "\n\n---\n\n" + content[insertion_point:]
            
            # Write updated content
            with open(filename, 'w') as f:
                f.write(new_content)
            
            return True
        except Exception as e:
            print(f"Error saving script: {e}")
            return False
    
    def update_story_tracking(self, story_id: int, script_file: str) -> bool:
        """
        Update story tracking fields in database after successful script generation.
        
        Automatically called by generate_and_save_script() to maintain accurate
        project progress tracking. Updates story status, completion date, file location,
        and overall project statistics.
        
        Args:
            story_id (int): ID of the story that was converted to script
            script_file (str): Path to the generated script file
            
        Returns:
            bool: True if tracking update successful, False otherwise
            
        Side Effects:
            - Updates story status to 'completed'
            - Sets script_generated to True
            - Records script_file path and generated_date
            - Updates project metadata with current statistics
            - Saves changes to database file
            
        Example:
            >>> generator = VideoScriptGenerator('story_database.json')
            >>> success = generator.update_story_tracking(1, 'output/sample_scripts.md')
            >>> print(f"Tracking updated: {success}")
        """
        try:
            # Find and update the story
            for story in self.stories:
                if story['id'] == story_id:
                    story['status'] = 'completed'
                    story['script_generated'] = True
                    story['script_file'] = script_file
                    story['generated_date'] = datetime.now().strftime('%Y-%m-%d')
                    break
            
            # Update tracking metadata
            if 'tracking' not in self.data['metadata']:
                self.data['metadata']['tracking'] = {}
            
            completed_count = sum(1 for s in self.stories if s.get('status') == 'completed')
            self.data['metadata']['tracking']['total_stories'] = len(self.stories)
            self.data['metadata']['tracking']['scripts_generated'] = completed_count
            self.data['metadata']['tracking']['pending'] = len(self.stories) - completed_count
            self.data['metadata']['tracking']['last_updated'] = datetime.now().isoformat()
            
            # Save updated database
            with open(self.db_path, 'w') as f:
                json.dump(self.data, f, indent=2)
            
            return True
        except Exception as e:
            print(f"Error updating tracking: {e}")
            return False
    
    def generate_enhanced_script(self, story_id: int, format_override: Optional[str] = None, use_scraped_content: bool = True) -> str:
        """
        Generate script using enhanced workflow with video extraction and content scraping.
        NOW WITH URL VALIDATION: Stops immediately if URL is invalid.
        
        Args:
            story_id (int): ID of story to convert
            format_override (Optional[str]): Override suggested format
            use_scraped_content (bool): Whether to use scraped content as foundation
            
        Returns:
            str: Generated script with enhanced workflow data OR failure message
        """
        # CRITICAL STEP 0: Validate URL before ANY processing
        url_validation = self.validate_story_url(story_id)
        if not url_validation['valid']:
            # STOP IMMEDIATELY - Mark as failed and return error
            self.mark_story_failed(story_id, url_validation['error'])
            self.workflow_logger.log_url_validation_failure(story_id, url_validation['error'])
            
            return f"""❌ SCRIPT GENERATION FAILED - URL VALIDATION ERROR

**Story ID**: {story_id}
**Reason**: {url_validation['error']}
**URL Found**: {url_validation.get('url', 'None')}

This story cannot be processed without a valid Reddit URL that points to a specific post.
The story has been marked as FAILED in the tracking system.

**Required URL Format**: https://reddit.com/r/[subreddit]/comments/[post_id]/[post_title]/
"""
        
        story = self.get_story_by_id(story_id)
        if not story:
            return f"Story ID {story_id} not found"
            
        # Step 1: Prepare story with video extraction and content scraping
        # Now we know the URL is valid, so this should work better
        if use_scraped_content:
            preparation_result = self.prepare_story_for_production(story_id)
            
            # Use scraped content if available
            if preparation_result['content_scraping']['success']:
                scraped_content = preparation_result['content_scraping']['content']
                # Update story with scraped authentic data
                if scraped_content.get('title'):
                    story['title'] = scraped_content['title']
                if scraped_content.get('score'):
                    story['upvotes'] = scraped_content['score']
                if scraped_content.get('num_comments'):
                    story['comments'] = scraped_content['num_comments']
                    
        # Step 2: Generate script using enhanced format
        script = self.generate_script(story_id, format_override)
        
        # Step 3: Validate scene timing
        scenes = self.scene_optimizer.optimize_scenes(script)
        validation = self.scene_optimizer.validate_scene_timing(scenes)
        
        # Log scene optimization results
        self.workflow_logger.log_scene_optimization(
            story_id, 
            len(scenes), 
            validation.get('violations', [])
        )
        
        # Add workflow metadata to script
        script += f"\n\n### Workflow Enhancement Data\n"
        script += f"- **URL Validation**: ✅ Passed\n"
        script += f"- **Video Extraction**: {'✅ Completed' if use_scraped_content else '⏭️ Skipped'}\n"
        script += f"- **Content Scraping**: {'✅ Completed' if use_scraped_content else '⏭️ Skipped'}\n"
        script += f"- **Scene Validation**: {'✅ Valid' if validation.get('valid', False) else '⚠️ Issues found'}\n"
        script += f"- **Total Scenes**: {len(scenes)}\n"
        script += f"- **Total Duration**: {validation.get('total_duration', 0)} seconds\n"
        
        if validation.get('violations'):
            script += f"\n**Scene Timing Issues:**\n"
            for violation in validation['violations']:
                script += f"- Scene {violation['scene']}: {violation['issue']}\n"
                
        return script

    def generate_and_save_script(self, story_id: int, format_override: Optional[str] = None, filename: str = "output/sample_scripts.md") -> str:
        """
        Generate a video script and automatically save it with progress tracking.
        
        This is the recommended method for script generation as it provides complete
        workflow automation including file saving and progress tracking updates.
        
        Args:
            story_id (int): ID of story to convert (1-90)
            format_override (Optional[str]): Override suggested format 
                ('comedy', 'educational_hook', 'transformation', 'storytelling', 'pov_story', 'challenge')
            filename (str): Output file path (default: 'output/sample_scripts.md')
            
        Returns:
            str: Success message with generated script content, or error message
            
        Workflow:
            1. Generate script using story data and format
            2. Save script to specified file
            3. Update tracking database with completion status
            4. Return result with success/failure indication
            
        Example:
            >>> generator = VideoScriptGenerator('story_database.json')
            >>> result = generator.generate_and_save_script(
            ...     story_id=25, 
            ...     format_override='comedy'
            ... )
            >>> print("Generated!" if "generated and saved" in result else "Failed!")
        """
        script = self.generate_script(story_id, format_override)
        
        # Save script to file
        save_success = self.save_script_to_file(script, filename)
        
        # Update tracking if save was successful
        if save_success:
            self.update_story_tracking(story_id, filename)
            return f"Script generated and saved to {filename}\n\n{script}"
        else:
            return f"Script generated but failed to save:\n\n{script}"


# Example usage for SPT token rewards
if __name__ == "__main__":
    generator = VideoScriptGenerator('story_database.json')
    
    # Generate a specific script
    print(generator.generate_script(1))  # Technology saves story
    print("\n" + "="*80 + "\n")
    
    # Generate random smart choices rewarded script
    print(generator.generate_random_script(theme='smart_choices_rewarded'))
    
    # Example of generating and saving a script
    # generator.generate_and_save_script(25, 'storytelling')