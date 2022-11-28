import pandas as pd
from kmodes.kmodes import KModes
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv("data_join.csv")

user_count = data["user_id"].value_counts()

# 너무 적은 양의 게임을 가지고 있는 행을 삭제한다.
for i in data["user_id"].unique():
    if user_count[i] <= 10:
        data = data[data["user_id"] != i]

# 유저 아이디와 게임 장르만을 가지는 데이터셋
game_genre = data[["user_id", "genres"]]
print("--------------------------------------")
print(game_genre)
print("--------------------------------------")


# game_genre = pd.DataFrame(game_genre.apply(lambda x : x.split(';')))
# print(game_genre)

# user id를 담은 리스트
id_list = game_genre["user_id"].unique()

# 각각의 유저가 구매한 게임의 장르를 모아놓은 groupby형태의 데이터
result = game_genre.groupby("user_id")["genres"]

# 중복된 값들을 지운 값
result_value = result.unique()

# 유저가 각 장르의 게임을 몇개 가지고 있는지의 데이터
result_count = result.value_counts()

# 유저 id를 인덱스로 가지고 각 장르별 몇개의 게임을 가지고 있는지 담기 위한 비어있는 데이터 프레임
new_data = pd.DataFrame(index = game_genre["user_id"].unique(), columns=[game_genre["genres"].unique()])

# 데이터 프레임에 값 넣기
for id in id_list[:]:
    for value in result_value[id]:
        new_data.loc[(id, value)] = result_count.loc[(id, value)]



new_data = new_data.div(new_data.sum(axis=1), axis = 0).round(3)
# 유저가 가지고 있지 않은 장르는 0으로 치환한다.
new_data = new_data.fillna(0)
print(new_data)

new_data.to_csv("genre_percentage.csv")
