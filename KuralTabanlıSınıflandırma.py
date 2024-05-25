#Görev 1: Aşağıdaki Soruları Yanıtlayınız.
#Soru 1: persona.csv dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.
import pandas as pd
df = pd.read_csv("Datasets/persona.csv")

df.info()
df.shape
df.head()
df.tail()
df.describe().T
df.columns
df.isnull().values.any()

# Soru 2: Kaç unique SOURCE vardır? Frekansları nedir?
df["SOURCE"].nunique()
df["SOURCE"].unique()
df["SOURCE"].value_counts()

#Soru 3: Kaç unique PRICE vardır?
df["PRICE"].nunique()
df["PRICE"].unique()

# Soru 4: Hangi PRICE'dan kaçar tane satış gerçekleşmiş?
df["PRICE"].value_counts()

#Soru 5: Hangi ülkeden kaçar tane satış olmuş?
df["COUNTRY"].value_counts()

# Soru 6: Ülkelere göre satışlardan toplam ne kadar kazanılmış?
df.groupby("COUNTRY").agg({"PRICE":"sum"})

#Soru 7: SOURCE türlerine göre satış sayıları nedir?
df["SOURCE"].value_counts()

#Soru 8: Ülkelere göre PRICE ortalamaları nedir?
df.groupby("COUNTRY").agg({"PRICE":"mean"})

#Soru 9: SOURCE'lara göre PRICE ortalamaları nedir?
df.groupby("SOURCE").agg({"PRICE":"mean"})

#Soru 10: COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?
df.groupby(["COUNTRY","SOURCE"]).agg({"PRICE":"mean"})

#Görev 2: COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?

df.groupby(["COUNTRY","SOURCE","SEX","AGE"]).agg({"PRICE":"mean"})

#Görev 3: Çıktıyı PRICE’a göre sıralayınız.

agg_df = df.groupby(["COUNTRY","SOURCE","SEX","AGE"]).agg({"PRICE":"mean"}).sort_values(ascending=False,by="PRICE")

#Görev 4: Indekste yer alan isimleri değişken ismine çeviriniz.

agg_df = agg_df.reset_index()

#Görev 5: Age değişkenini kategorik değişkene çeviriniz ve agg_df’e ekleyiniz.
pd.cut(agg_df["AGE"], bins=[0,18,23,30,40,agg_df["AGE"].max()] , labels = ["0_18","19_23","24_30","31_40","41_"+str(agg_df["AGE"].max())])
agg_df["AGE_CAT"] = pd.cut(agg_df["AGE"], bins=[0,18,23,30,40,agg_df["AGE"].max()] , labels = ["0_18","19_23","24_30","31_40","41_"+str(agg_df["AGE"].max())])

#Görev 6: Yeni seviye tabanlı müşterileri (persona) tanımlayınız.

agg_df.drop(["AGE","PRICE"],axis = 1).values

["_".join(i).upper() for i in agg_df.drop(["AGE","PRICE"],axis = 1).values]

agg_df["CUSTOMERS_LEVEL_BASED"] = ["_".join(i).upper() for i in agg_df.drop(["AGE","PRICE"],axis = 1).values]

agg_df.head()

agg_df = agg_df[["CUSTOMERS_LEVEL_BASED","PRICE"]]

agg_df =  agg_df.groupby("CUSTOMERS_LEVEL_BASED").agg({"PRICE":"mean"}).reset_index()

#Görev 7: Yeni müşterileri (personaları) segmentlere ayırınız.

agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"],q=4,labels=["D","C","B","A"])
agg_df.head()

agg_df.groupby("SEGMENT").agg({"PRICE":["mean","sum","min","max"]})

#Görev 8: Yeni gelen müşterileri sınıflandırıp, ne kadar gelir getirebileceklerini tahmin ediniz.

#33 yaşında ANDROID kullanan bir Türk kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?
new_user = "TUR_ANDROID_FEMALE_31_40"
agg_df[agg_df["CUSTOMERS_LEVEL_BASED"] == new_user]

#• 35 yaşında IOS kullanan bir Fransız kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?
new_user2 = "FRA_IOS_FEMALE_31_40"
agg_df[agg_df["CUSTOMERS_LEVEL_BASED"] == new_user2]