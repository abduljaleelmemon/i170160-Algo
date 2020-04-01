# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 15:14:39 2020

@author: Abdul Jalil
"""


import numpy as np
#question1-KMP-part-b
def kmp(pattern):
    print("---KMP---")
    arr=np.zeros(len(pattern))
    for i in range(1,len(pattern)+1):
        stri=pattern[0:i]
        for j in range(len(stri),len(pattern)+1):
            if stri == pattern[j-len(stri):j] and i!=j:
                arr[j-1]=i
    print(arr)
    return arr
#question2-RabinKarp-part-b
def Rk(Text,Pattern,modulo):
    print("---RabinKarp---")
    match=int(Pattern)%modulo
    s_hit=0
    for i in range(len(Pattern),len(Text)+1):
        check=int(Text[i-len(Pattern):i])%modulo
        if check==match and Pattern==(Text[i-len(Pattern):i]):print(Pattern,"match at index:",i-len(Pattern))
        elif check==match:s_hit+=1
    print("Spurious hits:",s_hit)
    return s_hit
#question4-Boyer-Moore-part-b
def BM(text,pattern):
    print("---Boyer-Moore---")
    print(text,pattern)
    lst_p=[]
    for i in pattern:
        lst_p.append(i)
    arr_p=np.array(lst_p)
    uni=np.unique(arr_p)
    arr=np.zeros(len(pattern))
    arr.fill(len(pattern))
    for i in range(len(pattern)):
        ind=np.where(uni==pattern[i])[0]
        if arr[ind]>max(1,len(pattern)-i-1):
            arr[ind]=max(1,len(pattern)-i-1)
    indd=len(pattern)-1
    num=-1
    while(True):
        if indd>len(text)-1:break
        if text[indd]==pattern[-1]:
            if text[indd-len(pattern)+1:indd+1]==pattern:
                print(pattern,"at index",indd-len(pattern)+1)
                num=indd-len(pattern)+1
                break
            w1=np.where(uni==text[indd])[0]
            w1=int(arr[w1[0]])
            indd=indd+w1
        else:
            w1=np.where(uni==text[indd])[0]
            if len(w1)!=0:w1=w1[0]
            else:w1=len(pattern)-1
            w1=int(arr[w1])
            print(w1,text[indd])
            indd=indd+w1
    return num
kmp("aabaabcab")
Rk("3141592653589793","26",11)
BM("this isatest","test")