import abc

from abc import ABC, abstractmethod
from ..database.db_config import async_session_maker


class AbstractRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def add_one(self, obj):
        raise NotImplemented()

    @abc.abstractmethod
    def get_one(self, obj, primary_key):
        raise NotImplemented()

    @abc.abstractmethod
    def delete_one(self, obj):
        raise NotImplemented()

    @abc.abstractmethod
    def mark_as_delete(self, obj):
        raise NotImplemented()

    @abc.abstractmethod
    def get_all_by_filter(self, obj, filter_condition):
        raise NotImplemented()


class SQLAlchemyRepository(AbstractRepository):
    def __init__(self, session: async_session_maker, model_class):
        self.session = session
        self.model_class = model_class

    def add_one(self, obj):
        self.session.add(obj)

    def delete_one(self, obj):
        self.session.delete(obj)

    def get_one(self, obj, primary_key):
        return self.session.querry(self.model_class).get(primary_key)

    def mark_as_delete(self, obj):
        obj.is_delete = True

    def get_all_by_filter(self, obj, filter_condition):
        return self.session.querry(self.model_class).filter(filter_condition).all()
