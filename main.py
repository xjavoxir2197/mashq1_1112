# 1 - misol
harorat = int(input("Hozirgi haroratni kiriting (°C): "))

if harorat > 30:
    print("Juda issiq, uyda qoling!")
elif 20 <= harorat <= 30:
    print("Havo yaxshi, sayr qiling!")
elif 10 <= harorat < 20:
    print("Havo salqin, ko‘ylagi kiying!")
elif harorat < 0:
    # 0°C dan 10°C gacha bo'lgan holat o'z-o'zidan elif bilan qamrab olinadi, lekin 0°C dan past sovuq deb ajratiladi.
    print("Juda sovuq, ehtiyot bo‘ling!")
else:
    # 0°C dan 10°C gacha bo'lgan holat uchun
    print("Havo sovuq, issiqroq kiyining.")

# 2 - misol
tanlov = input("Tanlang (pizza, burger, salat): ").lower() # Kiritilgan matnni kichik harfga o'tkazamiz

if tanlov == "pizza":
    narx = 50000
    print(f"Tanlovingiz: Pizza. Narx: {narx} ming so‘m.")
elif tanlov == "burger":
    narx = 30000
    print(f"Tanlovingiz: Burger. Narx: {narx} ming so‘m.")
elif tanlov == "salat":
    narx = 20000
    print(f"Tanlovingiz: Salat. Narx: {narx} ming so‘m.")
else:
    print("Bizda bunday taom yo‘q!")

# 3 - misol
yosh = int(input("Yoshingizni kiriting: "))
narx = 100000

if yosh < 18:
    chegirma_foiz = 50
    chegirma_narxi = narx * (1 - chegirma_foiz / 100)
    print(f"Sizga {chegirma_foiz}% chegirma bor! Yangi narx: {int(chegirma_narxi)} so‘m.")
elif 18 <= yosh <= 60:
    print(f"Chegirma yo‘q, to‘liq narx: {narx} so‘m.")
else: # yosh > 60
    chegirma_foiz = 30
    chegirma_narxi = narx * (1 - chegirma_foiz / 100)
    print(f"Keksalarga {chegirma_foiz}% chegirma bor! Yangi narx: {int(chegirma_narxi)} so‘m.")

# 4 - misol
rang = input("Trafik chirog'ining rangini kiriting (qizil, sariq, yashil): ").lower()

if rang == "qizil":
    print("To‘xtang!")
elif rang == "sariq":
    print("Tayyorlaning!")
elif rang == "yashil":
    print("Yuring!")
else:
    print("Bunday rang yo‘q!")

# 5 - misol
tezlik = int(input("Internet tezligini kiriting (Mbps): "))

if tezlik > 100:
    print("Sizda ajoyib tezlik!")
elif 50 <= tezlik <= 100:
    print("Tezlik yaxshi, lekin yaxshilash mumkin.")
elif 10 <= tezlik < 50:
    print("Tezlik past, provayder bilan bog‘laning.")
else: # tezlik < 10
    print("Bu tezlik bilan internet ishlatib bo‘lmaydi!")
