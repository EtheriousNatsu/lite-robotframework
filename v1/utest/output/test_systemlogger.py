#!/usr/bin/env python
# encoding: utf-8


"""
@version: 2.7
@author: 'john'
@time: 2017/10/4 下午11:12
@contact: zhouqiang847@gmail.com
"""

import unittest
from robot.output.systemLogger import _FileLogger
from StringIO import StringIO
from robot import utils
from robot.utils.asserts import *




class TestSystemFileLogger(unittest.TestCase):

    def setUp(self):
        _FileLogger._get_writer = lambda *args: StringIO()
        self.logger = _FileLogger('whatever', 'INFO')
        utils.robottime._current_time = (2006, 6, 13, 8, 37, 42, 123)

    def tearDown(self):
        utils.robottime._current_time = None

    def test_write(self):
        self.logger.write('my message')
        expected = '20060613 08:37:42.123 | INFO  | my message\n'
        assert_equal(self.logger._writer.getvalue(), expected)
        self.logger.write('my 2nd msg\nwith 2 lines', 'ERROR')
        expected += '20060613 08:37:42.123 | ERROR | my 2nd msg\nwith 2 lines\n'
        assert_equal(self.logger._writer.getvalue(), expected)

    def test_write_helpers(self):
        self.logger.info('my message')
        expected = '20060613 08:37:42.123 | INFO  | my message\n'
        assert_equal(self.logger._writer.getvalue(), expected)
        self.logger.warn('my 2nd msg\nwith 2 lines')
        expected += '20060613 08:37:42.123 | WARN  | my 2nd msg\nwith 2 lines\n'
        assert_equal(self.logger._writer.getvalue(), expected)

    def test_set_level(self):
        self.logger.write('msg', 'DEBUG')
        assert_equals(self.logger._writer.getvalue(), '')
        self.logger.set_level('DEBUG')
        self.logger.write('msg', 'DEBUG')
        assert_equals(self.logger._writer.getvalue(), '20060613 08:37:42.123 | DEBUG | msg\n')


if __name__ == '__main__':
    unittest.main()