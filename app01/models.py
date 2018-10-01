from django.db import models
import mongoengine

class User(mongoengine.Document):
    name = mongoengine.StringField()
    age = mongoengine.IntField()
    meta = {"db_alias": "default"}
