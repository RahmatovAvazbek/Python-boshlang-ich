#Quyidagi dasturlarni alohida fayllarga yozing va bajaring:
#Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.
'''
son = int(input('juft son kiriting : '))
if son / 2 == 0 : 
    print('Rahmat!')
elif son / 2 !=0 :
    print('Bu son juft son emas')
'''
#Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
#Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
#Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
#Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
'''
yosh = int(input('yoshingiz nechada?\n>>>'))
if 0 < yosh < 4  or yosh > 60  :
    print('bepul')
elif 4 < yosh < 18 :
    print('10000 so`m')
elif 60 >= yosh >= 18 :
    print('20000 so`m')
elif yosh < 0 :
    print ('yosh manfiy bomaydiku dal@#!$%')
'''
#Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring
'''
a = int(input('1-sonni kiriting: '))
b = int(input('2-sonni kiriting: '))
if a > b :
    print('1-son 2-sondan katta ')
elif a == b :
    print('sonlar teng')
elif a < b :
    print('2-son 1-sondan katta')   
''' 
#mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan bo'sh ro'yxat yarating
# va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring
# va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
'''
savat = []
savat.append(input('savatga mahsulot qo`shing\n>>>'))
savat.append(input('yana savatga mahsulot qo`shing\n>>>'))
savat.append(input('yana savatga mahsulot qo`shing\n>>>'))
savat.append(input('yana savatga mahsulot qo`shing\n>>>'))
savat.append(input('yana savatga mahsulot qo`shing\n>>>'))
savat.append(input('savatga oxirgi mahsulotni qo`shing\n>>>'))
mahsulotlar = []
mahsulotlar.append('kartoshka')
mahsulotlar.append('sabzi')
mahsulotlar.append('piyoz')
mahsulotlar.append('karam')
mahsulotlar.append('qalampir')
mahsulotlar.append('ko`kat')
mahsulotlar.append('go`sht')
mahsulotlar.append('dumba')
mahsulotlar.append('charvi')
mahsulotlar.append('ismaloq')
mahsulotlar.append('ziravor')
for mahsulot in savat :
    if mahsulot.lower in mahsulotlar :
        print(f"{mahsulot} do`konimizda bor")
    else :
        print(f"{mahsulot} do`konimizda yo`q")
'''
# Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang,
# bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing. Agar mavjud_emas ro'yxati bo'sh bo'lsa,
# "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.
'''
savat = []
savat.append(input('savatga mahsulot qo`shing\n>>>'))
savat.append(input('yana savatga mahsulot qo`shing\n>>>'))
savat.append(input('yana savatga mahsulot qo`shing\n>>>'))
savat.append(input('yana savatga mahsulot qo`shing\n>>>'))
savat.append(input('yana savatga mahsulot qo`shing\n>>>'))
savat.append(input('savatga oxirgi mahsulotni qo`shing\n>>>'))
mahsulotlar = []
mahsulotlar.append('kartoshka')
mahsulotlar.append('sabzi')
mahsulotlar.append('piyoz')
mahsulotlar.append('karam')
mahsulotlar.append('qalampir')
mahsulotlar.append('ko`kat')
mahsulotlar.append('go`sht')
mahsulotlar.append('dumba')
mahsulotlar.append('charvi')
mahsulotlar.append('ismaloq')
mahsulotlar.append('ziravor')
bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot.lower() in mahsulotlar :
        bor_mahsulotlar.append(mahsulot.lower())
    else :
        mavjud_emas.append(mahsulot.lower())
if mavjud_emas :
    print(f'quyidagi mahsulotlar do`konimizda yo`q : {mavjud_emas}')
else:
    print('siz so`ragan barcha mahsulotlar do`konimizda bor')


'''
#foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login tanlashni so'rang va
#  foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring.
#  Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.
'''
foydalanuvchilar =[]
foydalanuvchilar.append('avazbek1')
foydalanuvchilar.append('avazbek2')
foydalanuvchilar.append('avazbek3')
foydalanuvchilar.append('avazbek4')
foydalanuvchilar.append('avazbek5')
yangi_login = input('login tanlang : ')
if yangi_login in foydalanuvchilar :
    print('login band, yangi login tanlang! ')
else :
    print('xush kelibsiz, foydalanuvchi !')
'''
#Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring. 

butun_son = int(input('butun son kiriting: '))
b = list(range(2,11))
for son in b :
    if butun_son % son == 0 :
        print(f'{butun_son} soni  {son} ga qoldiqsiz bo`linadi')
else :
    print('tub son kiritmang')