import random


def trad_pw_gen():
    pw_len = 16
    char_list = ['0', '1', '2', '3', '4', '5',
                 '6', '7', '8', '9', 'a', 'b',
                 'c', 'd', 'e', 'f', 'g', 'h',
                 'i', 'j', 'k', 'l', 'm', 'n',
                 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z',
                 'A', 'B', 'C', 'D', 'E', 'F',
                 'G', 'H', 'I', 'J', 'K', 'L',
                 'M', 'N', 'O', 'P', 'Q', 'R',
                 'S', 'T', 'U', 'V', 'W', 'X',
                 'Y', 'Z']
    pw = ""

    for i in range(pw_len):
        pw = pw + random.choice(char_list)

    return pw
