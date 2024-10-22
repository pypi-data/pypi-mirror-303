from django.urls import path
from django.contrib.sitemaps.views import sitemap
from . import views

from shared_lib.sitemaps import BlogPostSitemap, PortfolioSitemap
from .sitemaps import StaticViewSitemap

app_name = 'herobiz'

sitemaps = {
    "posts": BlogPostSitemap,
    "portfolios": PortfolioSitemap,
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('', views.herobiz_home, name='home'),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap",),

    path('portfolio_details/<int:pk>/', views.herobiz_portfolio_details, name='portfolio_details'),

    path('blog_list/', views.HerobizBlogListView.as_view(), name='blog_list'),
    path('blog_details/<slug>', views.HerobizBlogDetailView.as_view(), name='blog_details'),
    path('blog_category/<str:category_filter>', views.HerobizBlogCategoryListView.as_view(), name='blog_category'),
    path('blog_search_word/', views.HerobizBlogSearchWordListView.as_view(), name='blog_search_word'),
    path('blog_tag/<str:tag>', views.HerobizBlogTagListView.as_view(), name='blog_tag'),

    path('terms_of_use/', views.herobiz_terms, name='terms'),
    path('privacy_policy/', views.herobiz_privacy, name='privacy'),
]
