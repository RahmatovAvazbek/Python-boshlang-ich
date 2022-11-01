#otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta m'alumot kiriting
#  (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring :
# Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan
'''
otam = {'ismi':'azamat','tug`ilgan yili':1973,'shahri':'g`ijduvon'}
print('otamning ismi :',otam['ismi'] , end=' ')
print("otamning tug`ilgan yili" , otam['tug`ilgan yili'], end=' ')
print('otamning shahri ',otam['shahri']), 
'''
#Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. 
# Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh
'''
sevimli_taomlar = {'onam':'shashlik',"otam":'sho`rva','ukam':'pelmen','opam':'somsa','men':'norin'}
for ism,taom in sevimli_taomlar.items() :
        print(f'{ism} ning sevimli taomi {taom}')
'''


#Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting 
# (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.
#Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering. 
# Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.
#Yuqoridagi vazifani if-else yordamida qiling va natijani ham foydalanuvchiga tushunarli ko'rinishda chiqaring.
'''
soz = input('soz kiriting: ')
python = {'integer' : 'butun son' , 'float' : 'haqiqiy son' , 'string' : 'matn' , 'boolean' : 'true yoki false'}
for lugat,tarjima in python.items() :
    if lugat == soz :
        print(f' {tarjima} ')
else :
    print('bunday lug`at mavjud emas')
'''

