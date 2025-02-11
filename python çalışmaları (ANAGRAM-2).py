tek_hal = []
cift_hal = []

def anagram_mi(kelime1, kelime2):
    # Kelimeleri küçük harfe çevirip, harflerini sıralayarak karşılaştırıyoruz
    B= sorted(kelime1.lower())
    C= sorted(kelime2.lower())
    for i in B:
        if i not in tek_hal:
            tek_hal.append(i)

    for i in C:
        if  i not in cift_hal:
            cift_hal.append(i)

    if tek_hal == cift_hal:
        return True

    else:
        return False

# Kullanıcıdan kelimeleri alalım
kelime1 = input("Birinci kelimeyi girin: ")
kelime2 = input("İkinci kelimeyi girin: ")

# Anagram kontrolü yapalım
if anagram_mi(kelime1, kelime2):
    print(f"'{kelime1}' ve '{kelime2}' anagramdır.")
else:
    print(f"'{kelime1}' ve '{kelime2}' anagram değildir.")


print(f"Liste budur {tek_hal}")
print(f"Liste budur {cift_hal}")
