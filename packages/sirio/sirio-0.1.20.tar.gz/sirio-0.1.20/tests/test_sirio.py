#!/usr/bin/env python

"""Tests for `sirio` package."""


import unittest

from sirio import event

from sirio.business_object import BusinessObject, Object

url_sirio_get_business_object = 'https://sirio-engine-backend.srv-test.eu-central-1.aws.cervedgroup.com/sirio/enginebackend/businessobjects/{businessKey}'
url_sirio_complete = 'https://sirio-engine-backend.srv-test.eu-central-1.aws.cervedgroup.com/sirio/enginebackend/processes/domains/{domain}/tasks/{taskId}'
bo = BusinessObject('67063d15abcaec5dc6e87bb9',url_sirio_get_business_object, url_sirio_complete)
testJson = {'a':'paskA','b':'paskB'}
obj = Object('TEST-PASK','pask', extension='json')
obj.createByJson(testJson)
bo.uploadObject(obj)
bo.complete('ir4','6316d202-ba63-4785-84ac-a0415e44177e')

class TestSirio(unittest.TestCase):
    """Tests for `sirio` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""
