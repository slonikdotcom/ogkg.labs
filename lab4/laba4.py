import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
from sklearn.cluster import DBSCAN
from shapely.geometry import MultiPoint

# 1. Зчитування даних з файлу
def read_dataset(file_name):
    with open(file_name, 'r') as file:
        points = [tuple(map(int, line.strip().split())) for line in file]
    return np.array(points)

# 2. Групування точок у зв'язані області
def find_connected_regions(points, eps=5, min_samples=1):
    clustering = DBSCAN(eps=eps, min_samples=min_samples).fit(points)
    labels = clustering.labels_
    regions = {}
    for label in set(labels):
        region_points = points[labels == label]
        regions[label] = region_points
    return regions

# 3. Знаходження центру ваги кожної області
def calculate_centroids(regions):
    centroids = {}
    for label, region_points in regions.items():
        if len(region_points) > 0:
            centroid = np.mean(region_points, axis=0)
            centroids[label] = centroid
    return centroids

# 4. Побудова Діаграми Вороного
def plot_voronoi(points, centroids, output_file):
    vor = Voronoi(list(centroids.values()))
    
    # Параметри графіка
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_xlim(0, 960)
    ax.set_ylim(0, 540)
    
    # Побудова Діаграми Вороного
    voronoi_plot_2d(vor, ax=ax, show_vertices=False, line_colors='orange', line_width=1, line_alpha=0.8)
    
    # Відображення центроїдів
    for centroid in centroids.values():
        ax.plot(centroid[0], centroid[1], 'ro', markersize=5)

    # Відображення вихідних точок
    ax.scatter(points[:, 0], points[:, 1], c='black', alpha=0.1, s=5)

    # Збереження зображення
    plt.savefig(output_file, dpi=300)
    plt.close()

# 5. Основна функція
def main():
    input_file = "DS2.txt"
    output_file = "output_voronoi.png"

    # Зчитування датасету
    points = read_dataset(input_file)

    # Знаходження зв'язаних областей
    regions = find_connected_regions(points)

    # Обчислення центрів ваги
    centroids = calculate_centroids(regions)

    # Побудова Діаграми Вороного
    plot_voronoi(points, centroids, output_file)

    print(f"Результати збережено у файл {output_file}")

if __name__ == "__main__":
    main()