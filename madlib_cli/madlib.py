txt_file1 = './assets/dark_and_stormy_night_template.txt'
txt_file2 = '../assets/make_me_a_video_game_template.txt'
def welcome():
    print('''
    *********************************
    Welcome to MadLibs Rescue Mission! 
    To play, please enter the 
    correct word type when prompted.
    Enter quit to exit.
    *********************************''')


def read_template(txt_file):
    try:
        with open(txt_file,'r') as f:
            contents = f.read()
            return contents
    except FileNotFoundError:
        raise FileNotFoundError





def merge():
    pass

def parse_template():
    pass

welcome()
read_template(txt_file1)
