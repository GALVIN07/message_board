from django.test import SimpleTestCase
from django.urls import reverse

class PagesTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_template_used(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "homePage.html")

    def test_home_page_uses_base(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "base.html")

    def test_home_page_content(self):
        response = self.client.get("/")
        self.assertContains(response, "Whats the Scuttle Butt?")

    def test_home_page_reverse_lookup(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        response_from_path = self.client.get("/")
        self.assertTemplateUsed(response, "homePage.html")
        self.assertTemplateUsed(response_from_path, "homePage.html")

    # def test_about_page_status_code(self):
    #     response = self.client.get("/about/")
    #     self.assertEqual(response.status.code, 200)


