# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.add_index_response import AddIndexResponse
from swagger_server.models.get_index_response import GetIndexResponse
from swagger_server.models.index import Index
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestIndexController(BaseTestCase):
    """ IndexController integration test stubs """

    def test_add_index(self):
        """
        Test case for add_index

        Added a new Index
        """
        body = Index()
        response = self.client.open('//indexes',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_index_by_index_id(self):
        """
        Test case for get_index_by_index_id

        Get Index by indexId
        """
        response = self.client.open('//indexes/{indexId}'.format(indexId=56),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_index_by_object_id(self):
        """
        Test case for get_index_by_object_id

        Get Index by objectId
        """
        response = self.client.open('//indexes/objects/{objectId}'.format(objectId='objectId_example'),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
