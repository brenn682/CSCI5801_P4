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
        back.ui.attr_nameQuery = 'test1a'
        back.ui.filenameQuery = './testcase_files/addNums.cc'
        self.assertEqual(back.attempt_import(), True, "Should be true")
    
    def test_non_ascii(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test1b'
        back.ui.filenameQuery = './testcase_files/slick.bin'
        self.assertEqual(back.attempt_import(), False, "Should be false")

    def test_file_not_found(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test1c'
        back.ui.filenameQuery = './testcase_files/file_DNE.py'
        self.assertEqual(back.attempt_import(), False, "Should be false")

class Test_In_Ex_Lines(unittest.TestCase):
    process = PPALMS()
    back = process.backend
    back.ui.attr_nameQuery = 'test2'
    back.ui.filenameQuery = './testcase_files/examplehtml.html'

    def test_good(self):
        # set conditions here
        self.assertEqual(back.in_ex_lines(1,2,'Include',10), True, "Should be true")
    
    def test_empty_field(self):
        # set conditions here
        self.assertEqual(back.in_ex_lines('',2,'Include',10), False, "Should be False")

    def test_up_ld_low(self):
        # set conditions here
        self.assertEqual(back.in_ex_lines(2,1,'Include',10), False, "Should be False")

    def test_low_oob(self):
        # set conditions here
        self.assertEqual(back.in_ex_lines(-1,2,'Include',10), False, "Should be False")

    def test_high_oob(self):
        # set conditions here
        self.assertEqual(back.in_ex_lines(1,11,'Include',10), False, "Should be False")

class Test_Remove_Lines(unittest.TestCase):
    process = PPALMS()
    back = process.backend
    
    def test_good(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test3a'
        back.ui.filenameQuery = './testcase_files/helloworld/js'

        self.assertEqual(back.remove_lines(), True, "Should be true")
    
    def test_file_not_found(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test3b'
        back.ui.filenameQuery = './testcase_files/file_DNE.py'
        self.assertEqual(back.remove_lines(), False, "Should be False")

class Test_Select_Lines(unittest.TestCase):
    process = PPALMS()
    back = process.backend
    
    def test_good(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test4a'
        back.ui.filenameQuery = './testcase_files/exampleocaml.ml.ml'

        self.assertEqual(back.select_lines(), True, "Should be true")
    
    def test_file_not_found(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test4b'
        back.ui.filenameQuery = './testcase_files/file_DNE.py'
        self.assertEqual(back.select_lines(), False, "Should be False")

class Test_Make_Tuple(unittest.TestCase):
    process = PPALMS()
    back = process.backend
    back.ui.attr_nameQuery = 'test5'
    back.ui.filenameQuery = './testcase_files/examples.py'
    
    def test_good(self):
        # set conditions here
        self.assertEqual(back.make_tuple(2, 3, 32), True, "Should be true")
    
    def test_empty_field(self):
        # set conditions here
        self.assertEqual(back.make_tuple('', 14, 32), False, "Should be False")

    def test_snd_ld_fst(self):
        # set conditions here
        self.assertEqual(back.make_tuple(18, 17, 32), False, "Should be False")

    def test_fst_oob(self):
        # set conditions here
        self.assertEqual(back.make_tuple(-1, 0, 32), False, "Should be False")

    def test_snd_oob(self):
        # set conditions here
        self.assertEqual(back.make_tuple(31, 32, 32), False, "Should be False")

    def test_adj_error(self):
        # set conditions here
        self.assertEqual(back.make_tuple(5, 7, 32), False, "Should be False")

class Test_Tuple_Lines(unittest.TestCase):
    process = PPALMS()
    back = process.backend
    
    def test_good(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test6a'
        back.ui.filenameQuery = './testcase_files/primeNum.cc'

        self.assertEqual(back.tuple_lines, True, "Should be true")
    
    def test_os_error(self):
        # set conditions here
        back.ui.attr_nameQuery = 'boink'
        back.ui.filenameQuery = './testcase_files/primeNum.cc'
        self.assertEqual(back.tuple_lines(), False, "Should be False")

    def test_file_not_found_source(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test6c'
        back.ui.filenameQuery = './testcase_files/file_DNE.py'
        self.assertEqual(back.tuple_lines(), False, "Should be False")

    def test_file_not_found_solution(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test6d'
        back.ui.filenameQuery = './solution_code/file_DNE/file_DNE.py'
        self.assertEqual(back.tuple_lines(), False, "Should be False")

class Test_Choice_Made(unittest.TestCase):
    process = PPALMS()
    back = process.backend
    
    def test_LMS_good(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test7a'
        back.ui.filenameQuery = './testcase_files/primeNum.cc'
        back.LMS_choice = 'canvas'
        self.assertEqual(back.choice_made('LMS', []), True, "Should be true")

    def test_qType_good(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test7b'
        back.ui.filenameQuery = './testcase_files/primeNum.cc'
        back.LMS_choice = 'canvas'
        back.qType_choice = 'multiple choice'
        sample_options = ['multiple choice','reordering','fill-in-the-blank','find the bug','indentation']
        self.assertEqual(back.choice_made('qType', sample_options), True, "Should be true")
    
    def test_LMS_choice_invalid(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test7c'
        back.ui.filenameQuery = './testcase_files/primeNum.cc'
        back.LMS_choice = 'wrong_option' # erroneous
        self.assertEqual(back.choice_made('LMS', []), False, "Should be False")

    def test_qType_choice_invalid(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test7d'
        back.ui.filenameQuery = './testcase_files/primeNum.cc'
        sample_options = ['multiple choice','reordering','fill-in-the-blank','find the bug','indentation']
        back.LMS_choice = 'moodle'
        back.qType_choice = 'invalid_option' # erroneous
        self.assertEqual(back.choice_made('qType', sample_options), False, "Should be False")

    def test_mode_parameter_invalid(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test7e'
        back.ui.filenameQuery = './testcase_files/primeNum.cc'
        sample_options = ['multiple choice','reordering','fill-in-the-blank','find the bug','indentation']
        back.LMS_choice = 'moodle'
        back.qType_choice = 'reordering'
        # 'mode3' is erroneous
        self.assertEqual(back.choice_made('mode3', sample_options), False, "Should be False")

class Test_QType_Select(unittest.TestCase):
    process = PPALMS()
    back = process.backend
    
    def test_good(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test8a'
        back.ui.filenameQuery = './testcase_files/primeNum.cc'
        back.LMS_choice = 'blackboard'
        self.assertEqual(back.qType_select(), True, "Should be true")
    
    def test_LMS_invalid(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test8b'
        back.ui.filenameQuery = './testcase_files/primeNum.cc'
        back.LMS_choice = 'oops'
        self.assertEqual(back.qType_select(), False, "Should be False")

class Test_Create_Config_File(unittest.TestCase):
    process = PPALMS()
    back = process.backend
    back.tuples = [(1,2),(3,4)]
    back.sol_folder_name = 'primeNum'
    back.qType_choice = 'indentation'
    back.LMS_choice = 'canvas'
    
    def test_good(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test9a'
        back.ui.filenameQuery = './testcase_files/primeNum.cc'

        self.assertEqual(back.create_config_file(), True, "Should be true")
    
    def test_file_not_found(self):
        # set conditions here
        back.ui.attr_nameQuery = 'test9b'
        back.ui.filenameQuery = './testcase_files/file_DNE.py'
        self.assertEqual(back.create_config_file(), False, "Should be False")

if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()
