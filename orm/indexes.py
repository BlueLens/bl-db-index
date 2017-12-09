import os
import time
from orm.database import DataBase
from swagger_server.models.add_index_response import AddIndexResponse
from swagger_server.models.add_index_response_data import AddIndexResponseData
from swagger_server.models.get_index_response import GetIndexResponse
from swagger_server.models.index import Index

from bluelens_log import Logging

REDIS_SERVER = os.environ['REDIS_SERVER']
REDIS_PASSWORD = os.environ['REDIS_PASSWORD']

options = {
  'REDIS_SERVER': REDIS_SERVER,
  'REDIS_PASSWORD': REDIS_PASSWORD
}
log = Logging(options, tag='bl-db-index:Indexes')

class Indexes(DataBase):
  def __init__(self):
    super().__init__()
    self.indexes = self.db.indexes

  @staticmethod
  def add_index(connexion):
    start_time = time.time()
    orm = Indexes()
    res = AddIndexResponse()
    data = AddIndexResponseData()
    response_status = 200
    if connexion.request.is_json:
      index = connexion.request.get_json()
      index['_id'] = index['object_id']

      try:
        r = orm.indexes.find_one_and_update({"_id": index['object_id']},
                                         {"$set": index},
                                         upsert=True,
                                         return_document=True)
        res.message = 'Successful'
        res.data = r
      except Exception as e:
        res.message = str(e)
        response_status = 400

    elapsed_time = time.time() - start_time
    log.debug('add_index time: ' + str(elapsed_time))
    return res, response_status

  @staticmethod
  def get_index_by_index_id(index_id):
    start_time = time.time()
    orm = Indexes()
    res = GetIndexResponse()
    response_status = 200

    try:
      r = orm.indexes.find_one({"index_id": index_id})
      res.message = 'Successful'
      res.data = r
    except Exception as e:
      res.message = str(e)
      response_status = 400

    elapsed_time = time.time() - start_time
    log.debug('get_index_by_index_id time: ' + str(elapsed_time))
    return res, response_status

  @staticmethod
  def get_index_by_object_id(object_id):
    start_time = time.time()
    orm = Indexes()
    res = GetIndexResponse()
    response_status = 200

    try:
      r = orm.indexes.find_one({"_id": object_id})
      res.message = 'Successful'
      res.data = r
    except Exception as e:
      res.message = str(e)
      response_status = 400

    elapsed_time = time.time() - start_time
    log.debug('get_index_by_object_id time: ' + str(elapsed_time))
    return res, response_status
