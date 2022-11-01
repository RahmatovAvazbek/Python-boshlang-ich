#Quyidagi o'zgaruvchilarni yarating: 

#kocha="Bog'bon"
#mahalla="Sog'bon"
#tuman="Bodomzor" 
#viloyat="Samarqand"

#Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
'''
#Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati
#print( kocha , "ko'chasi," , mahalla , 'mahallasi,' , tuman , 'tumani,' , viloyat , 'viloyati')
'''
#uqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang.
'''
kocha =input('ko`cha nomini kiriting(son kiritmang yana! shart operatorlariga ancha bor!) : ')
mahalla = input('mahalla nomini kiriting(son kiritmang yana! shart operatorlariga ancha bor!) : ')
tuman = input('tuman nomini kiriting(son kiritmang yana! shart operatorlariga ancha bor!)')
viloyat = input('viloyat nomini kiriting(son kiritmang yana! shart operatorlariga ancha bor!) : ')
print( kocha , "ko'chasi," , mahalla , 'mahallasi,' , tuman , 'tumani,' , viloyat , 'viloyati')
'''
#Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing
'''
kocha =input('ko`cha nomini kiriting(son kiritmang yana! shart operatorlariga ancha bor!) : ')
mahalla = input('mahalla nomini kiriting(son kiritmang yana! shart operatorlariga ancha bor!) : ')
tuman = input('tuman nomini kiriting(son kiritmang yana! shart operatorlariga ancha bor!) : ')
viloyat = input('viloyat nomini kiriting(son kiritmang yana! shart operatorlariga ancha bor!) : ')
print( kocha , "ko'chasi,\n" , mahalla ,"mahallasi,\n" ,tuman , "tumani,\n" ,viloyat , "viloyati")
'''
#Yuqoridagi matnni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga yuklang
'''
kocha =input('ko`cha nomini kiriting(son kiritmang yana! shart operatorlariga ancha bor!) : ')
mahalla = input('mahalla nomini kiriting(son kiritmang yana! shart operatorlariga ancha bor!) : ')
tuman = input('tuman nomini kiriting(son kiritmang yana! shart operatorlariga ancha bor!) : ')
viloyat = input('viloyat nomini kiriting(son kiritmang yana! shart operatorlariga ancha bor!) : ')
yangi_manzil = f' {kocha} {mahalla} {tuman} {viloyat}' 
print(yangi_manzil) 
'''
#manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini qo'llab ko'ring.

kocha =input('ko`cha nomini kiriting(son kiritmang yana! shart operatorlariga ancha bor!) : ')
mahalla = input('mahalla nomini kiriting(son kiritmang yana! shart operatorlariga ancha bor!) : ')
tuman = input('tuman nomini kiriting(son kiritmang yana! shart operatorlariga ancha bor!) : ')
viloyat = input('viloyat nomini kiriting(son kiritmang yana! shart operatorlariga ancha bor!) : ')#yangi_manzil = f' {kocha} {mahalla} {tuman} {viloyat}'
print(yangi_manzil.upper())
print(yangi_manzil.lower())
print(yangi_manzil.title())
print(yangi_manzil.capitalize()) 
