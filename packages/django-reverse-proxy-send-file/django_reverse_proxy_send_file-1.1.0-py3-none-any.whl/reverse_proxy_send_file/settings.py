from django.conf import settings


def get_mode():
    return getattr(settings, "REVERSE_PROXY_SENDFILE_MODE", "nginx")


def get_media_url():
    return getattr(settings, "REVERSE_PROXY_SENDFILE_MEDIA_URL", "smedia/")


def get_media_root():
    return getattr(settings, "REVERSE_PROXY_SENDFILE_MEDIA_ROOT", getattr(settings, "MEDIA_ROOT", None))


def get_reverse_proxy_root():
    return getattr(settings, "REVERSE_PROXY_SENDFILE_REVERSE_PROXY_ROOT", get_media_root())


def get_header_name():
    return getattr(settings, "REVERSE_PROXY_SENDFILE_HEADER_NAME", None)


def get_debug_serve_resource():
    return getattr(settings, "REVERSE_PROXY_SENDFILE_DEBUG_SERVE_RESOURCE", True)
