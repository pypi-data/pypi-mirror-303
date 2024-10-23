from django.template import Library
from shared_lib.models import BlogPost
from shared_lib.forms import SearchForm

register = Library()

# https://localcoder.org/django-inclusion-tag-with-configurable-template


@register.inclusion_tag('zenblog/header.html', takes_context=True)
def header(context):
    context.update({'form': SearchForm()})
    return context


@register.inclusion_tag('zenblog/components/category_grid1.html', takes_context=True)
def category_gid1(context, category_filter):
    objects = BlogPost.objects.filter(status=1).filter(category__filter=category_filter).order_by('-updated_on')
    return {
        'top4': objects[:4],
        'the_others': objects[4:10]
    }


@register.inclusion_tag('zenblog/components/category_grid2.html', takes_context=True)
def category_gid2(context, category_filter):
    objects = BlogPost.objects.filter(status=1).filter(category__filter=category_filter).order_by('-updated_on')
    return {
        'top4': objects[:4],
        'the_others': objects[4:10]
    }


@register.inclusion_tag('zenblog/components/category_grid3.html', takes_context=True)
def category_gid3(context, category_filter):
    objects = BlogPost.objects.filter(status=1).filter(category__filter=category_filter).order_by('-updated_on')
    return {
        'top3': objects[:3],
        'the_others1': objects[3:6],
        'the_others2': objects[6:9],
        'the_others3': objects[9:15],
    }


@register.inclusion_tag('zenblog/footer.html', takes_context=True)
def footer(context):
    # about 모듈 사용여부에 따라 footer의 배치를 다르게 하기 위해
    is_about_used = False
    for module, is_used, _, _ in context['components']:
        if module == 'about' and is_used:
            is_about_used = True
            break

    context.update({
        'is_about_used': is_about_used,
        'recents4': BlogPost.objects.filter(status=1).order_by('-updated_on')[:4],
    })
    return context

