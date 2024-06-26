# Görev 1: Verilen değerlerin veri yapılarını inceleyiniz.

x = 8
type(x)

y = 3.2
type(y)

z = 8j + 18
type(z)

a = "Hello World"
type(a)

b = True
type(b)

c = 23 < 22
type(c)

l = [1,2,3,4]
type(l)

d = {"Name":"Jake","Age":27,"Adress":"Downtown"}
type(d)

t = ("Machine Learning","Data Science")
type(t)

s = {"Python", "Machine Learning", "Data Science"}
type(s)

#Görev 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz,
#kelime kelime ayırınız.

text = "The goal is to turn data into information, and information into insight."
text = text.replace(","," ")
text = text.replace("."," ")
text = text.upper()
text = text.split()
text

#Görev 3: Verilen listeye aşağıdaki adımları uygulayınız

lst =["D","A","T","A","S","C","I","E","N","C","E"]

#Adım 1: Verilen listenin eleman sayısına bakınız.
len(lst)

#Adım 2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
lst[0]
lst[10]

#Adım 3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz
lst[0:4]

#Adım 4: Sekizinci indeksteki elemanı siliniz
lst.pop(8)

#Adım 5: Yeni bir eleman ekleyiniz.
lst.append("B")

#Adım 6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.
lst.insert(8,"N")

#Görev 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.

dict = {'Christian':["America",18],
        'Daisy':["England",12],
        'Antonio':["Spain",22],
        'Dante':["Italy",25]}

#Adım 1: Key değerlerine erişiniz.
dict.keys()

#Adım 2: Value'lara erişiniz
dict.values()

#Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
dict["Daisy"][1] = 13

#Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz
dict["Ahmet"] = ["Turkey",24]

#Adım 5: Antonio'yu dictionary'den siliniz.
del dict["Antonio"]


#Görev 5: Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri
#return eden fonksiyon yazınız.

l = [1,33,22,24,46,79]

def even_odd(l):
    even = []
    odd = []
    for i in l:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even , odd

e , o = even_odd(l)
e
o

#Görev 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri
#bulunmaktadır. Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de
#tıp fakültesi öğrenci sırasına aittir. Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.

ogrenciler = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]

for index,student in enumerate(ogrenciler,1):
    if index < 4:
        print("Mühendislik Fakültesi",index,".Öğrenci:",student)
    else:
        print("Tıp Fakültesi",index - 3 ,".Öğrenci:",student)

#Görev 7: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer
#almaktadır. Zip kullanarak ders bilgilerini bastırınız

ders_kodu = ["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

a = list(zip(ders_kodu,kredi,kontenjan))

print("Kredisi",a[0][1],"olan",a[0][0],"kodlu dersin kontenjanı",a[0][2],"kişidir.")
print("Kredisi",a[1][1],"olan",a[1][0],"kodlu dersin kontenjanı",a[1][2],"kişidir.")
print("Kredisi",a[2][1],"olan",a[2][0],"kodlu dersin kontenjanı",a[2][2],"kişidir.")
print("Kredisi",a[3][1],"olan",a[3][0],"kodlu dersin kontenjanı",a[3][2],"kişidir.")

#Görev 8: Aşağıda 2 adet set verilmiştir. Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını
#eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.

kume1 = set(["data","python"])
kume2 = set(["data","function","qcut","lambda","python","miuul"])

def set_f(x,y):
    if x.issuperset(y):
        return x.intersection(y)
    else:
        return y.difference(x)

set_f(kume1,kume2)