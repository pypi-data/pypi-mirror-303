from shared_lib import utils
from _data import zenblog
from django.shortcuts import render
from shared_lib.models import BlogCategory, BlogPost
from shared_lib.forms import SearchForm
from taggit.models import Tag

c = zenblog.context

def about(request):
    return render(request, 'zenblog/pages/about.html', c)


def contact(request):
    return render(request, 'zenblog/pages/contact.html', c)


def zenblog_home(request):
    category_list = BlogCategory.objects.all()
    category_n_num = []
    for category_item in category_list:
        category_n_num.append([category_item.filter, BlogPost.objects.filter(status=1)
                        .filter(category__filter=category_item.filter).count()])
    """
    category_n_num = [
        ['A', 10],  # 카테고리 A의 filter 값과 게시물 개수
        ['B', 5],   # 카테고리 B의 filter 값과 게시물 개수
        ['C', 8]    # 카테고리 C의 filter 값과 게시물 개수
        ]
    """
    # footer, header, index, sidebar.html 에서 사용
    c.update({
        'category_list': category_list,
        'category_n_num': category_n_num,
    })

    try:
        published_posts = BlogPost.objects.filter(status=1)
    except BlogPost.DoesNotExist:
        published_posts = None

    if published_posts is not None:
        tags = Tag.objects.all()
        c.update({
            'latest1': published_posts.latest('updated_on'),

            # hero.html 에서 사용
            'remarkables': published_posts.filter(remarkable=True).order_by('-updated_on'),

            # post_grid.html 에서 사용
            'the_others': published_posts.order_by('-updated_on')[1:7],
            'trending5': published_posts.order_by('hit_count_generic')[:5],

            # sidebar.html 에서 사용
            'all_tags': tags,
            'latest6': published_posts.order_by('-updated_on')[:6],
            'trending6': published_posts.order_by('hit_count_generic')[:6],
        })
    else:
        c.update({
            'latest1': None,
            'remarkables': None,
            'the_others': None,
            'trending5': None,
            'all_tags': None,
            'latest6': None,
            'trending6': None,
        })
    return utils.home(request,'zenblog/index.html', c)

# 이후의 함수 및 클래스에 컨택스트를 전달하는 이유는 color 변수 때문으로 다른 템플릿에서는 전달할 필요 없다.

def zenblog_terms(request):
    return utils.terms(request, 'zenblog/terms.html', c)

def zenblog_privacy(request):
    return utils.privacy(request, 'zenblog/privacy.html', c)

def zenblog_portfolio_details(request, pk):
    return utils.portfolio_details(request, 'zenblog/portfolio_details.html', pk, c)


class ZenblogBlogDetailView(utils.BlogDetailView):
    template_name = "zenblog/pages/blog_details.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(c)
        return context


class ZenblogBlogCategoryListView(utils.BlogCategoryListView):
    template_name = "zenblog/pages/category.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(c)
        context.update({
            'selected_category': self.kwargs['category_filter']
        })
        return context


class ZenblogBlogSearchWordListView(utils.BlogSearchWordListView):
    template_name = "zenblog/pages/search_result.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(c)
        return context


class ZenblogBlogTagListView(utils.BlogTagListView):
    template_name = "zenblog/pages/search_result.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(c)
        return context






