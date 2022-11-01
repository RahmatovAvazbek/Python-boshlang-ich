#botir ziyatov
#kabisa yili 400 100 4 
'''
a = int(input('Yil  kiriting : '))
if a % 100 == 0 :
    if a % 400 == 0 :
        print('bu yil kabisa yilidir')
    else :
            print('bu yil kabisa emas')
elif a % 4 == 0 :
    print('bu yil kabisa yilidir')
else :
    print('bu yil kabisamas')
'''
#sariq dev
'''
menu = ['somsa','shashlik','tuxum']
buyurtma = ['osh' ,' manti' , 'shashlik']
for taom in buyurtma :
    if taom in menu:
        print(f"menu da {taom} bor")
    else:
            print(f"menuda {taom} yo\'q")
            '''
#Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing,
 #ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.
'''
Yangi_cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for cars in Yangi_cars:
    if cars == 'gm':
        print(cars.upper())
    else :
        print(cars.title())
'''
#Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring. 
'''
Yangi_cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for cars in Yangi_cars:
    if cars != 'gm':
       print(cars.title())
    else :
        print(cars.upper())
'''
#Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?"
#xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga chiqaring.
'''
login = input('Login uchun ism kiriting: ')
if login.lower() == 'admin' :
    print('"Xush kelibsiz , Admin . Foydalanuvchilar ro\'yxatini ko\'rasizmi?"')
else:
    print(f"Xush kelibsiz , {login}!")
    '''
#Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
'''
a=int(input('1-sonni kiriting:'))
b=int(input('2-sonni kiriting:'))
if a == b :
    print('sonlar teng')
'''
#Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son",
#agar musbat bo'lsa "Musbat son" degan xabarni chiqaring. 
'''
son = int(input('istalgan son kiriting:'))
if son<0 :
    print('Manfiy son')
else :
    print('Musbat son')
'''

#Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring.
#Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring. 
'''
son = int(input('son kiriting :'))
if son>0 :
    b = son**(1/2)
    print(b)
else :
    print('musbat son kiriting!')
'''

