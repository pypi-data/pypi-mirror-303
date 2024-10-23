import base64
import datetime
import os
import shutil
import tempfile
from contextlib import (
    contextmanager,
)
from pathlib import (
    Path,
)

from django.test import (
    TestCase,
    override_settings,
)

from edu_eldoc_registry.api.common import (
    load_local_file,
    mark_ready,
    mark_rejected,
    mark_signed,
    sign_document,
)
from edu_eldoc_registry.constants import (
    EXT_SGN,
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


_test_data_dir_name = 'test_data'
_test_data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), _test_data_dir_name)

_doc_0_filename = '1.txt'
_sign_0_filename = '2.txt'
_sign_1_filename = '3.txt'

_doc_0_path = os.path.join(_test_data_dir, _doc_0_filename)
_sign_0_path = os.path.join(_test_data_dir, _sign_0_filename)
_sign_1_path = os.path.join(_test_data_dir, _sign_1_filename)


def _read_base64(path: str) -> bytes:
    """
    Получить base64 из файла
    """
    with open(path, 'rb') as file:
        return base64.b64encode(file.read())


_sign_0_base64 = _read_base64(_sign_0_path)
_sign_1_base64 = _read_base64(_sign_1_path)


TMP_MEDIA_ROOT = tempfile.mkdtemp()
SIGN_DOCUMENT_STORE_PATH = 'test_sign'


@override_settings(MEDIA_ROOT=TMP_MEDIA_ROOT, 
                   SIGN_DOCUMENT_STORE_PATH=SIGN_DOCUMENT_STORE_PATH)
class DocumentTestCase(TestCase):
    databases = '__all__'

    def setUp(self) -> None:
        super().setUp()
        # Очистим файлы если по какой-то причине они там есть
        sign_dir = os.path.join(TMP_MEDIA_ROOT, SIGN_DOCUMENT_STORE_PATH)
        if os.path.isdir(sign_dir):
            shutil.rmtree(sign_dir)
        
        self.cert_0 = Certificate.objects.create(
            serial='7c000000000000000000000000000000000000',
            name='Test Certificate 0',
            subject='Test Subject 0',
            issuer='Test Issuer 0',
            date_from=datetime.date.today(),
            date_to=datetime.date(9999, 12, 31),
        )

        self.cert_1 = Certificate.objects.create(
            serial='7c111111111111111111111111111111111111',
            name='Test Certificate 1',
            subject='Test Subject 1',
            issuer='Test Issuer 1',
            date_from=datetime.date.today(),
            date_to=datetime.date(9999, 12, 31),
        )

    def tearDown(self):
        super().tearDown()
        if os.path.isdir(TMP_MEDIA_ROOT):
            shutil.rmtree(TMP_MEDIA_ROOT)

    @contextmanager
    def _chdir_to_test_data(self):
        """
        Сменить рабочую папку на папку с файлами для тестов

        Django кидает SuspiciousFileOperation, если пытаться использовать 
        файлы по абсолютному пути
        """
        current = os.getcwd()
        try:
            os.chdir(_test_data_dir)
            yield None
        finally:
            os.chdir(current)

    def _compare_files(self, left_path: str, right_path: str) -> None:
        """
        Сравниваем содержимое двух файлов

        :param left_path: Путь до первого файла
        :param right_path: Путь до второго файла
        """
        with open(left_path, 'rb') as left:
            with open(right_path, 'rb') as right:
                self.assertEqual(
                    left.read(), right.read(), 
                    f'Файлы {left_path} и {right_path} не идентичны')

    def _get_doc(self, from_file=_doc_0_filename) -> Document:
        """
        Получить новый документ для подписания
        """
        with self._chdir_to_test_data():
            return load_local_file(from_file)

    def test_load_doc(self):
        """
        Проверяем загрузку локального файла
        """
        with self._chdir_to_test_data():
            doc = load_local_file(_doc_0_filename)

        # После загрузки проверяем что документ существует, 
        # загружен по ожидаемому пути и файл идентичен тому что мы загружали
        self.assertTrue(Document.objects.filter(pk=doc.id).exists())
        self.assertEqual(doc.status, Document.STATUS_NEW)
        self.assertEqual(doc.file.path, os.path.join(
            TMP_MEDIA_ROOT, SIGN_DOCUMENT_STORE_PATH, doc.uuid.hex, _doc_0_filename))
        self._compare_files(doc.file.path, _doc_0_path)

    def test_mark_ready(self):
        """
        Проверяем смену статуса документа на "Готов к подписанию"
        """
        doc = self._get_doc(_doc_0_filename)
        # Помечаем документ как "Готовый к подписанию" и проверяем что статус сменился
        mark_ready(doc)
        self.assertEqual(doc.status, Document.STATUS_READY)

        # Второй раз статус сменить нельзя так как изначальный статус не "Новый"
        with self.assertRaises(DocException):
            mark_ready(doc)

    def test_signing_doc(self):
        """
        Проверяем добавление подписи к документу
        """
        doc = self._get_doc(_doc_0_filename)

        # Подписать новый документ нельзя, сначала нужно пометить 
        # его как "Готовый к подписанию"
        with self.assertRaises(SignException):
            sign_document(doc, _sign_0_base64, True, self.cert_0, last_sign=False)
        self.assertFalse(Sign.objects.filter(document=doc).exists())

        mark_ready(doc)
        sign_0 = sign_document(doc, _sign_0_base64, True, self.cert_0, last_sign=False)
        # После добавления подписи проверяем что подпись добавлена, 
        # расширение файла по умолчанию и файл идентичен ожидаемому файлу подписи 
        self.assertEqual(Sign.objects.filter(document=doc).count(), 1)
        self._compare_files(sign_0.sign_file.path, _sign_0_path)
        self.assertEqual(Path(sign_0.sign_file.path).suffix, f'.{EXT_SIG}')
        
        # Проверим добавление нескольких подписей
        with self.assertRaises(SignException):
            # Нельзя подписать документ одним сертификатом дважды 
            sign_document(doc, _sign_1_base64, True, self.cert_0, last_sign=False)
        sign_1 = sign_document(doc, _sign_1_base64, True, self.cert_1, last_sign=False)
        self.assertEqual(Sign.objects.filter(document=doc).count(), 2)
        self._compare_files(sign_1.sign_file.path, _sign_1_path)
        self.assertEqual(Path(sign_1.sign_file.path).suffix, f'.{EXT_SIG}')

        # Проверяем что первая подпись всё ещё на месте
        self._compare_files(sign_0.sign_file.path, _sign_0_path)

    def test_mark_signed(self):
        """
        Проверяем перевод документа в статус "Подписано"
        """
        doc = self._get_doc(_doc_0_filename)

        # Можно пометить подписанным только если 
        # статус документа = "Готов к подписанию"
        with self.assertRaises(DocException):
            mark_signed(doc)
        
        mark_ready(doc)
        # У документа нет подписей
        with self.assertRaises(DocException):
            mark_signed(doc)
        
        sign_document(doc, _sign_0_base64, True, self.cert_0, last_sign=False)
        mark_signed(doc)
        self.assertEqual(doc.status, Document.STATUS_SIGNED)

    def test_signing_doc_with_status_change(self):
        """
        Проверяем добавление подписи к документу с последующей сменой статуса
        """
        doc = self._get_doc(_doc_0_filename)
        mark_ready(doc)
        sign = sign_document(
            doc, _sign_0_base64, True, self.cert_0, sign_extension=EXT_SGN, last_sign=True)

        # После добавления подписи проверяем что подпись добавлена, 
        # расширение файла указанное нами и файл идентичен ожидаемому файлу подписи 
        self.assertEqual(Sign.objects.filter(document=doc).count(), 1)
        self._compare_files(sign.sign_file.path, _sign_0_path)
        self.assertEqual(Path(sign.sign_file.path).suffix, f'.{EXT_SGN}')
        self.assertEqual(doc.status, Document.STATUS_SIGNED)

    def test_mark_rejected(self):
        """
        Проверяем перевод документа в статус "Отклонён"
        """
        doc_0 = self._get_doc(_doc_0_filename)
        doc_1 = self._get_doc(_doc_0_filename)

        # Один из документов уже подписан
        mark_ready(doc_0)
        sign_document(doc_0, _sign_0_base64, True, self.cert_0, last_sign=False)

        # Подписанный документ нельзя отклонить
        with self.assertRaises(DocException):
            mark_rejected(doc_0)
        self.assertEqual(doc_0.status, Document.STATUS_READY)

        # Отклоняем документ и проверяем смену статуса
        mark_rejected(doc_1)
        self.assertEqual(doc_1.status, Document.STATUS_REJECTED)

        # Нельзя отклонить документ во второй раз
        with self.assertRaises(DocException):
            mark_rejected(doc_1)
        
        # Если передан raise_rejected=False функция не бросит исключения
        mark_rejected(doc_1, raise_rejected=False)
