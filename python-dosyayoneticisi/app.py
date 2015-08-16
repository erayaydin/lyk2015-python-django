from dosyayoneticisi import DosyaYoneticisi

dy = DosyaYoneticisi("test.txt", True)
print(dy.oku())
print(dy.populer(3))
print(dy.ilk_harf())
print(dy.wc())