def greedy_knapsack(items, max_weight):
    """
    items: List các tuple (giá trị, trọng lượng)
    max_weight: trọng lượng tối đa balo
    """
    # Gắn chỉ số để in ra vật nào
    indexed_items = [(i + 1, value, weight) for i, (value, weight) in enumerate(items)]

    # Sắp xếp theo value / weight giảm dần
    indexed_items.sort(key=lambda x: x[1] / x[2], reverse=True)

    selected = []
    total_value = 0
    total_weight = 0

    for idx, value, weight in indexed_items:
        if total_weight + weight <= max_weight:
            selected.append(idx)
            total_weight += weight
            total_value += value

    return selected, total_value, total_weight


def main():
    # Dữ liệu bài toán
    items = [
        (60, 10),   # Vật 1
        (100, 20),  # Vật 2
        (120, 30),  # Vật 3
    ]
    Wmax = 50

    selected, value, weight = greedy_knapsack(items, Wmax)

    print("Các vật được chọn (theo chỉ số):", selected)
    print("Tổng giá trị:", value)
    print("Tổng trọng lượng:", weight)


if __name__ == "__main__":
    main()
# Tham lam giải bài toán balo