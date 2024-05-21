from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .views import user_profile_create, user_profile_detail, user_profile_update, user_profile_delete


class UserAuthenticationTest(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        # Create a test client
        self.client = Client()

    def test_login_page(self):
        # Test if the login page returns a 200 status code
        response = self.client.get(reverse('travel:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'travel/login.html')

    def test_valid_login(self):
        # Test logging in with valid credentials
        response = self.client.post(reverse('travel:login'), {
            'username': 'testuser',
            'password': 'testpassword',
        })
        self.assertEqual(response.status_code, 302)  # Should be a redirect after successful login
        self.assertRedirects(response, reverse('travel:index'))

    def test_invalid_login(self):
        # Test logging in with invalid credentials
        response = self.client.post(reverse('travel:login'), {
            'username': 'testuser',
            'password': 'wrongpassword',
        })
        self.assertEqual(response.status_code, 200)  # Should stay on the login page
        self.assertContains(response, 'Please enter a correct username and password. Note that both fields may be case-sensitive.')

    def test_authenticated_user_access(self):
        # Test if an authenticated user can access a protected page (e.g., dashboard)
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('travel:user_profile_detail', kwargs={'username': 'testuser'}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'travel/user_profile/detail.html')

    def test_unauthenticated_user_access(self):
        # Test if an unauthenticated user is redirected to the login page when accessing a protected page
        response = self.client.get(reverse('travel:user_profile_detail', kwargs={'username': 'testuser'}))
        self.assertEqual(response.status_code, 302)  # Should be a redirect to the login page
        self.assertRedirects(response, reverse('travel:login') + '?next=' + reverse('travel:user_profile_detail', kwargs={'username': 'testuser'}))

    def test_logout(self):
        # Test if a logged-in user can successfully log out
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('travel:logout'))
        self.assertEqual(response.status_code, 302)  # Should be a redirect after logout
        self.assertRedirects(response, reverse('travel:login'))
        self.assertFalse(self.client.session.has_key('_auth_user_id'))  # Check if user is no longer in the session
