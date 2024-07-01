import os
import glob
import pandas as pd
import subprocess
say =0
# Read the Excel file
df = pd.read_excel('r94.xlsx')
#print(df)
files = glob.glob('*.fq.gz')
#print(files)
for file in files:
    #print(file)
    ilkDosya = file
    ilkDosyaParcali = ilkDosya.split('_')
    #print(ilkDosyaParcali)

    mgiBarkod = ilkDosyaParcali[2]
    #print(mgiBarkod)
    if mgiBarkod == "undecoded":
        continue
    else:
        dosyaGeriKalan = ilkDosyaParcali[3]
       
        lane = ilkDosyaParcali[1].split('0')
        lane = lane[1]
        lane = int(lane)
        mgiBarkod = int(mgiBarkod)
        # print("Lane : ",lane)
        # print("MGI Barkod : ",mgiBarkod)

        bulunan = df[(df['lane'] == lane) & (df['mgiBarkod'] == mgiBarkod)]

        if not bulunan.empty:
            say +=1 
            barkod = int(bulunan['barkod'])
            
            #print(barkod)

            x = f"{barkod}_L0{lane}_{mgiBarkod}_{dosyaGeriKalan}"

            print(x)

            komut = f"mv {ilkDosya} {x}"

            print(komut)

            try:
                subprocess.run(komut, check=True, shell=True)
            except subprocess.CalledProcessError as e:
                print(f"Hata çıktı: {e}")

print(say)
