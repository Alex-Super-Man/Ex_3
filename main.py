from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

# Загружаем датасет Iris
iris = load_iris()
X, y = iris.data, iris.target

# Обучаем модель логистической регрессии
model = LogisticRegression()
model.fit(X, y)

# Предсказываем класс цветка по заданным признакам
prediction = model.predict([[1, 1, 1, 1]])
print("Predicted class:", prediction)
