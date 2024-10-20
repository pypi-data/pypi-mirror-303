from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# ============================ Home ===================================
from taggit.models import Tag

def home(request):
    context = {
        'all_tags' : Tag.objects.all()
    }
    return render(request, 'shared_lib/_home.html', context)


# ============================= Portfolio ===================================
from .models import Portfolio


def portfolio_details(request, pk, template_name, title) -> HttpResponse:
    """
    Portfolio Details 페이지 뷰 함수 각 템플릿에서 래핑해서 사용한다.
    :param request:
    :param pk: portfolio model pk
    :param template_name:
    :param title: breadcrumbs title
    :return:
    """
    context = {
        "obj": get_object_or_404(Portfolio, pk=pk),
        "breadcrumb": {"title": title},
    }
    return render(request, template_name, context)


def test_portfolio_details(request, pk):
    """
    위의 함수 테스트를 위한 래퍼함수
    :param request:
    :param pk:
    :return:
    """
    return portfolio_details(request, pk, 'shared_lib/_test_portfolio_details.html', 'Portfolio Details')


# ============================= Blog =====================================
from hitcount.views import HitCountDetailView
from django.views import generic
from .models import BlogPost
from .forms import SearchForm

num_pagination = 6


def make_page_bundle(page_range, n=5):
    # 전체 페이지를 n 개수의 묶음으로 만든다.
    # pagination에 사용
    l = [i for i in page_range]
    return [l[i:i + n] for i in range(0, len(l), n)]


class BlogListView(generic.ListView):
    # 템플릿 이름은 이후에 오버라이드할 예정
    template_name = "shared_lib/_test_blog_list.html"
    paginate_by = num_pagination

    def get_queryset(self):
        # https://stackoverflow.com/questions/56067365/how-to-filter-posts-by-tags-using-django-taggit-in-django
        return BlogPost.objects.filter(status=1).order_by('-updated_on')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pages_devided = make_page_bundle(context['paginator'].page_range)

        # 현재 페이지에 해당하는 묶음을 page_bundle로 전달한다.
        for page_bundle in pages_devided:
            if context['page_obj'].number in page_bundle:
                context['page_bundle'] = page_bundle

        context.update({
            "breadcrumb": {"title": "Blog"}
        })
        return context


class BlogCategoryListView(generic.ListView):
    # 템플릿 이름은 이후에 오버라이드할 예정
    template_name = "shared_lib/_test_blog_list.html"
    paginate_by = num_pagination

    def get_queryset(self):
        return BlogPost.objects.filter(status=1).filter(category__filter=self.kwargs['category_filter']).order_by('-updated_on')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pages_devided = make_page_bundle(context['paginator'].page_range)

        # 현재 페이지에 해당하는 묶음을 page_bundle로 전달한다.
        for page_bundle in pages_devided:
            if context['page_obj'].number in page_bundle:
                context['page_bundle'] = page_bundle

        context.update({
            "breadcrumb": {"title": "Category: " + self.kwargs['category_filter']}
        })
        return context


class BlogDetailView(HitCountDetailView):
    model = BlogPost
    # 템플릿 이름은 이후에 오버라이드할 예정
    template_name = "shared_lib/_test_blog_detail.html"
    context_object_name = 'object'
    slug_field = 'slug'
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #author = get_object_or_404(BlogPost, slug=self.kwargs['slug']).author
        #author = self.kwargs['object'].author
        #print(author.image)

        context.update(
            {'breadcrumb': {'title': 'Blog Detail'}}
        )
        return context


class BlogSearchWordListView(generic.ListView):
    # 템플릿 이름은 이후에 오버라이드할 예정
    template_name = "shared_lib/_test_blog_list.html"
    paginate_by = num_pagination

    def get_queryset(self):
        form = SearchForm(self.request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']
        else:
            q = ''
        return BlogPost.objects.filter(content__contains='' if q is None else q).filter(status=1).order_by(
            '-updated_on')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pages_devided = make_page_bundle(context['paginator'].page_range)

        # 현재 페이지에 해당하는 묶음을 page_bundle로 전달한다.
        for page_bundle in pages_devided:
            if context['page_obj'].number in page_bundle:
                context['page_bundle'] = page_bundle
        return context


class BlogTagListView(generic.ListView):
    # 템플릿 이름은 이후에 오버라이드할 예정
    template_name = "shared_lib/_test_blog_list.html"
    paginate_by = num_pagination

    def get_queryset(self):
        # https://stackoverflow.com/questions/56067365/how-to-filter-posts-by-tags-using-django-taggit-in-django
        return BlogPost.objects.filter(tags__name__in=[self.kwargs['tag']]).filter(status=1).order_by('-updated_on')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pages_devided = make_page_bundle(context['paginator'].page_range)

        # 현재 페이지에 해당하는 묶음을 page_bundle로 전달한다.
        for page_bundle in pages_devided:
            if context['page_obj'].number in page_bundle:
                context['page_bundle'] = page_bundle

        context.update({
            "breadcrumb": { "title": "Tag: " + self.kwargs['tag']}
        })
        return context


class SharedLibBlogListView(BlogListView):
    template_name = "shared_lib/_test_blog_list.html"

class SharedLibBlogDetailView(BlogDetailView):
    template_name = "shared_lib/_test_blog_detail.html"

class SharedLibBlogCategoryListView(BlogCategoryListView):
    template_name = "shared_lib/_test_blog_list.html"

class SharedLibBlogSearchWordListView(BlogSearchWordListView):
    template_name = "shared_lib/_test_blog_list.html"

class SharedLibBlogTagListView(BlogTagListView):
    template_name = "shared_lib/_test_blog_list.html"


