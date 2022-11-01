#ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
#Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring:
'''
ismlar = ['javohir','shahzod','keldiyor']
print('salom ', ismlar[0] ,'qalayshing')
print(ismlar[1].capitalize(),'ishlaring yaxshimi jora')
print(ismlar[2].upper() + '!' , 'yozib tur munay bir')
'''
#sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik). 
#Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring.
# Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring. 
'''
sonlar = [12 , -5 , 4.32 , -323.323]
print('ro\'yxatdagi 1-va 2-element yig\'indisi : ', sonlar[1]+sonlar[0])
a = sonlar[2] * sonlar[3]
sonlar[0] = 'olma'
sonlar[3] = sonlar[3] / 25
print('ro\'yxatdagi 3-elementni 4-elementga ko\'paytirsa  ', a , 'bo\'ladi')
print(sonlar)
'''
#t_shaxslar va z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning,
# ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting. 
'''
z_shaxslar = ['ota-ona','domlo','do\'stlar']
t_shaxslar = ['amir temur', 'bill geyts', 'beruniy' ]
print(z_shaxslar , t_shaxslar.pop())
'''
#friendsnomli bo'sh ro'yxat tuzing va 
#unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.
'''
friends = []
friends.append('Javohir')
friends.append('shahzod')
friends.append('keldiyor')
print(friends)
'''
#Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang
'''
friends = []
friends.append('Javohir')
friends.append('shahzod')
friends.append('keldiyor')
a = friends.pop()
print('tug\'ilgan kunga keladiganlar :', friends , 'tug\'ilgan kunga kelolmaydiganlar :', a )
'''
#Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
'''
friends = []
friends.append('Javohir')
friends.append('shahzod')
friends.append('keldiyor')
friends.insert(0 , 'otabek')
friends.insert(2 , 'hasan')
friends.insert(5 , 'abdu')
print(friends)
'''
#Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating.
#.pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib,
# mehmonlar ro'yxatiga qo'shing.
'''
friends = []
friends.append('Javohir')
friends.append('shahzod')
friends.append('keldiyor')
friends.append('otabek')
friends.append('hasan')
friends.append('abdu')
print(friends)
yangi_mehmonlar = []
yangi_mehmonlar.append(friends.pop())
print(yangi_mehmonlar)
yangi_mehmonlar.append(friends.pop())
print(yangi_mehmonlar)
yangi_mehmonlar.append(friends.pop())
print(yangi_mehmonlar)
'''



