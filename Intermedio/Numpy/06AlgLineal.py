# ALGEBRA LINEAL
import numpy as np
arr1=np.array([[1,2],[3,4]])
arr2=np.array([[1,1],[2,2]])

multip=arr1@arr2
print(f"Multiplicacion de matrices \n{multip}")
print(f"Matriz inversa: \n{np.linalg.inv(arr1)}")
print(f"Matriz transpuesta: \n{np.transpose(arr1)}\n o \n{arr1.T}")
arr3=np.array([1,2,3])
arr4=np.array([1,3,1])
print(f"\nTraza: {np.trace(arr1)}, {np.trace(arr2)}")
print(f"\n Operador Daga: \n{arr1.conj().T}")

print(f"Producto escalar: {np.vdot(arr3,arr4)}")

print(f"Producto vectorial: {np.cross(arr3,arr4)}")

print(f"Producto tensorial: \n{np.kron(arr1,arr2)}")

print(f"\nDeterminante arr1 {np.linalg.det(arr1)} y redondeado {np.round(np.linalg.det(arr1), decimals=2)}")

print(f"La norma: {np.round(np.linalg.norm(arr1), decimals=2)}")

print(f"Los autovalores: {np.round(np.linalg.eigvals(arr1), decimals=2)}")

print(f"Los autovectores: \n{np.round(np.linalg.eig(arr1)[1], decimals=2)}")

Q, R = np.linalg.qr(arr1)
print(f"Q:\n{np.round(Q, 2)}")
print(f"R:\n{np.round(R, 2)}")
print(np.allclose(Q @ R, arr1)) 


A = np.array([[1, 2], [3, 4], [5, 6]])

U, S, Vh = np.linalg.svd(A, full_matrices=False)

print(f"U:\n{np.round(U, 2)}")
print(f"S: {np.round(S, 2)}")
print(f"Vh:\n{np.round(Vh, 2)}")

print(np.allclose(A, U @ np.diag(S) @ Vh)) 


print(f"Pinv de arr1: \n{np.round(np.linalg.pinv(arr1), decimals=2)}")
# Pinv vs inverse, la pinv es la inversa generalizada, que se puede calcular para matrices no cuadradas o singulares.
# La inversa solo se puede calcular para matrices cuadradas y no singulares.