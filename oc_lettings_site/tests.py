""" Test oc_lettings_site """
from django.test import TestCase
from django.urls import reverse


class TestOcLettingsSite(TestCase):
    """Test home oc_lettings_site_index"""
    def test_index(self):
        """home index page should contain
        <title>Holiday Homes</title>
        """
        response = self.client.get(reverse('index'))
        assert response.status_code == 200
        self.assertEqual(True, b'<title>Holiday Homes</title>' in response.content)
