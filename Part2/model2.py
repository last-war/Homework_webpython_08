from mongoengine import Document
from mongoengine.fields import DateTimeField, StringField, BooleanField
from connector import connect

class Contact(Document):
    fullname = StringField()
    born_date = DateTimeField()
    email = StringField()
    ad_send = BooleanField(default=False)
