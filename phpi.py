#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      yanwar
#
# Created:     10/03/2015
# Copyright:   (c) yanwar 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
os.system("cls")

shows = """
PHP Interactive Shell Version 1.0.0 (Yanwar Solahudin)
please typing 'phpi:help' for help.
"""
print shows
print




def write_session(data):
    data_error_handling = """
    //error handler function
    function customError($errno, $errstr) {
      echo "\n* Error : [$errno] \n* $errstr !\n";
    }

    //set error handler
    set_error_handler("customError");
    """
    file = open("session.php", "w+")
    file.write("<?php \n")
    file.write(data_error_handling)
    file.write(data)
    file.write(" ?>")
    file.close()
    return "session.php"

def write_all(data, directory, filename):
    file = open(directory+"/"+filename, "w")
    file.write("<?php \n")
    file.write('\n'.join(data))
    file.write(" ?>")
    file.close()
    return "check file in : " + directory+"/"+filename

def read_path_phpi():
    file = open("path.phpi", "r")
    try:
        data_path = file.readlines()[0]
    except:
        data_path = False
    file.close()
    return data_path

command = []

session_file = "se"
number_line = 0

iCommand = True

while True:
    number_line = number_line + 1
    com = "phpi-> "
    ins = raw_input(com)
    command.append(ins)

    if ins == "phpi:exit":
        exit()
        break
    if ins == "phpi:run":
        if len(command) > 0:
            command.pop()
            script = "\n".join(command)
            php_file = write_session(script)
            if read_path_phpi():
                os.system(read_path_phpi() + " " + php_file)
            else:
                os.system("php " + php_file )
            print
            write_session(" ")
        else:
            print "empty set script"

    if ins == 'phpi:line':
        command.pop()
        print
        print "<?php"
        for n,i in enumerate(command):
            print "[" + str(n) + "] \t" + i + " "
        print "?>"
        print

    if ins == "phpi:clear":
        del command[:]

    if ins == "phpi:out":
        command.pop()
        outs = raw_input("out code in line > ")
        outs = int(outs)
        command.remove(command[outs])

    if ins == "phpi:repair":
        command.pop()
        outs = raw_input("repair number > ")
        line = int(outs)
        outs = raw_input("insert code > ")
        data = str(outs)
        line_out = line + 1
        command.insert(line, data)
        command.remove(command[line_out])


    if ins == "phpi:help":
        command.pop()
        print
        data_help = """

        * phpi:run     > running script in interactive shell
        * phpi:exit    > stop interactive shell
        * phpi:line    > show all your code in interactive shell
        * phpi:clear   > reset interactive
        * phpi:out     > remove code based index in interactive shell
        * phpi:repair  > repair line code in interactive shell
        * phpi:path    > setting path php
        * phpi:info    > About PHPI
        * phpi:save    > Save Script in your directory
        * phpi:toclear > Clear code from ... to ...
        * phpi:server  > Running Script to server

        """
        print data_help
        print

    if ins == "phpi:save":
        command.pop()
        dirs = raw_input("Directory: ")
        filename = raw_input("Filename: ")
        result = write_all(command, dirs, filename)
        print result

    if ins == "phpi:info":
        command.pop()
        print
        print "<?phpi"
        print "     PHPI - PHP Intrecative"
        print "     By Yanwar Solahudin"
        print "     Version 1.0.0"
        print "     Backend in Python Console"
        print "?>"
        print

    if ins == "phpi:path":
        command.pop()
        path = raw_input("set php path: ")
        file = open("path.phpi","w")
        file.write(path)
        file.close()

    if ins == "phpi:server":
        command.pop()

        script = " ".join(command)
        php_file = write_session(script)
        if read_path_phpi():
            try:
                os.system(read_path_phpi() + " -S localhost:8000 " + php_file)
            except:
                os.system("php_editor.py")
        else:
            try:
                os.system("php -S localhost:8000 " + php_file )
            except:
                os.system("php_editor.py")


    if ins == "phpi:toclear":
        command.pop()
        froms = raw_input("from: ")
        to = raw_input("to: ")
        if int(to) < int(froms):
            print "the initial value is greater than the value of end target"
        else:
            to = int(to)
            froms = int(froms)

            del command[froms:to+1]

for n,i in enumerate(command):
    print "number of : " + str(n) + " | command : " + str(i)