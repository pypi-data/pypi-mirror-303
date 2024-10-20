from django.shortcuts import HttpResponse


def robots(request):
    robots_contents = """User-agent: *
Disallow: /admin
Allow: /

User-agent: Mediapartners-Google
Allow: /

User-agent: bingbot
Crawl-delay: 30"""
    return HttpResponse(robots_contents, content_type="text/plain")