from django.test import TestCase
from django.template import Context, Template

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse

from webdriver_hj3415 import drivers


class SeleniumTestCase(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.browser = drivers.get(headless=False)
        cls.browser.implicitly_wait(10)  # 페이지 로딩을 최대 10초 대기

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def get_full_url(self, path):
        return f'{self.live_server_url}{path}'

class AnalyticsTests(TestCase):
    def setUp(self):
        pass

    def test_analytics(self):
        template = Template("{% load shared_tags %}{% analytics %}")
        context = Context({})
        content = template.render(context)
        print(content)


class ModalsTests(SeleniumTestCase):
    def setUp(self):
        pass

    def test_modal_1(self):
        self.browser.get(self.get_full_url(reverse('shared_lib:test')))  # 페이지 로드