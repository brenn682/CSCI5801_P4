# Group 15 PPALMS Driver Code
# Authors: Brennan, Egi, Gasser, Scheck

import tkinter
from tkinter import *  # GUI module
import tkinter.scrolledtext as scrolledtext
from tkinter import ttk, messagebox, Label, Button

import os

class UI(tkinter.Tk):
    '''
    Purpose: The User Interface for PPALMS, initializes with a PPALMS backend process in order to
            create the buttons for the interface
    Attributes: 
        lbl: process step instructions / context
        instr1: further instructions for filenameQuery box
        instr2: further instructions for attr_nameQuery box
        filenameQuery: stores user input 1
        attr_nameQuery: stores user input 2
        enter: 'execute' button
        enter2: second, optional execute button
        display: display textbox for user's code (source or solution)
        next_step: button to move on to next step in process (for tupling and line inclusion / exclusion
    Methods: 
        update_sys_msg: update the system message displayed on the right-side of the UI
        make_display: display imported source code, update source code, and solution code
        import_layout: create the UI for the import source code step
        line_time: create the UI for the line inclusion/exclusion step
        tuple_ui: create the UI for the line tupling step
        selection_ui: create the UI for LMS and qType selection
        numStudents_ui: create the UI for entering the number of students to generate the set for
        finish_ui: displays the finishing message and clears the process (if you select 'Start' the process can begin again!)
    '''

    def __init__(self, backend):

        super().__init__()

        self.backend = backend
        
        # Add widgets here
        self.title("THE PPALMS GUI")

        self.label = Label(self, text="Welcome to PPALMS! To make a new Problem Set, click 'Start'!")
        self.label.pack()
        
        self.greet_button = Button(self, text="Start", command=self.import_layout)
        self.greet_button.pack()
        
        self.close_button = Button(self, text="Exit PPALMS", command=self.destroy)
        self.close_button.pack()

        # UI ELEMENTS
        self.lbl = ''
        self.instr1 = ''
        self.instr2 = ''
        self.filenameQuery = ''
        self.attr_nameQuery = ''
        self.enter = ''
        self.enter2 = ''
        self.display = ''
        self.next_step = ''
        self.numStudents = ''

        self.sys_msg = Label(self, text="System Messages and Errors will appear here", fg='red')
        self.sys_msg.place(x=360, y=90)
        
    def update_sys_msg(self, msg):
        self.sys_msg.config(text = msg)

    def make_display(self, display_text, update_bool):
        if update_bool == True:
            self.display.destroy()
        self.display = Text(self.backend.ui, wrap=WORD, width=70, height=20)
        self.display.insert(INSERT, display_text)
        self.display.place(x = 80, y = 220)

    def import_layout(self):
        self.lbl = Label(self, text="Enter File Path (1st Box) and new Source Code name (2nd Box):", fg='blue') # button widget
        self.lbl.place(x=10, y=90)

        self.instr1 = Label(self, text="Ex: /Desktop/foo.py")
        self.instr1.place(x=220,y=120)
        
        self.instr2 = Label(self, text="Ex: my_code.py")
        self.instr2.place(x=220,y=150)
        
        filename = tkinter.StringVar()
        self.filenameQuery = Entry(self, text="Enter the File Path to the Source Code you wish to Import", bd=5, textvariable = filename) # text entry widget
        self.filenameQuery.place(x=80, y=120)
        
        self.backend.name = tkinter.StringVar()
        self.attr_nameQuery = Entry(self, text="Enter the Name for the Source Code File", bd=5, textvariable = self.backend.name) # text entry widget
        self.attr_nameQuery.place(x=80, y=150)

        self.enter = Button(self, text="Import!", command=self.backend.attempt_import)
        self.enter.place(x = 80, y = 180)

    def line_time(self, length):
        self.lbl.destroy()
        self.lbl = Label(self, text="Enter Lower Bound (1st Box) and Upper Bound (2nd Box):", fg='blue') # button widget
        self.lbl.place(x=10, y=90)
    
        lower = tkinter.StringVar()
        self.filenameQuery.destroy()
        self.filenameQuery = Entry(self, text="lower bound", bd=5, textvariable = lower) # text entry widget
        self.filenameQuery.place(x=80, y=120)
        
        upper = tkinter.StringVar()
        self.attr_nameQuery.destroy()
        self.attr_nameQuery = Entry(self, text="upper bound", bd=5, textvariable = upper) # text entry widget
        self.attr_nameQuery.place(x=80, y=150)

        self.instr1.destroy()
        self.instr1 = Label(self, text="This must be less than upper bound")
        self.instr1.place(x=220,y=120)

        self.instr2.destroy()
        self.instr2 = Label(self, text="This must be greater than lower bound")
        self.instr2.place(x=220,y=150)
        try:
            self.next_step.destroy()
        except:
            pass
        self.next_step = Button(self, text="Create Tuples", command=self.backend.tuple_lines)
        self.next_step.place(x = 360, y = 180)

        self.enter.destroy()
        self.enter = Button(self, text="Include Lines", command=lambda: self.backend.in_ex_lines(lower.get(), upper.get(), 'Include', length))
        self.enter.place(x = 80, y = 180)

        try:
            self.enter2.destroy()
        except:
            pass
        self.enter2 = Button(self, text="Exclude Lines", command=lambda: self.backend.in_ex_lines(lower.get(), upper.get(), 'Exclude', length))
        self.enter2.place(x = 180, y = 180)

    def tuple_ui(self):
        self.lbl.destroy()
        self.lbl = Label(self, text="Enter Two Adjecent Line Numbers to 'tuple' them (tuples are only used in the question type 'reordering):", fg='blue') # button widget
        self.lbl.place(x=10, y=90)
    
        first = tkinter.StringVar()
        self.filenameQuery.destroy()
        self.filenameQuery = Entry(self, text="First line # (lower bound)", bd=5, textvariable = first) # text entry widget
        self.filenameQuery.place(x=80, y=120)
        
        second = tkinter.StringVar()
        self.attr_nameQuery.destroy()
        self.attr_nameQuery = Entry(self, text="Second line # (upper bound)", bd=5, textvariable = second) # text entry widget
        self.attr_nameQuery.place(x=80, y=150)

        self.instr1.destroy()
        self.instr1 = Label(self, text="First line #")
        self.instr1.place(x=220,y=120)

        self.instr2.destroy()
        self.instr2 = Label(self, text="Second line #")
        self.instr2.place(x=220,y=150)

        self.enter.destroy()

        self.next_step.destroy()
        self.next_step = Button(self, text="LMS Selection", command=self.backend.LMS_select)
        self.next_step.place(x = 360, y = 180)

        self.enter.destroy()
        self.enter = Button(self, text="Include Tuple", command=lambda: self.backend.make_tuple(first.get(), second.get(), self.backend.sol_code_len))
        self.enter.place(x = 80, y = 180)
            
        self.enter2.destroy()

    def selection_ui(self, mode, options):
        options_text = ''
        try:
            self.next_step.destroy()
        except:
            pass
        if mode == 'LMS':
            try:
                self.backend.LMS_choice = tkinter.StringVar()
                self.lbl.config(text = "Type the LMS selection from the given options")
                #self.next_step.config(text="Question Type Selection", command=self.backend.qType_select)
                self.backend.LMS_choice = tkinter.StringVar()
                self.filenameQuery.config(textvariable=self.backend.LMS_choice)
            except: # no UI needs to be altered
                pass
        else:
            try:
                self.backend.qType_choice = tkinter.StringVar()
                self.lbl.config(text = "Type the Question Type selection from the given options")
                #self.next_step.config(text="Finish", command=self.finish_ui)
                self.backend.qType_choice = tkinter.StringVar()
                self.filenameQuery.config(textvariable=self.backend.qType_choice)
            except:
                pass

        for i in options:
            options_text+=i+' | '

        try: # in unit testing, these are ignored
            self.instr1.config(text=options_text)

            self.enter.config(text="Enter Selection", command=lambda: self.backend.choice_made(mode, options))
        except:
            pass

        try:
            self.instr2.destroy()
            self.attr_nameQuery.destroy()
        except:
            pass
        
    def numStudents_ui(self):

        try:
            self.next_step.destroy()
        except:
            pass

        self.update_sys_msg("Number of Students Selection: System Messages and \nErrors will appear here")

        self.backend.numStudents = tkinter.StringVar()
        try:
            self.lbl.config(text = "Input Number of Students")
        except:
            pass
        try:
            self.filenameQuery.config(textvariable=self.backend.numStudents)
        except:
            pass

        try: # in unit testing, these are ignored
            self.enter.config(text="Enter Selection", command=lambda: self.backend.numStudents_select)
        except:
            pass

        try:
            self.instr1.destroy()
        except:
            pass
        try:
            self.instr2.destroy()
        except:
            pass
        try:
            self.attr_nameQuery.destroy()
        except:
            pass
        try:
            self.enter.destroy()
        except:
            pass

        self.next_step = Button(self, text="Input Number of Students", command=self.backend.numStudents_select)
        self.next_step.place(x = 360, y = 180)
    
    def finish_ui(self): #display a celebratory message
        try:
            self.lbl.destroy()
            self.instr1.destroy()
            self.instr2.destroy()
            self.filenameQuery.destroy()
            self.attr_nameQuery.destroy()
            self.enter.destroy()
            self.enter2.destroy()
            self.display.destroy()
            self.next_step.destroy()
        except:
            pass
        self.update_sys_msg("PPALMS is now generating your problem set. :)")
        return True
##########################################################################
class PPALMS_BACKEND:
    '''
    Purpose: 
    Attributes: 
        name: the name of the PPALMS process (will be the name of the solution code, imported 
                source code and the solution code's folder.)
        sol_code_len: the number of lines in the solution code file.
        sol_folder_name: the name of the folder that the solution code will be saved in
        exclude: a list of integers. The lines to exclude from the source code when creating 
                the solution code.
        include: a list of integers. The lines to include in the source code when creating 
                the solution code. Is also used to 'undo' accidental line exclusions in the
                line selection step.
        tuples: a list of integer tuples. These are included in the solution code configuration file,
                which is located with the solution code in it's respective folder within the 
                solution_code folder.
        sol_code_indentation: a list of positive integers, representing the number of 'tabs' in the
                solution code. This is used for qType 'reordering'
        LMS_choice: the LMS selection, either Blackboard, Canvas, or Moodle
        qType_choie: the question type selection, depends on the LMS_choice
        
    Methods: 
        attempt_import: Attempts to open and import the file described by the user into the system's
                        source_code folder.
        in_ex_lines: Checks the validity of the user inputs for line inclusion/exclusion.
        remove_lines: Called when the user indicates they are done selecting
                    lines for inclusion and exclusion and updates the source code file
        select_lines: Displays the source code for the user such that the user may select lines
                    for tupling.
        make_tuple: Checks the validity of the user inputs for tuple-making.
                    If all parameters passed in are valid, a tuple is formed and
                    added to the process' tuple list.
        tuple_lines: Creates the Solution Code folder for the Source Code, the tuples chosen
                    are stored as a list of tuples in the Solution Code's configuration file.
        choice_made: validates that the LMS and qTypes chosen by the user in the UI are valid.
        LMS_select: Calls the ui for LMS (and qType) selection and records the user's chosen LMS.
        qType_select: Calls the ui for qType (and LMS) selection and records the user's chosen qType
        numStudents_select: Records the user's entered number of students to generate the problem set for.
        create_config_file: Creates a configuration file unique to each instance of the PPALMS prep process.
                        Format of the file is included in the method documentation, and is dependent on the qType
    '''
    def __init__(self):
        # super().__init__()

        # OUR USER INTERFACE
        self.ui = UI(self)  # create the UI and pass itself in so the UI can attach
                            # the PPALMS process commands/methods to buttons

        # PPALMS PROCESS ATTRIBUTES
        self.name = '' # source code file name (also will be solution code name)
        self.sol_code_len = 0 # number of lines in the solution code
        self.sol_folder_name = '' # the name of the folder in which the solution code and the config file will be in
        self.exclude = []
        self.include = []
        self.tuples = []
        self.sol_code_indentation = []
        self.LMS_choice = ''
        self.qType_choice = ''
        self.numStudents = ''

        # self.ppalms_qTypes = ['reordering','multiple choice','python indentation','find the bug','fill-in-the-blank']
        ''' PPALMS qTypes descriptions:
        reordering -- the order that the lines and tuples are correctly organized is changed (matching)
        mult. choice -- provide a # of incorrect 'mutant' answers for each line or tuple
        indentation -- python only, implemented as 2-D parson's problems
        find the bug -- the upload lines are replaced with mutants
        fill-in-the-blank -- one term (variable, operator, character) is removed from the line
        '''
        
    def attempt_import(self):
        '''
        Purpose: Attempts to open and import the file described by the user into the system.
                Source code files are stored under the user-specified name within the source_code
                folder in the PPALMS system folder.
        Return: True upon fully sucessful import of file and process involved.
                False if:
                    - Imported file contains non-ASCII character(s)
                    - FileNotFound error is raised
                    - Unexpected error occurs while reading the lines from the open file
        '''
        # Grab the entries from the user's boxes
        try: 
            filename = self.ui.filenameQuery.get()
            attr_name = self.ui.attr_nameQuery.get()  
        except:
            filename = self.ui.filenameQuery
            attr_name = self.ui.attr_nameQuery
        display_text = ''
        text_lines = []
        count = 1
        if filename == '' or attr_name == '':
            self.ui.update_sys_msg("Error: Both text boxes must have input data to continue")
        else:
            # print("got entries!\nfilename: %s\nattr_name: %s" % (filename, attr_name))
            try:
                with open(filename,'r') as fp:
                    text_lines = fp.readlines()
                    for line in text_lines:
                        if line.isascii() == False:
                            self.ui.update_sys_msg("Error: Imported files can only contain ASCII characters")
                            raise Exception("Imported files can only contain ASCII characters")
                            return False
                        else:
                            #display_text += str(count) + ": " + line
                            display_text += line
                        count += 1
            except FileNotFoundError:
                self.ui.update_sys_msg("Error: File does not exist")
                # print("That file does not exist")
                return False
            except:
                self.ui.update_sys_msg("Error: an unexpected import error has occurred")
                # print("attempt_import: An unexpected import error has occurred")
                return False
            if display_text != '':
                self.ui.make_display(display_text,False)
                new_file = open(("./source_code/"+attr_name),"w")
                new_file.write(display_text)
                self.ui.update_sys_msg("Import successful. Source Code file is now \nready for annotation")
                new_file.close()
            self.ui.next_step = Button(self.ui, text="Include/Exclude Lines", command=self.select_lines)
            self.ui.next_step.place(x = 360, y = 180)
            return True
        
    def in_ex_lines(self, lower, upper, in_ex, length):
        '''
        Purpose: Checks the validity of the user inputs for line inclusion/exclusion.
                lower and upper must be positive integers. Lower must be less than or equal
                to upper. Upper must be greater than or equal to lower. Neither can exceed
                the number of lines in the source code file.
        Parameters: 
            lower: an int. lower bound of the lines to include/exclude (inclusive)
            upper: an int. upper bound of the lines to include/exclude (inclusive)
            in_ex: a string. 'Include' or 'Exclude'. Determines which branch to take. 
            length: the number of lines in the source code file.
        Return: True upon both user-entered parameters are valid and the line lists are successfully updated.
                False if:
                    - One or both fields are empty
                    - Upper is less than Lower / Lower is greater than Upper
                    - Lower is negative, greater than the number of lines in the file, or is not an integer
                    - Upper is negative, greater than the number of lines in the file, or is not an integer
        '''
        #print("in in_ex_lines...")
        if lower == '' or upper == '':
            #print("One or more fields empty, doing nothing...")
            self.ui.update_sys_msg("Error: Both fields must not be empty to continue")
            return False
        elif int(lower) > int(upper) or int(upper) < int(lower):
            self.ui.update_sys_msg("Error: Range invalid; Upper must be greater\nthan Lower Bound and Lower must\nbe less than Upper bound")
            return False
        elif int(lower) < 0 or int(lower) > int(length) or int(upper) < 0 or int(upper) > length-1:
            self.ui.update_sys_msg("Error: Range invalid; \nSelect from Lines 0 through %s (inclusive)"%(str(length-1)))
            return False
        else:
            new_lst = []
            lower = int(lower)
            upper = int(upper)
            if in_ex == 'Include':
                for i in range(lower, upper+1):
                    if i not in self.include:
                        self.include.append(i)
                for x in self.exclude: # remove duplicate elements from exclude list
                    if x not in new_lst and x not in self.include:
                        new_lst.append(x)
                self.exclude = new_lst
                self.ui.update_sys_msg("Success: Lines %s-%s added for inclusion" % (lower,upper))
                # print("include list:")
                # print(self.include)
                # print("exclude list: ")
                # print(self.exclude)
            else:
                for i in range(lower, upper+1):
                    if i not in self.exclude:
                        self.exclude.append(i)
                for x in self.include: # remove duplicate elements from include list
                    if x not in self.exclude and x not in new_lst:
                        new_lst.append(x)
                self.include = new_lst
                self.ui.update_sys_msg("Success: Lines %s-%s added for exclusion" % (lower,upper))
                # print("include list:")
                # print(self.include)
                # print("exclude list: ")
                # print(self.exclude)
            #print(new_lst)
            return True
        
    def remove_lines(self):
        '''
        Purpose: Called when the user indicates they are done selecting
                lines for inclusion and exclusion. Updates the source code
                file to contain only the lines that were not in the
                list of lines for exclusion.
                The final resulting file contents are displayed for the user.
        Return: True upon successful opening of the source code and updating the lines to be included.
                False if:
                    - FileNotFound error is raised
        '''
        solution_code = ''
        count = 0
        attr_name = ''
        try:
            attr_name = self.name.get()
        except:
            attr_name = self.name
        # print("updating: %s" % (attr_name))
        try:
            cwd = os.getcwd()
            cwd+= '/source_code/'+attr_name
            # print("attr_name: "+attr_name) 
            # print(cwd)
            if os.path.isfile(cwd) == False:
                raise FileNotFoundError
            with open(cwd, 'r') as fp:
                #print("including: %s" % (self.include))
                #print("excluding: %s" % (self.exclude))
                text_lines = fp.readlines()
                for i in range(len(text_lines)):
                    if i in self.include or (i not in self.include and i not in self.exclude): # line was included and not specifically excluded
                        # print("including: %s" % (text_lines[i]))
                        solution_code += text_lines[i]
                        count+=1
            fp.close()
            #print(solution_code)
            self.sol_code_len = count
            with open(('./source_code/'+attr_name), 'w') as updated_fp:
                updated_fp.write(solution_code)
                # print(self.sol_code_len)
            updated_fp.close()
            return True
        except FileNotFoundError:
            self.ui.update_sys_msg("Error: File does not exist")
            #print("remove_lines: That file does not exist")
            return False

    def select_lines(self):
        '''
        Purpose: Displays the source code for the user such that the user may select lines
                for tupling. After displaying the source code file, the UI method for
                creating this step's page is called. From there, in_ex_lines is called
                when the user inputs values.
        Return: True upon fully successful opening of the source code file and reading the lines for display.
                False if:
                    - FileNotFound error is raised
                    - Unexpected error occurs while reading the lines from the open file
        '''
        attr_name = ''
        try:
            attr_name = self.ui.attr_nameQuery.get()  # stores the name of the file that the
        except:
            attr_name = self.ui.attr_nameQuery

        try:    # FLAG FOR BUGS                   # user imported
            self.ui.next_step.destroy()
        except:
            pass
        display_text = ''
        length = 0

        self.ui.make_display(display_text,True)

        self.ui.update_sys_msg("Line Inclusion/Exclusion: System Messages \nand Errors will appear here")
        
        try:
            #print("opening file...")
            #print(attr_name)
            with open(('./source_code/'+attr_name), 'r') as fp:
                text_lines = fp.readlines()
                length = len(text_lines)
                #print("read done")
                for line in text_lines:
                    display_text += line
                #print("done, closing file.")
            self.ui.make_display(display_text,True)
            fp.close()
            #print("file is closed")
        except FileNotFoundError:
            self.ui.update_sys_msg("Error: File does not exist")
            # print("select_lines: That file does not exist")
            return False
        except:
            self.ui.update_sys_msg("Error: Unexpected error in select_lines")
            # print("select_lines: An error has occurred")
            return False

        try: # should not run if in unit testing mo
            self.ui.line_time(length)
        except: 
            pass

        return True
        
    def make_tuple(self, first, second, length):
        '''
        Purpose: Checks the validity of the user inputs for tuple-making.
                If all parameters passed in are valid, a tuple is formed and
                added to the process' tuple list. This will be included in the
                configuration file for the solution code.
        Parameters:
            first: the first in the pair of adjacent lines. Must be less than second.
            second: the second in the pair of adjacent lines. Must be greater than second.
            length: the length of the source code file (after line inclusion/exclusion)
        Return: True if the tuple is valid. If tuple is already in self.tuples it will not add a duplicate but return True.
                False if:
                    - One or both fields are empty
                    - second is less than first / first is greater than second
                    - first is negative, greater than the number of lines in the file, or is not an integer
                    - second is negative, greater than the number of lines in the file, or is not an integer
                    - first and second are not adjacent (the difference between them must be exactly 1)
        
        '''
        if first == '' or second == '':
            self.ui.update_sys_msg("Error: Both fields must not be empty to continue")
            return False
        elif int(second) != int(first)+1:
            self.ui.update_sys_msg("Error: Lines must be adjacent to become a tuple")
            return False
        elif int(first) > int(second) or int(second) < int(first):
            self.ui.update_sys_msg("Error: Range invalid; \nFirst Line must be greater than Second Line\n and Lower must be less than Upper bound")
            return False
        elif int(first) < 0 or int(first) > int(length) or int(second) < 0 or int(second) > length:
            self.ui.update_sys_msg("Error: Range invalid; \nSelect from Lines 0 through %s (inclusive)"%(str(length-1)))
            return False
        else:
            if (first,second) not in self.tuples:
                self.ui.update_sys_msg("Success: tuple (%s,%s) added" % (first,second))
                self.tuples.append((first,second))
                # print(self.tuples)
            return True

    def tuple_lines(self):
        '''
        Purpose: Creates the Solution Code folder for the Source Code and allows user
                to select lines for tupling until the 'next' button is pressed.
                Saves the Solution Code file to its respective folder. The tuples chosen
                Are stored as a list of tuples in the Solution Code's configuration file.
        Return: True if the solution code folder and file are created successfully.
                False if:
                    - A folder in the solution code folder already exists under the name the user provided
                    - Error in creating solution code file
                    - Error in opening source code file
        '''
        folder_name = ''
        solution_code = ''
        display_text = ''
        tuples = []
        attr_name = ''

        try:    # during Unit Testing, self.name will not be populated with an Entry StringVar
            attr_name = str(self.name.get())
        except: # Therefore the self.name value will be a simple String object
            attr_name = str(self.name)
        # print(attr_name)
        
        self.ui.update_sys_msg("Line Tupling: System Messages and\nErrors will appear here")
        
        self.remove_lines()
        
        #print(len(attr_name))
        try:
            cleave = -1
            for i in range(len(attr_name)):
                #print(attr_name[i])
                if attr_name[i] == '.':
                    cleave = i
            #print(cleave)
            if cleave != -1:  # imported file has a file extension type
                folder_name += attr_name[:cleave]
            else:  # imported file does not has a . file extension type
                folder_name += attr_name
            #print(folder_name)

            self.sol_folder_name = folder_name
            # print(self.sol_folder_name)

            # TUPLE UI CREATION: is not to execute during Unit Testing
            try:
                self.ui.tuple_ui()
            except: # in unit testing mode if fails; move on...
                pass

            # Make our directory and write the tuple / exclusion file
            cwd = os.getcwd()
            cwd+='/solution_code/'+self.sol_folder_name
            if os.path.exists(cwd) == False:    # if the solution code folder does not yet exist...
                os.mkdir(cwd)
            #print(cwd)
            
            # 12/6 THIS WAS THE SOURCE OF THE ORIGINAL 'config' ABORT
            new_file = open((cwd+"/"+attr_name),"w")
            new_file.write(solution_code)
            new_file.close()

            self.ui.make_display(display_text,True)

            # 12/12: Added functionality for counting the indentations in each line of code.
            # This is to add customized functionality for the 'indentation' qType.
            # The indentation counts are saved as a list of positive integers under the var self.sol_code_indentation
            try:
                with open(('./source_code/'+attr_name), 'r') as fp:
                    with open(('./solution_code/'+self.sol_folder_name+'/'+attr_name), 'w') as solution_fp:
                        text_lines = fp.readlines()
                        length = len(text_lines)
                        # 12/12: preceding whitespace counter and while loop added for 'indentation'
                        for line in text_lines:
                            count = 0
                            whitespace = 0
                            while (line[count] == '\t' or line[count] == ' ') and count < len(line):
                                whitespace += 1
                                count += 1
                            self.sol_code_indentation.append(whitespace)
                            display_text += line
                        solution_fp.write(display_text)
                        # print(self.sol_code_indentation)  # 12/12 FOR TESTING PURPOSES, COMMENT OUT WHEN DONE
                        solution_fp.close()
                    self.ui.make_display(display_text,True)
                    fp.close()
                return True
            except FileNotFoundError:
                self.ui.update_sys_msg("Error: File does not exist")
                # print("Tuple Lines: File '%s' does not exist" % (attr_name))
                return False
        except ValueError: # this is simply a warning, still runs as expected in the system
            # print("Filename given by User does not have a file extension.\nUnique Solution Code folder will have the same name as the solution code file")
            pass

    def choice_made(self, mode, options = []):
        '''
        Purpose: helper function to LMS_select and qType_select. confirms the validity of the choice the user made.
        Parameters:
            mode: 'LMS' or 'qType', depending on the step in the process that we are on
        Return: True if the user makes a valid selection (either LMS or qType)
                False if:
                    - the choice the user made is not valid (not in the LMS or qType options available)
                    - mode parameter is not 'LMS' or 'qType'
        '''
        # LMS AND THEIR CORRESPONDING QUESTION TYPES (not verified)
        # blackboard_qTypes = ['multiple choice','fill-in-the-blank','reordering','find the bug']
        # canvas_qTypes = ['multiple choice','fill-in-the-blank','reordering','find the bug', 'indentation']
        # moodle_qTypes = ['multiple choice','reordering','fill-in-the-blank','find the bug','indentation']
        
        selection = ''
        if mode == 'LMS':       # we are in selection mode for LMS
            try:
                selection = self.LMS_choice.get()
                selection = selection.lower()
            except:
                selection = self.LMS_choice
            if selection != 'blackboard' and selection != 'canvas' and selection != 'moodle':
                self.ui.update_sys_msg("Error: LMS selection is not valid.")
                return False
            else:
                # print("Valid choice, call 'self.qType_select'")
                self.qType_select()
                return True
        elif mode == 'qType':       # we are in selection mode for qType
            try:
                selection = self.qType_choice.get()
                selection = selection.lower()
            except:
                selection = self.qType_choice
            if selection not in options:
                self.ui.update_sys_msg("Error: Question Type selection is not valid.")
                return False
            else:
                # Valid choice, create the config file for the solution code
                self.ui.numStudents_ui()
                return True
        else:
            # print('invalid mode')
            return False
        

    def LMS_select(self):
        '''
        Purpose: User selects LMS for configuration file, creates config file
                for Solution Code folder.
        '''
        self.ui.update_sys_msg("LMS Selection: System Messages and \nErrors will appear here")

        self.ui.selection_ui('LMS',['Blackboard','Canvas','Moodle'])

        # print("In LMS_select")
        return True

    def qType_select(self):
        '''
        Purpose: Final step! User selects qType for the configuration file in the UI, but here
                is where what qTypes they can choose from based on the LMS they chose
        '''
        self.ui.update_sys_msg("Question Type Selection: System Messages and \nErrors will appear here")

        options = []
        #print(self.LMS_choice)
        try:
            self.LMS_choice = self.LMS_choice.get()
        except:
            self.LMS_choice = self.LMS_choice
        self.LMS_choice = self.LMS_choice.lower()
        
        if self.LMS_choice == 'blackboard':
            #print(self.LMS_choice)
            options = ['multiple choice','fill-in-the-blank','reordering','find the bug', 'inden']
        elif self.LMS_choice == 'canvas':
            #print(self.LMS_choice)
            options = ['multiple choice','fill-in-the-blank','reordering','find the bug', 'indentation']
        elif self.LMS_choice == 'moodle':
            #print(self.LMS_choice)
            options = ['multiple choice','reordering','fill-in-the-blank','find the bug','indentation']
        else:
            #print("Unexpected error in qType_select: LMS_choice is not valid")
            return False

        self.ui.selection_ui('qType',options)
        
        # print("In qType_select")
        # print(options)
        return True

    def numStudents_select(self):
        '''
        Purpose: User enters the number of students (and thus, the number of mutated questions to generate) that
            that the problem set will be made for.
        '''
        try:
            self.numStudents = self.numStudents.get()
        except:
            self.numStudents = self.numStudents
        # self.ui.numStudents= int(self.ui.numStudents)

        #  as well as call the ui for 'finish' to close out the process
        self.create_config_file()    # added 12/6 2:30pm by Gasser
        self.ui.finish_ui()

        return True

    def create_config_file(self):
        '''
        Purpose: generates the config.txt that will be located in the solution code's unique folder.
                The contents of this file will be:
                    1   LMS_choice
                    2   qType_choice
                    3   tuple list or indentation list or included lines list (dependent on qType_choice)
                    4   numStudents
        '''
        try:
            self.qType_choice = self.qType_choice.get()
        except:
            self.qType_choice = self.qType_choice

        include_list = '['
        config_tuples = '['
        indent_list =  '['
        # MULTIPLE CHOICE AND FILL-IN-THE-BLANK QTYPE PREP FOR CONFIG FILE -- 12/9
        if self.qType_choice == 'multiple choice' or self.qType_choice == 'fill-in-the-blank':
            count = 0
            for num in range(self.sol_code_len):
                include_list += str(num)
                if count != self.sol_code_len-1:
                    include_list += ','
                count += 1
            include_list += ']'
            #print(include_list)
        
        # INDENTATION QTYPE PREP FOR CONFIG FILE -- 12/12
        elif self.qType_choice == 'indentation':
            count = 0
            for i in self.sol_code_indentation:
                indent_list += str(i)
                if count != len(indent_list)-1:
                    indent_list += ','
                count += 1
            indent_list += ']'
            #print(indent_list)


        # REORDERING AND FIND THE BUG QTYPE PREP FOR CONFIG FILE -- 12/9
        #if self.qType_choice == 'reordering' or self.qType_choice == 'find the bug':
        else:
            count = 0
            for t in self.tuples:
                config_tuples += '(' + str(t[0]) + ',' + str(t[1]) + ')'
                if count != len(self.tuples)-1:
                    config_tuples += ','
                count += 1
            config_tuples += ']'
            #print(config_tuples)

        try:
            # attr_name = self.name.get()
            cwd = os.getcwd()
            cwd += '/solution_code/'

            # If the solution code folder does not exist already...
            if os.path.exists(cwd) == False:
                os.mkdir(cwd+self.sol_folder_name)

            cwd += self.sol_folder_name
            #print(self.sol_folder_name)

            with open(cwd+'/config.txt','w') as fp:
                fp.write(self.LMS_choice+'\n')
                fp.write(self.qType_choice+'\n')
                if self.qType_choice == 'multiple choice' or self.qType_choice == 'fill-in-the-blank':
                    fp.write(include_list+'\n')
                # 12/13 Sprint 3 addition to add functionality for indentation and find the bug qtypes
                elif self.qType_choice == 'indentation':
                    fp.write(indent_list+'\n')
                else:
                    fp.write(config_tuples+'\n')
                fp.write(str(self.numStudents))
                fp.close()
            #print("done with making the file")
            return True
        except FileNotFoundError:
            self.ui.update_sys_msg("Error: File does not exist")
            #print("That file does not exist")
            #print("file not found")
            return False

##########################################################################
class PPALMS:
    def __init__(self):
        self.backend = PPALMS_BACKEND()

        # FOR TESTING
        # back = self.backend
        # back.name = 'test22.py'
        # back.sol_folder_name = 'test22'
        # back.LMS_choice = 'blackboard'
        # back.qType_choice = 'multiple choice'
        # back.tuples = [(1,2),(3,4)]
        # back.create_config_file()
        # testing:
        # C:\Users\webgi\Desktop\CLASSES\FALL22Classes\CSCI5801\P4_CSCI5801_v3\CSCI5801_P4\P4_CSCI5801\testcase_files\examples.py

if __name__ == '__main__':  # main, where all of the 'driving' will be done
    process = PPALMS()  # This sets up our application object (aka our interface)
    process.backend.ui.title('PPALMS Interactive Window')
    process.backend.ui.geometry("700x700+10+20")  # This is how we size our window (can be modified)
    process.backend.ui.mainloop()
