from shared_lib.models import BlogPost, PortfolioCategory, Portfolio
from django import template

register = template.Library()


@register.inclusion_tag("herobiz/components/portfolio.html")
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

@register.inclusion_tag("herobiz/components/recent_blog_posts.html")
def recent_blog_posts(title, subtitle, top_n):
    posts = BlogPost.objects.filter(status=1).filter(remarkable=True).order_by('-updated_on')
    context = {
        'title': title,
        'subtitle': subtitle,
        'top_n': posts[:top_n],
    }
    return context

@register.inclusion_tag("herobiz/footer.html", takes_context=True)
def footer(context, top_n):
    context.update({
        'latest': BlogPost.objects.filter(status=1).order_by('-updated_on')[:top_n],
    })
    return context
