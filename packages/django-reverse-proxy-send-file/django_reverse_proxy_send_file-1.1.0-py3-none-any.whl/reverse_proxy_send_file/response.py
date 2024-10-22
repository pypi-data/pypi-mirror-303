from http import HTTPStatus

from django.conf import settings as django_settings
from django.http import HttpResponse
from django.views.static import serve

from reverse_proxy_send_file import settings as rpr_settings


def get_sendfile_response(request, resource_url):
    if rpr_settings.get_debug_serve_resource() and django_settings.DEBUG:
        return serve(request, resource_url, document_root=rpr_settings.get_media_root())

    response = HttpResponse(status=HTTPStatus.OK)
    response["Content-Type"] = ""

    reverse_proxy_resource_path = get_reverse_proxy_path(request, resource_url)
    header = rpr_settings.get_header_name()
    if not header:
        if rpr_settings.get_mode() == "apache":  # noqa: SIM108
            header = "X-Sendfile"
        else:  # nginx
            header = "X-Accel-Redirect"

    response[header] = reverse_proxy_resource_path

    return response


def get_reverse_proxy_path(request, resource_url):
    reverse_proxy_send_file_root = rpr_settings.get_reverse_proxy_root()
    if not reverse_proxy_send_file_root.endswith("/"):
        reverse_proxy_send_file_root += "/"
    return reverse_proxy_send_file_root + resource_url
