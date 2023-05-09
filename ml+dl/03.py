

# sample data
bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0]
bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]

smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

# 산점도
# x, y축으로 이뤄진 좌표계에 두 변수(x,y)의 관계를 표현하는 matplotlib
import matplotlib.pyplot as plt

plt.scatter(bream_length, bream_weight)
plt.scatter(smelt_length, smelt_weight)
plt.xlabel('length')
plt.ylabel('weight')
plt.show()  

length = bream_length + smelt_length
weight = bream_weight + smelt_weight

# 리스트 내포
fish_Data = [[l, w] for l, w in zip(length, weight)]

# 정답 data
# python 연산자 오버로딩 사용
# 도미 데이터 35개, 빙어 데이터 14개
# 정답 데이터를 1로 넣는 것을 이진 분류임.
fish_target = [1]*35+[0]*14 

# k-최근접 이웃
from sklearn.neighbors import KNeighborsClassifier
kn = KNeighborsClassifier()

# 훈련 fit
kn.fit(fish_Data, fish_target)
kn.score(fish_Data, fish_target)

# 새로운 데이터 예측 predict
kn.predict([[30,600]])

# 예제 2
# KNeighborsClassifier 매개변수로 샘플 개수 변경 가능, 알고리즘 정확도 변동됨
kn49 = KNeighborsClassifier(n_neighbors=49)

kn49.fit(fish_Data, fish_target)
kn49.score(fish_Data, fish_target)
# 정확도 0.7142857142857143 

