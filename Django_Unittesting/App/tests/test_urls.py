from django.test import SimpleTestCase
from django.urls import resolve, reverse
from App.views import project_list, project_detail, ProjectCreateView

class TestUrls(SimpleTestCase):
    
    def test_plist_urls(self):
        url = reverse('list')
        self.assertEquals(resolve(url).func, project_list)

    def test_create_urls(self):
        url = reverse('add')
        self.assertEquals(resolve(url).func.view_class, ProjectCreateView)

    def test_detail_urls(self):
        url = reverse('detail', args=['some-slug'])
        self.assertEquals(resolve(url).func, project_detail)

    