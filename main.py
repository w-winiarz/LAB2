import math
from math import *
import sys
# a=56
# print(a)
# print(type(a))
# b=5.5
# print(b)
# print(type(b))
# zmienna_tekstowa='wizualizacja danych'
# print (zmienna_tekstowa)
# print(type(zmienna_tekstowa))

# a=6
# b=3
# c=a+b
# print(c)
# d=a-b
# print(d)
# e=4
# f=b//a
# print(f)
# f=a//b
# print(f)
# g=a**2
# print(g)
# h=pow(a,2)
# print(h)
#
# i=6**(1/2)
# j=pow(6,1/2)
# print(i)
# print(j)
#
# k='wizualizacja danych'
# l=' grupa '
# m=2
# print(k+l+str(m))
# print('liczba a jest rowna {:.2f}, liczba b jest rowna {:d}'.format(a,b))
# a=input('Wprowadz liczbe: ')

# print (a)
# print(type(a))
# a=int(a)
# print(a*5)
# print(type(a))

# sys.stdout.write('Wprowadz liczbe ')
# b=sys.stdin.readline()
# print(b)
# print(type(b))

# lista=[5,6.6,34,'a','b',[2,3,4],'ab']
# print(lista)
# lista.append(67)
# print(lista)
# lista.insert(2,'c')
# print(lista)
# lista.extend([20,21,22])
# print(lista)
# lista.pop()
# print(lista)
# lista.pop(2)
# print(lista)
# lista.remove([2,3,4])
# print(lista)
# del lista[1]
# print(lista)
# del lista
# print (lista)
# lista.reverse()
# print(lista)
# lista.sort()
# print(lista)

# slownik={'klucz':'wartosc',1:2,'a':5,4:'b',1:10}
# print(slownik)
# print(slownik[4])
# slownik[6]=45
# print(slownik)
# slownik.pop(1)
# print(slownik)
# print(slownik.keys())
# print(slownik.values())
# del slownik[6]
# a=8
# b=8
#
# if a>b:
#     print("a is greater than b")
# elif a<b:
#     print("a is less than b")
# else:
#     print("b is equal to a")
# ctrl + d
# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())
# if(a>b)&(c>d):
#     print(a,c)
# else:
#     print(b,d)

# for i in range(2,8,2):
#     print(i)
# else:
#     print('koniec petli')

# for i in lista:
#     print(i)


# for i in range(0,5):
#     for j in range (0,5):
#         result=i+j
#         print(result)
#     print('')

# licznik=0
# while licznik<len(lista):
#     print(lista[licznik])
#     licznik+=1
# else:
#     print('koniec petli')

# licznik=0
# while licznik!=10:
#     if licznik ==7:
#         print(licznik)
#         break
#     else:
#         licznik+=1
# else:
#     print('licznik')
# licznik=0
# lista=[1,2,3,4]
# a=int(input('Wprowadz liczbe'))
# while licznik<len(lista):
#     if(a-lista[licznik]==0):
#         break
#     licznik+=1
# else:
#     print("liczba nie jest z listy")

# LAB3
# try:
#     a = int(input())
#     b = int(input())
#     result = a / b
#     print(result)
# except ZeroDivisionError:
#     print("Error")
# except ValueError:
#     print("Wrong value")
# except Exception:
#     print("Error")
# else:
#     print (result)

# 2 mozliwosci ten sam wynik
# list1 =[1,2,3,4,5,6,7,8,9]
# l2=[]
# for i in list1:
#     l2.append(pow(i,2))
# print(l2)
# l2=[x**2 for x in list1]
# print (l2)
# l3=[3**y for y in range(0,6)]
# print(l3)
# l4=[x for x in l2 if x % 2== 1]
# print(l4)
# l5=[(x,y) for x in l3 for y in l4]
# print(l5)
# l6=[]
# for x in l3:
#     for y in l4:
#         l6.append((x,y))
# print(l6)
# s1={1: 2,2: 3,3: 4,4: 5}
# s2={}
# for key,value in s1.items():
#     s2[value]=key
# print(s1)
# print(s2)
# s3={v:k for k, v in s1.items()}
# print(s3)

# def rownanie_kwadratowe(a, b, c):
#     delta=b**2-4*a*c
#     if delta<0:
#         print("Brak pierwiastków")
#         return 0
#     elif delta==0:
#         print("Jeden pierwiastek")
#
#         x=(-b)/(2*a)
#         return x
#     elif delta>0:
#         print("Dwa pierwiastki")
#         # mozna bez math
#         x1 = (-b + math.sqrt((delta)) / (2 * a))
#         x2 = (-b - math.sqrt((delta)) / (2 * a))
#         return x1,x2
# print(rownanie_kwadratowe(6, 1, 3))
# print(rownanie_kwadratowe(1, 2, 1))
# print(rownanie_kwadratowe(1, 4, 2))

# def dlugosc_odcinka(x1=1,x2=2,y1=3,y2=4):
#     return sqrt((x1-x2)**2+(y1-y2)**2)
#
# print(dlugosc_odcinka())
#
# print(dlugosc_odcinka(4,2,6,3))
#
# print(dlugosc_odcinka(y2=5,y1=5,x2=2, x1=8))
#
# print(dlugosc_odcinka(3,5,y2=4, y1=3))

# plik=open('tekst.txt','r',encoding='utf-8')
# znaki=plik.read(10)
#
# linia=plik.readline()
# linie=plik.readlines()
# plik.close()
# print(znaki)
# print(linia)
# print(linie)
#
# for l in linie:
#     print(l)

# plik=open('tekst.txt','a+')
# plik.write('aaaaa')
# plik.seek(105)
# znaki=plik.read(10)
#
# plik.close()
# print(znaki)

# nie trzeba pamietać o zamknięciu pliku!
# with open('tekst.txt','r') as f:
#     lines=f.readlines()
# print(lines)





