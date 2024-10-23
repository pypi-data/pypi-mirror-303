"""
Модуль содержит общие функции для работы с пакетом
"""
from __future__ import (
    annotations,
)

from pathlib import (
    Path,
)
from typing import (
    Any,
)

from django.core.files import (
    File,
)
from django.db.transaction import (
    atomic,
)

from edu_eldoc_registry.api.dev import (
    add_sign,
)
from edu_eldoc_registry.constants import (
    EXT_SIG,
)
from edu_eldoc_registry.exceptions import (
    DocException,
    SignException,
)
from edu_eldoc_registry.models import (
    Certificate,
    Document,
    Sign,
)


@atomic  # type: ignore
def sign_document(doc: Document,
                  sign_data: str,
                  attached: bool,
                  cert: Certificate,
                  sign_extension: str = EXT_SIG,
                  last_sign: bool = True
                  ) -> Sign:
    """
    Подписать документ

    :param doc: Документ для подписания
    :param sign_data: Подпись в формате base64
    :param attached: Признак прикреплённой подписи
    :param cert: Сертификат подписания
    :param sign_extension: Расширение для файла с подписью
    :param last_sign: Отметить документ подписанным по завершению
    :returns: Объект файла подписи
    """
    if doc.status != Document.STATUS_READY:
        raise SignException(
            'Подписать можно только документ в статусе "Готов к подписанию"')
    
    sign = add_sign(doc, sign_data, attached, cert, sign_extension)

    if last_sign:
        mark_signed(doc)

    return sign


def mark_signed(doc: Document) -> None:
    """
    Отметить документ подписанным

    :param doc: Объект документа
    """
    if doc.status != Document.STATUS_READY:
        raise DocException('Документ должен быть в статусе "Готов к подписанию"')

    if not Sign.objects.filter(document=doc).exists():
        raise DocException('Документ не имеет подписей')

    doc.status = Document.STATUS_SIGNED
    doc.save()


def mark_ready(doc: Document) -> None:
    """
    Отметить документ готовым к подписанию

    :param doc: Объект документа
    """
    if doc.status != Document.STATUS_NEW:
        raise DocException('Документ должен быть в статусе "Новый"')

    doc.status = Document.STATUS_READY
    doc.save()


def mark_rejected(doc: Document, raise_rejected: bool = True) -> None:
    """
    Отклонить документ

    :param doc: Объект документа
    :param raise_rejected: Бросать исключение если документ уже в статусе "Отклонён"
    """
    if Sign.objects.filter(document=doc).exists():
        raise DocException('Документ уже имеет подпись')

    if doc.status == Document.STATUS_REJECTED:
        if raise_rejected:
            raise DocException('Документ уже отклонён')
        return

    doc.status = Document.STATUS_REJECTED
    doc.save()


def load_file(file: Any, filename: str, **extra: Any) -> Document:
    """
    Добавить файл в реестр документов

    :param file: Объект файла
    :param filename: Наименование файла
    :param extra: Дополнительные параметры
    :returns: Созданный объект документа
    """
    djangofile = File(file)
    return Document.objects.create(
        name=filename,
        file=djangofile,
        **extra
    )


def load_local_file(path: str, filename: str | None = None, **extra: Any) -> Document:
    """
    Добавить локальный файл в реестр документов

    Путь до файла не должен быть абсолютным или содержать ".." 
    так как в этом случае Django бросит исключение `SuspiciousFileOperation`

    :param path: Путь до файла
    :param filename: Наименование файла
    :param extra: Дополнительные параметры
    :returns: Созданный объект документа
    """
    with open(path, 'rb') as local_file:
        if filename is None:
            p = Path(path)
            filename = f'{p.stem}{p.suffix}'
        return load_file(local_file, filename)
