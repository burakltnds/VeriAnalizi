df["Etiket3"] = df["Country"] + " (" + df["Year"].astype(str) + ")"
df["macBasi"] = df["GoalsScored"].astype(float)/ df["MatchesPlayed"].astype(float)
sonuc = df.set_index("Etiket3"),["macBasi"]
sonuc = sonuc.sort_values( by="macBasi" ,ascending=False)


maxVal = sonuc.max()
limitYa = maxVal + 1

artisMiktari = np.arange(0, limitYa+1 ,maxVal // 10)

figur3 = plt.figure(figsize=(12,6))
eksen3 = figur3.add_axes([0.1,0.1,0.7,0.7])

eksen3.bar(sonuc.index , sonuc.values , "cyan",alpha=0.5)

eksen3.set_xlabel("Ülke(Yıl)",fontsize=12)
eksen3.set_ylabel("Maç Başı Gol",fontsize=12)
eksen3.set_title("Dünya Kupası Maç Başına Gol İstatistiği" ,fontsize=14)
eksen3.set_yticks(artisMiktari)
eksen3.set_xticklabels(sonuc.index ,rotation=45 , ha="right")
eksen3.set_ylim(0,limitYa)

eksen3.grid(axis="y" , linestyle = "--" , alpha=0.3)
print(sonuc)
plt.show()