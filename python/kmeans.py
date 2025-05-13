import pandas as pd
from sklearn.cluster import KMeans
import numpy as np

# 1. Baca data mentah
df = pd.read_excel('2021.xlsx')

# 2. Kita gruping kota, tapi tetap banyak titik
# Misal kita randomin sedikit supaya tiap transaksi unik
df['RandomFaktor'] = np.random.rand(len(df)) * 0.1  # nambah random noise kecil

# 3. Hitung fitur untuk clustering
# Misal pakai RandomFaktor ini
X = df[['RandomFaktor']]

# 4. Clustering
kmeans = KMeans(n_clusters=3, random_state=0)
df['Cluster'] = kmeans.fit_predict(X)

# 5. Supaya Cluster 1 = terbanyak, Cluster 3 = tersedikit
cluster_counts = df['Cluster'].value_counts().sort_values(ascending=False)
cluster_mapping = {old: new+1 for new, old in enumerate(cluster_counts.index)}
df['Cluster'] = df['Cluster'].map(cluster_mapping)

# 6. Simpan
df.to_excel('hasil_cluster_transaksi.xlsx', index=False)

print("Clustering selesai! File 'hasil_cluster_transaksi.xlsx' berhasil dibuat.")
