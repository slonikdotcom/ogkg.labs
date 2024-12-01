import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

# Функція для зчитування датасету з файлу
def read_dataset(file_path):
    points = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                x, y = map(int, line.strip().split())
                points.append((x, y))
    except Exception as e:
        print(f"Помилка під час зчитування файлу: {e}")
    return points

# Функція для збереження опуклої оболонки у файл
def save_convex_hull(hull_points, output_file):
    try:
        with open(output_file, 'w') as file:
            for x, y in hull_points:
                file.write(f"{x} {y}\n")
        print(f"Опуклу оболонку збережено у файл: {output_file}")
    except Exception as e:
        print(f"Помилка під час збереження файлу: {e}")

def main():
    dataset_file = "DS2.txt"
    points = read_dataset(dataset_file)
    
    if not points:
        print("Файл порожній або дані не зчитано!")
        return
    
    points = [(x, y) for x, y in points]
    points_array = [[x, y] for x, y in points]
    
    # Знаходження опуклої оболонки
    hull = ConvexHull(points_array)
    hull_points = [points[idx] for idx in hull.vertices]
    
    save_convex_hull(hull_points, "convex_hull.txt")
    
    # Візуалізація
    plt.figure(figsize=(960 / 100, 540 / 100))
    plt.scatter(*zip(*points), color="pink", label="Вихідні точки")
    
    # Відображення опуклої оболонки
    for simplex in hull.simplices:
        plt.plot(
            [points_array[simplex[0]][0], points_array[simplex[1]][0]],
            [points_array[simplex[0]][1], points_array[simplex[1]][1]],
            color="blue",
            linewidth=1.5,
        )
    
    # Налаштування графіка
    plt.axis("off")
    plt.gca().set_facecolor("white")
    plt.legend(loc="upper left")
    
    # Збереження графіку у файл
    output_file = "convex_hull.png" # Формат можна змінити
    plt.savefig(output_file, dpi=100, bbox_inches='tight', pad_inches=0)
    plt.show()
    print(f"Графік з опуклою оболонкою збережено у файл: {output_file}")

if __name__ == "__main__":
    main()
