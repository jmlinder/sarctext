#! /usr/local/opt/python/libexec/bin/python
import sys


def sarctext(text):
    '''
    Takes a string and returns it in alternating upper and lowercase text,
    similar to the sarcastic Spongebob meme.
    '''

    ns = []
    for index, letter in enumerate(text):
        if index % 2 == 0:
            ns.append(letter.upper())
        else:
            ns.append(letter.lower())
    print(''.join(ns))


if __name__ == "__main__":

    sarctext(' '.join(sys.argv[1:]))
