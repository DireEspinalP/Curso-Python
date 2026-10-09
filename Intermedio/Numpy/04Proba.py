import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

"""
La probabilidad de que el valor sea 3 se establece en 0,1.

La probabilidad de que el valor sea 5 se establece en 0,3.

La probabilidad de que el valor sea 7 se establece en 0,6.

La probabilidad de que el valor sea 9 se establece en 0.

"""
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(10))

print(x)

arr2=np.array([[0.1, 0.3 ,0.6]])
print(f"\n Array de probabilidaes {arr2}")
print(f"\n La suma de las prob. del arr es {np.sum(arr2)}") #Suma de elementos

# Distribuciones 
#Todas distribuciones con su parametro y tamaño
"""
1) Binomial:            binomial(n, p, size=None)
2) Poisson:             poisson(lam, size=None)
3) Exponential:         exponential(scale, size=None)
4) Uniform:             uniform(low, high, size=None)
5) Normal:              normal(loc, scale, size=None)
6) Chi-square:          chisquare(df, size=None)
7) t-Student:            t(df, size=None)
"""
# Usaremos 
# sns.displot para graficar las distribuciones 
# plt.show() para mostrar la grafica

sns.displot(random.binomial(10, 0.4, size=1000))
plt.show()

sns.displot(random.poisson(2,size=1000))
plt.show()

sns.displot(random.exponential(2,size=1000))
plt.show()
sns.displot(random.exponential(size=1000), kind="kde")
plt.show()

sns.displot(random.uniform(1,3,size=1000))
plt.show()
sns.displot(random.uniform(size=1000), kind="kde")
plt.show()

sns.displot(random.normal(1.2, 0.5 , size=10000))
plt.show()
sns.displot(random.normal(size=1000), kind="kde")
plt.show()

sns.displot(random.chisquare(1.3 , size=10000))
plt.show()
sns.displot(random.chisquare(df=2, size=1000), kind="kde")
plt.show()

sns.displot(random.t(1.3 , size=10000))
plt.show()
sns.displot(random.t(df=2, size=1000), kind="kde")
plt.show()
#kind="kde" grafica la densidad de probabilidad de la distribucion, en lugar del histograma

# Comparacion de distribuciones

data = {
  "normal": random.normal(loc=50, scale=5, size=1000),
  "binomial": random.binomial(n=100, p=0.5, size=1000)
}

sns.displot(data, kind="kde")
plt.show()