####GİRİLEN SAYILARI TEK VE ÇİFT OLARAK AYIRAN PROGRAM#######
i = 0
yeni_liste = []

ciftler_listesi = []
tekler_listesi = []


while i < 6:
    SAYİ_GİR = int(input("Bir sayı giriniz:"))
    yeni_liste.append(SAYİ_GİR)
    i += 1

for i in yeni_liste:
    if i % 2 == 0:
        ciftler_listesi.append(i)
    else:
        tekler_listesi.append(i)

print(f"Girdiğiniz sayılarda tek olanlar bunlardır: {tekler_listesi} ve çift olanlar ise bunlardır: {ciftler_listesi}")


