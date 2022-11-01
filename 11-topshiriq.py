#Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. 
#Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring. 
'''
python = {'boolean' : 'mantiqiy qiymat' , 'true' : 'rost' , 'false' : 'yolg`on' , 'kalit' : 'qiymat'}
for kalit,qiymat in python.items() :
    print(f'{kalit.capitalize()} = {qiymat}')
    '''
#Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni,
#keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring. 
'''
davlatlar = {'o`zb':'toshkent','qozoq':'astana','tojik':'dushanbe','amerika':'vashington'}
for kalit,qiymat in davlatlar.items():
    print(f'  {qiymat.capitalize()} ')
'''
#Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). 
#Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan taomlarni menu bilan solishtiring,
#agar taom menuda bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.

menu = {'sho`rva':15000 , 'shashlik':60000,'somsa':20000, 'kola':12000}
ovqat1 = input('1-ovqatni buyurtma bering :\n')
ovqat2 = input('2-ovqatni buyurtma bering :\n')
ovqat3 = input('3-ovqatni buyurtma bering :\n')
buyurtma = []
buyurtma.append(ovqat1)
buyurtma.append(ovqat2)
buyurtma.append(ovqat3)
for taom in buyurtma :
    if taom in menu :
        print(f'{taom.title()} {menu[taom]} turadi\n')
    else :
        print('bizda bunday taom yo`q\n')