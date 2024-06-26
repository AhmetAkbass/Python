#Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")
df.head()

# Görev 2: Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
df["sex"].value_counts()

# Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz
df.nunique()

# Görev 4: pclass değişkeninin unique değerlerinin sayısını bulunuz.
df["pclass"].nunique()

# Görev 5: pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.
df[["pclass","parch"]].nunique()

#Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz ve tekrar kontrol ediniz.
type(df["embarked"])
df["embarked"] = df["embarked"].astype("category")
df.info()

# Görev 7: embarked değeri C olanların tüm bilgelerini gösteriniz.
df[df["embarked"] == "C"]

# Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.
df[df["embarked"] != "S"]

#Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz
df[((df["age"] < 30 )  & (df["sex"] == "female"))]

# Görev 10: Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.
df[(df["fare"] > 500 ) | (df["age"] > 70 )]

# Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.
df.isnull().sum()

#Görev 12: who değişkenini dataframe’den çıkarınız
df.drop("who",axis =1 , inplace = True)
df.head()

#Görev 13: deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.
df["deck"].fillna(df["deck"].mode()[0])

# Görev 14: age değikenindeki boş değerleri age değişkenin medyanı ile doldurunuz.
df["age"] = df["age"].fillna(df["age"].median())

#Görev 15: survived değişkeninin pclass ve cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz
df.groupby(["pclass","sex"]).agg({"survived": ["sum","count","mean"]})

#Görev 16: 30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazın. Yazdığınız fonksiyonu kullanarak titanik veri
#setinde age_flag adında bir değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız)

df["age_flag"] = df["age"].apply(lambda x : 1 if x < 30 else 0)

#Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.

t = sns.load_dataset("tips")
t.head()

#Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
t.groupby("time").agg({"total_bill":["sum","min","max","mean"]})

#Görev 19: Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
df.groupby(["time","day"]).agg({"total_bill":["sum","min","max","mean"]})

# Görev 20: Lunch zamanına ve kadın müşterilere ait total_bill ve tip değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz.
x = t[(t["time"] == "Lunch") & (t["sex"] == "Female")]
x.groupby("day").agg({"total_bill":["sum","min","max","mean"],
                      "tip":["sum","min","max","mean"]})

#Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir? (loc kullanınız)

t.loc[(t["size"] < 3) & (t["total_bill"] > 10),"total_bill"].mean()

# Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturunuz. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.

t["total_bill_tip_sum"]  = t["total_bill"] + t["tip"]
t.head()

# Görev 23: total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.
t_top30 = t["total_bill_tip_sum"].sort_values().head(30)