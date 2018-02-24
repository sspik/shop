from elasticsearch_dsl.connections import connections
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from elasticsearch_dsl import DocType, Text, Date, Integer

from .models import Item

connections.create_connection()

class ItemIndex(DocType):

    class Meta:
        index = 'item-index'

    name = Text
    price = Integer
    short_desc = Text
    detail_desc = Text


def bulk_indexing():
    ItemIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in Item.objects.all().iterator()))