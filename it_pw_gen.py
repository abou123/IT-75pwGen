from xkcd_pw_gen import xkcd_pw_gen
import string


def it_pw_gen():
    pw = string.capwords(xkcd_pw_gen())

    pw = pw.replace('a', '4')
    pw = pw.replace('e', '3')
    pw = pw.replace('i', '1')
    pw = pw.replace('o', '0')
    pw = pw.replace('u', '\\_/')
    print(pw)


it_pw_gen()
