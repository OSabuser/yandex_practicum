def main():
    print("Hello from introduction!")


def zip_lists(list_length, list1, list2):
    if list_length < 1 or list_length > 1000:
        return
    if len(list1) != len(list2):
        return
    if len(list1) != list_length or len(list2) != list_length:
        return
    if len(list1) < 1 or len(list2) < 1:
        return
    if len(list1) > 1000 or len(list2) > 1000:
        return

    output = []
    for list_element in range(list_length):
        output.append(list1[list_element])
        output.append(list2[list_element])

    return output[:]


# Сложность:  O(N*K)
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


#  N = 24*30*60*60 = 2592000 min, K = 60*60 = 3600 min
if __name__ == "__main__":

    # array = [1 if x % 2 == 0 else 0 for x in range(5)]
    # print(array)
    # array = [x for x in range(5) if x % 2 == 0]
    # print(array)

    total_samples = int(input())
    samples_array = list(map(int, input().split()))
    window_size = int(input())
    print(*get_simple_moving_average_naive(total_samples, samples_array, window_size))
    main()

# Срезы: строка[start:stop:step)


# Необходимо вычислить общее число прямоугольников (w1*h1) не умещающихся целиком на плоскости (rect_w*rect_h)
def calculate_possible_rects(rect_width, rect_height, w1, h1) -> int:
    in_width = rect_width // w1  # Помещается по ширине
    in_height = rect_height // h1  # Помещается по высоте

    not_in_height = int(rect_height % h1 != 0)  # 1 - не все, 0 - поместились все
    not_in_width = int(rect_width % w1 != 0)

    h_rects = not_in_height * in_width + not_in_width * not_in_height
    w_rects = not_in_width * in_height

    total = h_rects + w_rects

    return total
