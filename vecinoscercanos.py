from sklearn.neighbors import NearestNeighbors
import numpy as np
import matplotlib.pyplot as plt
# ----------------------------------------
# 1 Creamos algunos puntos de ejemplo
# ----------------------------------------
X = np.array([
    [1, 2],
    [2, 3],
    [3, 4],
    [5, 5],
    [8, 8],
])

# ----------------------------------------
# 2 Definimos el modelo k-NN
# ----------------------------------------

# n_neighbors = número de vecinos más cercanos que queremos encontrar
# metric = tipo de distancia ('euclidean', 'manhattan', etc.)
knn = NearestNeighbors(n_neighbors=2, metric='euclidean') # n_neighbors=2 para coincidir con la imagen

# Entrenamos el índice con nuestros puntos
knn.fit(X)

# ----------------------------------------
# 3 Punto de consulta
# ----------------------------------------

# Este es el punto para el cual queremos buscar los vecinos más cercanos
query_point = np.array([[3.5, 3.5]])

# ----------------------------------------
# 4 Hacemos la consulta k-NN
# ----------------------------------------

# distances: distancias a cada vecino
# indices: posiciones de los vecinos más cercanos en X
distances, indices = knn.kneighbors(query_point)

print("Punto de consulta:", query_point)
print("Vecinos más cercanos (coordenadas):", X[indices][0]) # [0] para que no muestre un array anidado
print("Distancias a los vecinos más cercanos:", distances[0])

# ----------------------------------------
# 5 Visualización
# ----------------------------------------

plt.figure(figsize=(8, 6)) # Tamaño de la figura para una mejor visualización

# 1. Graficar todos los puntos originales
plt.scatter(X[:, 0], X[:, 1], color='blue', s=80, label='Puntos', zorder=2) # zorder para que estén por encima de la cuadrícula

# 2. Graficar el punto de consulta
plt.scatter(query_point[0, 0], query_point[0, 1], color='red', marker='x', s=150, linewidth=2, label='Punto de consulta', zorder=2)

# 3. Obtener los vecinos más cercanos encontrados
nearest_neighbors_points = X[indices[0]]

# 4. Graficar los vecinos más cercanos
plt.scatter(nearest_neighbors_points[:, 0], nearest_neighbors_points[:, 1], color='green', s=100, label='Vecinos más cercanos', zorder=2)

# 5. Dibujar líneas punteadas desde el punto de consulta a los vecinos
for neighbor_point in nearest_neighbors_points:
    plt.plot([query_point[0, 0], neighbor_point[0]], 
             [query_point[0, 1], neighbor_point[1]], 
             'k--', linewidth=1) # 'k--' para línea negra punteada

# Configuración del gráfico
plt.title('k-NN Búsqueda de vecinos más cercanos')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True) # Activa la cuadrícula
plt.legend() # Muestra la leyenda
plt.xlim(0, 8.5) # Ajusta los límites del eje X
plt.ylim(1.5, 8.5) # Ajusta los límites del eje Y
plt.xticks(np.arange(0, 9, 1)) # Marcas del eje X
plt.yticks(np.arange(1, 9, 1)) # Marcas del eje Y
plt.gca().set_aspect('equal', adjustable='box') # Hace que los ejes tengan la misma escala

plt.show() # Muestra el gráfico