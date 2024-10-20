from django import template
from _data import shared_lib
from shared_lib.models import BlogCategory, BlogPost, PortfolioCategory, Portfolio


register = template.Library()


# ============================== analytics ============================================
@register.inclusion_tag('shared_lib/analytics.html')
def analytics():
    return shared_lib.analytics


# =============================== modal ==============================================
from ..models import ModalImageOnly, ModalSingleBG, ModalLinkVideo, ModalRotateBG

@register.inclusion_tag(f"shared_lib/modal/_load.html")
def show_modal():
    popup = None
    try:
        # 활성화된 type5에서 하나(제일 처음 것)을 선택함.
        popup = ModalImageOnly.objects.filter(activate__exact=True)[0]
        print(f"Activated {ModalImageOnly.__name__} objects : {popup}")
    except IndexError:
        pass

    try:
        # 활성화된 type4에서 하나(제일 처음 것)을 선택함.
        popup = ModalSingleBG.objects.filter(activate__exact=True)[0]
        print(f"Activated {ModalSingleBG.__name__} objects : {popup}")
    except IndexError:
        pass
    try:
        # 활성화된 type2에서 하나(제일 처음 것)을 선택함.
        popup = ModalLinkVideo.objects.filter(activate__exact=True)[0]
        print(f"Activated {ModalLinkVideo.__name__} objects : {popup}")
    except IndexError:
        pass

    try:
        # 활성화된 type1에서 하나(제일 처음 것)을 선택함.
        popup = ModalRotateBG.objects.filter(activate__exact=True)[0]
        print(f"Activated {ModalRotateBG.__name__} objects : {popup}")
    except IndexError:
        pass

    context = {
        "dont_show_again": "다시보지않기",
        "type": popup.__class__.__name__,
        "popup": popup,
    }
    print("popup context: ", context)
    return context


# ================================== calendar ====================================
from datetime import datetime, timedelta
from ..models import Calendar, Event

@register.inclusion_tag(f"shared_lib/calendar/_load.html")
def show_calendar():
    try:
        # 활성화된 달력에서 하나(제일 처음 것)을 선택함.
        calendar1 = Calendar.objects.filter(activate__exact=True)[0]
    except IndexError:
        calendar1 = None

    try:
        # 달력의 이벤트 날짜들을 저장함.
        events = Event.objects.filter(calendar__exact=calendar1)
    except IndexError:
        events = None

    print(events)
    context = {
        "dont_show_again": "다시보지않기",
        "calendar": calendar1,
        "events": events,
        "default_date": set_default_date().strftime("%Y-%m-%d"),
    }
    print("calendards context: ", context)
    return context


def set_default_date(date=25) -> datetime:
    """
    full calendar의 defaultDate를 설정하는 함수
    date 인자 이후의 날짜는 다음달을 표시하도록 default day를 다음달로 반환한다.
    """
    today = datetime.today()
    if today.day >= date:
        return today + timedelta(days=7)
    else:
        return today


# ================================== Blog ===================================
import re
from django.template.loader import render_to_string

from shared_lib.forms import SearchForm
from taggit.models import Tag


@register.simple_tag
def sidebar(template_name):
    tags = Tag.objects.all()
    categories = BlogCategory.objects.all()
    category = []
    for category_item in categories:
        category.append([category_item.filter, BlogPost.objects.filter(status=1)
                        .filter(category__filter=category_item.filter).count()])

    context = {
        'template_name': template_name,
        'form': SearchForm(),
        'category': category,
        'all_tags': tags,
        'latest': BlogPost.objects.filter(status=1).order_by('-updated_on')[:6],
    }
    return render_to_string(template_name, context)


@register.filter
def add_img_class(value):
    """
    HTML 문자열에서 모든 <img> 태그에 'img-fluid' 클래스를 추가합니다.
    """
    # 이미 class 속성이 있는 경우 처리
    def replace(match):
        img_tag = match.group(0)
        if 'class="' in img_tag:
            # 기존 클래스에 'img-fluid' 추가
            return re.sub(r'class="([^"]+)"', r'class="\1 img-fluid"', img_tag)
        else:
            # 클래스 속성이 없으면 추가
            return img_tag[:-1] + ' class="img-fluid">'
    # <img> 태그를 찾아서 교체
    return re.sub(r'<img[^>]*>', replace, value)

# =========================== Testing ===================================================
@register.inclusion_tag("shared_lib/_portfolio.html")
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

@register.inclusion_tag("shared_lib/_recent_blog_posts.html")
def recent_blog_posts(title, subtitle, top_n):
    posts = BlogPost.objects.filter(status=1).filter(remarkable=True).order_by('-updated_on')
    context = {
        'title': title,
        'subtitle': subtitle,
        'top_n': posts[:top_n],
    }
    return context
