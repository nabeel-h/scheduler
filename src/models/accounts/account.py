import uuid
from src.common.db.mongodb.database import Database
from src.models.accounts.constants import

__author__ = 'nablh'


class Account(object):
    def __init__(self,
                 name,
                 repsly_id,
                 address,
                 keyaccount_status,
                 asm,
                 lat_lng=None,
                 region=None,
                 w1day=None,
                 w2day=None,
                 w3day=None,
                 w4day=None,
                 active_status=None,
                 schedule_notes=None,
                 last_visit=None,
                 last_merch_form=None,
                 last_po=None,
                 last_updated=None,
                 _id=None
                 ):
        self.name = name
        self.repsly_id = repsly_id
        self.address = address
        self.keyaccount_status = keyaccount_status
        self.asm = asm
        self.active_status = True if active_status is None else False
        self.lat_lng = None if lat_lng is None else lat_lng
        self.region = None if region is None else region
        self.w1day = None if w1day is None else w1day
        self.w2day = None if w2day is None else w2day
        self.w3day = None if w3day is None else w3day
        self.w4day = None if w4day is None else w4day
        self.schedule_notes = None if schedule_notes is None else schedule_notes
        self.last_visit = None if last_visit is None else last_visit
        self.last_merch_form = None if last_merch_form is None else last_merch_form
        self.last_po = None if last_po is None else last_po
        self.last_updated = None if last_updated is None else last_updated
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<Account: {}>".format(self.name)

    def json(self):
        return {
                "name": self.name,
                "repsly_id": self.repsly_id,
                "address": self.address,
                "keyaccount_status": self.keyaccount_status,
                "asm": self.asm,
                "lat_lng": self.lat_lng,
                "region": self.region,
                "w1day": self.w1day,
                "w2day": self.w2day,
                "w3day": self.w3day,
                "w4day": self.w4day,
                "active_status": self.active_status,
                "schedule_notes": self.schedule_notes,
                "last_visit": self.last_visit,
                "last_merch_form": self.last_merch_form,
                "last_po": self.last_po,
                "last_updated": self.last_updated,
                "_id": self._id
                }

    def delete(self):
        Database.remove(AccountConstants.COLLECTION, {'_id': self._id})

    def save_to_mongo(self):
        Database.update(AccountConstants.COLLECTION, {'_id': self._id}, self.json())