import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("WorldCup.csv")



#sampiyonlar sıralaması
sampiyon = df["Winner"].value_counts()
plt.figure(figsize=(10, 6))
plt.bar(sampiyon.index, sampiyon.values, color="gray")
plt.title("FIFA Dünya Kupası Şampiyonluk Sayıları", fontsize=14)
plt.ylabel("Şampiyonluk Sayısı", fontsize=12)
plt.xticks(rotation=25)
plt.grid(axis="y", linestyle="--", alpha=0.7)  
#plt.show()

#ikinci sıralaması
ikinci = df["Runners-Up"].value_counts()
plt.figure(figsize=(10,6))
plt.bar(ikinci.index , ikinci.values,color="red")
plt.title("FIFA Dünya Kupası İkincilik Sayıları", fontsize=14)
plt.ylabel("İkincilik Sayısı", fontsize=12)
plt.xticks(rotation=25)
plt.grid(axis="y", linestyle="--", alpha=0.7)  
#plt.show()

#üçüncü sıralaması
ucuncu = df["Third"].value_counts()
plt.figure(figsize=(10,6))
plt.bar(ucuncu.index , ucuncu.values,color="red")
plt.title("FIFA Dünya Kupası Üçüncülük Sayıları", fontsize=14)
plt.ylabel("Üçüncülük Sayısı", fontsize=12)
plt.xticks(rotation=25)
plt.grid(axis="y", linestyle="--", alpha=0.7)
#plt.show()

#dördüncü sıralaması
dorduncu = df["Fourth"].value_counts()
plt.figure(figsize=(10,6))
plt.bar(dorduncu.index , dorduncu.values,color="red")
plt.title("FIFA Dünya Kupası Dördüncü Sayıları", fontsize=14)
plt.ylabel("Dördüncü Sayısı", fontsize=12)
plt.xticks(rotation=25)
plt.grid(axis="y", linestyle="--", alpha=0.7)
#plt.show()

#en çok ilk 4 de olma(yarı finale kalma)
tum = set(df["Fourth"].dropna().unique()) | \
            set(df["Third"].dropna().unique()) | \
            set(df["Winner"].dropna().unique()) | \
            set(df["Runners-Up"].dropna().unique())
siralama = (
    df["Fourth"].value_counts(dropna=True).reindex(tum,fill_value=0) + 
    df["Third"].value_counts(dropna=True).reindex(tum,fill_value=0) + 
    df["Winner"].value_counts(dropna=True).reindex(tum,fill_value=0) + 
    df["Runners-Up"].value_counts(dropna=True).reindex(tum , fill_value=0)
)
siralama = siralama.sort_values(ascending=False)
plt.figure(figsize=(12,6))
max_value = siralama.max()
y_limit = max_value + 2
y_ticks = np.arange(0 , y_limit + 1 , 1)
plt.bar(siralama.index , siralama.values,color="red")
plt.title("FIFA Dünya Kupası İlk Dörtte Bitirme Sayıları", fontsize=14)
plt.ylabel("İlk Dörtte Bitirme Sayısı", fontsize=12)
plt.xticks(rotation=45)
plt.yticks(y_ticks)
plt.grid(axis="y", linestyle="--", alpha=0.7)
#plt.show()


#en çok gol atılan yıllar ve ülkeleri

df["Etiket2"] = df["Country"] + " (" + df["Year"].astype(str) + ")"

gol = df.set_index("Etiket2")["GoalsScored"]
gol = gol.sort_values(ascending=False)

maxVa=gol.max()
limitY=maxVa + 10
artisM = np.arange(0 , limitY + 1 , maxVa // 10 )
figur2 = plt.figure(figsize=(12,6))
eksen2 = figur2.add_axes([0.1,0.1,0.7,0.7])
eksen2.bar(gol.index , gol.values , color="#00FF00",alpha=0.3)
eksen2.set_ylabel("Gol",fontsize=12)
eksen2.set_xlabel("Ülke(Yıl)")
eksen2.set_title("En Çok Gol Olan Yıllar")
eksen2.set_xticklabels(gol.index , rotation = 45 , ha="right")
eksen2.set_yticks(artisM)
eksen2.set_ylim(0,limitY)
eksen2.grid(axis="y" , linestyle="--" , alpha=0.5)


#en çok katılım(attedance)
df["Etiket"] = df["Country"] + " (" + df["Year"].astype(str) + ")"
katilim = df.set_index("Etiket")["Attendance"]
katilim = katilim.sort_values(ascending=False)
maxV = katilim.max()
yLimit = maxV+50000

yAralik = np.arange(0,yLimit+1,maxV // 15)
figur = plt.figure(figsize=(12,6))
eksen1 = figur.add_axes([0.2,0.2,0.7,0.7])

eksen1.bar(katilim.index ,katilim.values ,color="red")
eksen1.set_xlabel("Ülkeler" , fontsize=9)
eksen1.set_ylabel("Katılım",fontsize=9)
eksen1.set_title("En Çok Katılımın Olduğu Ülkeler")
eksen1.set_xticklabels(katilim.index, rotation=45,ha="right")
eksen1.set_yticks(yAralik)
eksen1.set_ylim(0,yLimit)
eksen1.grid(axis="y",linestyle="--",alpha=0.3)



# Maç Başına Gol Grafiği
df["Etiket3"] = df["Country"] + " (" + df["Year"].astype(str) + ")"
df["macBasi"] = df["GoalsScored"].astype(float) / df["MatchesPlayed"].astype(float)
sonuc = df.set_index("Country")["macBasi"]

sonuc = sonuc.sort_values(ascending=False)

maxVal = sonuc.max()
limitYa = maxVal + 1

artisMiktari = np.arange(0, limitYa + 1 ,1)

figur3 = plt.figure(figsize=(12,6))
eksen3 = figur3.add_axes([0.1,0.1,0.7,0.7])

eksen3.bar(sonuc.index , sonuc.values , color="cyan", alpha=0.5)

eksen3.set_xlabel("Ülke(Yıl)", fontsize=12)
eksen3.set_ylabel("Maç Başı Gol", fontsize=12)
eksen3.set_title("Dünya Kupası Maç Başına Gol İstatistiği", fontsize=14)
eksen3.set_yticks(artisMiktari)
eksen3.set_xticks(np.arange(len(sonuc.index)))  # Bu satırı düzelttik
eksen3.set_xticklabels(sonuc.index , rotation=45 , ha="right")
eksen3.set_ylim(0, limitYa)

eksen3.grid(axis="y" , linestyle="--", alpha=0.3)

plt.show()

