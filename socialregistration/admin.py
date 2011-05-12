from django.contrib import admin
from socialregistration.models import (FacebookProfile, TwitterProfile, LinkedinProfile,
    OpenIDProfile, OpenIDStore, OpenIDNonce)

class FBAdmin(admin.ModelAdmin):
    list_display = ('user', 'username', 'uid')
    search_fields = ['user__username', 'user__email']

class TWAdmin(admin.ModelAdmin):
    list_display = ('user', 'username', 'twitter_id')
    search_fields = ['user__username', 'user__email']

class LIAdmin(admin.ModelAdmin):
    list_display = ('user', 'username', 'linkedin_id')
    search_fields = ['user__username', 'user__email']

admin.site.register(FacebookProfile, FBAdmin)
admin.site.register(TwitterProfile, TWAdmin)
admin.site.register(LinkedinProfile, LIAdmin)
admin.site.register([OpenIDProfile, OpenIDStore, OpenIDNonce])
