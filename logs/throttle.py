from rest_framework.throttling import BaseThrottle


class log_throttle(BaseThrottle):
    def allow_request(self, request, view):
        user = request.user
        if user.is_authenticated:
            count = request.session.get("view_count", 0)
            if count >= 3:
                return False
            request.session["view_count"] = count + 1
            return True
        count = request.session.get("view_count", 0)
        if count >= 2:
            return False
        request.session["view_count"] = count + 1
        return True
