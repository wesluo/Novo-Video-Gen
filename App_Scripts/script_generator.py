#!/usr/bin/env python3
"""
Novo App Video Script Generator
Transforms driving safety stories into viral video scripts

Enhanced with Universal Workflow Guidelines:
- Video extraction from Reddit posts
- Original content scraping for authentic foundations  
- Scene timing optimization (≤10 seconds per scene)
- Production-ready video asset management
"""

import json
import os
import random
import sys
from datetime import datetime
from typing import Dict, List, Optional

# Add Shared_Resources to path for workflow utilities
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Shared_Resources'))
from workflow_utils import VideoExtractor, ContentScraper, SceneOptimizer, WorkflowFolders, WorkflowLogger, URLValidator
from url_correction import URLCorrectionSystem

class VideoScriptGenerator:
    """
    Novo Insurance Video Script Generation System with Tracking
    =========================================================
    
    Main class for generating viral video scripts from driving safety stories.
    Includes comprehensive progress tracking and analytics integration.
    
    Features:
    - 6 viral video format generators
    - Automatic Novo brand integration
    - Progress tracking and database updates
    - 30-second standardized timing
    - Production-ready script output
    
    Attributes:
        db_path (str): Path to story database file
        stories (List[Dict]): Loaded story data with tracking fields
        novo_messages (List[str]): Brand messaging options
        ctas (List[str]): Call-to-action options
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
        self.workflow_logger = WorkflowLogger("Novo_App")
        
        # Ensure video/ and post/ folders exist
        self.video_path, self.post_path = WorkflowFolders.ensure_folders(self.base_path)
        
        # Novo brand messaging elements
        self.novo_messages = [
            "This is why Novo rewards safe drivers",
            "Novo believes in turning roads into corridors of care",
            "Technology and safe driving go hand in hand with Novo",
            "Every safe decision matters - that's the Novo way",
            "Novo: Transforming insurance by rewarding responsibility",
            "Safe drivers deserve better - that's why Novo exists",
            "Novo empowers drivers with technology for safety",
            "Your safe driving choices matter to Novo"
        ]
        
        # CTA options
        self.ctas = [
            "Follow for more safe driving content",
            "Share this to save a life",
            "Tag someone who needs to see this",
            "What would you do? Comment below",
            "Have a similar story? Share it",
            "Double tap if you agree",
            "Save this as a reminder",
            "Send this to a new driver"
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
        """Extract videos from a story's Reddit URL for production use."""
        story = self.get_story_by_id(story_id)
        if not story:
            return {'success': False, 'error': f'Story {story_id} not found'}
        if 'url' not in story or not story['url']:
            return {'success': False, 'error': 'No URL available for story'}
        result = self.video_extractor.extract_from_reddit_url(story['url'])
        if result['success']:
            video_file = os.path.join(self.video_path, f"story_{story_id:03d}_videos.json")
            with open(video_file, 'w') as f:
                json.dump(result, f, indent=2)
        self.workflow_logger.log_video_extraction(story_id, result)
        return result
    
    def scrape_story_content(self, story_id: int) -> Dict:
        """Scrape original Reddit post content for authentic script foundation."""
        story = self.get_story_by_id(story_id)
        if not story:
            return {'success': False, 'error': f'Story {story_id} not found'}
        if 'url' not in story or not story['url']:
            return {'success': False, 'error': 'No URL available for story'}
        result = self.content_scraper.scrape_reddit_post(story['url'])
        if result['success']:
            content_file = os.path.join(self.post_path, f"story_{story_id:03d}_original.md")
            self._save_scraped_content_as_markdown(result['content'], content_file)
            json_file = os.path.join(self.post_path, f"story_{story_id:03d}_content.json")
            with open(json_file, 'w') as f:
                json.dump(result, f, indent=2)
        self.workflow_logger.log_content_scraping(story_id, result)
        return result
    
    def _save_scraped_content_as_markdown(self, content: Dict, file_path: str):
        """Save scraped content in readable markdown format."""
        with open(file_path, 'w') as f:
            f.write(f"# {content.get('title', 'Unknown Title')}\n\n")
            f.write(f"**Score**: {content.get('score', 0):,} ({content.get('upvote_ratio', 0):.1%} upvoted)\n")
            f.write(f"**Comments**: {content.get('num_comments', 0):,}\n\n")
            if content.get('selftext'):
                f.write("## Original Post\n\n")
                f.write(f"{content['selftext']}\n\n")
            if content.get('top_comments'):
                f.write("## Top Comments\n\n")
                for i, comment in enumerate(content['top_comments'], 1):
                    f.write(f"### Comment {i} (Score: {comment['score']})\n")
                    f.write(f"{comment['body']}\n\n")
    
    def validate_story_url(self, story_id: int) -> Dict:
        """
        Enhanced URL validation with automatic correction system.
        
        Process:
        1. Check current URL validity
        2. If invalid, attempt URL correction (Method #1 → Method #2)
        3. Update database if correction succeeds
        4. Return validation result
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
        
        url_corrector = URLCorrectionSystem("App_Scripts")
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
        """Mark story as failed with specific reason."""
        for story in self.stories:
            if story['id'] == story_id:
                story['status'] = 'failed'
                story['failure_reason'] = reason
                story['failed_date'] = datetime.now().strftime('%Y-%m-%d')
                story['script_generated'] = False
                break
        
        self.workflow_logger.log_story_failure(story_id, reason)
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
        
        with open(self.db_path, 'w') as f:
            json.dump(self.data, f, indent=2)
    
    def prepare_story_for_production(self, story_id: int) -> Dict:
        """Complete workflow preparation: extract videos + scrape content."""
        results = {
            'story_id': story_id,
            'video_extraction': self.extract_story_videos(story_id),
            'content_scraping': self.scrape_story_content(story_id),
            'preparation_complete': False
        }
        results['preparation_complete'] = (
            results['video_extraction']['success'] and 
            results['content_scraping']['success']
        )
        return results
    
    def generate_comedy_script(self, story: Dict) -> str:
        """Generate a comedy/relatable format script"""
        script = f"""## **Script: {story['title']}**

**Format**: Comedy/Relatable
**Duration**: 30 seconds
**Hook**: "{self._create_hook(story, 'comedy')}"
**Structure**: Hook → Setup → Escalation → Punchline → CTA

### Full Script:

**HOOK (0-3 seconds):**
[Text Overlay: "{self._create_hook(story, 'comedy')}"]
[Visual: Person looking at camera with exaggerated expression]

**SETUP (3-12 seconds):**
"So apparently {story['narrative'].lower()}..."
[Shows relevant footage or reenactment]
"And I'm just thinking..."

**PUNCHLINE (12-25 seconds):**
"{self._create_comedy_escalation(story)}"
[Visual reactions, comedic gestures]
"{self._create_punchline(story)}"
[Deadpan delivery]

**CTA + NOVO (25-30 seconds):**
"{random.choice(self.novo_messages)}"
"{random.choice(self.ctas)}"

---
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}
Story Source: {story['source']} ({story['upvotes']:,} upvotes)
"""
        return script
    
    def generate_educational_hook_script(self, story: Dict) -> str:
        """Generate an educational hook format script"""
        script = f"""## **Script: {story['title']}**

**Format**: Educational Hook
**Duration**: 30 seconds
**Hook**: "{self._create_hook(story, 'educational')}"
**Structure**: Hook → Exclusivity → Benefit → Reveal → Proof → CTA

### Full Script:

**HOOK (0-3 seconds):**
[Text Overlay: "{self._create_hook(story, 'educational')}"]
[Visual: Person looking around conspiratorially]

**SETUP (3-10 seconds):**
"This got {story['upvotes']:,} upvotes because it's THAT important."
"Here's what happened: {story['narrative']}"

**LESSON (10-22 seconds):**
"The lesson? {story['key_lesson']}"
[Show relevant visuals or graphics]
"Over {story['comments']:,} people confirmed this works."

**CTA + NOVO (22-30 seconds):**
"{random.choice(self.novo_messages)}"
"{random.choice(self.ctas)}"

---
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}
Story Source: {story['source']} ({story['upvotes']:,} upvotes)
"""
        return script
    
    def generate_transformation_script(self, story: Dict) -> str:
        """Generate a transformation/before & after format script"""
        script = f"""## **Script: {story['title']}**

**Format**: Transformation/Before & After
**Duration**: 30 seconds
**Hook**: "{self._create_hook(story, 'transformation')}"
**Structure**: Hook → Problem → Process → Reveal → Tips → CTA

### Full Script:

**HOOK (0-3 seconds):**
[Text Overlay: "{self._create_hook(story, 'transformation')}"]
[Visual: Dramatic before footage]

**PROBLEM (3-8 seconds):**
"This is what happened: {self._get_before_state(story)}"
[Show the incident or problem]

**LESSON (8-22 seconds):**
"{story['narrative']}"
[Show the incident unfolding]
"The transformation: {story['key_lesson']}"
[Show the positive outcome]

**CTA + NOVO (22-30 seconds):**
"Remember: {self._create_actionable_tip(story)}"
"{random.choice(self.novo_messages)}"
"{random.choice(self.ctas)}"

---
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}
Story Source: {story['source']} ({story['upvotes']:,} upvotes)
"""
        return script
    
    def generate_storytelling_script(self, story: Dict) -> str:
        """Generate a storytelling/emotional format script"""
        script = f"""## **Script: {story['title']}**

**Format**: Storytelling/Emotional
**Duration**: 30 seconds
**Hook**: "{self._create_hook(story, 'storytelling')}"
**Structure**: Hook → Setup → Struggle → Twist → Victory → Lesson → CTA

### Full Script:

**HOOK (0-3 seconds):**
[Text Overlay: "{self._create_hook(story, 'storytelling')}"]
[Visual: Person looking directly at camera, serious expression]

**SETUP (3-10 seconds):**
"This got {story['upvotes']:,} people talking..."
"{self._get_story_setup(story)}"
[Visual: Establish the scene]

**STORY (10-22 seconds):**
"{story['narrative']}"
[Visual: Show the story unfolding]
"Then... {self._create_story_twist(story)}"
[Visual: The turning point]

**CTA + NOVO (22-30 seconds):**
"The takeaway? {self._simplify_lesson(story['key_lesson'])}"
"{random.choice(self.novo_messages)}"
"{random.choice(self.ctas)}"

---
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}
Story Source: {story['source']} ({story['upvotes']:,} upvotes)
"""
        return script
    
    def generate_pov_script(self, story: Dict) -> str:
        """Generate a POV format script"""
        script = f"""## **Script: {story['title']}**

**Format**: POV
**Duration**: 30 seconds
**Hook**: "POV: {self._create_pov_hook(story)}"

### Full Script:

**HOOK (0-3 seconds):**
[Text Overlay: "POV: {self._create_pov_hook(story)}"]
[Visual: First-person perspective]

**SETUP (3-12 seconds):**
"{self._create_pov_setup(story)}"
[Shows situation from driver's perspective]
Internal thought: "{self._create_internal_monologue(story)}"

**EXPERIENCE (12-22 seconds):**
"{story['narrative']}"
[POV footage or reenactment]
"My heart is racing..."

**CTA + NOVO (22-30 seconds):**
"{story['key_lesson']}"
"{random.choice(self.novo_messages)}"
"{random.choice(self.ctas)}"

---
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}
Story Source: {story['source']} ({story['upvotes']:,} upvotes)
"""
        return script
    
    def generate_challenge_script(self, story: Dict) -> str:
        """Generate a challenge/interactive format script"""
        script = f"""## **Script: {story['title']}**

**Format**: Challenge/Interactive
**Duration**: 30 seconds
**Hook**: "{self._create_challenge_hook(story)}"
**Structure**: Hook → Challenge Setup → Instructions → Benefits → Call to Action

### Full Script:

**HOOK (0-3 seconds):**
[Text Overlay: "{self._create_challenge_hook(story)}"]
[Visual: Person pointing at camera confidently]

**CHALLENGE SETUP (3-12 seconds):**
"After seeing {story['title'].lower()}, {story['upvotes']:,} people agreed..."
"Here's the challenge: {self._create_challenge_action(story)}"

**BENEFITS (12-22 seconds):**
"{story['key_lesson']}"
"Just try it for one week."
[Visual: Demonstrate the action]

**CTA + NOVO (22-30 seconds):**
"{story['comments']:,} people said this works."
"{random.choice(self.novo_messages)}"
"Comment 'DAY 1' if you're starting!"

---
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}
Story Source: {story['source']} ({story['upvotes']:,} upvotes)
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
        """Generate a script for a specific story"""
        story = self.get_story_by_id(story_id)
        if not story:
            return f"Story ID {story_id} not found"
        
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
        return generator(story)
    
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
        """Generate script with URL validation - STOPS if URL invalid."""
        # CRITICAL: Validate URL first
        url_validation = self.validate_story_url(story_id)
        if not url_validation['valid']:
            self.mark_story_failed(story_id, url_validation['error'])
            self.workflow_logger.log_url_validation_failure(story_id, url_validation['error'])
            
            return f"""❌ SCRIPT GENERATION FAILED - URL VALIDATION ERROR

**Story ID**: {story_id}
**Reason**: {url_validation['error']}
**URL Found**: {url_validation.get('url', 'None')}

This story cannot be processed without a valid Reddit URL.
Story marked as FAILED in tracking.

**Required Format**: https://reddit.com/r/[subreddit]/comments/[post_id]/[title]/
"""
        
        story = self.get_story_by_id(story_id)
        if not story:
            return f"Story ID {story_id} not found"
            
        if use_scraped_content:
            preparation_result = self.prepare_story_for_production(story_id)
            
            if preparation_result['content_scraping']['success']:
                scraped_content = preparation_result['content_scraping']['content']
                if scraped_content.get('title'):
                    story['title'] = scraped_content['title']
                if scraped_content.get('score'):
                    story['upvotes'] = scraped_content['score']
                if scraped_content.get('num_comments'):
                    story['comments'] = scraped_content['num_comments']
                    
        script = self.generate_script(story_id, format_override)
        
        scenes = self.scene_optimizer.optimize_scenes(script)
        validation = self.scene_optimizer.validate_scene_timing(scenes)
        
        self.workflow_logger.log_scene_optimization(
            story_id, 
            len(scenes), 
            validation.get('violations', [])
        )
        
        script += f"\n\n### Workflow Enhancement Data\n"
        script += f"- **URL Validation**: ✅ Passed\n"
        script += f"- **Video Extraction**: {'✅ Completed' if use_scraped_content else '⏭️ Skipped'}\n"
        script += f"- **Content Scraping**: {'✅ Completed' if use_scraped_content else '⏭️ Skipped'}\n"
        script += f"- **Scene Validation**: {'✅ Valid' if validation.get('valid', False) else '⚠️ Issues found'}\n"
        
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


# Example usage
if __name__ == "__main__":
    generator = VideoScriptGenerator('story_database.json')
    
    # Generate a specific script
    print(generator.generate_script(1))  # Semi-truck BMW crash
    print("\n" + "="*80 + "\n")
    
    # Generate random road rage script
    print(generator.generate_random_script(theme='road_rage'))
    
    # Example of generating and saving a script
    # generator.generate_and_save_script(25, 'storytelling')