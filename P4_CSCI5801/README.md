# P3 - Group 15

Initial submission for Implementation and Testing for PPALMS system (problem generation NOT developed yet)

### Prerequisites

Requirements for the software and other tools to run and test
- [Python3](https://realpython.com/installing-python/)
- [Tkinter](https://realpython.com/python-gui-tkinter/)

### Installing

Download/unzip/extract P4_CSCI5801 folder/directory and all contents

Make sure you have python3 and tkinter installed

Navigate cwd to P4_CSCI5801

From shell, compile and run project with python3

    shell>> python3 -i .\splitclass.py

Follow directions as they appear on the UI

  ![image](https://user-images.githubusercontent.com/114303423/204431089-f730c14b-5811-4757-a539-c130b951a855.png)

Successful completion should look similar to the following:

 ![image](https://user-images.githubusercontent.com/100863839/204441088-7b75fdc5-38de-4dd3-ab18-79c65e045d6b.png)

## Running the tests

A file named `testcase_1.py` is provided to execute unit tests for the system. It's output is printed to the terminal and an output text file called `test_output.txt`

From your terminal, compile and execute testcase_1.py

       shell>> python3 .\testcase_1.py
       
Note: -i isn't necessary for testing because interaction with the UI is not part of our unit tests

See test results in terminal or open `test_output.txt`.

### Sample Tests

The **Test_Attempt_Import** class tests the attempt_import function from the PPALMS_BACKEND class in splitclass.py. The results are dependent on the values of atrr_nameQuery and filenameQuery, so these conditions are changed among the various tests

True upon fully sucessful import of file and process involved. 

False if:
    - Imported file contains non-ASCII character(s)
    - FileNotFound error is raised
    - Unexpected error occurs while reading the lines from the open file

    class Test_Attempt_Import(unittest.TestCase):
        def test(self):
            ____.ui.attr_nameQuery = 'test1a'
            ____.ui.filenameQuery = './testcase_files/addNums.cc'
            self.assertEqual(____.attempt_import(), [Expected Output], "Should be [Expect Output]")
        
The **Test_In_Ex_Lines** class tests the in_ex_lines function from the PPALMS_BACKEND class in splitclass.py. The results are dependent on the values of lower, upper, in_ex, and length, so these conditions are changed among the various tests

True upon both user-entered parameters are valid and the line lists are successfully updated.
                
False if:
     - One or both fields are empty
     - Upper is less than Lower / Lower is greater than Upper
     - Lower is negative, greater than the number of lines in the file, or is not an integer
     - Upper is negative, greater than the number of lines in the file, or is not an integer

    class Test_In_Ex_Lines(unittest.TestCase):
        def test(self):
            self.assertEqual(____.in_ex_lines([lower test value],[upper test value],[Include or Exclude],[length test value]), [Expected Output], "Should be [Expected Output]")
            
The **Test_Remove_Lines** class tests the remove_lines function from the PPALMS_BACKEND class in splitclass.py. The results are dependent on the values of attr_nameQuery, filenameQuery, and name, so these conditions are changed among the various tests

True upon successful opening of the source code and updating the lines to be included.

False if:
    - FileNotFound error is raised

    class Test_Remove_Lines(unittest.TestCase):
        def test(self):
            ____.ui.attr_nameQuery = 'test3a'
            ____.name = 'helloworld.js'
            ____.ui.filenameQuery = './testcase_files/helloworld.js'
            self.assertEqual(back.remove_lines(), [Expected Output], "Should be [Expected Output]")
            
The **Test_Select_Lines** class tests the select_lines function from the PPALMS_BACKEND class in splitclass.py. The results are dependent on the values of attr_nameQuery and filenameQuery, so these conditions are changed among the various tests

True upon fully successful opening of the source code file and reading the lines for display.

False if:
    - FileNotFound error is raised
    - Unexpected error occurs while reading the lines from the open file

    class Test_Select_Lines(unittest.TestCase):
        def test(self):
            ____.ui.attr_nameQuery = 'test4a'
            ____.ui.filenameQuery = './testcase_files/exampleocaml.ml.ml'

            self.assertEqual(back.select_lines(), [Expected Output], "Should be [Expected Output]")
            
The **Test_Make_Tuple** class tests the make_tuple function from the PPALMS_BACKEND class in splitclass.py. The results are dependent on the values of first, second, and length, so these conditions are changed among the various tests

True if the tuple is valid. If tuple is already in self.tuples it will not add a duplicate but return True.

False if:
    - One or both fields are empty
    - second is less than first / first is greater than second
    - first is negative, greater than the number of lines in the file, or is not an integer
    - second is negative, greater than the number of lines in the file, or is not an integer
    - first and second are not adjacent (the difference between them must be exactly 1)
    
    class Test_Make_Tuple(unittest.TestCase):
        back.ui.attr_nameQuery = 'test5'
        back.ui.filenameQuery = './testcase_files/examples.py'
        def test(self):
            self.assertEqual(back.make_tuple([lower test value], [upper test value], [length test value]), [Expected Output], "Should be [Expected Output]")
            
The **Test_Tuple_Lines** class tests the tuple_lines function from the PPALMS_BACKEND class in splitclass.py. The results are dependent on the values of attr_nameQuery, filenameQuery, and name, so these conditions are changed among the various tests

True if the solution code folder and file are created successfully.

False if:
    - A folder in the solution code folder already exists under the name the user provided
    - Error in creating solution code file
    - Error in opening source code file
    
    class Test_Tuple_Lines(unittest.TestCase):
        def test(self):
            ____.ui.attr_nameQuery = 'test6a'
            ____.ui.filenameQuery = './testcase_files/examplewcss.html'
            ____.name = 'examplewcss.html'
            self.assertEqual(back.tuple_lines(), [Expected Output], "Should be [Expected Output]")
            
The **Test_Choice_Made** class tests the choice_made function from the PPALMS_BACKEND class in splitclass.py. The results are dependent on the values of attr_nameQuery, filenameQuery, LMS_choice, mode, and options, so these conditions are changed among the various tests

True if the user makes a valid selection (either LMS or qType)

False if:
    - the choice the user made is not valid (not in the LMS or qType options available)
    - mode parameter is not 'LMS' or 'qType'

    class Test_Choice_Made(unittest.TestCase):
        def test(self):
            back.ui.attr_nameQuery = 'test7a'
            back.ui.filenameQuery = './testcase_files/primeNum.cc'
            back.LMS_choice = 'canvas'
            self.assertEqual(back.choice_made([mode test value], [option test value(s)]), [Expected Output], "Should be [Expected Output]")
            
The **Test_QType_Select** class tests the qType_select function from the PPALMS_BACKEND class in splitclass.py. The results are dependent on the values of attr_nameQuery, filenameQuery, LMS_choice, and qType_choice, so these conditions are changed among the various tests

True if the user makes a valid qType (question type) selection

False if:
    - LMS_choice is not valid
    
    class Test_QType_Select(unittest.TestCase):
        def test(self):
            ____.ui.attr_nameQuery = 'test8a'
            ____.ui.filenameQuery = './testcase_files/primeNum.cc'
            ____.LMS_choice = 'blackboard'
            self.assertEqual(back.qType_select(), [Expected Output], "Should be [Expected Output]")
            
The **Test_Create_Config_File** class tests the create_config_file function from the PPALMS_BACKEND class in splitclass.py. The results are dependent on the values of attr_nameQuery, filenameQuery, LMS_choice, qType_choice, tuples, and sol_folder_name so these conditions are changed among the various tests
    
True upon fully sucessful creation of file and process involved. 

False if:
    - FileNotFound error is raised
    
    class Test_Create_Config_File(unittest.TestCase):
        def test(self):
            ____.tuples = [(1,2),(3,4)]
            ____.sol_folder_name = 'primeNum'
            ____.qType_choice = 'indentation'
            ____.LMS_choice = 'canvas'
            ____.ui.attr_nameQuery = 'test9a'
            ____.ui.filenameQuery = './testcase_files/primeNum.cc'

            self.assertEqual(back.create_config_file(), [Expected Output], "Should be [Expected Output]")


## Built With

  - Visual Studio Code
  - Google Drive
  - Discord

## Versioning

Current Version: v0.1

## Authors

  - **Christine Brennan**
  - **Omonigho Egi**
  - **Audrey Gasser**
  - **Katie Scheck**

  - **Billie Thompson** - *Provided README Template* -
    [PurpleBooth](https://github.com/PurpleBooth)

See also the list of
[contributors](https://github.com/PurpleBooth/a-good-readme-template/contributors)
who participated in this (the README Template) project.

## Acknowledgments

  - Hat tip to [StackOverflow](https://stackoverflow.com/questions/45956128/save-unittest-results-in-text-file)

