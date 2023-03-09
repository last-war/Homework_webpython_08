from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import ReferenceField, DateTimeField, EmbeddedDocumentField, ListField, StringField


class Author(Document):
    fullname = StringField()
    born_date = DateTimeField()
    born_location = StringField()
    description = StringField()


class Tag(EmbeddedDocument):
    name = StringField()


class Quotes(Document):
    tags = ListField(EmbeddedDocumentField(Tag))
    author = ReferenceField('Author')
    quote = StringField()
