# # # # # # # # # # # # # # # 1


# # # # # # # # # # # # # # # radius = 5
# # # # # # # # # # # # # # # pi = 3.14159
# # # # # # # # # # # # # # # yuza = pi * radius**2
# # # # # # # # # # # # # # # print("Radius", radius, "ga teng doira yuzi=", yuza)


# # # # # # # # # # # # # # # 2

# # # # # # # # # # # # # # # ism = "Azizbek"
# # # # # # # # # # # # # # # familya = "Xasanov"
# # # # # # # # # # # # # # # ism_sharif = f"{ism} {familya}"
# # # # # # # # # # # # # # # print(ism_sharif)

# # # # # # # # # # # # # # # 3

# # # # # # # # # # # # # # fname = "James"
# # # # # # # # # # # # # # lname = "Bond"
# # # # # # # # # # # # # # matn = f"salom, mening ismim {lname}. {fname} {lname}!"
# # # # # # # # # # # # # # print(matn)

# # # # # # # # # # # # # pl = "hello \n world"
# # # # # # # # # # # # # print(pl)

# # # # # # # # # # # # pl = "hello \t world"
# # # # # # # # # # # # print(pl)
# # # # # # # # # # # ism = 'Azizbek'
# # # # # # # # # # # familya = 'xasanov'
# # # # # # # # # # # ism_familya = f"{ism} - {familya}"
# # # # # # # # # # # print(ism_familya.upper())
# # # # # # # # # # ism = "Azizbek"
# # # # # # # # # # familya = "Xasanov"
# # # # # # # # # # ism_familya = f"{ism} - {familya}".upper()
# # # # # # # # # # print(ism_familya)
# # # # # # # # # ism = "Azizbek"
# # # # # # # # # familya = "Xasanov"
# # # # # # # # # ism_familya = f"{ism} - {familya}".title()
# # # # # # # # # print(ism_familya)

# # # # # # # # ism = "Azizbek"
# # # # # # # # familya  = "Xasanov"
# # # # # # # # ism_familya = f"{ism} - {familya}".capitalize()
# # # # # # # # print(ism_familya)
# # # # # # # print('james bond'.upper())
# # # # # # # meva = "  olma   "
# # # # # # # meva_olma = "Men " + meva.strip() + " yaxshi koraman"
# # # # # # # print(meva_olma)
# # # # # # # meva = "meva            Salom ".strip()
# # # # # # # print(meva)
# # # # # # # meva = "olma  "
# # # # # # # meva_strip = "Men" + meva + "yaxshi koraman"
# # # # # # # print(meva_strip.strip())
# # # # # # ism = input('ismingiz nima \n')
# # # # # # sorash_ism = "Assalomu  Aleykum   ".strip() + ism
# # # # # # print(sorash_ism)

# # # # # # bir = "Sizni"
# # # # # # ikki = "Ismigiz nima"
# # # # # # uch = input(ikki)
# # # # # # qoshish_qilish = f"{bir} {uch}".lower().title().strip()
# # # # # # print(qoshish_qilish)
# # # # # ism = input("Ismingiz nima?\n>>>")
# # # # # print(f"Assalomu Aleykum, {ism.title()}")

# # # # ism = input("Ismingiz nima?\n>>>")
# # # # ism_Ikki = f"Assalomu Aleykum, {ism.title()}"
# # # # print(ism_Ikki)

# # # kocha = input('kochangizni nomi?\n>>>')
# # # mahalla = input('mahallnigizni nomi ?\n>>>')
# # # tuman = input('tumaningzni nomi?\n>>>')
# # # viloyot = input('viloyatingizni nomi?\n>>> ')

# # # yigish_hammasi = f" {mahalla}  mahallasi {tuman}  tumani {viloyot}  viloyati yashaysiz".strip().title()
# # # print(yigish_hammasi)
# # # kocha = input("kochangizni nomi nima")
# # # print(f"{kocha} kochasi")
# # from pywebio.input import input, input_group
# # a = 20
# # b = -+30
# # c = 0
# # d = a + b
# # print(d)
# kvdt_tmi  = 20
# kvdt_yuzi = kvdt_tmi**2
# print(kvdt_yuzi)

# a = input('1-son')
# b = input('2-son')
# c = int(a) ** int(b)
# print('natija: ', c)
# pi = 3.14342
# radius = 10
# diametr = 2**radius
# print("Aylana uzunligi", pi*diametr, " ga teng")