from peewee import BooleanField
from peewee import CharField
from peewee import DateField
from peewee import DecimalField
from peewee import ForeignKeyField
from peewee import IntegerField
from peewee import Model

from settings import db


# Initial creation of tables
# db.connect()
# db.create_tables([Coordinate, Venue, VenueDetail])

class Coordinate(Model):
    coordinate = CharField()
    address = CharField()

    class Meta:
        database = db


class Venue(Model):
    coordinate = ForeignKeyField(Coordinate, related_name='venues')
    venue_id = CharField()

    class Meta:
        database = db


class VenueDetail(Model):
    venue = ForeignKeyField(Venue, related_name="detail")
    name = CharField()
    category = CharField()
    rating =  DecimalField()
    rating_signals = IntegerField()
    checkins_count = IntegerField()
    users_count = IntegerField()
    tip_count = IntegerField()
    visit_count = IntegerField()
    likes = IntegerField()
    photos = IntegerField()
    created_at = DateField()
    listed = IntegerField()
    price = IntegerField()
    verified = BooleanField()

    class Meta:
        database = db