""" Test case Lettings app """

import pytest
from django.test import TestCase
from django.urls import reverse

from profiles.models import Profile


@pytest.mark.django_db
class TestProfiles(TestCase):
    """Test Profile URL"""

    def test_index(self):
        """page should contain <title>Lettings</title>
        """
        response = self.client.get(reverse('profiles:index'))
        assert response.status_code == 200
        self.assertEqual(True, b'<title>Profiles</title>' in response.content)

    def test_profiles(self):
        """page should contain <title>lettings title value</title>
        """
        Profiles_tests = Profile.objects.all()
        for profile in Profiles_tests:
            response = self.client.get(reverse('profiles:profile', args=[profile.user]))
            assert response.status_code == 200
            print(profile.user)
            self.assertInHTML(str(profile.user), str(response.content))
