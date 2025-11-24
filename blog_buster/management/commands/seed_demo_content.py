from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils import timezone

from blog_buster.models import Category, Tag, Post


class Command(BaseCommand):
    help = "Seed the database with Lifewire-inspired demo posts, categories, and tags."

    def handle(self, *args, **options):
        user = self._get_or_create_user()
        categories = self._create_categories()
        tags = self._create_tags()
        posts_created = self._create_posts(user, categories, tags)

        self.stdout.write(
            self.style.SUCCESS(
                f"Seeded {len(categories)} categories, {len(tags)} tags, and {posts_created} posts."
            )
        )

    def _get_or_create_user(self):
        User = get_user_model()
        user, created = User.objects.get_or_create(
            username="editor",
            defaults={
                "first_name": "Tech",
                "last_name": "Editor",
                "email": "editor@example.com",
                "is_staff": True,
                "is_superuser": True,
            },
        )
        if created:
            user.set_password("password123")
            user.save()
            self.stdout.write(
                self.style.WARNING(
                    "Created default admin user 'editor' with password 'password123'. "
                    "Please change this password after login."
                )
            )
        return user

    def _create_categories(self):
        category_data = [
            (
                "Tech Essentials",
                "Core how-tos that help you get more from the devices you rely on every day.",
            ),
            (
                "Buying Guides",
                "Curated shopping advice inspired by Lifewire's detailed recommendation lists.",
            ),
            (
                "Troubleshooting",
                "Step-by-step fixes for the most common device and software problems.",
            ),
        ]
        categories = []
        for name, description in category_data:
            category, _ = Category.objects.get_or_create(
                name=name, defaults={"description": description}
            )
            categories.append(category)
        return {category.name: category for category in categories}

    def _create_tags(self):
        tag_names = [
            "Windows",
            "Android",
            "iOS",
            "Smart Home",
            "Streaming",
            "Productivity",
            "Security",
        ]
        tags = []
        for name in tag_names:
            tag, _ = Tag.objects.get_or_create(name=name)
            tags.append(tag)
        return {tag.name: tag for tag in tags}

    def _create_posts(self, user, categories, tags):
        post_data = [
            {
                "title": "How to Reset Your Wi-Fi Router (and When You Should)",
                "category": "Troubleshooting",
                "excerpt": (
                    "Routers need reboots just like computers do. "
                    "Here's the Lifewire way to reset your router safely without wiping important settings."
                ),
                "content": """If your Wi-Fi network suddenly slows down or devices refuse to connect, 
restarting the router should be your first troubleshooting step. Lifewire recommends following a
90-second power-cycle rule: unplug the router, wait a full minute, then plug it back in and allow 
another 30 seconds for the connection to stabilize. Still stuck? Log in to the router's admin page, 
check for firmware updates, and confirm that DHCP is enabled. Finish by running an internet speed test 
to make sure your ISP is delivering the bandwidth you pay for.""",
                "tags": ["Smart Home", "Windows", "Android"],
                "featured": True,
            },
            {
                "title": "The Best Noise-Cancelling Headphones of 2025",
                "category": "Buying Guides",
                "excerpt": (
                    "We tested more than a dozen flagship ANC headphones. "
                    "These four models deliver the Lifewire-approved mix of sound, comfort, and smart features."
                ),
                "content": """Premium noise-cancelling headphones are becoming part of the everyday commute.
To mimic Lifewire's review style, we analyzed comfort, sound profile, noise reduction, and companion apps.
The Sony WH-1000XM5 still leads overall thanks to its warm sound signature and adaptive ANC.
Apple's AirPods Max pair perfectly with iOS, while Bose QuietComfort Ultra Headphones are the best for travel 
thanks to airline adaptor support. Gamers should look at the SteelSeries Arctis Nova Pro Wireless for 
simultaneous 2.4GHz and Bluetooth pairing.""",
                "tags": ["Productivity", "Smart Home"],
                "featured": True,
            },
            {
                "title": "5 iPhone Privacy Settings Lifewire Editors Always Enable",
                "category": "Tech Essentials",
                "excerpt": (
                    "Strengthen your iPhone privacy in five minutes. "
                    "These built-in settings make sure apps only see what you approve."
                ),
                "content": """Start by visiting Settings > Privacy & Security. 
Flip on App Privacy Report to see how often apps access sensitive data. 
Next, disable precise location for social apps and ensure Photos access is set to 'Selected Photos.'
Lifewire also recommends enabling Lockdown Mode if you store sensitive work files, 
and using Apple's Hide My Email when signing up for newsletters. 
Finally, go to Safari settings to block cross-site tracking for a cleaner browsing footprint.""",
                "tags": ["iOS", "Security"],
                "featured": False,
            },
            {
                "title": "Stream TV Like a Pro: Lifewire's 4 Essential Tips",
                "category": "Tech Essentials",
                "excerpt": (
                    "Buffering and subscription chaos are fixable. "
                    "Here's how Lifewire streaming editors keep watchlists organized across apps."
                ),
                "content": """Consolidate your streaming history with Google TV's watchlist or 
Apple TV's Up Next queue so you don't forget where you left off. 
Use your router's Quality of Service (QoS) feature to prioritize the streaming box on movie nights.
When bandwidth dips, forcing the app to stream at 1080p instead of 4K can prevent buffering.
Finally, audit subscriptions every quarter—nearly 40% of people pay for a service they rarely open.""",
                "tags": ["Streaming", "Smart Home"],
                "featured": False,
            },
        ]

        created_count = 0
        for data in post_data:
            category = categories[data["category"]]
            post, created = Post.objects.get_or_create(
                title=data["title"],
                defaults={
                    "author": user,
                    "category": category,
                    "excerpt": data["excerpt"],
                    "content": data["content"],
                    "status": "published",
                    "featured": data["featured"],
                    "published_at": timezone.now(),
                },
            )
            if created:
                tag_objects = [tags[name] for name in data["tags"] if name in tags]
                post.tags.set(tag_objects)
                created_count += 1
        return created_count

