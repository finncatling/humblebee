#!/usr/bin/env python
#
#  XXX  Identifying information about tests here.
#
#===============
#  This is based on a skeleton test file, more information at:
#
#     https://github.com/linsomniac/python-unittest-skeleton

raise NotImplementedError('To customize, remove this line and '
        'customize where it says XXX')

import unittest

class test_XXX_Test_Group_Name(unittest.TestCase):
    @classmethod
    def setUp(self):
        ###  XXX code to do setup
        pass

    def tearDown(self):
        ###  XXX code to do tear down
        pass

    def test_XXX_Test_Name(self):
        raise NotImplementedError('Insert test code here.')
        #  Examples:
        # self.assertEqual(fp.readline(), 'This is a test')
        # self.assertFalse(os.path.exists('a'))
        # self.assertTrue(os.path.exists('a'))
        # self.assertTrue('already a backup server' in c.stderr)
        # with self.assertRaises(Exception):
        #    raise Exception('test')
        # self.assertIn('fun', 'disfunctional')

unittest.main()
