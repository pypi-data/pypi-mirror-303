from django.urls import path
from django.contrib.sitemaps.views import sitemap
from . import views

from shared_lib.sitemaps import BlogPostSitemap
from .sitemaps import StaticViewSitemap

app_name = 'zenblog'

sitemaps = {
    "posts": BlogPostSitemap,
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('', views.zenblog_home, name='home'),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap",),

    # path('blog_list/', views.ZenblogBlogListView.as_view(), name='blog_list'),
    path('blog_details/<slug>', views.ZenblogBlogDetailView.as_view(), name='blog_details'),
    path('blog_category/<str:category_filter>', views.ZenblogBlogCategoryListView.as_view(), name='blog_category'),
    path('blog_search_word/', views.ZenblogBlogSearchWordListView.as_view(), name='blog_search_word'),
    path('blog_tag/<str:tag>', views.ZenblogBlogTagListView.as_view(), name='blog_tag'),

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

]
