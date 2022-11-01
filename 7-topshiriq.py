#Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
'''
ismlar = ['Avaz','Asil','Elshod','orif','firdavs']
for ism in ismlar:
    
    print(f"{ism} qalay xay")

#Yuoqirdagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
n = len(ismlar)
print('kod', n , 'marta takrorlandi')
'''
#10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
'''
toq = list(range(11,100,2))
for n in toq :
    print(f'{n**3}')
print(toq)
'''
#Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
'''
kinolar = []
print('5 ta eng sevimli kinolaringizni kiriting')
for kino in range(5):
    kinolar.append(input(f"{kino+1}-kino nomini kiriting:"))
    print(kinolar)
'''
#Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, 
#va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring
'''
n = []
a = int(input('bugun nechta odam bilan uchrashdingiz?\n'))
for k in range(a):
    n.append(input(f'{k+1}-odamning idmini kiriting :'))
    print('siz' , n , 'shular bilan uchrashibsiz!')
'''
