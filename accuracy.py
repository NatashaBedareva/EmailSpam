import math
import os
from creatSlovar import del_puct


counter = 0
couter_yspex = 0
content_test = ""

def TEST(name,spam_slovar,ham_slovar,P_spam,P_ham):
    global counter
    global couter_yspex

    for filename in os.listdir("Tests//"+name+"//"):
        try:
            with open("Tests//"+name+"//" + filename,errors='ignore',encoding="utf-8") as f:

                counter+=1
                global content_test

                content_test = f.read()
                content_test = del_puct(content_test)
                content_test = content_test.split(" ")

            P_if_spam = 1
            P_if_ham = 1

            def f2(sl, value):
                if value in sl:
                    return sl[value]
                return 1

            for i in content_test:
                P_if_spam = P_if_spam * f2(spam_slovar, i)
                P_if_ham = P_if_ham * f2(ham_slovar, i)


            a = math.log(P_spam) + math.log(P_if_spam)
            b = math.log(P_ham) + math.log(P_if_ham)


            if (a > b):
                couter_yspex += 1
        finally:
            pass


    print("точность = ", couter_yspex / counter)
    return couter_yspex / counter


def TEST2(name,spam_slovar,ham_slovar,P_spam,P_ham):
    global counter
    global couter_yspex


    with open("test_email.txt",errors='ignore',encoding="utf-8") as f:

        counter+=1
        global content_test

        content_test = f.read()
        content_test = del_puct(content_test)
        content_test = content_test.split(" ")

        P_if_spam = 1
        P_if_ham = 1

        def f2(sl, value):
            if value in sl:
               return sl[value]
            return 1

        for i in content_test:
            P_if_spam = P_if_spam * f2(spam_slovar, i)
            P_if_ham = P_if_ham * f2(ham_slovar, i)


        a = math.log(P_spam) + math.log(P_if_spam)
        b = math.log(P_ham) + math.log(P_if_ham)


    if (a > b):
        couter_yspex += 1


    print("точность = ", couter_yspex / counter)
    return couter_yspex / counter


