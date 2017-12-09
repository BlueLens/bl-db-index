# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.add_index_response import AddIndexResponse
from swagger_server.models.get_index_response import GetIndexResponse
from swagger_server.models.index import Index
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestObjectController(BaseTestCase):
    """ ObjectController integration test stubs """

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

    def test_get_index_by_id(self):
        """
        Test case for get_index_by_id

        Get Index
        """
        response = self.client.open('//indexes/{indexId}'.format(indexId='indexId_example'),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
