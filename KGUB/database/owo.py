import threading
from sqlalchemy import Column
from . import BASE, SESSION
from sqlalchemy.sql.sqltypes import BigInteger


class OwO(BASE):
    __tablename__ = "approval"
    user_id = Column(BigInteger, primary_key=True)
    balance = Column(BigInteger, primary_key=False, default=0)

    def __init__(self, user_id):
        self.user_id = user_id
        self.balance = 0

    def __repr__(self):
        return "<OwO %s>" % self.user_id


OwO.__table__.create(checkfirst=True)

OWO_INSERTION_LOCK = threading.RLock()


def get_balance(user_id):
    try:
        return SESSION.query(OwO).get(user_id)
    finally:
        SESSION.close()


def update_balance(user_id, balance):
    with OWO_INSERTION_LOCK:
        owo_user = OwO(user_id, balance)
        SESSION.add(owo_user)
        SESSION.commit()


def add_user(user_id):
    with OWO_INSERTION_LOCK:
        owo_user = OwO(user_id)
        SESSION.add(owo_user)
        SESSION.commit()


def is_user(user_id):
    try:
        return SESSION.query(OwO).get(user_id)
    finally:
        SESSION.close()
