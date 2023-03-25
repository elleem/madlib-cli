#from madlib_cli.madlib import read_template, parse_template, merge

def welcome():
    print('''
*********************************
Welcome to MadLibs! 
To play, please enter the 
correct word type when prompted.
Enter quit to exit.
*********************************
''')


def read_template(txt_file):
    with open(txt_file, 'r') as f:
        contents = f.read()
        return contents

def parse_template():
    pass

def merge():
    pass

welcome()