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
plt.show()

#ikinci sıralaması
ikinci = df["Runners-Up"].value_counts()
limitIki = ikinci.max() 
limitIkinci = limitIki + 1 
artisIkinci = np.arange(0,limitIkinci+1 ,1)
figur4 = plt.figure(figsize=(10,6))
eksen4 = figur4.add_axes([0.15,0.2,0.7,0.7])
eksen4.bar(ikinci.index , ikinci.values,color="green",alpha=0.5 )
eksen4.set_title("FIFA Dünya Kupası İkincilik Sayıları", fontsize=14)
eksen4.set_ylabel("İkincilik Sayısı", fontsize=12)
eksen4.set_xticklabels(ikinci.index , rotation=90 , ha="right")
eksen4.set_ylim(0,limitIkinci)
eksen4.set_yticks(artisIkinci)
eksen4.grid(axis="y", linestyle="--", alpha=0.5)  
plt.show()


#üçüncü sıralaması
ucuncu = df["Third"].value_counts()
figur5 = plt.figure(figsize=(10,6))
eksen5 = figur5.add_axes([0.15,0.2,0.7,0.7])
eksen5.bar(ucuncu.index , ucuncu.values,color="red" , alpha = 0.9)
eksen5.set_title("FIFA Dünya Kupası Üçüncülük Sayıları", fontsize=14)
eksen5.set_ylabel("Üçüncülük Sayısı", fontsize=12)
eksen5.set_yticks(artisIkinci)
eksen5.set_ylim(0,limitIkinci)
eksen5.set_xticklabels(ucuncu.index ,rotation=90 , ha="right")
eksen5.grid(axis="y", linestyle="--", alpha=0.4)
plt.show()

#dördüncü sıralaması
dorduncu = df["Fourth"].value_counts()
figur6 = plt.figure(figsize=(10,6))
eksen6 = figur6.add_axes([0.15,0.2,0.7,0.7])
eksen6.bar(dorduncu.index , dorduncu.values,color="blue",alpha = 0.5)
eksen6.set_title("FIFA Dünya Kupası Dördüncü Sayıları", fontsize=14)
eksen6.set_ylabel("Dördüncü Sayısı", fontsize=12)
eksen6.set_yticks(artisIkinci)
eksen6.set_ylim(0,limitIkinci)
eksen6.set_xticklabels(dorduncu.index ,rotation=90,ha="right")
eksen6.grid(axis="y", linestyle="--", alpha=0.5)
plt.show()


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
figur7 = plt.figure(figsize=(12,6))
eksen7 = figur7.add_axes([0.15,0.2,0.7,0.7])

max_value = siralama.max()
y_limit = max_value + 2
y_ticks = np.arange(0 , y_limit + 1 , 1)

eksen7.bar(siralama.index , siralama.values,color="#000000",alpha = 0.7)
eksen7.set_title("FIFA Dünya Kupası İlk Dörtte Bitirme Sayıları", fontsize=14)
eksen7.set_ylabel("İlk Dörtte Bitirme Sayısı", fontsize=12)
eksen7.set_xticklabels(siralama.index,rotation=90 )
eksen7.set_yticks(y_ticks)
eksen7.set_ylim(0,y_limit)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.show()

#en çok gol atılan yıllar ve ülkeleri
df["Etiket"] = df["Country"] + " (" + df["Year"].astype(str) + ")"
gol = df.set_index("Etiket")["GoalsScored"]
gol = gol.sort_values(ascending=False)

maxVa=gol.max()
limitY=maxVa + 10
artisM = np.arange(0 , limitY + 1 , maxVa // 10 )
figur2 = plt.figure(figsize=(13,6.5))
eksen2 = figur2.add_axes([0.15,0.24,0.7,0.7])
eksen2.bar(gol.index , gol.values , color="#00FF00",alpha=0.6)
eksen2.set_ylabel("Gol",fontsize=12)
eksen2.set_title("En Çok Gol Olan Yıllar")
eksen2.set_xticklabels(gol.index , rotation = 90 , ha="right")
eksen2.set_yticks(artisM)
eksen2.set_ylim(0,limitY)
eksen2.grid(axis="y" , linestyle="--" , alpha=0.5)
plt.show()


#en çok katılım(attedance)
katilim = df.set_index("Etiket")["Attendance"]
katilim = katilim.sort_values(ascending=False)
maxV = katilim.max()
yLimit = maxV+50000

yAralik = np.arange(0,yLimit+1,maxV // 15)
figur = plt.figure(figsize=(14,7))
eksen1 = figur.add_axes([0.15,0.23,0.7,0.7])

eksen1.bar(katilim.index ,katilim.values ,color="#A0522D")
eksen1.set_ylabel("Katılım",fontsize=12)
eksen1.set_title("En Çok Seyirci Olduğu Ülkeler")
eksen1.set_xticklabels(katilim.index, rotation=90,ha="right")
eksen1.set_yticks(yAralik)
eksen1.set_ylim(0,yLimit)
eksen1.grid(axis="y",linestyle="--",alpha=0.3)
plt.show()

# Maç Başına Gol Grafiği
df["macBasi"] = df["GoalsScored"].astype(float) / df["MatchesPlayed"].astype(float)
sonuc = df.set_index("Etiket")["macBasi"]
sonuc = sonuc.sort_values(ascending=False)

maxVal = sonuc.max()
limitYa = maxVal + 1
artisMiktari = np.arange(0, limitYa + 1 ,0.4)

figur3 = plt.figure(figsize=(14,7))
eksen3 = figur3.add_axes([0.15,0.22,0.7,0.7])
eksen3.bar(sonuc.index , sonuc.values , color="black")
eksen3.set_ylabel("Maç Başı Gol", fontsize=12)
eksen3.set_title("Dünya Kupası Maç Başına Gol İstatistiği", fontsize=14)
eksen3.set_yticks(artisMiktari)
eksen3.set_xticks(np.arange(len(sonuc.index)))  
eksen3.set_xticklabels(sonuc.index , rotation=90 , ha="right")
eksen3.set_ylim(0, limitYa)
eksen3.grid(axis="y" , linestyle="--", alpha=0.3)
plt.show()
