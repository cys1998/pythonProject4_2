import pandas as pd

rose = pd.read_excel('C:/Users/최윤수/Desktop/flowers/일자별경매정보.xls', sheet_name = 0) #장미

y = pd.read_excel('C:/Users/최윤수/Desktop/flowers/일자별경매정보 (1).xls', sheet_name = 0) #국화

z = pd.read_excel('C:/Users/최윤수/Desktop/flowers/일자별경매정보 (2).xls', sheet_name = 0) #거베라

w = pd.read_excel('C:/Users/최윤수/Desktop/flowers/일자별경매정보 (3).xls', sheet_name = 0) #리시안

g = pd.read_excel('C:/Users/최윤수/Desktop/flowers/일자별경매정보 (4).xls', sheet_name = 0) #수국

f = pd.read_excel('C:/Users/최윤수/Desktop/flowers/일자별경매정보 (5).xls', sheet_name = 0) #백합

i = pd.read_excel('C:/Users/최윤수/Desktop/flowers/일자별경매정보 (6).xls', sheet_name = 0) #해바

s = pd.read_excel('C:/Users/최윤수/Desktop/flowers/일자별경매정보 (7).xls', sheet_name = 0) #해바

h = pd.read_excel('C:/Users/최윤수/Desktop/flowers/일자별경매정보 (8).xls', sheet_name = 0) #해바

n = pd.read_excel('C:/Users/최윤수/Desktop/flowers/일자별경매정보 (9).xls', sheet_name = 0) #해바

c = pd.read_excel('C:/Users/최윤수/Desktop/flowers/일자별경매정보 (11).xls', sheet_name = 0) #카네

flower = pd.concat((rose,y,z,w,g,f,i,s,h,n,c), axis=0, ignore_index=True)
flower = flower.drop(columns=['등급','속수량'], axis=0)
print(flower)