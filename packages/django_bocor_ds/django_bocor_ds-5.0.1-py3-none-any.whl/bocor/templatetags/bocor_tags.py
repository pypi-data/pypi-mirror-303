from django.template import Library
from shared_lib.models import PortfolioCategory, Portfolio


register = Library()

# https://localcoder.org/django-inclusion-tag-with-configurable-template

@register.inclusion_tag("bocor/components/portfolio.html")
def portfolio(title, subtitle):
    categories = PortfolioCategory.objects.all()
    items = Portfolio.objects.all()
    context = {
        'categories': categories,
        'items': items,
        'title': title,
        'subtitle': subtitle,
    }
    return context

