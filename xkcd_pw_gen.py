import random
from password_good import nouns
from password_good import verbs
from password_good import adjs

pw = ""

for i in range(4):
    selector = random.randint(0, 2)

    if selector == 0:
        selector = nouns
    elif selector == 1:
        selector = verbs
    else:
        selector = adjs

    pw = pw + selector[random.randint(0, len(selector) - 1)]

print("password is: ", pw)
