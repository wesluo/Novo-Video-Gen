#!/usr/bin/env python3
"""
Universal Video Generation Workflow Utilities
==============================================

Shared utilities for video extraction, content scraping, and workflow optimization
across all video generation projects (Insurance_Scripts, Crypto_Scripts, App_Scripts).

Features:
- YouTube and video link extraction from Reddit posts
- Original Reddit post content scraping  
- Scene timing validation and optimization
- Folder structure management
- Error handling and logging

Usage:
    from Shared_Resources.workflow_utils import VideoExtractor, ContentScraper, SceneOptimizer
    
    # Extract videos from Reddit post
    extractor = VideoExtractor()
    videos = extractor.extract_from_reddit_url(story_url)
    
    # Scrape original post content
    scraper = ContentScraper()  
    content = scraper.scrape_reddit_post(story_url)
    
    # Optimize scene timing
    optimizer = SceneOptimizer()
    scenes = optimizer.optimize_scenes(script_content)
"""

import os
import re
import json
import requests
import time
from datetime import datetime
from typing import Dict, List, Optional, Tuple, Any
from urllib.parse import urlparse, parse_qs
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class WorkflowFolders:
    """
    Enhanced utility class for managing per-story folder structure across projects.
    Creates organized storage with separate folders for each story's artifacts.
    """
    
    @staticmethod
    def ensure_folders(base_path: str) -> Tuple[str, str]:
        """
        Create video/ and post/ subfolders if they don't exist (legacy support).
        
        Args:
            base_path (str): Base project directory path
            
        Returns:
            Tuple[str, str]: (video_path, post_path)
        """
        video_path = os.path.join(base_path, 'video')
        post_path = os.path.join(base_path, 'post')
        
        os.makedirs(video_path, exist_ok=True)
        os.makedirs(post_path, exist_ok=True)
        
        logger.info(f"Ensured folders exist: {video_path}, {post_path}")
        return video_path, post_path
    
    @staticmethod
    def create_story_folder(base_path: str, story_id: int, story_title: str) -> str:
        """
        Create organized folder structure for a specific story.
        
        Args:
            base_path (str): Base project directory path
            story_id (int): Story ID number
            story_title (str): Story title for folder naming
            
        Returns:
            str: Path to created story folder
        """
        # Clean story title for folder name
        clean_title = re.sub(r'[^\w\s-]', '', story_title)
        clean_title = re.sub(r'[-\s]+', '_', clean_title).strip('_').lower()
        
        # Limit length to avoid filesystem issues
        if len(clean_title) > 50:
            clean_title = clean_title[:50].rstrip('_')
        
        # Create folder name
        folder_name = f"story_{story_id:03d}_{clean_title}"
        story_path = os.path.join(base_path, 'stories', folder_name)
        
        # Create directory structure
        os.makedirs(story_path, exist_ok=True)
        
        logger.info(f"Created story folder: {story_path}")
        return story_path
    
    @staticmethod
    def get_story_paths(story_folder: str) -> Dict[str, str]:
        """
        Get all file paths for a story folder.
        
        Args:
            story_folder (str): Path to story folder
            
        Returns:
            Dict[str, str]: Dictionary of file paths
        """
        return {
            'script': os.path.join(story_folder, 'script.md'),
            'content': os.path.join(story_folder, 'original_post.md'),
            'video': os.path.join(story_folder, 'video.mp4'),
            'metadata': os.path.join(story_folder, 'metadata.json'),
            'log': os.path.join(story_folder, 'generation_log.txt')
        }

class VideoExtractor:
    """
    Extract and download embedded videos from Reddit posts for use in video production.
    Enhanced with yt-dlp support for actual video downloading.
    """
    
    def __init__(self):
        self.supported_platforms = [
            'youtube.com', 'youtu.be', 'v.redd.it', 'streamable.com', 
            'gfycat.com', 'imgur.com'
        ]
        
    def download_video(self, video_url: str, output_path: str) -> Dict[str, Any]:
        """
        Download video from URL to specified path using yt-dlp.
        
        Args:
            video_url (str): URL of video to download
            output_path (str): Full path where video should be saved
            
        Returns:
            Dict containing download results and metadata
        """
        result = {
            'success': False,
            'output_file': None,
            'metadata': {},
            'errors': []
        }
        
        try:
            # Import yt-dlp dynamically to avoid dependency issues
            try:
                import yt_dlp
            except ImportError:
                result['errors'].append("yt-dlp not installed. Install with: pip install yt-dlp")
                return result
            
            # Configure yt-dlp options
            ydl_opts = {
                'outtmpl': output_path,
                'format': 'best[height<=720]/best',  # Prefer 720p or lower
                'writeinfojson': False,  # Don't create info JSON files
                'writedescription': False,
                'writesubtitles': False,
                'writeautomaticsub': False,
                'ignoreerrors': True,
                'no_warnings': True,
                'quiet': True
            }
            
            # Download video
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                # Extract info first
                info = ydl.extract_info(video_url, download=False)
                
                if info:
                    result['metadata'] = {
                        'title': info.get('title', 'Unknown'),
                        'duration': info.get('duration', 0),
                        'uploader': info.get('uploader', 'Unknown'),
                        'view_count': info.get('view_count', 0),
                        'upload_date': info.get('upload_date', ''),
                        'resolution': f"{info.get('width', 0)}x{info.get('height', 0)}"
                    }
                
                # Download the video
                ydl.download([video_url])
                
                # Check if file was created
                if os.path.exists(output_path):
                    result['success'] = True
                    result['output_file'] = output_path
                    logger.info(f"Video downloaded successfully: {output_path}")
                else:
                    # yt-dlp might have changed the filename, try to find it
                    base_path = os.path.dirname(output_path)
                    if os.path.exists(base_path):
                        files = [f for f in os.listdir(base_path) if f.startswith('video')]
                        if files:
                            actual_file = os.path.join(base_path, files[0])
                            # Rename to expected name
                            os.rename(actual_file, output_path)
                            result['success'] = True
                            result['output_file'] = output_path
                        else:
                            result['errors'].append("Video file not found after download")
                    else:
                        result['errors'].append("Output directory not found")
                        
        except Exception as e:
            result['errors'].append(f"Download error: {str(e)}")
            logger.error(f"Video download failed: {str(e)}")
            
        return result
        
    def extract_from_reddit_url(self, reddit_url: str) -> Dict[str, Any]:
        """
        Extract video links from a Reddit post URL.
        
        Args:
            reddit_url (str): Direct Reddit post URL
            
        Returns:
            Dict containing video information and status
        """
        result = {
            'success': False,
            'videos': [],
            'errors': [],
            'metadata': {
                'extracted_at': datetime.now().isoformat(),
                'source_url': reddit_url
            }
        }
        
        try:
            # Add .json to Reddit URL for API access
            if 'reddit.com' in reddit_url and not reddit_url.endswith('.json'):
                api_url = reddit_url.rstrip('/') + '.json'
            else:
                api_url = reddit_url
                
            # Request Reddit post data
            headers = {'User-Agent': 'VideoGeneration/1.0'}
            response = requests.get(api_url, headers=headers, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            # Extract post data
            if isinstance(data, list) and len(data) > 0:
                post_data = data[0]['data']['children'][0]['data']
            else:
                post_data = data['data']['children'][0]['data']
                
            # Look for videos in different locations
            videos_found = []
            
            # Check for direct video URLs
            if 'url' in post_data:
                video_info = self._extract_video_info(post_data['url'])
                if video_info:
                    videos_found.append(video_info)
                    
            # Check for embedded videos in selftext
            if 'selftext' in post_data and post_data['selftext']:
                embedded_videos = self._find_video_links_in_text(post_data['selftext'])
                videos_found.extend(embedded_videos)
                
            # Check for media/preview data
            if 'media' in post_data and post_data['media']:
                media_videos = self._extract_from_media_object(post_data['media'])
                videos_found.extend(media_videos)
                
            result['videos'] = videos_found
            result['success'] = len(videos_found) > 0
            
            if not result['success']:
                result['errors'].append("No extractable videos found in Reddit post")
                
        except requests.RequestException as e:
            result['errors'].append(f"Network error accessing Reddit: {str(e)}")
        except (KeyError, IndexError) as e:
            result['errors'].append(f"Reddit data parsing error: {str(e)}")
        except Exception as e:
            result['errors'].append(f"Unexpected error: {str(e)}")
            
        return result
    
    def _extract_video_info(self, url: str) -> Optional[Dict[str, str]]:
        """Extract video information from a URL."""
        if not self._is_video_url(url):
            return None
            
        parsed = urlparse(url)
        
        video_info = {
            'url': url,
            'platform': parsed.netloc,
            'type': 'unknown'
        }
        
        # YouTube-specific handling
        if 'youtube.com' in parsed.netloc or 'youtu.be' in parsed.netloc:
            video_info['type'] = 'youtube'
            video_info['video_id'] = self._extract_youtube_id(url)
            
        # Direct video file
        elif url.endswith(('.mp4', '.webm', '.mov', '.avi')):
            video_info['type'] = 'direct'
            
        # Reddit video
        elif 'v.redd.it' in parsed.netloc:
            video_info['type'] = 'reddit_video'
            
        return video_info
    
    def _is_video_url(self, url: str) -> bool:
        """Check if URL is likely to contain video content."""
        if not url:
            return False
            
        parsed = urlparse(url)
        
        # Check for supported platforms
        for platform in self.supported_platforms:
            if platform in parsed.netloc:
                return True
                
        # Check for direct video file extensions
        if url.endswith(('.mp4', '.webm', '.mov', '.avi', '.mkv', '.flv')):
            return True
            
        return False
    
    def _extract_youtube_id(self, url: str) -> Optional[str]:
        """Extract YouTube video ID from URL."""
        patterns = [
            r'(?:youtube\.com\/watch\?v=|youtu\.be\/)([a-zA-Z0-9_-]{11})',
            r'youtube\.com\/embed\/([a-zA-Z0-9_-]{11})'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
                
        return None
    
    def _find_video_links_in_text(self, text: str) -> List[Dict[str, str]]:
        """Find video links in text content."""
        videos = []
        
        # Pattern for URLs
        url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        urls = re.findall(url_pattern, text)
        
        for url in urls:
            video_info = self._extract_video_info(url)
            if video_info:
                videos.append(video_info)
                
        return videos
    
    def _extract_from_media_object(self, media: Dict) -> List[Dict[str, str]]:
        """Extract videos from Reddit media object."""
        videos = []
        
        # Handle different media types
        if 'reddit_video' in media:
            videos.append({
                'url': media['reddit_video']['fallback_url'],
                'platform': 'v.redd.it',
                'type': 'reddit_video',
                'duration': media['reddit_video'].get('duration')
            })
            
        return videos

class ContentScraper:
    """
    Scrape original Reddit post content for authentic script foundations.
    Enhanced with markdown file generation for organized storage.
    """
    
    def __init__(self):
        self.headers = {'User-Agent': 'VideoGeneration/1.0'}
    
    def save_content_to_file(self, content: Dict[str, Any], output_path: str) -> bool:
        """
        Save scraped content to markdown file.
        
        Args:
            content (Dict): Scraped content dictionary
            output_path (str): Path to save markdown file
            
        Returns:
            bool: Success status
        """
        try:
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            # Format content as markdown
            markdown_content = f"""# {content.get('title', 'Unknown Title')}

**Subreddit**: r/{content.get('subreddit', 'unknown')}  
**Author**: u/{content.get('author', 'unknown')}  
**Score**: {content.get('score', 0):,} upvotes ({content.get('upvote_ratio', 0):.1%} upvote ratio)  
**Comments**: {content.get('num_comments', 0):,}  
**Posted**: {datetime.fromtimestamp(content.get('created_utc', 0)).strftime('%Y-%m-%d %H:%M UTC') if content.get('created_utc') else 'Unknown'}  
**Original URL**: {content.get('url', 'N/A')}

---

## Post Content

{content.get('selftext', 'No text content') if content.get('selftext') else '*This post contains only a link or media*'}

---

## Top Comments

"""
            
            # Add top comments
            if content.get('top_comments'):
                for i, comment in enumerate(content['top_comments'], 1):
                    markdown_content += f"""### Comment #{i} ({comment.get('score', 0)} points)
**Author**: u/{comment.get('author', 'unknown')}

{comment.get('body', 'No content')}

---

"""
            else:
                markdown_content += "*No comments available*\n"
            
            # Add extraction metadata
            markdown_content += f"""
## Extraction Metadata

**Scraped**: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}  
**Source**: Reddit API  
**Status**: Successfully extracted
"""
            
            # Write to file
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
                
            logger.info(f"Content saved to: {output_path}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to save content to file: {str(e)}")
            return False
        
    def scrape_reddit_post(self, reddit_url: str) -> Dict[str, Any]:
        """
        Scrape original content from Reddit post URL.
        
        Args:
            reddit_url (str): Direct Reddit post URL
            
        Returns:
            Dict containing scraped content and metadata
        """
        result = {
            'success': False,
            'content': {},
            'errors': [],
            'metadata': {
                'scraped_at': datetime.now().isoformat(),
                'source_url': reddit_url
            }
        }
        
        try:
            # Convert to JSON API URL
            if 'reddit.com' in reddit_url and not reddit_url.endswith('.json'):
                api_url = reddit_url.rstrip('/') + '.json'
            else:
                api_url = reddit_url
                
            # Request post data
            response = requests.get(api_url, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            # Extract post data
            if isinstance(data, list) and len(data) > 0:
                post_data = data[0]['data']['children'][0]['data']
                comments_data = data[1]['data']['children'] if len(data) > 1 else []
            else:
                post_data = data['data']['children'][0]['data']
                comments_data = []
                
            # Extract content
            content = {
                'title': post_data.get('title', ''),
                'selftext': post_data.get('selftext', ''),
                'url': post_data.get('url', ''),
                'subreddit': post_data.get('subreddit', ''),
                'author': post_data.get('author', ''),
                'created_utc': post_data.get('created_utc', 0),
                'upvotes': post_data.get('ups', 0),
                'downvotes': post_data.get('downs', 0),
                'num_comments': post_data.get('num_comments', 0),
                'score': post_data.get('score', 0),
                'upvote_ratio': post_data.get('upvote_ratio', 0.0),
                'top_comments': []
            }
            
            # Extract top comments
            for comment in comments_data[:5]:  # Top 5 comments
                if comment['data'].get('body'):
                    content['top_comments'].append({
                        'body': comment['data']['body'],
                        'score': comment['data'].get('score', 0),
                        'author': comment['data'].get('author', 'unknown')
                    })
                    
            result['content'] = content
            result['success'] = True
            
        except requests.RequestException as e:
            result['errors'].append(f"Network error: {str(e)}")
        except (KeyError, IndexError, json.JSONDecodeError) as e:
            result['errors'].append(f"Data parsing error: {str(e)}")
        except Exception as e:
            result['errors'].append(f"Unexpected error: {str(e)}")
            
        return result
    
    def search_reddit_topic(self, subreddit: str, search_terms: List[str]) -> Dict[str, Any]:
        """
        Search Reddit subreddit for posts matching terms.
        
        Args:
            subreddit (str): Subreddit name (without r/)
            search_terms (List[str]): Terms to search for
            
        Returns:
            Dict containing search results
        """
        result = {
            'success': False,
            'posts': [],
            'errors': [],
            'metadata': {
                'searched_at': datetime.now().isoformat(),
                'subreddit': subreddit,
                'search_terms': search_terms
            }
        }
        
        try:
            # Build search query
            query = ' '.join(search_terms)
            search_url = f"https://www.reddit.com/r/{subreddit}/search.json?q={query}&restrict_sr=1&sort=top&limit=10"
            
            response = requests.get(search_url, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            posts = []
            
            for child in data['data']['children']:
                post_data = child['data']
                posts.append({
                    'title': post_data.get('title', ''),
                    'url': f"https://reddit.com{post_data.get('permalink', '')}",
                    'score': post_data.get('score', 0),
                    'num_comments': post_data.get('num_comments', 0),
                    'created_utc': post_data.get('created_utc', 0)
                })
                
            result['posts'] = posts
            result['success'] = len(posts) > 0
            
            if not result['success']:
                result['errors'].append("No matching posts found")
                
        except requests.RequestException as e:
            result['errors'].append(f"Network error: {str(e)}")
        except Exception as e:
            result['errors'].append(f"Search error: {str(e)}")
            
        return result

class SceneOptimizer:
    """
    Optimize script scenes for ≤10 second timing and production efficiency.
    Enhanced with dynamic scene generation to eliminate hardcoded timing patterns.
    """
    
    def __init__(self):
        self.max_scene_duration = 10  # seconds
        self.min_scene_duration = 3   # seconds
        self.total_duration = 30     # seconds (standard video length)
        
        # Pre-defined compliant scene structures for different formats
        self.scene_templates = {
            'comedy': [
                {'name': 'HOOK', 'duration': 3},
                {'name': 'SETUP', 'duration': 6}, 
                {'name': 'CONTEXT', 'duration': 3},
                {'name': 'PUNCHLINE_PART_1', 'duration': 6},
                {'name': 'PUNCHLINE_PART_2', 'duration': 6},
                {'name': 'CTA_SPT', 'duration': 6}
            ],
            'educational': [
                {'name': 'HOOK', 'duration': 3},
                {'name': 'EXCLUSIVITY', 'duration': 3}, 
                {'name': 'STORY_SETUP', 'duration': 3},
                {'name': 'LESSON_PART_1', 'duration': 3},
                {'name': 'LESSON_PART_2', 'duration': 3},
                {'name': 'PROOF', 'duration': 3},
                {'name': 'SPT_CONNECTION', 'duration': 3},
                {'name': 'CTA_MAIN', 'duration': 3},
                {'name': 'OUTRO', 'duration': 3},
                {'name': 'CLOSING', 'duration': 3}
            ],
            'transformation': [
                {'name': 'HOOK', 'duration': 3},
                {'name': 'PROBLEM', 'duration': 5},
                {'name': 'LESSON_PART_1', 'duration': 7},
                {'name': 'LESSON_PART_2', 'duration': 7},
                {'name': 'CTA_SPT', 'duration': 8}
            ],
            'storytelling': [
                {'name': 'HOOK', 'duration': 3},
                {'name': 'SETUP', 'duration': 7},
                {'name': 'STORY_PART_1', 'duration': 6},
                {'name': 'STORY_PART_2', 'duration': 6},
                {'name': 'CTA_SPT', 'duration': 8}
            ],
            'pov_story': [
                {'name': 'HOOK', 'duration': 3},
                {'name': 'SETUP', 'duration': 9},
                {'name': 'EXPERIENCE_PART_1', 'duration': 5},
                {'name': 'EXPERIENCE_PART_2', 'duration': 5},
                {'name': 'CTA_SPT', 'duration': 8}
            ],
            'challenge': [
                {'name': 'HOOK', 'duration': 3},
                {'name': 'CHALLENGE_SETUP', 'duration': 9},
                {'name': 'BENEFITS_PART_1', 'duration': 5},
                {'name': 'BENEFITS_PART_2', 'duration': 5},
                {'name': 'CTA_SPT', 'duration': 8}
            ]
        }
    
    def generate_scene_structure(self, format_type: str) -> List[Dict[str, Any]]:
        """
        Generate compliant scene structure for a given format.
        Eliminates all hardcoded timing patterns.
        
        Args:
            format_type (str): Script format (comedy, educational, etc.)
            
        Returns:
            List[Dict]: Scene structure with timing information
        """
        template = self.scene_templates.get(format_type, self.scene_templates['educational'])
        
        scenes = []
        current_time = 0
        
        for scene_info in template:
            scene = {
                'name': scene_info['name'],
                'start': current_time,
                'end': current_time + scene_info['duration'],
                'duration': scene_info['duration'],
                'timing_display': f"{scene_info['name']} ({current_time}-{current_time + scene_info['duration']} seconds)"
            }
            scenes.append(scene)
            current_time += scene_info['duration']
            
        return scenes
    
    def get_scene_timing_display(self, format_type: str, scene_name: str) -> str:
        """
        Get properly formatted timing display for a specific scene.
        Replaces hardcoded (X-Y seconds) patterns.
        
        Args:
            format_type (str): Script format
            scene_name (str): Name of the scene
            
        Returns:
            str: Formatted timing display like "HOOK (0-3 seconds)"
        """
        scenes = self.generate_scene_structure(format_type)
        
        for scene in scenes:
            if scene['name'] == scene_name:
                return scene['timing_display']
                
        # Fallback for unknown scenes
        return f"{scene_name} (0-{self.min_scene_duration} seconds)"
        
    def validate_scene_timing(self, scenes: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Validate that all scenes meet timing requirements.
        
        Args:
            scenes (List[Dict]): List of scene dictionaries with timing info
            
        Returns:
            Dict containing validation results
        """
        result = {
            'valid': True,
            'violations': [],
            'total_duration': 0,
            'scene_count': len(scenes)
        }
        
        for i, scene in enumerate(scenes):
            duration = self._extract_scene_duration(scene)
            result['total_duration'] += duration
            
            if duration > self.max_scene_duration:
                result['valid'] = False
                result['violations'].append({
                    'scene': i + 1,
                    'duration': duration,
                    'issue': f'Exceeds maximum {self.max_scene_duration}s'
                })
                
            if duration < self.min_scene_duration:
                result['valid'] = False
                result['violations'].append({
                    'scene': i + 1,
                    'duration': duration,
                    'issue': f'Below minimum {self.min_scene_duration}s'
                })
                
        return result
    
    def optimize_scenes(self, script_content: str) -> List[Dict[str, Any]]:
        """
        Break script content into optimized ≤10 second scenes.
        
        Args:
            script_content (str): Original script content
            
        Returns:
            List of optimized scene dictionaries
        """
        # Parse existing timing patterns
        timing_pattern = r'(\w+)\s*\((\d+)-(\d+)\s*seconds?\)'
        matches = re.findall(timing_pattern, script_content)
        
        optimized_scenes = []
        
        for match in matches:
            scene_name, start_time, end_time = match
            duration = int(end_time) - int(start_time)
            
            if duration <= self.max_scene_duration:
                # Scene already meets requirements
                optimized_scenes.append({
                    'name': scene_name,
                    'start': int(start_time),
                    'end': int(end_time),
                    'duration': duration
                })
            else:
                # Split scene into smaller parts
                sub_scenes = self._split_scene(scene_name, int(start_time), int(end_time))
                optimized_scenes.extend(sub_scenes)
                
        return optimized_scenes
    
    def _extract_scene_duration(self, scene: Dict[str, Any]) -> int:
        """Extract duration from scene dictionary."""
        if 'duration' in scene:
            return scene['duration']
        elif 'start' in scene and 'end' in scene:
            return scene['end'] - scene['start']
        else:
            return 0
            
    def _split_scene(self, scene_name: str, start: int, end: int) -> List[Dict[str, Any]]:
        """Split a long scene into multiple ≤10 second scenes."""
        total_duration = end - start
        num_parts = (total_duration + self.max_scene_duration - 1) // self.max_scene_duration  # Ceiling division
        
        scenes = []
        current_start = start
        
        for i in range(num_parts):
            part_duration = min(self.max_scene_duration, end - current_start)
            scenes.append({
                'name': f"{scene_name}_PART_{i+1}",
                'start': current_start,
                'end': current_start + part_duration,
                'duration': part_duration
            })
            current_start += part_duration
            
        return scenes

class URLValidator:
    """
    Validate URLs before attempting video extraction or content scraping.
    Ensures proper URL format and prevents processing invalid stories.
    """
    
    @staticmethod
    def validate_reddit_url(url: str) -> Dict[str, Any]:
        """
        Validate a Reddit URL for proper format and structure.
        
        Args:
            url (str): URL to validate
            
        Returns:
            Dict containing validation status and details
        """
        result = {
            'valid': False,
            'error': None,
            'url_type': None,
            'cleaned_url': None
        }
        
        # Check if URL exists
        if not url:
            result['error'] = 'No URL provided'
            return result
            
        # Check for protocol
        if not url.startswith(('http://', 'https://')):
            # Try adding https://
            if url.startswith('reddit.com'):
                url = 'https://' + url
                result['cleaned_url'] = url
            else:
                result['error'] = f'Invalid URL format: missing protocol (http/https)'
                return result
        
        # Parse URL
        try:
            parsed = urlparse(url)
            
            # Check if it's a Reddit URL
            if 'reddit.com' not in parsed.netloc:
                result['error'] = 'Not a Reddit URL'
                return result
                
            # Check for specific post path
            if '/comments/' in parsed.path:
                result['url_type'] = 'post'
                result['valid'] = True
                result['cleaned_url'] = url
            elif '/r/' in parsed.path and len(parsed.path.split('/')) <= 3:
                # Just a subreddit URL, not a specific post
                result['error'] = 'URL points to subreddit, not specific post'
                result['url_type'] = 'subreddit'
            else:
                result['error'] = 'Invalid Reddit URL structure'
                
        except Exception as e:
            result['error'] = f'URL parsing error: {str(e)}'
            
        return result
    
    @staticmethod
    def validate_story_urls(story_data: Dict) -> Dict[str, Any]:
        """
        Validate all URLs in a story data dictionary.
        
        Args:
            story_data (Dict): Story dictionary with potential URLs
            
        Returns:
            Dict containing validation results for all URLs found
        """
        results = {
            'all_valid': True,
            'validations': {}
        }
        
        # Check main URL field
        if 'url' in story_data:
            url_validation = URLValidator.validate_reddit_url(story_data['url'])
            results['validations']['main_url'] = url_validation
            if not url_validation['valid']:
                results['all_valid'] = False
                
        # Check for alternate URL fields
        for field in ['source_url', 'reddit_url', 'original_url']:
            if field in story_data:
                url_validation = URLValidator.validate_reddit_url(story_data[field])
                results['validations'][field] = url_validation
                if not url_validation['valid']:
                    results['all_valid'] = False
                    
        return results

class WorkflowLogger:
    """
    Centralized logging for workflow operations across projects.
    """
    
    def __init__(self, project_name: str):
        self.project_name = project_name
        self.log_file = f"{project_name}_workflow.log"
        
    def log_video_extraction(self, story_id: int, result: Dict[str, Any]):
        """Log video extraction results."""
        status = "SUCCESS" if result['success'] else "FAILED"
        video_count = len(result.get('videos', []))
        
        logger.info(f"[{self.project_name}] Video extraction for story {story_id}: {status} - {video_count} videos found")
        
        if result.get('errors'):
            for error in result['errors']:
                logger.warning(f"[{self.project_name}] Video extraction error: {error}")
                
    def log_content_scraping(self, story_id: int, result: Dict[str, Any]):
        """Log content scraping results."""
        status = "SUCCESS" if result['success'] else "FAILED"
        
        logger.info(f"[{self.project_name}] Content scraping for story {story_id}: {status}")
        
        if result.get('errors'):
            for error in result['errors']:
                logger.warning(f"[{self.project_name}] Content scraping error: {error}")
                
    def log_scene_optimization(self, story_id: int, scene_count: int, violations: List):
        """Log scene optimization results."""
        status = "VALID" if not violations else "VIOLATIONS"
        
        logger.info(f"[{self.project_name}] Scene optimization for story {story_id}: {status} - {scene_count} scenes")
        
        for violation in violations:
            logger.warning(f"[{self.project_name}] Scene timing violation: Scene {violation['scene']} - {violation['issue']}")
    
    def log_url_validation_failure(self, story_id: int, error: str):
        """Log URL validation failures."""
        logger.error(f"[{self.project_name}] URL validation FAILED for story {story_id}: {error}")
        
    def log_story_failure(self, story_id: int, reason: str):
        """Log story processing failure."""
        logger.error(f"[{self.project_name}] Story {story_id} marked as FAILED: {reason}")

# Example usage functions
def example_video_extraction():
    """Example of how to use video extraction."""
    extractor = VideoExtractor()
    result = extractor.extract_from_reddit_url("https://www.reddit.com/r/IdiotsInCars/comments/example/")
    
    if result['success']:
        print(f"Found {len(result['videos'])} videos")
        for video in result['videos']:
            print(f"- {video['platform']}: {video['url']}")
    else:
        print("Video extraction failed:", result['errors'])

def example_content_scraping():
    """Example of how to use content scraping."""
    scraper = ContentScraper()
    result = scraper.scrape_reddit_post("https://www.reddit.com/r/IdiotsInCars/comments/example/")
    
    if result['success']:
        content = result['content']
        print(f"Title: {content['title']}")
        print(f"Score: {content['score']}")
        print(f"Comments: {len(content['top_comments'])}")
    else:
        print("Content scraping failed:", result['errors'])

def example_scene_optimization():
    """Example of how to use scene optimization."""
    optimizer = SceneOptimizer()
    
    # Example script with current timing
    script = """
    HOOK (0-3 seconds): Hook content
    SETUP (3-15 seconds): Long setup content  
    CTA (15-30 seconds): Call to action
    """
    
    scenes = optimizer.optimize_scenes(script)
    validation = optimizer.validate_scene_timing(scenes)
    
    print(f"Optimized to {len(scenes)} scenes")
    print(f"Valid timing: {validation['valid']}")
    
    if validation['violations']:
        for violation in validation['violations']:
            print(f"- Scene {violation['scene']}: {violation['issue']}")

if __name__ == "__main__":
    # Run examples
    print("Video Extraction Example:")
    example_video_extraction()
    
    print("\nContent Scraping Example:")
    example_content_scraping()
    
    print("\nScene Optimization Example:")
    example_scene_optimization()