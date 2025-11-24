from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q, Prefetch, Count
from datetime import timedelta
from django.utils import timezone
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


def get_widget_context():
    """Get context for all widgets (homepage and sidebar)"""
    # Homepage widgets
    featured_guides = (
        BuyingGuide.objects.filter(published=True, featured=True)
        .prefetch_related(Prefetch('picks', queryset=GuidePick.objects.order_by('sort_order')))
        [:3]
    )
    if featured_guides.count() < 3:
        filler = (
            BuyingGuide.objects.filter(published=True)
            .exclude(id__in=featured_guides.values_list('id', flat=True))
            .prefetch_related('picks')[:3 - featured_guides.count()]
        )
        featured_guides = list(featured_guides) + list(filler)

    featured_reviews = (
        ProductReview.objects.filter(published=True, featured=True)
        .prefetch_related('scores')
        [:3]
    )
    if len(featured_reviews) < 3:
        filler = (
            ProductReview.objects.filter(published=True)
            .exclude(id__in=[r.id for r in featured_reviews])
            .prefetch_related('scores')[:3 - len(featured_reviews)]
        )
        featured_reviews = list(featured_reviews) + list(filler)

    featured_howtos = (
        HowToSeries.objects.filter(published=True, featured=True)
        .prefetch_related('steps')[:3]
    )
    if len(featured_howtos) < 3:
        filler = (
            HowToSeries.objects.filter(published=True)
            .exclude(id__in=[h.id for h in featured_howtos])
            .prefetch_related('steps')[:3 - len(featured_howtos)]
        )
        featured_howtos = list(featured_howtos) + list(filler)

    # Sidebar widgets
    sidebar_widgets = []
    active_widgets = SidebarWidget.objects.filter(is_active=True).order_by('sort_order')

    for widget in active_widgets:
        widget_data = {'widget': widget}

        if widget.widget_type == 'popular_posts':
            config = getattr(widget, 'popular_posts_config', None)
            if config:
                cutoff_date = timezone.now() - timedelta(days=config.time_period_days)
                widget_data['posts'] = (
                    Post.objects.filter(status='published', published_at__gte=cutoff_date)
                    .order_by('-views')[:config.post_count]
                )

        elif widget.widget_type == 'related_posts':
            # This will be handled in post_detail view with current post context
            pass

        elif widget.widget_type == 'author_bio':
            widget_data['author_bio'] = getattr(widget, 'author_bio_config', None)

        elif widget.widget_type == 'social_share':
            widget_data['social_config'] = getattr(widget, 'social_share_config', None)

        elif widget.widget_type == 'newsletter':
            widget_data['newsletter_config'] = getattr(widget, 'newsletter_config', None)

        elif widget.widget_type == 'categories':
            config = getattr(widget, 'categories_config', None)
            if config:
                categories = Category.objects.annotate(post_count=Count('posts')).order_by('-post_count')[:config.max_categories]
                widget_data['categories'] = categories
                widget_data['show_post_count'] = config.show_post_count

        elif widget.widget_type == 'recent_posts':
            config = getattr(widget, 'recent_posts_config', None)
            if config:
                widget_data['posts'] = Post.objects.filter(status='published').order_by('-published_at')[:config.post_count]

        elif widget.widget_type == 'quick_tips':
            config = getattr(widget, 'quick_tips_config', None)
            if config:
                widget_data['tips'] = QuickTip.objects.filter(is_active=True).order_by('sort_order')[:config.tip_count]

        elif widget.widget_type == 'buying_guides':
            config = getattr(widget, 'buying_guides_config', None)
            if config:
                widget_data['guides'] = (
                    BuyingGuide.objects.filter(published=True)
                    .order_by('-created_at')[:config.guide_count]
                )

        sidebar_widgets.append(widget_data)

    return {
        'featured_guides': featured_guides,
        'featured_reviews': featured_reviews,
        'featured_howtos': featured_howtos,
        'sidebar_widgets': sidebar_widgets,
    }


def index(request):
    """Homepage with featured, trending, and recent posts"""
    featured_posts = Post.objects.filter(status='published', featured=True)[:1]
    recent_posts = (
        Post.objects.filter(status='published')
        .exclude(id__in=featured_posts.values_list('id', flat=True))
        .order_by('-published_at')[:6]
    )
    trending_posts = (
        Post.objects.filter(status='published')
        .exclude(id__in=featured_posts.values_list('id', flat=True))
        .order_by('-views')[:4]
    )
    category_spotlight = Category.objects.filter(posts__status='published').distinct()[:4]
    settings = HomepageSettings.load()
    quick_tips = QuickTip.objects.filter(is_active=True).order_by('sort_order', '-created_at')[:6]

    context = {
        'featured_posts': featured_posts,
        'recent_posts': recent_posts,
        'trending_posts': trending_posts,
        'category_spotlight': category_spotlight,
        'quick_tips': quick_tips,
        'homepage_settings': settings,
    }
    context.update(get_widget_context())
    return render(request, 'blog_buster/index.html', context)


def post_list(request):
    """List all published posts"""
    posts = Post.objects.filter(status='published')
    
    # Search functionality
    search_query = request.GET.get('q')
    if search_query:
        posts = posts.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query) |
            Q(excerpt__icontains=search_query)
        )
    
    # Category filter
    category_slug = request.GET.get('category')
    if category_slug:
        posts = posts.filter(category__slug=category_slug)
    
    # Tag filter
    tag_slug = request.GET.get('tag')
    if tag_slug:
        posts = posts.filter(tags__slug=tag_slug)
    
    # Pagination
    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'posts': page_obj,
        'search_query': search_query,
        'selected_category': category_slug,
        'selected_tag': tag_slug,
        'tags': Tag.objects.all()[:12],
    }
    context.update(get_widget_context())
    return render(request, 'blog_buster/post_list.html', context)


def post_detail(request, slug):
    """Display a single post"""
    post = get_object_or_404(Post, slug=slug, status='published')

    # Increment view count
    post.views += 1
    post.save(update_fields=['views'])

    # Get related posts
    related_posts = Post.objects.filter(
        status='published',
        category=post.category
    ).exclude(id=post.id)[:3]

    # Get widget context and customize for this post
    context = get_widget_context()

    # Update related posts widget with post-specific data
    for widget_data in context['sidebar_widgets']:
        if widget_data['widget'].widget_type == 'related_posts':
            config = getattr(widget_data['widget'], 'related_posts_config', None)
            if config:
                related_posts_queryset = Post.objects.filter(status='published').exclude(id=post.id)

                if config.show_by_category and post.category:
                    related_posts_queryset = related_posts_queryset.filter(category=post.category)

                if config.show_by_tags and post.tags.exists():
                    related_posts_queryset = related_posts_queryset.filter(tags__in=post.tags.all())

                widget_data['posts'] = related_posts_queryset.distinct()[:config.post_count]

    context.update({
        'post': post,
        'related_posts': related_posts,
    })

    return render(request, 'blog_buster/post_detail.html', context)


def category_detail(request, slug):
    """Display posts in a category"""
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(status='published', category=category)
    
    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'category': category,
        'page_obj': page_obj,
        'posts': page_obj,
    }
    context.update(get_widget_context())
    return render(request, 'blog_buster/category_detail.html', context)


def tag_detail(request, slug):
    """Display posts with a specific tag"""
    tag = get_object_or_404(Tag, slug=slug)
    posts = Post.objects.filter(status='published', tags=tag)
    
    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'tag': tag,
        'page_obj': page_obj,
        'posts': page_obj,
    }
    context.update(get_widget_context())
    return render(request, 'blog_buster/tag_detail.html', context)


def buying_guides_list(request):
    guides = (
        BuyingGuide.objects.filter(published=True)
        .prefetch_related(Prefetch('picks', queryset=GuidePick.objects.order_by('sort_order')))
    )
    context = {'guides': guides}
    context.update(get_widget_context())
    return render(request, 'blog_buster/buying_guides_list.html', context)


def buying_guide_detail(request, slug):
    guide = get_object_or_404(
        BuyingGuide.objects.prefetch_related(Prefetch('picks', queryset=GuidePick.objects.order_by('sort_order'))),
        slug=slug,
        published=True,
    )
    context = {'guide': guide}
    context.update(get_widget_context())
    return render(request, 'blog_buster/buying_guide_detail.html', context)


def product_reviews_list(request):
    reviews = ProductReview.objects.filter(published=True).prefetch_related('scores')
    context = {'reviews': reviews}
    context.update(get_widget_context())
    return render(request, 'blog_buster/product_reviews_list.html', context)


def product_review_detail(request, slug):
    review = get_object_or_404(ProductReview.objects.prefetch_related('scores'), slug=slug, published=True)
    context = {'review': review}
    context.update(get_widget_context())
    return render(request, 'blog_buster/product_review_detail.html', context)


def howto_list(request):
    series = HowToSeries.objects.filter(published=True).prefetch_related('steps')
    context = {'series_list': series}
    context.update(get_widget_context())
    return render(request, 'blog_buster/howto_list.html', context)


def howto_detail(request, slug):
    series = get_object_or_404(HowToSeries.objects.prefetch_related('steps'), slug=slug, published=True)
    context = {'series': series}
    context.update(get_widget_context())
    return render(request, 'blog_buster/howto_detail.html', context)
