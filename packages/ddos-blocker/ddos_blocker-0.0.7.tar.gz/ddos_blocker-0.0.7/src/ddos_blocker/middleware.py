from django.conf import settings
from django.http import HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin

from .redis_adapter import RedisAdapter


class RateLimitMiddleware(MiddlewareMixin):
    def __init__(self, get_response=None):
        self.get_response = get_response
        self.redis_adapter = RedisAdapter(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            db=settings.REDIS_DB,
            timeout=settings.REDIS_TIMEOUT,
            max_requests=settings.REDIS_MAX_REQUESTS,
        )

    def __call__(self, request):
        ip = self.get_client_ip(request)
        self.redis_adapter.set_ip_mask(ip)

        if self.redis_adapter.count_keys(ip) > self.redis_adapter.max_requests:
            return HttpResponseForbidden(
                "You are blocked due to too many requests."
            )

        response = self.get_response(request)
        return response

    def get_client_ip(self, request):
        """Gets the client IP address from the request."""
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
        return ip
