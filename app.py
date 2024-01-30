def generate_ascii_art(text):
    # ASCII Art representations for each character
    ascii_art_dict = {
        'A': ['  A  ', ' A A ', 'AAAAA', 'A   A', 'A   A'],
        'B': ['BBBB ', 'B   B', 'BBBB ', 'B   B', 'BBBB '],
        # Add more characters here as needed
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
    text = input("Enter a text: ")
    ascii_art = generate_ascii_art(text)
    print(ascii_art)

if __name__ == '__main__':
    main()