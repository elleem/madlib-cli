

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

def parse_template(template_string):
    pieces_string = ""
    pieces = []
    is_a_piece = False
    temp_piece = ""

    for char in template_string:
        if char == "{":
            is_a_piece = True
            pieces_string += char
        elif char == "}":
            is_a_piece = False
            pieces_string += char
            pieces.append(temp_piece)
            temp_piece = ""
        else:
            if is_a_piece:
                temp_piece += char
            else:
                pieces_string += char

    return pieces_string, tuple(pieces)

def merge(pieces_string, pieces):
    result = pieces_string.format(*pieces)
    return result

welcome()
read_template(txt_file1)
parse_template(txt_file1)
#merge()


