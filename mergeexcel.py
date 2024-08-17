import os
import pandas as pd

# Excel dosyalarının bulunduğu dizin
path = 'D:\\Python Code 2024\\Clean_Data\\Excels'
list_dir = os.listdir(path)

dfs = []

for file in list_dir:
    # Dosya uzantısını kontrol et (Excel dosyası mı?)
    if file.endswith('.xlsx') or file.endswith('.xls'):
        # Dosyanın tam yolunu oluştur
        file_path = os.path.join(path, file)
        try:
            # Excel dosyasını DataFrame olarak oku
            df = pd.read_excel(file_path)
            dfs.append(df)
        except Exception as e:
            print(f"{file_path} dosyasını okurken hata oluştu: {e}")

# DataFrame'leri satır bazında birleştir
merged_df = pd.concat(dfs, axis=0, ignore_index=True)

# Birleştirilmiş DataFrame'i bir CSV dosyasına kaydet
output_path = 'D:\\Python Code 2024\\Clean_Data\\Excels\\sa.xlsx'
merged_df.to_excel(output_path, index=False)

print(f"Birleştirilmiş DataFrame {output_path} yoluna kaydedildi.")
