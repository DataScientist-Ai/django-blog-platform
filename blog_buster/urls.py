from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.post_list, name='post_list'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('tag/<slug:slug>/', views.tag_detail, name='tag_detail'),
    path('guides/', views.buying_guides_list, name='buying_guides_list'),
    path('guides/<slug:slug>/', views.buying_guide_detail, name='buying_guide_detail'),
    path('reviews/', views.product_reviews_list, name='product_reviews_list'),
    path('reviews/<slug:slug>/', views.product_review_detail, name='product_review_detail'),
    path('how-to/', views.howto_list, name='howto_list'),
    path('how-to/<slug:slug>/', views.howto_detail, name='howto_detail'),
]
