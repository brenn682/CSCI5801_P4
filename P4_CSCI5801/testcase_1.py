import tkinter
from tkinter import *  # GUI module
import tkinter.scrolledtext as scrolledtext
from tkinter import ttk, messagebox, Label, Button
import unittest
import os
import splitclass

class Test_Attempt_Import(unittest.TestCase):
    process = PPALMS()
    back = process.backend

    
    def test_good(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test1'
        back.ui.filenameQuery = './test1.py'
        self.assertEqual(back.attempt_import(), True, "Should be true")
    
    def test_non_ascii(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test1'
        back.ui.filenameQuery = 'non_ascii.py'
        self.assertEqual(back.attempt_import(), False, "Should be true")

    def test_file_not_found(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test1'
        back.ui.filenameQuery = 'file_DNE.py'
        self.assertEqual(back.attempt_import(), False, "Should be true")

class Test_In_Ex_Lines(unittest.TestCase):
    process = PPALMS()
    back = process.backend

    
    def test_good(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test1'
        back.ui.filenameQuery = './test1.py'

        self.assertEqual(back.attempt_import(), True, "Should be true")
    
    def test_empty_field(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test1'
        back.ui.filenameQuery = 'non_ascii.py'
        self.assertEqual(back.attempt_import(), False, "Should be False")

    def test_up_ld_low(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test1'
        back.ui.filenameQuery = 'xkcd.py'
        self.assertEqual(back.attempt_import(), False, "Should be False")

    def test_low_oob(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test1'
        back.ui.filenameQuery = 'xkcd.py'
        self.assertEqual(back.attempt_import(), False, "Should be False")

    def test_high_oob(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test1'
        back.ui.filenameQuery = 'fisdfsd.py'
        self.assertEqual(back.attempt_import(), False, "Should be False")

class Test_Remove_Lines(unittest.TestCase):
    process = PPALMS()
    back = process.backend
    
    def test_good(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test1'
        back.ui.filenameQuery = './test1.py'

        self.assertEqual(back.attempt_import(), True, "Should be true")
    
    def test_file_not_found(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test1'
        back.ui.filenameQuery = 'file_DNE.py'
        self.assertEqual(back.attempt_import(), False, "Should be False")

class Test_Select_Lines(unittest.TestCase):
    process = PPALMS()
    back = process.backend
    
    def test_good(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test1'
        back.ui.filenameQuery = './test1.py'

        self.assertEqual(back.attempt_import(), True, "Should be true")
    
    def test_file_not_found(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test1'
        back.ui.filenameQuery = 'file_DNE.py'
        self.assertEqual(back.attempt_import(), False, "Should be False")

class Test_Make_Tuple(unittest.TestCase):
    process = PPALMS()
    back = process.backend
    
    def test_good(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test1'
        back.ui.filenameQuery = './test1.py'

        self.assertEqual(back.attempt_import(), True, "Should be true")
    
    def test_empty_field(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test1'
        back.ui.filenameQuery = 'file_DNE.py'
        self.assertEqual(back.attempt_import(), False, "Should be False")

    def test_snd_ld_fst(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test1'
        back.ui.filenameQuery = 'file_DNE.py'
        self.assertEqual(back.attempt_import(), False, "Should be False")

    def test_fst_oob(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test1'
        back.ui.filenameQuery = 'file_DNE.py'
        self.assertEqual(back.attempt_import(), False, "Should be False")

    def test_snd_oob(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test1'
        back.ui.filenameQuery = 'file_DNE.py'
        self.assertEqual(back.attempt_import(), False, "Should be False")

    def test_adj_error(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test1'
        back.ui.filenameQuery = 'file_DNE.py'
        self.assertEqual(back.attempt_import(), False, "Should be False")

class Test_Tuple_Lines(unittest.TestCase):
    process = PPALMS()
    back = process.backend
    
    def test_good(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test1'
        back.ui.filenameQuery = './test1.py'

        self.assertEqual(back.attempt_import(), True, "Should be true")
    
    def test_os_error(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test1'
        back.ui.filenameQuery = 'file_DNE.py'
        self.assertEqual(back.attempt_import(), False, "Should be False")

    def test_file_not_found_source(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test1'
        back.ui.filenameQuery = 'file_DNE.py'
        self.assertEqual(back.attempt_import(), False, "Should be False")

    def test_file_not_found_solution(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test1'
        back.ui.filenameQuery = 'file_DNE.py'
        self.assertEqual(back.attempt_import(), False, "Should be False")

class Test_Choice_Made(unittest.TestCase):
    process = PPALMS()
    back = process.backend
    
    def test_good(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test1'
        back.ui.filenameQuery = './test1.py'

        self.assertEqual(back.attempt_import(), True, "Should be true")
    
    def test_choice_invalid(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test1'
        back.ui.filenameQuery = 'file_DNE.py'
        self.assertEqual(back.attempt_import(), False, "Should be False")

    def test_monde_parameter_invalid(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test1'
        back.ui.filenameQuery = 'file_DNE.py'
        self.assertEqual(back.attempt_import(), False, "Should be False")

class Test_QType_Select(unittest.TestCase):
    process = PPALMS()
    back = process.backend
    
    def test_good(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test1'
        back.ui.filenameQuery = './test1.py'

        self.assertEqual(back.attempt_import(), True, "Should be true")
    
    def test_LMS_invalid(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test1'
        back.ui.filenameQuery = 'file_DNE.py'
        self.assertEqual(back.attempt_import(), False, "Should be False")

class Test_QType_Select(unittest.TestCase):
    process = PPALMS()
    back = process.backend
    
    def test_good(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test1'
        back.ui.filenameQuery = './test1.py'

        self.assertEqual(back.attempt_import(), True, "Should be true")
    
    def test_file_not_found(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test1'
        back.ui.filenameQuery = 'file_DNE.py'
        self.assertEqual(back.attempt_import(), False, "Should be False")