from django.urls import path
from django.contrib.sitemaps.views import sitemap
from . import views

from shared_lib.sitemaps import BlogPostSitemap, PortfolioSitemap
from .sitemaps import StaticViewSitemap

app_name = 'medilab'

sitemaps = {
    "posts": BlogPostSitemap,
    "portfolios": PortfolioSitemap,
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('', views.medilab_home, name='home'),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap", ),

    path('blog_details/<slug>', views.MedilabBlogDetailView.as_view(), name='blog_details'),

    path('terms_of_use/', views.medilab_terms, name='terms'),
    path('privacy_policy/', views.medilab_privacy, name='privacy'),

    path('fee/', views.fee, name='fee'),
]
