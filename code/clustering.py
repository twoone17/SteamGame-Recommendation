import pandas as pd
from sklearn.cluster import KMeans

data = pd.read_csv("genre_percentage.csv")
model = KMeans(n_clusters = 15)

model.fit(data)
data['cluster'] = model.fit_predict(data)

print(data["cluster"].value_counts())