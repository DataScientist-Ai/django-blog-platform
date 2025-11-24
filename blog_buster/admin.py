from django.contrib import admin
from .models import (
    Post,
    Category,
    Tag,
    HomepageSettings,
    QuickTip,
    BuyingGuide,
    GuidePick,
    ProductReview,
    ReviewScore,
    HowToSeries,
    HowToStep,
    SidebarWidget,
    PopularPostsWidget,
    RelatedPostsWidget,
    AuthorBioWidget,
    SocialShareWidget,
    NewsletterWidget,
    CategoriesWidget,
    RecentPostsWidget,
    QuickTipsWidget,
    BuyingGuidesWidget,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'status', 'featured', 'published_at', 'views', 'created_at']
    list_filter = ['status', 'featured', 'category', 'tags', 'created_at', 'published_at']
    search_fields = ['title', 'content', 'excerpt']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ['tags']
    date_hierarchy = 'published_at'
    readonly_fields = ['views', 'created_at', 'updated_at']
    
    fieldsets = (
        ('Content', {
            'fields': ('title', 'slug', 'author', 'excerpt', 'content', 'featured_image')
        }),
        ('Categorization', {
            'fields': ('category', 'tags')
        }),
        ('Publishing', {
            'fields': ('status', 'featured', 'published_at')
        }),
        ('Statistics', {
            'fields': ('views', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(HomepageSettings)
class HomepageSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Hero', {
            'fields': (
                'hero_overline',
                'hero_heading',
                'hero_subheading',
                'hero_primary_cta_label',
                'hero_secondary_cta_label',
            )
        }),
        ('Newsletter', {
            'fields': (
                'newsletter_overline',
                'newsletter_heading',
                'newsletter_body',
                'newsletter_cta_label',
                'newsletter_disclaimer',
            )
        }),
    )

    def has_add_permission(self, request):
        return not HomepageSettings.objects.exists()


@admin.register(QuickTip)
class QuickTipAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'sort_order', 'created_at']
    list_editable = ['is_active', 'sort_order']
    list_filter = ['is_active']
    search_fields = ['title', 'description']
    ordering = ['sort_order', '-created_at']


class GuidePickInline(admin.TabularInline):
    model = GuidePick
    extra = 1
    fields = ('title', 'verdict', 'rating', 'price_range', 'sort_order')


@admin.register(BuyingGuide)
class BuyingGuideAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'published', 'featured', 'updated_at']
    list_filter = ['published', 'featured', 'category']
    search_fields = ['title', 'summary']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [GuidePickInline]
    fieldsets = (
        (None, {'fields': ('title', 'slug', 'category', 'summary', 'hero_quote')}),
        ('Publishing', {'fields': ('published', 'featured')}),
    )


class ReviewScoreInline(admin.TabularInline):
    model = ReviewScore
    extra = 1
    fields = ('label', 'score')


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'overall_score', 'published', 'featured', 'published_at']
    list_filter = ['published', 'featured', 'created_at']
    search_fields = ['product_name', 'summary', 'verdict']
    prepopulated_fields = {'slug': ('product_name',)}
    inlines = [ReviewScoreInline]
    fieldsets = (
        ('Overview', {'fields': ('product_name', 'slug', 'summary', 'verdict', 'hero_image', 'affiliate_url')}),
        ('Editorial', {'fields': ('pros', 'cons', 'why_trust_us', 'methodology')}),
        ('Scoring', {'fields': ('overall_score',)}),
        ('Publishing', {'fields': ('published', 'featured', 'published_at')}),
    )


class HowToStepInline(admin.TabularInline):
    model = HowToStep
    extra = 1
    fields = ('step_number', 'title', 'instructions', 'tip')


@admin.register(HowToSeries)
class HowToSeriesAdmin(admin.ModelAdmin):
    list_display = ['title', 'difficulty', 'published', 'featured', 'created_at']
    list_filter = ['difficulty', 'published', 'featured']
    search_fields = ['title', 'intro']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [HowToStepInline]
    fieldsets = (
        (None, {'fields': ('title', 'slug', 'intro')}),
        ('Details', {'fields': ('difficulty', 'estimated_time', 'prerequisites')}),
        ('Publishing', {'fields': ('published', 'featured')}),
    )


# Sidebar Widgets Admin
class PopularPostsWidgetInline(admin.StackedInline):
    model = PopularPostsWidget
    can_delete = False
    verbose_name_plural = 'Popular Posts Configuration'


class RelatedPostsWidgetInline(admin.StackedInline):
    model = RelatedPostsWidget
    can_delete = False
    verbose_name_plural = 'Related Posts Configuration'


class AuthorBioWidgetInline(admin.StackedInline):
    model = AuthorBioWidget
    can_delete = False
    verbose_name_plural = 'Author Bio Configuration'


class SocialShareWidgetInline(admin.StackedInline):
    model = SocialShareWidget
    can_delete = False
    verbose_name_plural = 'Social Share Configuration'


class NewsletterWidgetInline(admin.StackedInline):
    model = NewsletterWidget
    can_delete = False
    verbose_name_plural = 'Newsletter Configuration'


class CategoriesWidgetInline(admin.StackedInline):
    model = CategoriesWidget
    can_delete = False
    verbose_name_plural = 'Categories Configuration'


class RecentPostsWidgetInline(admin.StackedInline):
    model = RecentPostsWidget
    can_delete = False
    verbose_name_plural = 'Recent Posts Configuration'


class QuickTipsWidgetInline(admin.StackedInline):
    model = QuickTipsWidget
    can_delete = False
    verbose_name_plural = 'Quick Tips Configuration'


class BuyingGuidesWidgetInline(admin.StackedInline):
    model = BuyingGuidesWidget
    can_delete = False
    verbose_name_plural = 'Buying Guides Configuration'


@admin.register(SidebarWidget)
class SidebarWidgetAdmin(admin.ModelAdmin):
    list_display = ['get_widget_type_display', 'title', 'is_active', 'sort_order', 'updated_at']
    list_editable = ['is_active', 'sort_order']
    list_filter = ['widget_type', 'is_active']
    search_fields = ['title']
    ordering = ['sort_order', 'widget_type']

    def get_inlines(self, request, obj):
        if obj:
            if obj.widget_type == 'popular_posts':
                return [PopularPostsWidgetInline]
            elif obj.widget_type == 'related_posts':
                return [RelatedPostsWidgetInline]
            elif obj.widget_type == 'author_bio':
                return [AuthorBioWidgetInline]
            elif obj.widget_type == 'social_share':
                return [SocialShareWidgetInline]
            elif obj.widget_type == 'newsletter':
                return [NewsletterWidgetInline]
            elif obj.widget_type == 'categories':
                return [CategoriesWidgetInline]
            elif obj.widget_type == 'recent_posts':
                return [RecentPostsWidgetInline]
            elif obj.widget_type == 'quick_tips':
                return [QuickTipsWidgetInline]
            elif obj.widget_type == 'buying_guides':
                return [BuyingGuidesWidgetInline]
        return []
