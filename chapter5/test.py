import pandas as pd
df = pd.read_excel(r'C:\Users\KODI\Desktop\materials_info_old.xlsx')
for index,row in df.iterrows():
    print(f"update ebuy.materials_info_old set materials_code = '0{row['materials_code']}' where materials_id = '{row['materials_id']}';")