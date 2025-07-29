def greedy_withdraw(amount, denominations):
    """
    Hàm rút tiền theo thuật toán tham lam.
    amount: Số tiền cần rút
    denominations: Danh sách mệnh giá tiền (VD: [500, 200, 100, 50])
    """
    denominations.sort(reverse=True)  # Sắp xếp giảm dần
    result = {}

    for bill in denominations:
        count = amount // bill
        if count > 0:
            result[bill] = count
            amount -= bill * count

    if amount > 0:
        print("Không thể rút chính xác số tiền với mệnh giá cho trước.")
        return {}

    return result


def main():
    # Ví dụ: rút 860k với các mệnh giá phổ biến ở VN
    denominations = [500, 200, 100, 50, 20, 10]  # Đơn vị: nghìn
    amount = 1790

    print(f"\nRút số tiền: {amount}k")
    result = greedy_withdraw(amount, denominations)

    if result:
        print("Các tờ tiền được chọn:")
        for bill, count in result.items():
            print(f" - {count} tờ {bill}k")
        total = sum(bill * count for bill, count in result.items())
        print("Tổng:", total, "k")

if __name__ == "__main__":
    main()
# Tham lam giải bài toán rút tiền