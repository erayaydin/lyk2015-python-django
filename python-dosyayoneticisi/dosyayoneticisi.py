import collections

class DosyaYoneticisi:
    def __init__(self, filename=None, live=False):
        if filename == None:
            print("Please define filename!")
        else:
            self.file = filename

        self.live = live
        self.content = self.oku()

    def oku(self):
        try:
            file = open(self.file, 'r')
        except FileNotFoundError as e:
            print("File not found!")
        except PermissionError as e:
            print("File permission error!")
        else:
            self.content = file.read()
            file.close()
            return self.content

    def populer(self, limit=None):
        if self.live: self.oku()

        # dosya içeriğini kelimelere böl
        kelimeler = self.content.split(" ")
        counter = collections.Counter(kelimeler)
        mostcommon = counter.most_common()

        if limit == None:
            return mostcommon
        else:
            print(mostcommon)
            sonuc = {}
            for i in range(limit):
                sonuc[mostcommon[i][0]] = mostcommon[i][1]
            return sonuc

    def ilk_harf(self):
        if self.live: self.oku()

        satirlar = self.content.split("\n")
        sonuc = ""
        for i in range(len(satirlar)):
            if len(satirlar[i]) > 0:
                sonuc += satirlar[i][0]
        return sonuc

    def wc(self):
        if self.live: self.oku()
        karakter = len(self.content)
        kelime = len(self.content.split(" "))
        satir  = len(self.content.split("\n"))
        return [karakter, kelime, satir]