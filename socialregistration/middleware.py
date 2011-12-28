import facebook
from django.conf import settings

class Facebook(object):
    def __init__(self, user=None):
        self.user = user
        if user is None:
            self.uid = None
            self.graph = {}
        else:
            self.uid = user['uid']
            self.graph = facebook.GraphAPI(user['access_token'])


class FacebookMiddleware(object):
    def process_request(self, request):
        """
        Enables ``request.facebook`` and ``request.facebook.graph`` in your views 
        once the user authenticated the  application and connected with facebook. 
        You might want to use this if you don't feel confortable with the 
        javascript library.
        """
        try:
            fb_user = facebook.get_user_from_cookie(request.COOKIES,
                getattr(settings, 'FACEBOOK_APP_ID', settings.FACEBOOK_API_KEY), settings.FACEBOOK_SECRET_KEY)
        except facebook.GraphAPIError:
            fb_user = None
        request.facebook = Facebook(fb_user)
        return None
