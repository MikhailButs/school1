alphabet = 'abcdefghijklmnopqrstuvwxyz'

def make_dict(alph_str):
    return {i + 1: alph_str[i] for i in range(len(alph_str))}


def code(text, key, alphabet):
    coded_text = ''
    mask = key * (len(text)//len(key)+1)
    for i in range(len(text)):
        coded_text += alphabet[(alphabet.index(text[i]) + alphabet.index(mask[i])) % len(alphabet)]
    return coded_text


def decode(text, key, alphabet):
    decoded_text = ''
    mask = key * (len(text)//len(key)+1)
    for i in range(len(text)):
        decoded_text += alphabet[(alphabet.index(text[i]) - alphabet.index(mask[i])) % len(alphabet)]
    return decoded_text


if __name__ == '__main__':
    initial = 'abcde'
    key = 'zxc'
    coded = code(initial, key, alphabet)
    decoded = decode(coded, key, alphabet)
    print(f'initial {initial}')
    print(f'coded {coded}')
    print(f'decoded {decoded}')
