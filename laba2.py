import matplotlib.pyplot as plt

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

def main():
    dataset_file = "DS2.txt"
    points = read_dataset(dataset_file)
    
    if not points:
        print("Файл порожній або дані не зчитано!")
        return
    
    x_coords, y_coords = zip(*points)
    
    plt.figure(figsize=(960 / 100, 540 / 100))  # Розміри в дюймах (dpi=100)
    plt.scatter(x_coords, y_coords, color="pink", marker="o")
    plt.axis("off")
    
    plt.gca().set_facecolor("white")
    
    # Збереження результату у файл
    output_file = "result.png"  # Можна змінити на інший формат, наприклад, .jpg
    plt.savefig(output_file, dpi=100, bbox_inches='tight', pad_inches=0)
    plt.show()
    print(f"Графік збережено у файл: {output_file}")

if __name__ == "__main__":
    main()
