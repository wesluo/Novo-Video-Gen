#!/usr/bin/env python3
"""
URL Correction System
====================

Comprehensive URL correction system with fallback methods for fixing invalid 
Reddit URLs in story databases. Implements Method #1 (Reddit API Search) with 
Method #2 (Content Scraping) fallback, plus detailed failure tracking.

Usage:
    from Shared_Resources.url_correction import URLCorrectionSystem
    
    corrector = URLCorrectionSystem()
    result = corrector.attempt_url_correction(story_data)
    
Features:
- Method #1: Reddit API search using story title and subreddit
- Method #2: Content scraping fallback for edge cases  
- Comprehensive failure tracking and categorization
- Database update integration
- Performance logging and analytics

Author: Claude Code
Project: Multi-Product Video Generation System
"""

import json
import os
import re
import logging
from datetime import datetime
from typing import Dict, List, Optional, Any
from workflow_utils import ContentScraper, VideoExtractor, URLValidator

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# =============================================================================
# CONFIGURATION CONSTANTS
# =============================================================================

# Common words to exclude from search terms
COMMON_WORDS = {
    'with', 'in', 'the', 'a', 'an', 'and', 'or', 'but', 'of', 'to', 
    'for', 'by', 'from', 'on', 'at', 'is', 'was', 'are', 'were', 'has', 
    'have', 'had', 'will', 'would', 'could', 'should', 'may', 'might'
}

# Search term limits
MAX_SEARCH_TERMS_METHOD_1 = 6
MAX_SEARCH_TERMS_METHOD_2 = 4
MIN_WORD_LENGTH = 2
MIN_PRIORITY_WORD_LENGTH = 4

# Matching thresholds
TITLE_SIMILARITY_THRESHOLD_STRICT = 0.7
TITLE_SIMILARITY_THRESHOLD_LENIENT = 0.5
UPVOTE_TOLERANCE_STRICT = 1000
UPVOTE_TOLERANCE_LENIENT = 2000

# Confidence calculation weights
TITLE_SIMILARITY_WEIGHT = 0.7
UPVOTE_SIMILARITY_WEIGHT = 0.3
WORD_ORDER_BONUS_WEIGHT = 0.2

# Priority word patterns for enhanced search
PRIORITY_WORD_PATTERNS = [
    r'(?i)\b(corolla|camry|honda|toyota|bmw|ford|jeep|truck|semi|car|vehicle)\b',
    r'(?i)\b(crash|accident|rear|end|hit|collision|slam|wreck|smash)\b',
    r'(?i)\b(spacex|rocket|launch|highway|road|freeway|traffic|driver)\b',
    r'(?i)\b(dashcam|camera|video|footage|caught|captured)\b'
]

# Failure detection patterns
FAILURE_PATTERNS = {
    'no_search_results': ['no posts found', 'no matching posts', 'empty results'],
    'network_error': ['network', 'timeout', 'connection', 'unavailable', 'api error'],
    'subreddit_not_found': ['subreddit', 'invalid subreddit', 'not found'],
    'title_mismatch': ['no suitable matches', 'title', 'similarity'],
    'upvote_mismatch': ['upvote', 'engagement', 'score'],
    'parsing_error': ['parsing', 'json', 'decode', 'format']
}

class URLCorrectionSystem:
    """
    Comprehensive URL correction system with fallback methods.
    
    Implements a two-tier approach:
    1. Method #1: Reddit API Search (fast, effective)
    2. Method #2: Content Scraping (slower, edge cases)
    
    Features:
    - Automatic fallback between methods
    - Detailed failure tracking and categorization
    - Performance analytics and logging
    - Database integration support
    """
    
    def __init__(self, project_name: str = "URLCorrection"):
        """
        Initialize URL correction system.
        
        Args:
            project_name (str): Project name for logging
        """
        self.project_name = project_name
        self.content_scraper = ContentScraper()
        self.video_extractor = VideoExtractor()
        self.url_validator = URLValidator()
        
        # Failure tracking categories
        self.failure_categories = {
            'no_search_results': 'No matching posts found in Reddit search',
            'network_error': 'Reddit API unavailable or network issues',
            'title_mismatch': 'Found posts but no good title matches',
            'upvote_mismatch': 'Found posts but engagement doesnt match',
            'subreddit_not_found': 'Invalid or non-existent subreddit',
            'parsing_error': 'Error parsing Reddit API response',
            'unknown_error': 'Unexpected error during correction attempt'
        }
    
    def attempt_url_correction(self, story_data: Dict) -> Dict:
        """
        Main correction method with fallback system.
        
        Tries Method #1 first, falls back to Method #2 if needed,
        provides comprehensive failure tracking if both fail.
        
        Args:
            story_data (Dict): Story database entry with invalid URL
            
        Returns:
            Dict: Correction results with success status and details
        """
        correction_result = {
            'success': False,
            'story_id': story_data.get('id', 'unknown'),
            'original_url': story_data.get('url', ''),
            'corrected_url': None,
            'video_url': None,
            'method_used': None,
            'attempt_timestamp': datetime.now().isoformat(),
            'methods_attempted': [],
            'failure_reasons': [],
            'metadata': {}
        }
        
        logger.info(f"[{self.project_name}] Starting URL correction for story {story_data.get('id')}")
        
        # Method #1: Reddit API Search
        method1_result = self.try_method_1_reddit_search(story_data)
        correction_result['methods_attempted'].append('reddit_api_search')
        
        if method1_result['success']:
            logger.info(f"[{self.project_name}] Method #1 succeeded for story {story_data.get('id')}")
            correction_result.update(method1_result)
            correction_result['method_used'] = 'reddit_api_search'
            return correction_result
        else:
            correction_result['failure_reasons'].extend(method1_result.get('errors', []))
            logger.warning(f"[{self.project_name}] Method #1 failed for story {story_data.get('id')}: {method1_result.get('errors', [])}")
        
        # Method #2: Content Scraping Fallback
        method2_result = self.try_method_2_content_scraping(story_data, method1_result)
        correction_result['methods_attempted'].append('content_scraping')
        
        if method2_result['success']:
            logger.info(f"[{self.project_name}] Method #2 succeeded for story {story_data.get('id')}")
            correction_result.update(method2_result)
            correction_result['method_used'] = 'content_scraping'
            return correction_result
        else:
            correction_result['failure_reasons'].extend(method2_result.get('errors', []))
            logger.error(f"[{self.project_name}] Both methods failed for story {story_data.get('id')}")
        
        # Both methods failed - categorize failure
        correction_result['failure_category'] = self.categorize_failure(correction_result['failure_reasons'])
        logger.error(f"[{self.project_name}] URL correction failed for story {story_data.get('id')}: {correction_result['failure_category']}")
        
        return correction_result
    
    def try_method_1_reddit_search(self, story_data: Dict) -> Dict:
        """
        Method #1: Reddit API Search.
        
        Uses ContentScraper to search Reddit for matching posts using
        story title and subreddit information.
        
        Args:
            story_data (Dict): Story database entry
            
        Returns:
            Dict: Method #1 results
        """
        result = {
            'success': False,
            'corrected_url': None,
            'video_url': None,
            'match_confidence': 0.0,
            'errors': [],
            'metadata': {
                'method': 'reddit_api_search',
                'search_terms': [],
                'posts_found': 0
            }
        }
        
        try:
            # Extract search parameters
            subreddit = self.extract_subreddit(story_data.get('source', ''))
            search_terms = self.extract_search_terms(story_data.get('title', ''))
            
            if not subreddit:
                result['errors'].append('Cannot extract subreddit from source field')
                return result
                
            if not search_terms:
                result['errors'].append('Cannot extract search terms from title')
                return result
            
            result['metadata']['search_terms'] = search_terms
            
            # Search Reddit
            search_result = self.content_scraper.search_reddit_topic(
                subreddit=subreddit,
                search_terms=search_terms
            )
            
            if not search_result['success']:
                result['errors'].extend(search_result.get('errors', ['Reddit search failed']))
                return result
            
            posts = search_result.get('posts', [])
            result['metadata']['posts_found'] = len(posts)
            
            if not posts:
                result['errors'].append('No posts found in Reddit search')
                return result
            
            # Find best match
            best_match = self.find_best_match(posts, story_data)
            
            if not best_match:
                result['errors'].append('No suitable matches found in search results')
                return result
            
            # Extract video if possible
            video_url = None
            try:
                video_result = self.video_extractor.extract_from_reddit_url(best_match['url'])
                if video_result['success'] and video_result['videos']:
                    video_url = video_result['videos'][0]['url']
            except Exception as e:
                logger.warning(f"Video extraction failed but URL correction continues: {str(e)}")
            
            # Success
            result['success'] = True
            result['corrected_url'] = best_match['url']
            result['video_url'] = video_url
            result['match_confidence'] = best_match.get('confidence', 0.0)
            result['metadata']['matched_post'] = {
                'title': best_match['title'],
                'score': best_match['score'],
                'num_comments': best_match['num_comments']
            }
            
        except Exception as e:
            result['errors'].append(f'Method #1 exception: {str(e)}')
            logger.exception(f"Method #1 exception for story {story_data.get('id')}")
        
        return result
    
    def try_method_2_content_scraping(self, story_data: Dict, method1_result: Dict) -> Dict:
        """
        Method #2: Content Scraping Fallback.
        
        Attempts alternative approaches when Method #1 fails.
        Currently implements enhanced search with different parameters.
        
        Args:
            story_data (Dict): Story database entry
            method1_result (Dict): Results from Method #1 for context
            
        Returns:
            Dict: Method #2 results
        """
        result = {
            'success': False,
            'corrected_url': None,
            'video_url': None,
            'match_confidence': 0.0,
            'errors': [],
            'metadata': {
                'method': 'content_scraping',
                'fallback_strategy': 'enhanced_search'
            }
        }
        
        try:
            # Enhanced search with broader terms
            subreddit = self.extract_subreddit(story_data.get('source', ''))
            if not subreddit:
                result['errors'].append('Cannot extract subreddit for Method #2')
                return result
            
            # Try with fewer, more generic search terms
            enhanced_terms = self.extract_enhanced_search_terms(story_data.get('title', ''))
            result['metadata']['enhanced_search_terms'] = enhanced_terms
            
            if not enhanced_terms:
                result['errors'].append('Cannot generate enhanced search terms')
                return result
            
            # Enhanced Reddit search
            search_result = self.content_scraper.search_reddit_topic(
                subreddit=subreddit,
                search_terms=enhanced_terms
            )
            
            if not search_result['success']:
                result['errors'].extend(search_result.get('errors', ['Enhanced Reddit search failed']))
                return result
            
            posts = search_result.get('posts', [])
            result['metadata']['posts_found'] = len(posts)
            
            if not posts:
                result['errors'].append('No posts found in enhanced search')
                return result
            
            # More lenient matching for Method #2
            best_match = self.find_best_match(posts, story_data, lenient=True)
            
            if not best_match:
                result['errors'].append('No suitable matches in enhanced search')
                return result
            
            # Extract video if possible
            video_url = None
            try:
                video_result = self.video_extractor.extract_from_reddit_url(best_match['url'])
                if video_result['success'] and video_result['videos']:
                    video_url = video_result['videos'][0]['url']
            except Exception as e:
                logger.warning(f"Video extraction failed in Method #2: {str(e)}")
            
            # Success
            result['success'] = True
            result['corrected_url'] = best_match['url']
            result['video_url'] = video_url
            result['match_confidence'] = best_match.get('confidence', 0.0)
            result['metadata']['matched_post'] = {
                'title': best_match['title'],
                'score': best_match['score'],
                'num_comments': best_match['num_comments']
            }
            
        except Exception as e:
            result['errors'].append(f'Method #2 exception: {str(e)}')
            logger.exception(f"Method #2 exception for story {story_data.get('id')}")
        
        return result
    
    def extract_subreddit(self, source: str) -> Optional[str]:
        """Extract subreddit name from source field."""
        if not source:
            return None
            
        # Handle various formats: "r/IdiotsInCars", "IdiotsInCars", etc.
        source = source.strip()
        if source.startswith('r/'):
            return source[2:]
        elif source.startswith('/r/'):
            return source[3:]
        else:
            return source
    
    def extract_search_terms(self, title: str) -> List[str]:
        """Extract key search terms from story title."""
        if not title:
            return []
        
        # Split and clean words
        words = re.findall(r'\b[A-Za-z]+\b', title)
        search_terms = [word for word in words 
                       if word.lower() not in COMMON_WORDS and len(word) > MIN_WORD_LENGTH]
        
        return search_terms[:MAX_SEARCH_TERMS_METHOD_1]
    
    def extract_enhanced_search_terms(self, title: str) -> List[str]:
        """Extract broader search terms for Method #2."""
        if not title:
            return []
        
        # More aggressive filtering for broader search
        key_terms = []
        words = re.findall(r'\b[A-Za-z]+\b', title)
        
        # Prioritize using configured patterns
        for word in words:
            for pattern in PRIORITY_WORD_PATTERNS:
                if re.search(pattern, word):
                    key_terms.append(word)
                    break
        
        # Add other significant words if we don't have enough
        if len(key_terms) < 3:
            other_words = [w for w in words 
                          if len(w) > MIN_PRIORITY_WORD_LENGTH and w not in key_terms]
            key_terms.extend(other_words[:3])
        
        return key_terms[:MAX_SEARCH_TERMS_METHOD_2]
    
    def find_best_match(self, posts: List[Dict], story_data: Dict, lenient: bool = False) -> Optional[Dict]:
        """
        Find the best matching post from search results.
        
        Args:
            posts (List[Dict]): Search results from Reddit
            story_data (Dict): Original story data for comparison
            lenient (bool): Use more lenient matching criteria for Method #2
            
        Returns:
            Optional[Dict]: Best matching post with confidence score
        """
        if not posts:
            return None
        
        expected_upvotes = story_data.get('upvotes', 0) or story_data.get('expected_upvotes', 0)
        target_title = story_data.get('title', '')
        
        best_match = None
        best_score = 0.0
        
        # Select matching thresholds based on mode
        if lenient:
            title_threshold = TITLE_SIMILARITY_THRESHOLD_LENIENT
            upvote_tolerance = UPVOTE_TOLERANCE_LENIENT
        else:
            title_threshold = TITLE_SIMILARITY_THRESHOLD_STRICT
            upvote_tolerance = UPVOTE_TOLERANCE_STRICT
        
        for post in posts:
            # Calculate title similarity
            title_similarity = self.calculate_title_similarity(post['title'], target_title)
            
            # Calculate upvote proximity (normalize to 0-1 scale)
            if expected_upvotes > 0:
                upvote_diff = abs(post['score'] - expected_upvotes)
                upvote_similarity = max(0, 1 - (upvote_diff / max(expected_upvotes, upvote_tolerance)))
            else:
                upvote_similarity = 0.5  # Neutral if no expected upvotes
            
            # Combined confidence score using configured weights
            confidence = (title_similarity * TITLE_SIMILARITY_WEIGHT) + (upvote_similarity * UPVOTE_SIMILARITY_WEIGHT)
            
            # Check if this is a good match
            title_match = title_similarity >= title_threshold
            upvote_match = upvote_diff <= upvote_tolerance if expected_upvotes > 0 else True
            
            if (title_match or upvote_match) and confidence > best_score:
                best_score = confidence
                best_match = {
                    'url': post['url'],
                    'title': post['title'],
                    'score': post['score'],
                    'num_comments': post['num_comments'],
                    'confidence': confidence,
                    'title_similarity': title_similarity,
                    'upvote_similarity': upvote_similarity
                }
        
        return best_match
    
    def calculate_title_similarity(self, found_title: str, target_title: str) -> float:
        """Calculate similarity between titles using word overlap."""
        if not target_title or not found_title:
            return 0.0
        
        # Normalize and tokenize
        found_words = set(re.findall(r'\b[A-Za-z]+\b', found_title.lower()))
        target_words = set(re.findall(r'\b[A-Za-z]+\b', target_title.lower()))
        
        if not target_words:
            return 0.0
        
        # Calculate Jaccard similarity
        intersection = found_words.intersection(target_words)
        union = found_words.union(target_words)
        
        if not union:
            return 0.0
        
        jaccard = len(intersection) / len(union)
        
        # Also consider word order preservation (simple version)
        found_list = re.findall(r'\b[A-Za-z]+\b', found_title.lower())
        target_list = re.findall(r'\b[A-Za-z]+\b', target_title.lower())
        
        # Bonus for maintaining word order
        order_bonus = 0.0
        for i, word in enumerate(target_list):
            if word in found_list:
                found_index = found_list.index(word)
                # Bonus decreases with position difference
                order_bonus += 1.0 / (1 + abs(i - found_index))
        
        if target_list:
            order_bonus = order_bonus / len(target_list) * WORD_ORDER_BONUS_WEIGHT
        
        return min(1.0, jaccard + order_bonus)
    
    def categorize_failure(self, failure_reasons: List[str]) -> str:
        """Categorize failure reasons for analytics."""
        if not failure_reasons:
            return 'unknown_error'
        
        # Check for specific patterns in error messages
        all_errors = ' '.join(failure_reasons).lower()
        
        # Use configured failure patterns
        for category, patterns in FAILURE_PATTERNS.items():
            for pattern in patterns:
                if pattern in all_errors:
                    return category
        
        return 'unknown_error'
    
    def create_database_update(self, story_id: int, correction_result: Dict) -> Dict:
        """
        Create database update object for corrected story.
        
        Args:
            story_id (int): Story ID to update
            correction_result (Dict): Correction results
            
        Returns:
            Dict: Database update object
        """
        update_data = {
            'url_correction': {
                'attempted': True,
                'success': correction_result['success'],
                'attempt_date': correction_result['attempt_timestamp'],
                'method_used': correction_result.get('method_used'),
                'methods_attempted': correction_result['methods_attempted']
            }
        }
        
        if correction_result['success']:
            # Successful correction
            update_data['corrected_url'] = correction_result['corrected_url']
            if correction_result.get('video_url'):
                update_data['video_url'] = correction_result['video_url']
            update_data['url_correction']['match_confidence'] = correction_result.get('match_confidence', 0.0)
            
        else:
            # Failed correction
            update_data['url_correction']['failure_reasons'] = correction_result['failure_reasons']
            update_data['url_correction']['failure_category'] = correction_result.get('failure_category', 'unknown_error')
        
        return update_data

# Utility functions for integration
def correct_story_url(story_data: Dict, project_name: str = "URLCorrection") -> Dict:
    """
    Convenience function for single story URL correction.
    
    Args:
        story_data (Dict): Story database entry
        project_name (str): Project name for logging
        
    Returns:
        Dict: Correction results
    """
    corrector = URLCorrectionSystem(project_name)
    return corrector.attempt_url_correction(story_data)

def batch_correct_urls(stories: List[Dict], project_name: str = "URLCorrection") -> Dict:
    """
    Batch URL correction for multiple stories.
    
    Args:
        stories (List[Dict]): List of story database entries
        project_name (str): Project name for logging
        
    Returns:
        Dict: Batch correction statistics
    """
    corrector = URLCorrectionSystem(project_name)
    
    stats = {
        'total_attempted': len(stories),
        'successful_corrections': 0,
        'method_1_success': 0,
        'method_2_success': 0,
        'failures': 0,
        'failure_categories': {},
        'results': []
    }
    
    for story in stories:
        result = corrector.attempt_url_correction(story)
        stats['results'].append(result)
        
        if result['success']:
            stats['successful_corrections'] += 1
            if result['method_used'] == 'reddit_api_search':
                stats['method_1_success'] += 1
            elif result['method_used'] == 'content_scraping':
                stats['method_2_success'] += 1
        else:
            stats['failures'] += 1
            category = result.get('failure_category', 'unknown_error')
            stats['failure_categories'][category] = stats['failure_categories'].get(category, 0) + 1
    
    return stats

if __name__ == "__main__":
    # Example usage
    print("URL Correction System - Test Mode")
    
    # Test story (Story #15 format)  
    test_story = {
        "id": 15,
        "title": "Corolla Rear-Ended with SpaceX Launch in Background",
        "source": "r/Roadcam",
        "url": "reddit.com/r/Roadcam",  # Invalid URL
        "upvotes": 8881
    }
    
    # Test correction
    corrector = URLCorrectionSystem("Test")
    result = corrector.attempt_url_correction(test_story)
    
    print(f"Correction Result: {result['success']}")
    if result['success']:
        print(f"Method Used: {result['method_used']}")
        print(f"Corrected URL: {result['corrected_url']}")
        if result['video_url']:
            print(f"Video URL: {result['video_url']}")
    else:
        print(f"Failure Category: {result.get('failure_category')}")
        print(f"Errors: {result['failure_reasons']}")