from django.core.management.base import BaseCommand
from blog_buster.models import (
    SidebarWidget, PopularPostsWidget, RelatedPostsWidget,
    AuthorBioWidget, SocialShareWidget, NewsletterWidget,
    CategoriesWidget, RecentPostsWidget, QuickTipsWidget,
    BuyingGuidesWidget
)


class Command(BaseCommand):
    help = "Seed the database with default sidebar widgets"

    def handle(self, *args, **options):
        # Popular Posts Widget
        if not SidebarWidget.objects.filter(widget_type='popular_posts').exists():
            widget = SidebarWidget.objects.create(
                widget_type='popular_posts',
                title='Popular Posts',
                is_active=True,
                sort_order=1
            )
            PopularPostsWidget.objects.create(
                widget=widget,
                post_count=5,
                time_period_days=30
            )
            self.stdout.write('✓ Created Popular Posts widget')

        # Related Posts Widget
        if not SidebarWidget.objects.filter(widget_type='related_posts').exists():
            widget = SidebarWidget.objects.create(
                widget_type='related_posts',
                title='Related Posts',
                is_active=True,
                sort_order=2
            )
            RelatedPostsWidget.objects.create(
                widget=widget,
                post_count=4,
                show_by_category=True,
                show_by_tags=True
            )
            self.stdout.write('✓ Created Related Posts widget')

        # Author Bio Widget
        if not SidebarWidget.objects.filter(widget_type='author_bio').exists():
            widget = SidebarWidget.objects.create(
                widget_type='author_bio',
                title='About the Author',
                is_active=True,
                sort_order=3
            )
            AuthorBioWidget.objects.create(
                widget=widget,
                bio_text='Tech writer with 10+ years experience covering gadgets, software, and emerging technologies. Passionate about helping readers make informed tech decisions.',
                show_social_links=True
            )
            self.stdout.write('✓ Created Author Bio widget')

        # Social Share Widget
        if not SidebarWidget.objects.filter(widget_type='social_share').exists():
            widget = SidebarWidget.objects.create(
                widget_type='social_share',
                title='Share This Post',
                is_active=True,
                sort_order=4
            )
            SocialShareWidget.objects.create(
                widget=widget,
                show_facebook=True,
                show_twitter=True,
                show_linkedin=True,
                show_pinterest=True,
                show_email=True
            )
            self.stdout.write('✓ Created Social Share widget')

        # Newsletter Widget
        if not SidebarWidget.objects.filter(widget_type='newsletter').exists():
            widget = SidebarWidget.objects.create(
                widget_type='newsletter',
                title='Stay Updated',
                is_active=True,
                sort_order=5
            )
            NewsletterWidget.objects.create(
                widget=widget,
                description='Get the latest tech news, reviews, and tutorials delivered to your inbox weekly.',
                button_text='Subscribe Now',
                privacy_text='We respect your privacy. Unsubscribe anytime.'
            )
            self.stdout.write('✓ Created Newsletter widget')

        # Categories Widget
        if not SidebarWidget.objects.filter(widget_type='categories').exists():
            widget = SidebarWidget.objects.create(
                widget_type='categories',
                title='Categories',
                is_active=True,
                sort_order=6
            )
            CategoriesWidget.objects.create(
                widget=widget,
                show_post_count=True,
                max_categories=8
            )
            self.stdout.write('✓ Created Categories widget')

        # Recent Posts Widget
        if not SidebarWidget.objects.filter(widget_type='recent_posts').exists():
            widget = SidebarWidget.objects.create(
                widget_type='recent_posts',
                title='Recent Posts',
                is_active=True,
                sort_order=7
            )
            RecentPostsWidget.objects.create(
                widget=widget,
                post_count=5
            )
            self.stdout.write('✓ Created Recent Posts widget')

        # Quick Tips Widget
        if not SidebarWidget.objects.filter(widget_type='quick_tips').exists():
            widget = SidebarWidget.objects.create(
                widget_type='quick_tips',
                title='Quick Tips',
                is_active=True,
                sort_order=8
            )
            QuickTipsWidget.objects.create(
                widget=widget,
                tip_count=3
            )
            self.stdout.write('✓ Created Quick Tips widget')

        # Buying Guides Widget
        if not SidebarWidget.objects.filter(widget_type='buying_guides').exists():
            widget = SidebarWidget.objects.create(
                widget_type='buying_guides',
                title='Buying Guides',
                is_active=True,
                sort_order=9
            )
            BuyingGuidesWidget.objects.create(
                widget=widget,
                guide_count=3
            )
            self.stdout.write('✓ Created Buying Guides widget')

        self.stdout.write(self.style.SUCCESS('Successfully seeded all sidebar widgets!'))
