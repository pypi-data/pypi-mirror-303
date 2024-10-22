from django.core.files.storage import FileSystemStorage
from django.utils.functional import cached_property

from reverse_proxy_send_file import settings


class ReverseProxySendFileStorageMixin:
    @cached_property
    def base_location(self):
        return self._value_or_setting(self._location, settings.get_media_root())

    @cached_property
    def base_url(self):
        if self._base_url is not None and not self._base_url.endswith("/"):
            self._base_url += "/"
        return self._value_or_setting(self._base_url, settings.get_media_url())


class ReverseProxySendFileFileSystemStorage(ReverseProxySendFileStorageMixin, FileSystemStorage):
    pass
