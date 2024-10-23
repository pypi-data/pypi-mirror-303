from django.urls import path
from django.contrib.sitemaps.views import sitemap
from . import views

from shared_lib.sitemaps import PortfolioSitemap
from .sitemaps import StaticViewSitemap

app_name = 'bocor'

sitemaps = {
    "portfolios": PortfolioSitemap,
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('', views.bocor_home, name='home'),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap", ),

    path('portfolio_details/<int:pk>/', views.bocor_portfolio_details, name='portfolio_details'),

    path('terms_of_use/', views.bocor_terms, name='terms'),
    path('privacy_policy/', views.bocor_privacy, name='privacy'),
]
