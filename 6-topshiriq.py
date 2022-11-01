#O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
#davlatlar = ['o`zbekiston' , 'Qozog`iston' , 'Rossiya' , 'Turkiya' , 'Amerika']

#Ro'yxatning uzunligini konsolga chiqaring
#print(len(davlatlar))

#sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
#print(sorted(davlatlar))

#sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
#print(sorted(davlatlar , reverse=True))

#Asl ro'yxatni qaytadan konsolga chiqaring
#print(davlatlar)

#reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
#davlatlar.reverse()
#print(davlatlar)

#sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
'''
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)
'''
#120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing

#juft_sonlar = list(range(120,1201,2))
#print(juft_sonlar)

#Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
'''
yigindi = sum(juft_sonlar)
print(yigindi)
'''
#Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
'''
kichik = min(juft_sonlar)
print(kichik)
katta = max(juft_sonlar)
print(katta)
print('eng katta va eng kichik sonlar ayirmasi :' , katta - kichik)
'''
#Ro'yxatdagi elementlar sonini hisoblang

#print(len(juft_sonlar))

#Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring

#print(juft_sonlar[0:20])

#taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting

#taomlar = ['g`ilbindi','shashlik','somsa','halisa','tandir']


#nonushta degan yangi ro'yxatga taomlardan nusxa oling

#nonushta = taomlar[:]
#print(nonushta)

#Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
'''
nonushta.pop()
nonushta.pop()
nonushta.pop()
nonushta.append('tuxum')
nonushta.append('gerkules kasha')
print(nonushta)
'''
#Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
'''
nonushta.append('qaymoq va non')
nonushta = tuple(nonushta)
print(nonushta)
'''
