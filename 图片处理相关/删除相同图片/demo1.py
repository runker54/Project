#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date:2021-01-25
# Author:Runker54
# -----------------------
import unittest
import os
import sys
import main


class TestMethods(unittest.TestCase):

    def setUp(self):
        self.directory = r'C:\Users\65680\Desktop\test2'

    def test_imgs_len(self):
        length = len(os.listdir(self.directory))
        imgs = main.collect_imgs(self.directory)
        self.assertEqual(len(imgs), length)
        imgs = main.detect_features(imgs)
        self.assertEqual(len(imgs), length)

    def test_duplicates_found(self):
        imgs = main.collect_imgs(self.directory)
        imgs = main.detect_features(imgs)
        duplicates = main.similarity_check(imgs)
        self.assertEqual(duplicates, [r'C:\Users\65680\Desktop\test\road_duplicate.jpg'])


if __name__ == '__main__':
    unittest.main()
