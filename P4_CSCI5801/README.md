# P3 - Group 15

Initial submission for Implementation and Testing for PPALMS system (problem generation NOT developed yet)

### Prerequisites

Requirements for the software and other tools to run and test from the command line:
- [Python3](https://realpython.com/installing-python/)
- [Tkinter](https://realpython.com/python-gui-tkinter/)

### Installing

Download/unzip/extract/clone P4_CSCI5801 folder/directory and all contents

Make sure you have python3 and tkinter installed

Navigate cwd to P4_CSCI5801

From shell, compile and run project with python3

    shell>> python3 -i .\splitclass.py
    
OR run the executable for splitclass, located at dist/splitclass.exe

### Steps to use PPALMS

Follow directions as they appear on the UI

1. User starts PPLALMS application. ‘Exit’ will close out of the entire program. ‘Start’ will launch the next step of the PPALMS process.
  ![step1](https://user-images.githubusercontent.com/88807091/207693077-016c9254-09c3-4266-a04c-2b7a8e1ca74b.png)

2. User has pressed the ‘Start’ button. PPALMS now requires a filepath and a name to give the process (this will be the name of the source code, solution code, and solution code folder)
(*Note: When running the program, you must include the full file directory path (from root) to the file you would like to import.*)

  ![image](https://user-images.githubusercontent.com/114303423/204431089-f730c14b-5811-4757-a539-c130b951a855.png)
  
3. Enter valid destination filepath and desired process name for the solution code

  ![step3](https://user-images.githubusercontent.com/88807091/207693038-7d3840db-27b9-4e21-b068-afab3a924f3b.png)

 
4. Successful import and display of source code file contents

  ![step4](https://user-images.githubusercontent.com/88807091/207693000-b1b26726-2246-4cec-9af8-2becd8485456.png)

  
5. After clicking the ‘Include/Exclude Lines’ button, PPALMS is ready for the user to begin entering lines for inclusion or exclusion

  ![step5](https://user-images.githubusercontent.com/88807091/207692967-15f04d33-4d60-4c99-a2dc-2d5c98728d02.png)

  
6. Lines 0 through 5 are added for inclusion

  ![step6](https://user-images.githubusercontent.com/88807091/207692919-3bfe283b-8a06-458e-b61c-b4d98db065e0.png)

  
7. Lines 5 through 9 are excluded (the entire reverse_string method)

  ![step7](https://user-images.githubusercontent.com/88807091/207692875-a3aa4fe5-d0d8-42b8-9d25-dda6c92bfb85.png)

  
8. Excluded lines have been removed from the source code file. PPALMS is ready for the user to begin entering lines for tuples

   ![step8](https://user-images.githubusercontent.com/88807091/207692819-bcafc6cc-4a01-49aa-83c8-197ecb3c9659.png)

   
9. User creates tuple (1,2)

   ![step9](https://user-images.githubusercontent.com/88807091/207692787-3f530520-3fed-45be-9c43-4c15ff105eaa.png)

   
10. User selects ‘blackboard’ as their LMS

   ![step10](https://user-images.githubusercontent.com/88807091/207692754-0f62432a-5770-43e1-b66b-51898356a04d.png)

    
11. User select multiple choice from the list of available qTypes

   ![step11](https://user-images.githubusercontent.com/88807091/207692697-02433854-be4a-4e15-8132-da374274f4ad.png)


12. Preparatory process is complete

   ![step12](https://user-images.githubusercontent.com/88807091/207692633-60be324a-2022-4715-bb00-9a484247dba5.png)


## Running the tests

A file named `testcase_1.py` is provided to execute unit tests for the system. Its output is printed to the terminal and an output text file called `test_output.txt`

From your terminal, compile and execute testcase_1.py

       shell>> python3 .\testcase_1.py
       
Note: -i isn't necessary for testing because interaction with the UI is not part of our unit tests

See test results in terminal or open `test_output.txt`.

### Test Case Documentation

The **Test_Attempt_Import** class tests the attempt_import function from the PPALMS_BACKEND class in splitclass.py. The results are dependent on the values of atrr_nameQuery and filenameQuery, so these conditions are changed among the various tests

True upon fully sucessful import of file and process involved. 

False if:
-  Imported file contains non-ASCII character(s)
-  FileNotFound error is raised
-  Unexpected error occurs while reading the lines from the open file


        
The **Test_In_Ex_Lines** class tests the in_ex_lines function from the PPALMS_BACKEND class in splitclass.py. The results are dependent on the values of lower, upper, in_ex, and length, so these conditions are changed among the various tests

True upon both user-entered parameters are valid and the line lists are successfully updated.
                
False if:
- One or both fields are empty
- Upper is less than Lower / Lower is greater than Upper
- Lower is negative, greater than the number of lines in the file, or is not an integer
- Upper is negative, greater than the number of lines in the file, or is not an integer
- One or both fields are empty



            
The **Test_Remove_Lines** class tests the remove_lines function from the PPALMS_BACKEND class in splitclass.py. The results are dependent on the values of attr_nameQuery, filenameQuery, and name, so these conditions are changed among the various tests

True upon successful opening of the source code and updating the lines to be included.

False if:
- FileNotFound error is raised

            
The **Test_Select_Lines** class tests the select_lines function from the PPALMS_BACKEND class in splitclass.py. The results are dependent on the values of attr_nameQuery and filenameQuery, so these conditions are changed among the various tests

True upon fully successful opening of the source code file and reading the lines for display.

False if:
- FileNotFound error is raised
-  Unexpected error occurs while reading the lines from the open file

            
The **Test_Make_Tuple** class tests the make_tuple function from the PPALMS_BACKEND class in splitclass.py. The results are dependent on the values of first, second, and length, so these conditions are changed among the various tests

True if the tuple is valid. If tuple is already in self.tuples it will not add a duplicate but return True.

False if:
- One or both fields are empty
- second is less than first / first is greater than second
- first is negative, greater than the number of lines in the file, or is not an integer
- second is negative, greater than the number of lines in the file, or is not an integer
- first and second are not adjacent (the difference between them must be exactly 1)
   
    
            
The **Test_Tuple_Lines** class tests the tuple_lines function from the PPALMS_BACKEND class in splitclass.py. The results are dependent on the values of attr_nameQuery, filenameQuery, and name, so these conditions are changed among the various tests

True if the solution code folder and file are created successfully.

False if:
- A folder in the solution code folder already exists under the name the user provided
-  Error in creating solution code file
-  Error in opening source code file
    


            
The **Test_Choice_Made** class tests the choice_made function from the PPALMS_BACKEND class in splitclass.py. The results are dependent on the values of attr_nameQuery, filenameQuery, LMS_choice, mode, and options, so these conditions are changed among the various tests

True if the user makes a valid selection (either LMS or qType)

False if:
- the choice the user made is not valid (not in the LMS or qType options available)
-  mode parameter is not 'LMS' or 'qType'

   
   
            
The **Test_QType_Select** class tests the qType_select function from the PPALMS_BACKEND class in splitclass.py. 

True if the user makes a valid LMS selection

False if:
- LMS_choice is not valid


            
The **Test_Create_Config_File** class tests the create_config_file function from the PPALMS_BACKEND class in splitclass.py. This class has multiple tests that check to see if the configuration file is created as well as if the configuration file has the correct contents.
    
True upon fully sucessful creation of configuration file. 

False if:
- FileNotFound error is raised

   



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

