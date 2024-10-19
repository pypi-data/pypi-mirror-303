from unittest import TestCase, IsolatedAsyncioTestCase
from heaserver.service.db import awsservicelib
from heaobject.awss3key import encode_key
from botocore.exceptions import ClientError
from urllib.parse import quote

import heaserver.service.db.aws


class TestAWSServiceLib(TestCase):

    def test_decode_folder_root(self):
        self.assertEqual('', awsservicelib.decode_folder('root'))

    def test_decode_folder_non_root(self):
        self.assertEqual('/', awsservicelib.decode_folder('Lw=='))

    def test_decode_not_folder(self):
        self.assertEqual(None, awsservicelib.decode_folder('VGV4dEZpbGUucGRm'))

    def test_handle_client_error_404(self):
        c = ClientError(error_response={'Error': {'Code': heaserver.service.db.aws.CLIENT_ERROR_404}}, operation_name='foo')
        self.assertEqual(404, awsservicelib.handle_client_error(c).status)

    def test_handle_client_error_no_such_bucket(self):
        c = ClientError(error_response={'Error': {'Code': heaserver.service.db.aws.CLIENT_ERROR_NO_SUCH_BUCKET}}, operation_name='foo')
        self.assertEqual(404, awsservicelib.handle_client_error(c).status)

    def test_handle_client_error_unknown(self):
        c = ClientError(error_response={'Error': {'Code': "It's wrecked"}},
                        operation_name='foo')
        self.assertEqual(500, awsservicelib.handle_client_error(c).status)

class TestTestAWSServiceLib(IsolatedAsyncioTestCase):
    async def test_extract_source(self):
        actual = await awsservicelib._extract_source(
            {'bucket_id': 'arp-scale-2-cloud-bucket-with-tags11', 'id': encode_key('TestFolder2/')})
        self.assertEquals(('arp-scale-2-cloud-bucket-with-tags11', 'TestFolder2/'), actual)

    async def test_extract_target(self):
        actual = await awsservicelib._copy_object_extract_target({'template': {'data': [{'name': 'target',
                                                                                         'value': f'http://localhost:8080/volumes/12345678/buckets/arp-scale-2-cloud-bucket-with-tags11/awss3folders/{encode_key("TestFolder/")}'}]}})
        self.assertEquals(awsservicelib.TargetInfo(
                          'http://localhost:8080/volumes/12345678/buckets/arp-scale-2-cloud-bucket-with-tags11/awss3folders/VGVzdEZvbGRlci8=',
                          'arp-scale-2-cloud-bucket-with-tags11', 'TestFolder/', '12345678'), actual)

    async def test_extract_target_with_escaped_characters(self):
        actual = await awsservicelib._copy_object_extract_target({'template': {'data': [{'name': 'target',
                                                                                         'value': f'http://localhost:8080/volumes/12345678/buckets/arp-scale-2-cloud-bucket-with-tags11/awss3folders/{quote(encode_key("TestFolder/"))}'}]}})
        self.assertEquals(awsservicelib.TargetInfo(
                          f'http://localhost:8080/volumes/12345678/buckets/arp-scale-2-cloud-bucket-with-tags11/awss3folders/{quote(encode_key("TestFolder/"))}',
                          'arp-scale-2-cloud-bucket-with-tags11',
                          'TestFolder/', '12345678'),
            actual)


