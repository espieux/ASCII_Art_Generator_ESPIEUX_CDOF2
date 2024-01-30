def generate_ascii_art(text):
    # ASCII Art representations for each character
    ascii_art_dict = {
    'A': ['  A  ', ' A A ', 'AAAAA', 'A   A', 'A   A'],
    'B': ['BBBB ', 'B   B', 'BBBB ', 'B   B', 'BBBB '],
    'C': [' CCC ', 'C   C', 'C    ', 'C   C', ' CCC '],
    'D': ['DDDD ', 'D   D', 'D   D', 'D   D', 'DDDD '],
    'E': ['EEEEE', 'E    ', 'EEE  ', 'E    ', 'EEEEE'],
    'F': ['FFFFF', 'F    ', 'FFF  ', 'F    ', 'F    '],
    'G': [' GGG ', 'G    ', 'G  GG', 'G   G', ' GGG '],
    'H': ['H   H', 'H   H', 'HHHHH', 'H   H', 'H   H'],
    'I': [' III ', '  I  ', '  I  ', '  I  ', ' III '],
    'J': ['JJJJJ', '  J  ', '  J  ', 'J J  ', ' JJ  '],
    'K': ['K   K', 'K  K ', 'KK   ', 'K  K ', 'K   K'],
    'L': ['L    ', 'L    ', 'L    ', 'L    ', 'LLLLL'],
    'M': ['M   M', 'MM MM', 'M M M', 'M   M', 'M   M'],
    'N': ['N   N', 'NN  N', 'N N N', 'N  NN', 'N   N'],
    'O': [' OOO ', 'O   O', 'O   O', 'O   O', ' OOO '],
    'P': ['PPPP ', 'P   P', 'PPPP ', 'P    ', 'P    '],
    'Q': [' QQQ ', 'Q   Q', 'Q   Q', 'Q  Q ', ' QQ Q'],
    'R': ['RRRR ', 'R   R', 'RRRR ', 'R R  ', 'R  RR'],
    'S': [' SSS ', 'S    ', ' SSS ', '    S', 'SSSS '],
    'T': ['TTTTT', '  T  ', '  T  ', '  T  ', '  T  '],
    'U': ['U   U', 'U   U', 'U   U', 'U   U', ' UUU '],
    'V': ['V   V', 'V   V', 'V   V', ' V V ', '  V  '],
    'W': ['W   W', 'W   W', 'W W W', 'WW WW', 'W   W'],
    'X': ['X   X', ' X X ', '  X  ', ' X X ', 'X   X'],
    'Y': ['Y   Y', ' Y Y ', '  Y  ', '  Y  ', '  Y  '],
    'Z': ['ZZZZZ', '   Z ', '  Z  ', ' Z   ', 'ZZZZZ'],
    '0': [' 000 ', '0   0', '0   0', '0   0', ' 000 '],
    '1': ['  1  ', ' 11  ', '  1  ', '  1  ', '11111'],
    '2': [' 222 ', '2   2', '   2 ', '  2  ', '22222'],
    '3': ['3333 ', '    3', ' 333 ', '    3', '3333 '],
    '4': ['4  4 ', '4  4 ', '44444', '   4 ', '   4 '],
    '5': ['55555', '5    ', '5555 ', '    5', '5555 '],
    '6': [' 666 ', '6    ', '6666 ', '6   6', ' 666 '],
    '7': ['77777', '   7 ', '  7  ', ' 7   ', '7    '],
    '8': [' 888 ', '8   8', ' 888 ', '8   8', ' 888 '],
    '9': [' 999 ', '9   9', ' 9999', '   9 ', ' 999 ']
    }

    # Convert text to ASCII Art
    result = ['' for _ in range(5)]  # 5 lines high ASCII Art
    for char in text.upper():
        if char in ascii_art_dict:
            for i in range(5):
                result[i] += ascii_art_dict[char][i] + '  '
        else:
            for i in range(5):
                result[i] += '     '  # Space for unrecognized characters

    return '\n'.join(result)

def generate_ascii_art2(text):
    ascii_art_dict={
        'A':[ 
            "  ,---.   ",   
            " /  O  \  ",
            "|  .-.  | ",
            "|  | |  | ",
            "`--' `--' ",
        ],
        'B':[
            ",-----.   ",
            "|  |) /_  ",
            "|  .-.  \ ",
            "|  '--' / ",
            "`------'  ",
        ],
        'C':[
            " ,-----. ",
            "'  .--./ ",
            "|  |     ",
            "'  '--'\ ",
            " `-----' ",
        ],
        'D':[
            ",------.   ",
            "|  .-.  \  ",
            "|  |  \  : ",
            "|  '--'  / ",
            "`-------'  ",
        ]

    }

    # Convert text to ASCII Art
    result = ['' for _ in range(5)]  # 5 lines high ASCII Art
    for char in text.upper():
        if char in ascii_art_dict:
            for i in range(5):
                result[i] += ascii_art_dict[char][i] + '  '
        else:
            for i in range(5):
                result[i] += '     '  # Space for unrecognized characters

    return '\n'.join(result)


def main():
    choice = input("Choose a function: \n1 - regular ascii art\n2 - bubble ascii art\n\n1 or 2? : ")
    text = input("\nEnter a text: ")
    if(choice=='1'):ascii_art = generate_ascii_art(text)
    elif(choice=='2'):ascii_art = generate_ascii_art2(text)
    
    print(ascii_art)

if __name__ == '__main__':
    main()