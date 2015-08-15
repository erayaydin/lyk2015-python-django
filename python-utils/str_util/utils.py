from random import choice
import re

def is_palindrome(value):
    # Str'ye zorla ve tersiyle kontrol et
    # [::-1] -> dizinin tersini verir
    return str(value) == str(value)[::-1]

def gen_word(list, sayi=10):
    # Boş bir kelime oluştur
    word = ""
    # Belirtilen sayı kadar harf ekle
    for i in range(sayi):
        word = word + choice(list)

    # Oluşan kelimeyi geri döndür
    return word

def is_url(url):
    # http:// ile başlayıp başlamadığını kontrol et
    return url.startswith("http://")

def title_make(value):
    # Boşluklara böl
    wordlist = re.split(" ",value)

    # İlk harfi büyüt
    result = [wordlist[0].capitalize()]

    # Her kelime için(ilki hariç) işlem yap
    for word in wordlist[1:]:
        result.append(word.capitalize())

    # Oluşan kelime listesini cümle haline getir.
    return " ".join(result)

def zip_str(str1, str2):
    result = ""
    length = 0
    if(len(str1) >= len(str2)):
        length = len(str1)
    else:
        length = len(str2)
    x = 0
    for character in range(length):
        if len(str1) >= x+1:
            result = result + str1[x]
        if len(str2) >= x+1:
            result = result + str2[x]
        x += 1
    return result