# -*- coding: utf-8 -*-
"""Unit test suite for the models of the application."""
from polaris_core.model import DBSession
from polaris_core.tests import load_app
from polaris_core.tests import setup_db, teardown_db

__all__ = ['ModelTest']


def setup_module():
    """Setup test fixture for all model tests."""
    load_app()
    setup_db()


def teardown_module():
    """Tear down test fixture for all model tests."""
    teardown_db()


class ModelTest(object):
    """Base unit test case for the models."""

    klass = None
    attrs = {}

    def setup_method(self, method):
        """Setup test fixture for each model test method."""
        try:
            new_attrs = {}
            new_attrs.update(self.attrs)
            new_attrs.update(self.do_get_dependencies())
            self.obj = self.klass(**new_attrs)
            DBSession.add(self.obj)
            DBSession.flush()
            return self.obj
        except:
            DBSession.rollback()
            raise

    def teardown_method(self, method):
        """Tear down test fixture for each model test method."""
        DBSession.rollback()

    def do_get_dependencies(self):
        """Get model test dependencies.

        Use this method to pull in other objects that need to be created
        for this object to be build properly.

        """
        return {}

    def test_create_obj(self):
        """Model objects can be created"""
        pass

    def test_query_obj(self):
        """Model objects can be queried"""
        obj = DBSession.query(self.klass).one()
        for key, value in self.attrs.items():
            assert getattr(obj, key) == value
