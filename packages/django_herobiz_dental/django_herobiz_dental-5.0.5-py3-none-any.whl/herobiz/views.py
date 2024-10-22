from shared_lib import utils
from _data import herobiz

c = herobiz.context


def herobiz_home(request):
    return utils.home(request,'herobiz/index.html', c)

# 이후의 함수 및 클래스에 컨택스트를 전달하는 이유는 color 변수 때문으로 다른 템플릿에서는 전달할 필요 없다.

def herobiz_terms(request):
    return utils.terms(request, 'herobiz/pages/terms.html', c)

def herobiz_privacy(request):
    return utils.privacy(request, 'herobiz/pages/privacy.html', c)

def herobiz_portfolio_details(request, pk):
    return utils.portfolio_details(request, 'herobiz/components/portfolio_details.html', pk, c)


class HerobizBlogListView(utils.BlogListView):
    template_name = "herobiz/pages/blog_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(c)
        return context


class HerobizBlogDetailView(utils.BlogDetailView):
    template_name = "herobiz/pages/blog_details.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(c)
        return context


class HerobizBlogCategoryListView(utils.BlogCategoryListView):
    template_name = "herobiz/pages/blog_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(c)
        return context


class HerobizBlogSearchWordListView(utils.BlogSearchWordListView):
    template_name = "herobiz/pages/blog_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(c)
        return context


class HerobizBlogTagListView(utils.BlogTagListView):
    template_name = "herobiz/pages/blog_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(c)
        return context






