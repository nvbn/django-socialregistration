from django.db import models

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib.contenttypes.models import ContentType

class SocialProfile(models.Model):
    user = models.ForeignKey(User, related_name='social')
    site = models.ForeignKey(Site, default=Site.objects.get_current)
    username = models.CharField(max_length=255)
    type = models.ForeignKey(ContentType, editable=False)

    # Tokens
    access_token = models.CharField(max_length=255, blank=True, null=True)
    secret = models.CharField(max_length=255, blank=True, null=True)

    def get_instance(self):
        """ Returns the child instance """
        return self.type.get_object_for_this_type(id=self.id)

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        """ Custom save method so the child of the published item can be found """
        if self.type_id == None:
            self.type = ContentType.objects.get_for_model(self.__class__)
        super(SocialProfile, self).save(force_insert, force_update, *args, **kwargs)

    def __unicode__(self):
        return self.username

class FacebookProfile(SocialProfile):
    uid = models.CharField(max_length=255, blank=False, null=False)

    def __unicode__(self):
        return u'%s: %s' % (self.user, self.uid)

    def authenticate(self):
        return authenticate(uid=self.uid)

class TwitterProfile(SocialProfile):
    twitter_id = models.PositiveIntegerField()

    def __unicode__(self):
        return u'%s: %s' % (self.user, self.twitter_id)

    def authenticate(self):
        return authenticate(twitter_id=self.twitter_id)

class LinkedinProfile(SocialProfile):
    linkedin_id = models.CharField(max_length=255, blank=False, null=False)

    def __unicode__(self):
        return '%s: %s' % (self.user, self.linkedin_id)

    def authenticate(self):
        return authenticate(linkedin_id=self.linkedin_id)

class OpenIDProfile(SocialProfile):
    identity = models.TextField()

    def __unicode__(self):
        try:
            return 'OpenID profile for %s, via provider %s' % (self.user, self.identity)
        except User.DoesNotExist:
            return 'OpenID profile for None, via provider None'

    def authenticate(self):
        return authenticate(identity=self.identity)

class OpenIDStore(models.Model):
    site = models.ForeignKey(Site, default=Site.objects.get_current)
    server_url = models.CharField(max_length=255)
    handle = models.CharField(max_length=255)
    secret = models.TextField()
    issued = models.IntegerField()
    lifetime = models.IntegerField()
    assoc_type = models.TextField()

    def __unicode__(self):
        return u'OpenID Store %s for %s' % (self.server_url, self.site)

class OpenIDNonce(models.Model):
    server_url = models.CharField(max_length=255)
    timestamp = models.IntegerField()
    salt = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'OpenID Nonce for %s' % self.server_url
