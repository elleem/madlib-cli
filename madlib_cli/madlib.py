

txt_file1 = './assets/dark_and_stormy_night_template.txt'
txt_file2 = './assets/make_me_a_video_game_template.txt'

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

def mad_lib():
    print('''
       *********************************
       Welcome to MadLibs Rescue Mission! 
       To play, please enter the 
       correct word type when prompted.
       Enter quit to exit.
       *********************************''')
    template = read_template(txt_file2)

    pieces_string, pieces = parse_template(template)
    user_input = []

    for word in pieces:
        word_input = input(f"Please enter {word}> ")
        user_input.append(word_input)

    madlib = merge(pieces_string,user_input)
    print(f"Madlib: {madlib}")
    with open("./assets/new_file.txt", "w" ) as f:
        f.write(madlib)


mad_lib()
