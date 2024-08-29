file = "235722_L03_76.sorted_coverage.xlsx"

import pandas as pd

df = pd.read_excel(file)

# Gen_Adı_Ekzon kolunundaki genlerin 20x_% kolonundaki değerlerin ortalamasını al ve excele yazdır


print(df.groupby('Gen_Adı_Ekzon')['20x_%'].mean())

asi = df.groupby('Gen_Adı_Ekzon')['20x_%'].mean()

# excel dosyasına yazdır


asi.to_excel(file[:6]+'.xlsx')

