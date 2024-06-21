import sys


def read_input(prompt):
    print(prompt, end='', flush=True)
    input_str = ''
    while True:
        char = sys.stdin.read(1)
        if char == '\n':
            break
        input_str += char
        sys.stdout.write(char)
        sys.stdout.flush()
    return input_str


b = read_input('Please enter a value for b: ')
print(f'\nYou entered: {b}')
