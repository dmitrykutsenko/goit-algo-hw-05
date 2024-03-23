# Binary search example

def binary_search(arr, x):
    """
    Функція двійкового пошуку для відсортованого масиву з дробовими числами.

    Args:
        arr: Відсортований масив з дробовими числами.
        x: Значення, яке потрібно знайти.

    Returns:
        Кортеж з двох елементів:
        - Кількість ітерацій, необхідних для знаходження елемента.
        - Верхня межа - найменший елемент, який є більшим або рівним заданому значенню.
    """

    low = 0
    high = len(arr) - 1
    iterations = 0

    while low <= high:
        iterations += 1
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return iterations, arr[mid]

    # Якщо елемент не знайдений
    return (iterations, arr[high] if arr[high] >= x else None)

# Приклад використання
arr = [0.1, 0.52, 1.0, 2.2, 3.14, 4.56, 7.89, 8.31, 9.07, 11.77]


while True:
    # Введення значення для пошуку
    x = input("Введіть значення для пошуку (або exit для виходу): ")

    # Перевірка на exit
    if x.lower() == "exit":
        break
    else:
       
        # Перевірка, чи введено число
        try:
            # Перетворення введенного значення в float
            x = float(x)
        except ValueError:
            print("Введено невірне значення. Спробуйте ще раз.")
            continue

        # Пошук значення
        iterations, upper_bound = binary_search(arr, x)

        # Вивід результатів
        if upper_bound is not None:
            print(f"Елемент знайдений за {iterations} ітерацій. Верхня межа: {upper_bound}")
        else:
            print(f"Елемент не знайдений за {iterations} ітерацій. Верхня межа: {upper_bound}")
