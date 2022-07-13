import os
import sys
import unittest
from unittest import loader

from unit_tests.service.account import TestAccount
from unit_tests.service.content import TestContent
from unit_tests.service.income import TestIncome
from unit_tests.service.profile import TestProfile
from unit_tests.service.user import TestUser
from unit_tests.service.work_platfrom import TestWorkPlatform

sys.path.append(os.path.realpath('.'))


def suite():
    test_classes = [TestAccount, TestUser, TestContent, TestIncome, TestWorkPlatform, TestProfile]

    ut_suite = unittest.TestSuite()
    for test_class in test_classes:
        tests = loader.TestLoader().loadTestsFromTestCase(test_class)
        ut_suite.addTests(tests)
    return ut_suite


if __name__ == '__main__':
    try:
        runner = unittest.TextTestRunner()
        response = runner.run(suite())
        if len(response.errors) != 0 or len(response.failures) != 0:
            raise Exception('Unit Test Cases Failed')
    except Exception as e:
        raise e
