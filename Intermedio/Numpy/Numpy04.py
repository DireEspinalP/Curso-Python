# Distribuciones 
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
#Todas distribuciones con su parametro y tamaño
"""
1) Binomial:            binomial(n, p, size=None)
2) Poisson:             poisson(lam, size=None)
3) Exponential:         exponential(lam, size=None)
4) Uniform:             uniform(low, high, size=None)
5) Normal:              normal(u, sigma, size=None)
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