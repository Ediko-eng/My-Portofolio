from django.test import TestCase
from django.urls import reverse

from .models import ContactMessage, Profile, Project, Skill


class HomeViewTests(TestCase):
    def test_home_renders_with_content(self):
        Profile.objects.create(name="Test Person", about="Hello there.")
        Skill.objects.create(title="Backend", description="Django", order=1)
        Project.objects.create(title="Cool Project", description="Does things.", order=1)

        response = self.client.get(reverse("core:home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Person")
        self.assertContains(response, "Cool Project")
        self.assertContains(response, "Backend")


class ContactViewTests(TestCase):
    def test_post_saves_message_and_redirects(self):
        response = self.client.post(
            reverse("core:contact"),
            {"name": "Jane", "email": "jane@example.com", "message": "Hi!", "website": ""},
        )

        self.assertRedirects(response, reverse("core:home") + "#contact")
        self.assertEqual(ContactMessage.objects.count(), 1)
        self.assertEqual(ContactMessage.objects.first().email, "jane@example.com")

    def test_honeypot_blocks_bots(self):
        response = self.client.post(
            reverse("core:contact"),
            {"name": "Bot", "email": "bot@example.com", "message": "spam", "website": "http://spam"},
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(ContactMessage.objects.count(), 0)

    def test_get_redirects_home(self):
        response = self.client.get(reverse("core:contact"))
        self.assertRedirects(response, reverse("core:home") + "#contact")
