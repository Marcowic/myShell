This is the user manual for the myshell.py

Run the shell program by typing "python3 myshell.py" on UNIX operating systems 

The shell program has some simple built in commands which perform similarly as commands which can be used in most terminals (UNIX or Windows).

//////////////////////////////////////////////
/This manual will be separated in three parts/
\---->Commands Information                   /
\---->Child Processes                        /
\---->Input/Output Redirection               /
//////////////////////////////////////////////


>The following commands and their usage are as follows:

/****************************************************************************************************
Command:    cd
Usage:      cd <path>

Description:
            Calling the cd command will change the current working directory to the path or directory specified <path>. <path> is the name of directory or full path to change the current working directory to.
            If the <path> is not specified, the current working directory will be displayed.
Example:
            Typing "cd .." will change the current working directory to the parent directory.
*****************************************************************************************************/
/****************************************************************************************************
Command:    clr
Usage:      clr

Description:
            Calling clr will clear the screen(terminal).
*****************************************************************************************************/

/****************************************************************************************************
Command:    quit
Usage:      quit

Description:
            Closes the shell program.
*****************************************************************************************************/
/****************************************************************************************************
Command:    dir
Usage:      dir <directory>

Description:
            Calling the dir command will display all the files within <directory>.
            <directory> is the full path to the directory you wish to display the contents of.
            If the <directory> is not supplied, the contents of the current working directory will be displayed

*****************************************************************************************************/
/****************************************************************************************************
Command:    echo
Usage:      echo <message>

Description:
            Calling echo will display the <message> on the screen (terminal).
            <message> can contain any arbitrary number of characters.
            Multiple tabs and whitespaces will be treated as a single whitespace.
            Any characters written after the command will be treated as the <message>.
Example:
            Typing "echo 1 two              three!" 
            will display "1 two three!"
*****************************************************************************************************/
/****************************************************************************************************
Command:    environ
Usage:      environ <variable>

Description:
            Calling the environ command will display the environment variables and their path.
            <variable> is the name of environment variable's path to be displayed. 
            Can be left blank to display all environment variables and path associated with them.
Example:
            Typing "environ public"
            will display the path of the public environment.
*****************************************************************************************************/
/****************************************************************************************************
Command:    pause
Usage:      pause

Description:
            Calling the pause command will temporarily halt the function of the shell commands.
            Child processes will not be affected by the pause command.
            To exit pause mode, press enter on an empty line.
*****************************************************************************************************/
/****************************************************************************************************
Command:    help
Usage:      help <command>

Description:
            Calling help along with a command will display a higher level detailed information about the specific command.
            <command> is one of the built in commands of the shell.
            Leaving <command> blank will display all the built in command of the shell program with a low level of detail. An additional exclusive option will be available after calling "help" without any other arguments. Typing "more" will display higher level information about all of the built in commands.
Example:
            Typing "help environ"
            will display a hiher level information about the environ command
*****************************************************************************************************/


>Child Processes

        Programs can be called from the shell program by typing the approriate program call for the said program following the syntax of the operating system (UNIX).

        Example:

                Typing "python" will open an instance of python on the terminal.
                Typing "python program_name.py", the shell program will try to execute the program_name.py with python.
                Typing "gedit" will open gedit text editor.




>Input/Output redirection

         To utilise the input and output redirection properly, make sure that the program call is using proper syntax as per operating system. Eg, calling python3 on linux will yield in python version 3.x.x (whatever python version 3 is installed) will be used. However, calling python3 in Windows operating system is invalid. Instead, you must call python which does not specify whether python version 2 or 3 will be used but whatever is instaled will be used.

         Standard in can be redirected to use the provided file as a source. Note, standard input can only be redirected from one file only, otherwise the program will be invalid even if it has perfect syntax for the system.

         Example usage:

                 Typing "python3 sample_program.py args.txt args2.txt" will be invalid and an error will errupt.

         Outputs can be redirected using the following signatures:
         >> - create a file if it does not exist already and append to it.
         > - create a file if it does not exist already and write to it (overwriting what it already contains)

         Example usage:

                 Typing "python3 sample_program.py args.txt >> sample_output.txt" 
                 will execute the sample_program.py using python version 3 (on Linux) using the file args.txt file as the source of input. All standard out procedures during the execution of the program will be writter to the file sample_output.txt. If the sample_output.txt does not exist, it will be created and appended to.


Miscellaneous feature:

        Typing "&" at the end of child process execution call at the shell program will run the program in the background. In the meanwhile the shell program will be fully functional.

        Example usage:

                    Typing "python3 sample_program.py args.txt &"
                    will execute sample_program.py with python using args.txt as redirected input. THis will then run in the background and the shell program will resume functionality.