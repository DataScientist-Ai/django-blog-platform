from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('tag_detail', kwargs={'slug': self.slug})


class Post(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    
    featured_image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    excerpt = models.TextField(max_length=300, help_text="Short description for preview")
    content = models.TextField()
    
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    featured = models.BooleanField(default=False, help_text="Feature this post on homepage")
    
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-published_at', '-created_at']
        indexes = [
            models.Index(fields=['-published_at', 'status']),
            models.Index(fields=['slug']),
        ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if self.status == 'published' and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    @property
    def reading_time(self):
        """Calculate estimated reading time in minutes"""
        words_per_minute = 200
        word_count = len(self.content.split())
        return max(1, round(word_count / words_per_minute))


class SingletonModel(models.Model):
    """Base class to enforce single-row settings models."""

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class HomepageSettings(SingletonModel):
    hero_overline = models.CharField(max_length=120, default="Lifewire-inspired")
    hero_heading = models.CharField(max_length=200, default="Smart guides for the tech you actually use.")
    hero_subheading = models.CharField(
        max_length=280,
        default="Reviews, explainers, and troubleshooting tips crafted with the same editorial polish you love on Lifewire.",
    )
    hero_primary_cta_label = models.CharField(max_length=50, default="Browse articles")
    hero_secondary_cta_label = models.CharField(max_length=50, default="Latest drops")

    newsletter_overline = models.CharField(max_length=120, default="Inbox utility")
    newsletter_heading = models.CharField(max_length=180, default="Weekly digest with zero fluff.")
    newsletter_body = models.CharField(
        max_length=280,
        default="Get Lifewire-inspired explainers and buying advice each Monday. We only send the good stuff.",
    )
    newsletter_cta_label = models.CharField(max_length=80, default="Subscribe")
    newsletter_disclaimer = models.CharField(max_length=160, default="No spam. Unsubscribe anytime.")

    class Meta:
        verbose_name = "Homepage Settings"

    def __str__(self):
        return "Homepage Settings"


class QuickTip(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=280)
    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['sort_order', '-created_at']

    def __str__(self):
        return self.title


class BuyingGuide(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    summary = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='buying_guides')
    hero_quote = models.CharField(max_length=200, blank=True)
    published = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('buying_guide_detail', kwargs={'slug': self.slug})


class GuidePick(models.Model):
    buying_guide = models.ForeignKey(BuyingGuide, on_delete=models.CASCADE, related_name='picks')
    title = models.CharField(max_length=150)
    verdict = models.CharField(max_length=80, help_text="e.g. Best Overall, Best Budget")
    tagline = models.CharField(max_length=200, blank=True)
    pros = models.TextField(help_text="One item per line")
    cons = models.TextField(help_text="One item per line")
    price_range = models.CharField(max_length=80, blank=True)
    affiliate_url = models.URLField(blank=True)
    rating = models.PositiveIntegerField(default=4, help_text="1-5 scale")
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['sort_order', 'id']

    def __str__(self):
        return f"{self.title} ({self.verdict})"


class ProductReview(models.Model):
    product_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    summary = models.TextField()
    verdict = models.CharField(max_length=200)
    affiliate_url = models.URLField(blank=True)
    hero_image = models.ImageField(upload_to='review_images/', blank=True, null=True)
    overall_score = models.DecimalField(max_digits=3, decimal_places=1, default=4.0)
    pros = models.TextField(help_text="One per line")
    cons = models.TextField(help_text="One per line")
    why_trust_us = models.TextField(blank=True)
    methodology = models.TextField(blank=True)
    published = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_at', '-created_at']

    def __str__(self):
        return self.product_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product_name)
        if self.published and self.published_at is None:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product_review_detail', kwargs={'slug': self.slug})


class ReviewScore(models.Model):
    review = models.ForeignKey(ProductReview, on_delete=models.CASCADE, related_name='scores')
    label = models.CharField(max_length=80)
    score = models.DecimalField(max_digits=3, decimal_places=1, help_text="0-10 scale")

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.label}: {self.score}"


class HowToSeries(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    intro = models.TextField()
    difficulty = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='beginner')
    estimated_time = models.CharField(max_length=80, blank=True)
    prerequisites = models.TextField(blank=True, help_text="One item per line")
    published = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('howto_detail', kwargs={'slug': self.slug})


class HowToStep(models.Model):
    series = models.ForeignKey(HowToSeries, on_delete=models.CASCADE, related_name='steps')
    step_number = models.PositiveIntegerField()
    title = models.CharField(max_length=150)
    instructions = models.TextField()
    tip = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['step_number']

    def __str__(self):
        return f"Step {self.step_number}: {self.title}"


class SidebarWidget(models.Model):
    """Base widget model for sidebar management"""
    WIDGET_TYPES = [
        ('popular_posts', 'Popular Posts'),
        ('related_posts', 'Related Posts'),
        ('author_bio', 'Author Bio'),
        ('social_share', 'Social Share'),
        ('newsletter', 'Newsletter Signup'),
        ('categories', 'Categories'),
        ('recent_posts', 'Recent Posts'),
        ('quick_tips', 'Quick Tips'),
        ('buying_guides', 'Buying Guides'),
    ]

    widget_type = models.CharField(max_length=20, choices=WIDGET_TYPES, unique=True)
    title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['sort_order', 'created_at']

    def __str__(self):
        return f"{self.get_widget_type_display()} - {self.title}"


class PopularPostsWidget(models.Model):
    widget = models.OneToOneField(SidebarWidget, on_delete=models.CASCADE, related_name='popular_posts_config')
    post_count = models.PositiveIntegerField(default=5, help_text="Number of posts to display")
    time_period_days = models.PositiveIntegerField(default=30, help_text="Show posts from last N days")

    def __str__(self):
        return f"Popular posts config ({self.post_count} posts)"


class RelatedPostsWidget(models.Model):
    widget = models.OneToOneField(SidebarWidget, on_delete=models.CASCADE, related_name='related_posts_config')
    post_count = models.PositiveIntegerField(default=5)
    show_by_category = models.BooleanField(default=True)
    show_by_tags = models.BooleanField(default=True)

    def __str__(self):
        return f"Related posts config ({self.post_count} posts)"


class AuthorBioWidget(models.Model):
    widget = models.OneToOneField(SidebarWidget, on_delete=models.CASCADE, related_name='author_bio_config')
    bio_text = models.TextField(help_text="Author biography text")
    show_social_links = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='author_avatars/', blank=True, null=True)

    def __str__(self):
        return "Author bio config"


class SocialShareWidget(models.Model):
    widget = models.OneToOneField(SidebarWidget, on_delete=models.CASCADE, related_name='social_share_config')
    show_facebook = models.BooleanField(default=True)
    show_twitter = models.BooleanField(default=True)
    show_linkedin = models.BooleanField(default=True)
    show_pinterest = models.BooleanField(default=True)
    show_email = models.BooleanField(default=True)

    def __str__(self):
        return "Social share config"


class NewsletterWidget(models.Model):
    widget = models.OneToOneField(SidebarWidget, on_delete=models.CASCADE, related_name='newsletter_config')
    description = models.TextField(default="Get the latest tech news and tutorials delivered to your inbox.")
    button_text = models.CharField(max_length=50, default="Subscribe Now")
    privacy_text = models.CharField(max_length=200, default="We respect your privacy.")

    def __str__(self):
        return "Newsletter config"


class CategoriesWidget(models.Model):
    widget = models.OneToOneField(SidebarWidget, on_delete=models.CASCADE, related_name='categories_config')
    show_post_count = models.BooleanField(default=True)
    max_categories = models.PositiveIntegerField(default=10)

    def __str__(self):
        return f"Categories config (max {self.max_categories})"


class RecentPostsWidget(models.Model):
    widget = models.OneToOneField(SidebarWidget, on_delete=models.CASCADE, related_name='recent_posts_config')
    post_count = models.PositiveIntegerField(default=5)

    def __str__(self):
        return f"Recent posts config ({self.post_count} posts)"


class QuickTipsWidget(models.Model):
    widget = models.OneToOneField(SidebarWidget, on_delete=models.CASCADE, related_name='quick_tips_config')
    tip_count = models.PositiveIntegerField(default=3)

    def __str__(self):
        return f"Quick tips config ({self.tip_count} tips)"


class BuyingGuidesWidget(models.Model):
    widget = models.OneToOneField(SidebarWidget, on_delete=models.CASCADE, related_name='buying_guides_config')
    guide_count = models.PositiveIntegerField(default=3)

    def __str__(self):
        return f"Buying guides config ({self.guide_count} guides)"
