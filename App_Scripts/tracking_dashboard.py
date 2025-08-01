#!/usr/bin/env python3
"""
Novo Video Script Tracking Dashboard
=====================================

A comprehensive analytics and progress monitoring system for the Novo Video Script Generation project.
Provides real-time insights into story completion, theme diversity, engagement analysis, and intelligent
suggestions for optimal content creation workflow.

Features:
- Real-time progress tracking (7/90 stories completed - 7.8%)
- Theme and format completion breakdowns
- High-engagement story prioritization
- Smart story selection algorithm balancing engagement + diversity
- Export capabilities for project management
- Actionable insights for content strategy

Usage:
    # Run dashboard in terminal
    python3 tracking_dashboard.py
    
    # Use programmatically
    from tracking_dashboard import TrackingDashboard
    dashboard = TrackingDashboard('story_database.json')
    dashboard.print_dashboard()
    
    # Get smart suggestions
    suggestions = dashboard.get_next_story_suggestions(5)

Author: Claude Code
Project: Novo Insurance Video Script Generation System
"""

import json
from datetime import datetime
from collections import Counter
from typing import Dict, List

class TrackingDashboard:
    """
    Analytics and tracking dashboard for Novo Video Script Generation project.
    
    Provides comprehensive insights into project progress, story completion rates,
    theme diversity, and intelligent recommendations for optimal content creation.
    
    Attributes:
        stories (List[Dict]): List of all story records with tracking data
        metadata (Dict): Project metadata including tracking statistics
        
    Example:
        >>> dashboard = TrackingDashboard('story_database.json')
        >>> stats = dashboard.get_overview_stats()
        >>> print(f"Completion: {stats['completion_rate']}")
        >>> suggestions = dashboard.get_next_story_suggestions(3)
    """
    
    def __init__(self, story_db_path: str):
        """
        Initialize dashboard with story database.
        
        Args:
            story_db_path (str): Path to the story database JSON file
            
        Raises:
            FileNotFoundError: If database file doesn't exist
            json.JSONDecodeError: If database file is malformed
        """
        with open(story_db_path, 'r') as f:
            self.data = json.load(f)
        self.stories = self.data['stories']
        self.metadata = self.data.get('metadata', {})
    
    def get_overview_stats(self) -> Dict:
        """
        Get high-level project statistics.
        
        Returns:
            Dict: Statistics including total stories, completion counts, and rate
            
        Example:
            >>> stats = dashboard.get_overview_stats()
            >>> print(f"Progress: {stats['completed']}/{stats['total_stories']}")
        """
        completed = sum(1 for s in self.stories if s.get('status') == 'completed')
        in_progress = sum(1 for s in self.stories if s.get('status') == 'in_progress')
        pending = sum(1 for s in self.stories if s.get('status') == 'pending')
        
        return {
            'total_stories': len(self.stories),
            'completed': completed,
            'in_progress': in_progress,
            'pending': pending,
            'completion_rate': f"{(completed / len(self.stories) * 100):.1f}%"
        }
    
    def get_theme_breakdown(self) -> Dict:
        """Get breakdown by theme"""
        theme_stats = {}
        
        # Group stories by theme
        theme_counter = Counter(s['theme'] for s in self.stories)
        
        for theme, total in theme_counter.items():
            completed = sum(1 for s in self.stories 
                          if s['theme'] == theme and s.get('status') == 'completed')
            theme_stats[theme] = {
                'total': total,
                'completed': completed,
                'pending': total - completed,
                'completion_rate': f"{(completed / total * 100):.1f}%"
            }
        
        return theme_stats
    
    def get_format_breakdown(self) -> Dict:
        """Get breakdown by suggested format"""
        format_stats = {}
        
        # Group stories by format
        format_counter = Counter(s['suggested_format'] for s in self.stories)
        
        for format_type, total in format_counter.items():
            completed = sum(1 for s in self.stories 
                          if s['suggested_format'] == format_type and s.get('status') == 'completed')
            format_stats[format_type] = {
                'total': total,
                'completed': completed,
                'pending': total - completed,
                'completion_rate': f"{(completed / total * 100):.1f}%"
            }
        
        return format_stats
    
    def get_high_engagement_pending(self, limit: int = 10) -> List[Dict]:
        """Get highest engagement stories that haven't been converted yet"""
        pending_stories = [s for s in self.stories if s.get('status') == 'pending']
        # Sort by upvotes descending
        sorted_stories = sorted(pending_stories, key=lambda x: x['upvotes'], reverse=True)
        
        return sorted_stories[:limit]
    
    def get_recently_completed(self, limit: int = 10) -> List[Dict]:
        """Get recently completed scripts"""
        completed_stories = [s for s in self.stories if s.get('status') == 'completed']
        # Sort by generated_date descending (most recent first)
        sorted_stories = sorted(
            completed_stories, 
            key=lambda x: x.get('generated_date', ''), 
            reverse=True
        )
        
        return sorted_stories[:limit]
    
    def print_dashboard(self):
        """Print a formatted dashboard view"""
        print("=" * 80)
        print("NOVO VIDEO SCRIPT TRACKING DASHBOARD")
        print("=" * 80)
        
        # Overview stats
        stats = self.get_overview_stats()
        print("\n📊 OVERVIEW")
        print(f"Total Stories: {stats['total_stories']}")
        print(f"✅ Completed: {stats['completed']} ({stats['completion_rate']})")
        print(f"⏳ In Progress: {stats['in_progress']}")
        print(f"📝 Pending: {stats['pending']}")
        
        # Theme breakdown
        print("\n🎯 BY THEME")
        theme_stats = self.get_theme_breakdown()
        for theme, data in sorted(theme_stats.items(), key=lambda x: x[1]['total'], reverse=True):
            print(f"{theme.replace('_', ' ').title():30} | "
                  f"Total: {data['total']:3} | "
                  f"Done: {data['completed']:3} | "
                  f"Rate: {data['completion_rate']:>6}")
        
        # Format breakdown
        print("\n🎬 BY FORMAT")
        format_stats = self.get_format_breakdown()
        for format_type, data in sorted(format_stats.items(), key=lambda x: x[1]['total'], reverse=True):
            print(f"{format_type.replace('_', ' ').title():30} | "
                  f"Total: {data['total']:3} | "
                  f"Done: {data['completed']:3} | "
                  f"Rate: {data['completion_rate']:>6}")
        
        # High engagement pending
        print("\n🔥 TOP PENDING STORIES (BY ENGAGEMENT)")
        pending = self.get_high_engagement_pending(5)
        for story in pending:
            print(f"ID {story['id']:3} | {story['upvotes']:,} upvotes | {story['title'][:50]}...")
        
        # Recently completed
        print("\n✨ RECENTLY COMPLETED")
        recent = self.get_recently_completed(5)
        for story in recent:
            date = story.get('generated_date', 'Unknown')
            print(f"ID {story['id']:3} | {date} | {story['title'][:50]}...")
        
        # Last update
        if 'tracking' in self.metadata:
            last_update = self.metadata['tracking'].get('last_updated', 'Unknown')
            if last_update != 'Unknown':
                # Parse ISO format and make it readable
                try:
                    dt = datetime.fromisoformat(last_update.replace('Z', '+00:00'))
                    last_update = dt.strftime('%Y-%m-%d %H:%M')
                except:
                    pass
            print(f"\n📅 Last Updated: {last_update}")
        
        print("\n" + "=" * 80)
    
    def export_pending_list(self, filename: str = "pending_stories.txt"):
        """Export list of pending stories to a text file"""
        pending_stories = [s for s in self.stories if s.get('status') == 'pending']
        sorted_stories = sorted(pending_stories, key=lambda x: x['upvotes'], reverse=True)
        
        with open(filename, 'w') as f:
            f.write("PENDING STORIES FOR SCRIPT GENERATION\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
            f.write("=" * 80 + "\n\n")
            
            for story in sorted_stories:
                f.write(f"ID: {story['id']}\n")
                f.write(f"Title: {story['title']}\n")
                f.write(f"Engagement: {story['upvotes']:,} upvotes, {story['comments']:,} comments\n")
                f.write(f"Theme: {story['theme']}\n")
                f.write(f"Format: {story['suggested_format']}\n")
                f.write(f"Key Lesson: {story['key_lesson']}\n")
                f.write("-" * 40 + "\n\n")
        
        return f"Exported {len(sorted_stories)} pending stories to {filename}"
    
    def get_next_story_suggestions(self, count: int = 5) -> List[Dict]:
        """
        Suggest next stories to convert using intelligent scoring algorithm.
        
        Balances high engagement with theme diversity to optimize content strategy.
        Scoring combines engagement metrics with theme underrepresentation to
        ensure balanced content portfolio.
        
        Args:
            count (int): Number of suggestions to return (default: 5)
            
        Returns:
            List[Dict]: Ranked story suggestions with scoring breakdown
            
        Algorithm:
            - Engagement Score: story_upvotes / 1000 (normalized)
            - Diversity Score: 10 / (completed_theme_count + 1)
            - Total Score: engagement_score + diversity_score
            
        Example:
            >>> suggestions = dashboard.get_next_story_suggestions(3)
            >>> for item in suggestions:
            ...     story = item['story']
            ...     print(f"{story['title']} (Score: {item['score']:.2f})")
        """
        pending_stories = [s for s in self.stories if s.get('status') == 'pending']
        
        # Get current theme distribution of completed stories
        completed_themes = Counter(s['theme'] for s in self.stories 
                                 if s.get('status') == 'completed')
        
        # Score each pending story
        scored_stories = []
        for story in pending_stories:
            # Higher score for high engagement
            engagement_score = story['upvotes'] / 1000  # Normalize
            
            # Higher score for underrepresented themes
            theme_count = completed_themes.get(story['theme'], 0)
            diversity_score = 10 / (theme_count + 1)  # Inverse relationship
            
            # Combined score
            total_score = engagement_score + diversity_score
            
            scored_stories.append({
                'story': story,
                'score': total_score,
                'engagement_score': engagement_score,
                'diversity_score': diversity_score
            })
        
        # Sort by score
        scored_stories.sort(key=lambda x: x['score'], reverse=True)
        
        return scored_stories[:count]


# Example usage
if __name__ == "__main__":
    dashboard = TrackingDashboard('story_database.json')
    
    # Print main dashboard
    dashboard.print_dashboard()
    
    # Get suggestions for next stories
    print("\n📋 SUGGESTED NEXT STORIES")
    suggestions = dashboard.get_next_story_suggestions(5)
    for i, item in enumerate(suggestions, 1):
        story = item['story']
        print(f"\n{i}. {story['title']}")
        print(f"   ID: {story['id']} | Theme: {story['theme']} | Format: {story['suggested_format']}")
        print(f"   Score: {item['score']:.2f} (Engagement: {item['engagement_score']:.2f}, "
              f"Diversity: {item['diversity_score']:.2f})")
    
    # Export pending list
    # print(dashboard.export_pending_list())