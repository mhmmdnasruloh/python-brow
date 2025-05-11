import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# Membaca data dari file Excel
# Gantilah 'data_pesanan.xlsx' dengan nama file Excel Anda
df = pd.read_excel('2021.xlsx')

# Melihat beberapa data pertama untuk memastikan format
print(df.head())

# Encode data kategorikal menjadi numerik
label_encoder_kota = LabelEncoder()
df['Kota/Kabupaten_encoded'] = label_encoder_kota.fit_transform(df['Kota/Kabupaten'])

label_encoder_provinsi = LabelEncoder()
df['Provinsi_encoded'] = label_encoder_provinsi.fit_transform(df['Provinsi'])

# Menyiapkan data untuk clustering
X = df[['Kota/Kabupaten_encoded', 'Provinsi_encoded']]

# Terapkan K-Means untuk clustering (misalnya 3 cluster)
kmeans = KMeans(n_clusters=3, random_state=42)  # Membuat 3 cluster
df['Cluster'] = kmeans.fit_predict(X)

# Visualisasi hasil clustering menggunakan scatter plot
plt.figure(figsize=(10,8))
plt.scatter(df['Kota/Kabupaten_encoded'], df['Provinsi_encoded'], c=df['Cluster'], cmap='viridis', s=100)

# Menambahkan nama kota/kabupaten pada plot
for i, row in df.iterrows():
    plt.text(row['Kota/Kabupaten_encoded'], row['Provinsi_encoded'], row['Kota/Kabupaten'], 
             horizontalalignment='center', verticalalignment='center', fontsize=9)

# Menandai centroid dari setiap cluster
centroids = kmeans.cluster_centers_
plt.scatter(centroids[:, 0], centroids[:, 1], s=200, c='red', marker='X', label='Centroid')

# Menambahkan label dan title
plt.title('Clustering Wilayah Berdasarkan Data Pesanan')
plt.xlabel('Kota/Kabupaten')
plt.ylabel('Provinsi')
plt.legend()
plt.grid(True)
plt.show()

# Tampilkan hasil clustering dalam DataFrame
print(df)
