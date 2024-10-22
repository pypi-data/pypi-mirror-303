from django.http import HttpResponseForbidden
from django.views import View

from reverse_proxy_send_file.response import get_sendfile_response


class ReverseProxySendFileView(View):
    """
    Deprecated
    """

    def get(self, request, resource_url, *args, **kwargs):
        if not self.check_permission(request, resource_url):
            return HttpResponseForbidden()

        return get_sendfile_response(request, resource_url)

    def check_permission(self, request, resource_url):
        return True
