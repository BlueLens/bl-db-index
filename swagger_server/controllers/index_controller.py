import connexion
from swagger_server.models.add_index_response import AddIndexResponse
from swagger_server.models.index import Index
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

from orm.indexes import Indexes


def add_index(body):
    """
    Added a new Index
    
    :param body: Object that needs to be added to the db.
    :type body: dict | bytes

    :rtype: AddIndexResponse
    """
    return Indexes.add_index(connexion)

def get_index_by_index_id(indexId):
    """
    Get Index
    Returns a single Index
    :param indexId: ID of Index to return
    :type indexId: str

    :rtype: GetIndexResponse
    """
    return Indexes.get_index_by_index_id(indexId)

def get_index_by_object_id(objectId):
    """
    Get Index by objectId
    Returns a single Index
    :param objectId: ID of Object to return
    :type objectId: str

    :rtype: GetIndexResponse
    """
    return Indexes.get_index_by_object_id(objectId)
