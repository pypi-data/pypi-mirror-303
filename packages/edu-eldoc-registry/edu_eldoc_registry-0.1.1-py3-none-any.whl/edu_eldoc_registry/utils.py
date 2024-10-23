from django.core.files import (
    File,
)
from django.utils.safestring import (
    SafeString,
    mark_safe,
)


def get_download_link(file: File, text: str = 'Скачать') -> SafeString:
    """
    Получить html-ссылку на скачивание
    """
    return mark_safe(
        f'<a href="{file.url}" target="_blank">{text}</a>'
    )
