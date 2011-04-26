"""
Created on 22.09.2009

@author: alen
"""
from django.contrib.auth.models import User
from django.contrib.sites.models import Site

from socialregistration.models import (FacebookProfile, TwitterProfile, HyvesProfile, LinkedinProfile,
    FriendFeedProfile, OpenIDProfile)

class Auth(object):
    supports_object_permissions = False
    supports_anonymous_user = False
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

class FacebookAuth(Auth):
    def authenticate(self, uid=None):
        try:
            return FacebookProfile.objects.get(
                uid=uid,
                site=Site.objects.get_current()
            ).user
        except:
            return None

class TwitterAuth(Auth):
    def authenticate(self, twitter_id=None):
        try:
            return TwitterProfile.objects.get(
                twitter_id=twitter_id,
                site=Site.objects.get_current()
            ).user
        except:
            return None

class HyvesAuth(Auth):
    def authenticate(self, hyves_id=None):
        try:
            return HyvesProfile.objects.get(
                hyves_id=hyves_id,
                site=Site.objects.get_current()
            ).user
        except:
            return None

class LinkedinAuth(Auth):
    def authenticate(self, linkedin_id=None):
        try:
            return LinkedinProfile.objects.get(
                linkedin_id=linkedin_id,
                site=Site.objects.get_current()
            ).user
        except:
            return None

class OpenIDAuth(Auth):
    def authenticate(self, identity=None):
        try:
            return OpenIDProfile.objects.get(
                identity=identity,
                site=Site.objects.get_current()
            ).user
        except:
            return None
