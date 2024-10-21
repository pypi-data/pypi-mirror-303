def imports():
    '''import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.datasets import fetch_openml
from sklearn.metrics import mean_squared_error, r2_score'''

def num1():
    '''california_housing = fetch_openml(name='california_housing', version=1)
data = pd.DataFrame(california_housing.data, columns=california_housing.feature_names)
print(california_housing.DESCR) # Вывод текстового описания датасета
X = california_housing.data
y = california_housing.target'''


def num2():
    '''data = pd.DataFrame(california_housing.data, columns=california_housing.feature_names)
data['target'] = california_housing.target
print(data.describe())
print(data.shape)'''

def num3():
    '''print(data.dtypes) # Вывод типа данных каждого признака и целевой переменной
# Проверка, что все признаки являются числовыми
non_numeric_columns = data.select_dtypes(exclude=['number']).columns

if len(non_numeric_columns) > 0:
    print(f"\nОбнаружены нечисловые колонки: {non_numeric_columns}")
    data = data.drop(columns=non_numeric_columns)
else:
    print("\nВсе признаки являются числовыми.")'''

def num4():
    '''# Проверка наличия пропущенных значений
missing_values = data.isna().sum()
print("Количество пропущенных значений в каждом признаке и целевой переменной:")
print(missing_values)

# Заполнение пропусков медианными значениями, если они есть
if missing_values.any():
    data.fillna(data.median(), inplace=True)
else:
    print("\nПропущенных значений нет.")'''

def num5():
    '''# Построение гистограммы распределения целевой переменной
plt.figure(figsize=(10, 6))
plt.hist(data['target'], bins=30, color='skyblue', edgecolor='black')
plt.title('Гистограмма распределения целевой переменной')
plt.xlabel('Целевая переменная')
plt.ylabel('Частота')
plt.grid(True)
plt.show()
'''

def num6():
    '''X = data.drop(columns=['target'])
y = data['target']
class MultipleRegression(object):
    def __init__(self):
        self.b = None

    def predict(self, x):
        return x @ self.b

    def MSE(self, x, y):
        return (((y - self.predict(x)).T @ (y - self.predict(x))) / (2 * x.shape[0])).values

    def MAE(self, x, y):
        return (abs(y - self.predict(x)).mean()).values

    def MAPE(self, x, y):
        return (abs((y - self.predict(x))/y).mean()).values

    def coefs(self):
        return self.b

    def fit(self, x, y, alpha=0.1, accuracy=0.1, max_steps=10000, intercept=True):
        y = np.array(y).reshape(-1, 1)
        if intercept:
            x['intercept'] = 1
        self.b = np.zeros((x.shape[1], 1))
        steps, errors = [], []
        step = 0
        for _ in range(max_steps):
            dJ_b = x.T @ (self.predict(x) - y) / x.shape[0]
            self.b -= alpha * dJ_b
            new_error = self.MSE(x, y)
            step += 1
            steps.append(step)
            errors.append(new_error)
        return steps, errors
model = MultipleRegression()
steps, errors = model.fit(X, y, alpha = 1e-20, accuracy = 0.01, max_steps = 1000, intercept = True)

# MinMaxScaler() для нормализации данных
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
X_scaled = pd.DataFrame(X_scaled, columns=X.columns)

model_1 = MultipleRegression()
steps, errors = model_1.fit(X_scaled, y, alpha=0.01, accuracy=0.01, max_steps=10000, intercept=True)

y_pred = model_1.predict(X_scaled)
plt.scatter(y_pred, y)
plt.plot(y, y, c='r')
plt.show()

coefficients = model.coefs()
print(coefficients)'''

def num7():
    '''model_sklearn = LinearRegression().fit(X, y)
y_pred = model_sklearn.predict(X)
plt.scatter(y_pred, y)
plt.plot(y, y, c='r')
plt.show()'''

def num8():
    '''# Модель model_1
y_pred = model_1.predict(X_scaled)
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)
print(mse, r2)

# Модель model_sklearn
y_pred = model_sklearn.predict(X)
mse = mean_squared_error(y, y_pred)
r2 = model_sklearn.score(X, y)
print(mse, r2)'''

def dop():
    '''# Полиномиальные модели
def fit_polynoms(degree):
    poly_features = PolynomialFeatures(degree=degree)
    X_poly = poly_features.fit_transform(X_scaled)
    model = LinearRegression()
    model.fit(X_poly, y)
    return model, poly_features

models = {}
poly_features = {}
for degree in [2, 3, 4]:
    models[degree], poly_features[degree] = fit_polynoms(degree)


plt.figure(figsize=(10, 6))
for degree in [2, 3, 4]:
    x = poly_features[degree].transform(X_scaled)
    y_pred = models[degree].predict(x)
    plt.scatter(y_pred, y, label=f'Degree {degree}')
plt.plot(y, y, c='r')
plt.legend()
plt.show()'''