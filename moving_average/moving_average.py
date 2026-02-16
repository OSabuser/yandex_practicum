import matplotlib.pyplot as plt


def get_simple_moving_average_naive(measure_time, values, window_size):
    if measure_time < 1 or measure_time > 10**5:
        return

    if not all(0 <= n <= 1000 for n in values):
        return

    length = len(values)

    if measure_time != length:
        return

    if window_size < 1 or window_size > length:
        return

    average = []
    # Размер результирующего массива = measure_time - window_size + 1 (n - k + 1)
    for i in range(0, measure_time - window_size + 1):
        average.append(sum(values[i : i + window_size]) / window_size)

    return average


def get_simple_moving_average_enhanced(measure_time, values, window_size):
    if measure_time < 1 or measure_time > 10**5:
        return

    if not all(0 <= n <= 1000 for n in values):
        return

    length = len(values)

    if measure_time != length:
        return

    if window_size < 1 or window_size > length:
        return

    average = []
    current_sum = sum(values[:window_size])
    average.append(current_sum / window_size)  # Первая итерация
    # Размер результирующего массива = measure_time - window_size + 1 <=> (n - k + 1)
    for index in range(0, measure_time - window_size):
        current_sum -= values[index]
        current_sum += values[index + window_size]
        average.append(current_sum / window_size)

    return average


def create_demo_subplots(samples_array):

    # Создание сетки 3 строки × 3 столбца
    fig, axes = plt.subplots(3, 3)
    # До фильтрации
    axes[0, 0].plot(
        list(range(len(samples_array))),
        samples_array,
        linestyle="-",
        color="red",
    )
    axes[0, 0].grid(True)
    axes[0, 0].set_title("Данные до фильтрации")
    axes[0, 0].set_xlabel("Секунды")
    axes[0, 0].set_ylabel("Собачки")

    ncol = 0
    nrow = 1

    for window_size in range(1, 9):
        filtered_array = get_simple_moving_average_enhanced(
            len(samples_array), samples_array, window_size
        )
        axes[nrow, ncol].plot(
            list(range(len(filtered_array))),
            filtered_array,
            "bo-",
            linestyle="-",
            color="blue",
            markersize=3,
            linewidth=2,
        )
        axes[nrow, ncol].grid(True)
        axes[nrow, ncol].set_title(f"Данные после фильтрации, K = {window_size}")
        axes[nrow, ncol].set_xlabel("Секунды")
        axes[nrow, ncol].set_ylabel("Собачки")

        nrow += 1
        if nrow == 3:
            nrow = 0
            ncol += 1

        if ncol == 3:
            ncol = 0

    plt.tight_layout()
    plt.show()


samples_array = [
    4,
    3,
    8,
    1,
    5,
    6,
    3,
    4,
    7,
    8,
    9,
    10,
    11,
    4,
    6,
    4,
    2,
    3,
]

create_demo_subplots(samples_array)
