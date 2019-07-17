import subprocess
from multiprocessing import *

# line = "python3 sample_program.py test1.txt test2.txt test3.txt"





def create_file(t,program,arg,out):
    if arg:
        arg = open(arg,'r')
    if out:
        out = open(out,t)

    process = subprocess.Popen(program,stdin=arg,stdout=out).wait()             #Wait for the program to stop executing and return to the shell immediately after
    if arg:
        arg.close()
    if out:
        out.close()

def run_prog(t,program,arg=None,out=None):
    """
    This function takes care of the execution of the program being called on the shell.
    Checks if background is True, if it is, then the program will run in the background using threding.

    """
    if background:
        print("\nBackground process commencing\n")
        Process(target=create_file, args = (t,program,arg,out)).start()
        print("\nFinished background process!\n")

    else:
        create_file(t,program,arg,out)

#Example command
# line = "python3 sample_program.py test1.txt >> test3.txt &"
def check(line):
    """
    This function checks for the additional functions given by the user on the shell.
    Appropriate outcomes have been implemented.

    ------
    > for create (if it does not exist already) and write to a file
    >> for create (if it does not exist already) and append to a file 
    & to enable background execution of the program (threading)
    ------
    Only one argument file can be passed to the main program.
    """


    line = line.split()


    if line[-1] == "&":                                                         #Check if the program is meant to be run in the background
        line.pop()                                                              #THe use for the command & is no longer needed. Removed from the commands list.
        global background
        background = True                                                       #Acts as a flag if the program needs to be run in background.
    else:
        background = False


    if ">" in line:
        # print("Found the > write to file")                                    #Find the file to write to and the arguments to the program if available.
        
        program = line[0:2]                                                     #The first two commands will always be the program to be run.
        i = 2
        while line[i] != ">":
            i += 1
        if i == 2:
            pass
        elif i >3:
            raise Exception                                                     #More than one argument specified. Raise an exception to break out.
        else:
            arg = line[2]
        out = line[-1]                                                          #The file to create and write to will always be at the end of the shell command so index -1 can be used for foolproofing.
        write_type = "w+"                                                       #THe file permission which will be needed for creating and overwriting the file.
        run_prog(write_type,program,arg,out)


    elif ">>" in line:
        # print("found the >>, must append to file")
        program = line[0:2]                                                     #The first two commands will always be the program to be run.
        i = 2
        while line[i] != ">>":
            i += 1
        if i == 2:
            pass
        elif i >3:
            raise Exception                                                     #More than one argument specified. Raise an exception to break out.
        else:
            arg = line[2]
        out = line[-1]                                                          #The file to create and write to will always be at the end of the shell command so index -1 can be used for foolproofing.
        write_type = "a+"                                                       #The file permission which will be needed for creating and appending to the file.

        run_prog(write_type,program,arg,out)

    else:

        run_prog(None,line)                                                     #No additional functions are specified. Pass the whole command line command to the run_prog function which will
                                                                                #create the process and execute if possible.(No >, >> and or & found in the command)
            
            
