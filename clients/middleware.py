from django.conf import settings
from django.shortcuts import redirect




class LoginRequiredMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.path.lstrip('/') not in settings.LOGIN_REQUIRED_EXAMPT:
            return redirect(settings.LOGIN_URL)
        response = self.get_response(request)
        return response

