import numpy as np
import os

def del_puct(stroke):
    stroke = stroke.lower()
    res=''
    for i in stroke:
        if i in "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm":
            res+=i
        else: res +=' '
    return res

def CreatSet(name,arr):
    counter=0
    slovar = {}
    for filename in os.listdir("Lerning//"+name+'//'):
        try:
            with open("Lerning//"+name+'//' + filename,errors='ignore',encoding="utf-8") as f:
                counter+=1
                content = f.read()
                content = del_puct(content)
                content=content.split(" ")
                for i in content:
                    if(i!=''):
                        arr.add(i)
                        if i in slovar:
                            slovar[i]+=1
                        else:
                            slovar[i] =1
        finally:
            pass

    return counter,slovar

def write_slovar(name,slovar,P):
    f = open(name + '.txt', 'w')
    f.write(str(P) + '\n')
    for i in slovar:
        f.write(i +" "+ str(slovar[i]) + '\n')

def CreateSlovarSpamAndHamEmail():

    #main.setLebelText("Start")

    setHamEmail=set([])
    setSpamEmail=set([])

    count_ham_email,ham_slovar = CreatSet('ham',setHamEmail)
    count_spam_email,spam_slovar = CreatSet('spam',setSpamEmail)


    for i in spam_slovar:
        spam_slovar[i]=(spam_slovar[i]+1)/count_spam_email+2

    for i in ham_slovar:
        ham_slovar[i]=(ham_slovar[i]+1)/count_ham_email+2

    P_spam = count_spam_email/(count_spam_email+count_ham_email)
    P_ham = count_ham_email/(count_spam_email+count_ham_email)

    write_slovar('slovarHam',ham_slovar,P_ham)
    print("Created slovarHam ")
    write_slovar('slovarSpam',spam_slovar,P_spam)
    print("Created slovarSpam ")
    return 0


def readSet(name):
    mySet= {}
    f = open(name + '.txt', 'r')
    P = float(f.readline())
    while True:

        line = f.readline().split()
        if not line:
            break

        mySet[line[0]] = float(line[1])
    f.close()

    return mySet,P



