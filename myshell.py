"""
Project started Sunday March 24, 2019
This is my attempt at making a functional command line interface with 
functional and practical arguments.
"""
#The help commands are purposely left commented for possible future reference or usage.
#They are the help commands which are inherited from the cmd module.
#They are commented because they have been overwritten by a more general help command.

import os
import sys
import cmd
import subprocess
import myshell_help as utils                                                                     #Import utility functions for displaying help commands
import redirection as rambo

class mySHELL(cmd.Cmd):
    prompt = os.getcwd() + "> "                                                                 #The initial current working directory displayed. This is overwrittep per cd command call.
    commands = {
            "cd" : "<path> ",
            "clr" : "",
            "dir" : "<directory>",
            "environ" : "<variable>",
            "echo" : "<message>",
            "help" : "",
            "pause" : "",
            "quit" : "",
        }                                                                                       #The initial commands built in the shell program. Used by the help command.
                                                                                                #Stored in a dictionary for possible future change of commands. Addition, removal or updation.

    help_flag = False                                                                           #The flag for the help command to enable or disable the 'more' functionality. The 'more' function for the help command
                                                                                                #will only be available to use directly after calling the help command without any argument.

    def do_cd(self,arg):
        """ 
        Changes the current working directory of the SHELL, arguments can
        passed to manipulate where the working directory goes. Utilises
        the os module to obtain the CWD. If the method argument is not valid,
        an appropriate error message is displayed on the cli and then
        proceeds with execution.
        """
        if len(arg)<1:                                                                          #Checks if the argument passed has length less than 1 due to "/" being a valid directory.
            print(os.getcwd())                                                                  #If there are no arguments, the current working directory is displayed.
        else:                                                                                   #If an argument with a valid length is detected then the following will try to
            try:                                                                                #change the working directory to the argument supplied.
                os.chdir(arg)
                self.prompt = os.getcwd()+"> "
            except FileNotFoundError:                                                           #If the argument length was valid but such directory does not exist or isn't valid. The exception is caught.
                print("Directory/path \'"+arg+ "\' does not exist.")                            #This message will appear stating that the argument supplied is not valid.

    #def help_cd(self):                                                                         #Help command for cd purposely commented for possible future reference or usage..
    #    utils.cd()                                                                             #call for the cd funtion to display appropriate command information.



    ####################################################################
    def do_clr(self,arg):
        """
        Clears the screen. Does not/ should not take any arguments.
        """
        if len(arg)>0:                                                                          #Checks if there are agrguments after the clr command by checking the length of the given argument.
            print("Invalid usage of command. Type \'help clr\' to find out more")               #If there is/are arguments then clr is being misused
        else:                                                                                   #When there are no arguments, clr is going to do its intended purpose.
            os.system("clear")
    #def help_clr(self):                                                                        #Help command for clr purposely left for possible future reference or usage..
    #    utils.clr()                                                                            #Call for the clr function which will display clr command information.


    def postloop(self):                                                                         #After the shell loop has finished, this method will execute, then continue to terminate.
        print()                                                                                 #Print statement added to fix the display when the shell terminates from a batch file.



########################################################################
    def do_quit(self,arg):
        """
        Closes the SHELL by raising a SystemExit call.
        """
        if len(arg)>0:                                                                          #Checks the length of the argument. If it is more than 0 then there is a misuse of the command.
            print("Invalid usage of \'quit\' command. Type \'help quit\' to find out more.")    #Error message for the user. After execution the shell will continue operation as normal.
        else:                                                                                   #Successful call of the quit command.
            dying_message = "Terminating shell. Thank you for using myshell\n"                  #Confirmation message for terminating shell.
            return True


    #def help_quit(self):                                                                       #Help command for quit purposely left for possible future reference or usage.
    #   utils.quit()                                                                            #Call for the quit function which will display quit command information




########################################################################
    def do_dir(self,arg):
        """
        Lists the contents of the current working directory. 
        """
        if len(arg) >0:                                                                         #Checks if there is a path argument given with the dir command.
            try:                                                                                #If there is, then the following will try to display the contents of the directory.
                print()
                for file in os.listdir(arg):
                    print(file)
                print()
            except FileNotFoundError:                                                           #If there is no such directory exist, the exception is caught.
                print("Invalid directory \'"+arg+"\'. Type \'help dir\' to find out more.")     #Display message to the user stating the issue.
        else:                                                                                   #If there is no argument supplied to the command,
            print()
            for file in os.listdir():
                    print(file)                                                             #the contents of the current working directory will be displayed instead.
            print()


    #def help_dir(self):                                                                        #Help command for dir purposely left for possible future reference or usage.
    #    utils.dir()                                                                            #Call for the dir function which will display dir command information




########################################################################
    def do_echo(self,arg):
        """
        Prints the argument(s) given by the user removing any traiing
        whitespace or tabs in between.
        """
        text = arg.split()                                                                      #Split the arguments given to remove all the trailing whitespace.
        print()
        for word in text:                                                                       #Concatenate the words back togeter with a single whitespace in between.
            print(word,end=" ")
        print("\n")           


    #def help_echo(self):                                                                       #Help command for echo purposely left for possible future reference or usage.
    #        utils.echo()                                                                       #Call the echo funtion to display echo command information.





########################################################################
    def do_environ(self,arg):
        """
        Displays the environment variables. Specific environment variables
        can be displayed by providing a path argument
        """
        print()                                                                                 #Just a separation line
        environ_var = os.environ                                                                #Store the environment map tp environ_var variable for reference.
        guideline = max(len(x) for x in environ_var)
        if len(arg)<1:                                                                          #If there are no arguments given with the environ command
            for k in environ_var:                                                               #Go through every key on the environ_var dictionary and display the key and item values in a formatted way. All
                print("{:^{width}} : {}".format(k,environ_var[k],width=int(guideline)))         #the keys and values of the dictinary is displayed in line on the colon, taking into account the longest key for
            print()                                                                             #reference for formatting.
        else:
            try:
                print("{:^{width}} : {}\n".format(arg,environ_var[arg],width=int(guideline)))   #If there is a and argument passed with the command, the following will try to access the environ_var
            except KeyError:                                                                    #to display the path associated with it. If such key does not exist within the environ_var dictionary then
                print("Invalid environment variable: \'",arg,"\'\n")                            #an appropriate message is then displayed.


    #def help_environ(self):                                                                    #Help commanmd for environ command purposely left for possible future reference or usage.
    #    utils.environ()                                                                        #Call for the environ funciton to display useful information on environ command.





########################################################################
    def do_pause(self,arg):
        """
        Runs an infinite loop asking the user for an input.
        While paused, all given commands will have no function.
        When the input is the empty string (equivalent to hitting the enter key
        without any other arguments prior to hitting the enter key), the
        shell will return to function normally.
        """
        print()                                                                                 #Just another separation line.
        print("The shell is now paused!")                                                       #Paused message.
        print("To exit pause mode, press enter.")                                               #Exit pause condition instruction.
        while(True):                                                                            #While the corresponding exit key condition is not met, the shell will keep prompting the user for input.
            checko = input()                                                                    #Store the input from the user.
            if checko == "":                                                                    #If the user input is equal to the empty string, which is equivalent to just hitting the enter key without additional
                break                                                                           #characters before or after, Break out of the infinite loop. Keep looping until the condition is met.


    #def help_pause(self):                                                                      #Left commented for possible future reference.
    #    utils.pause()                                                                          #Call to the pause funtion for displaying pause command information/



########################################################################
    def do_help(self,arg):    
        if len(arg) == 0:                                                                       #Help command method.
            print("Commands:")                                                                  #Help header.
            print()                                                                             #Another separation line.
            for k,v in self.commands.items():                                                   #Go through the commands dictionary of the class which has been seet at the beginning and display them. The key is the
                print(k,v)                                                                      #exact command call and its associated value is its arguments (if available).
            self.help_flag = True                                                               #Set the help flag to true to enable 'more' functionality. 
            print()
            print("For more commands, type \'more\'.")                                          #Ask the user if they want to see a more detailed description of all commands.
        else:
            if arg in self.commands.keys():
                method_to_call = getattr(utils,arg)
                method_to_call()
    def do_more(self,arg):
        if self.help_flag ==True:                                                               #If the help_flag is set when this command is called, the following takes place. Arguments are neither required or
                                                                                                #processed when present.
            self.help_flag = False                                                              #Reset the help flag to avoid misuse of more command.
            utils.more()                                                                        #Display all commands in detail
        else:
            print("*** Unknown syntax: more")                                                   #Simulate an unknown syntax error upon misuse of the 'more' command..

    #def help_help(self):                                                                       #Left commented for possible future reference or usage.
    #    utils.help()                                                                           #Call to the jelp function to display more detailed description of help command.
    def default(self,arg):                                                                      #This function catches the commands where there is no available do_ method.
        try:
            print(arg)
            if arg == "clear" or arg == "ls":
                raise Exception                                                                 #Catches the exeption for unwanted Linux shell commands which still work within this shell somehow.

            rambo.check(arg)                                                                    
        except:
            print("Invalid syntax or cannot execute:  \'",arg,"\'")                             #Error message.



    def do_EOF(self,arg):                                                                       #Handles End of file calls.
        return True                                                                             #Returns true to the cmdloop which ultimately terminates the program.





if __name__ == '__main__':
    if len(sys.argv)>=2:                                                                        #If any batchfiles are give as command line arguments upon calling the python program, the program will 
        commands = []                                                                           #attempt to open the batcfile(s) and pass its contents to the shell as command calls.
        for arg in sys.argv[1:]:
            try:
                current_file = arg
                batchfile = open(current_file,'r')                                              #Open the batchfile(s) upplied and store them in a variable.
                myshell = mySHELL()                                                             #Create an instance of the shell.
                commands.append(batchfile.read().splitlines())                                  #Retrieve all the commands stored in the file(s)
                myshell.cmdqueue = commands                                                     #Move the commands into the cmd queue which will get executed when the shell is started.
                myshell.use_rawinput = True
                myshell.cmdloop()
            except FileNotFoundError:                                                           #File does not exist, cannot open, raise exception.
                print(current_file,"is not available")

    else:
        mySHELL().cmdloop(intro="Welcoming message welcomes you.")
