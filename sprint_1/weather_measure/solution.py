# Метеорологическая служба вашего города решила исследовать погоду новым способом.
# Под температурой воздуха в конкретный день будем понимать максимальную температуру в этот день
# Под хаотичностью погоды за n дней служба понимает количество дней, в которые температура
# строго больше, чем в день до (если такой существует) и в день после текущего
# (если такой существует). Например, если за 5 дней максимальная температура воздуха составляла
# [1,2,5,4,8]  градусов, то хаотичность за этот период равна 2:
# в 3-й и 5-й дни выполнялись описанные условия.
# Определите по ежедневным показаниям температуры хаотичность погоды за этот период
# Заметим, что если число показаний n = 1, то единственный день будет хаотичным.


def get_temp_data():
    n = int(input())

    if n <= 0 or n > 100000:
        return

    return list(map(int, input().split()))


if __name__ == "__main__":
    measurements = get_temp_data()

    if measurements is not None:
        if all(abs(value) <= 273 for value in measurements):
            days = len(measurements)

            if days == 1:
                print(1)
            else:
                count = 0

                if measurements[0] > measurements[1]:
                    count += 1

                if measurements[-1] > measurements[-2]:
                    count += 1

                if days > 2:
                    for day_number in range(1, days - 1):
                        if (
                            measurements[day_number] > measurements[day_number - 1]
                            and measurements[day_number] > measurements[day_number + 1]
                        ):
                            count += 1

                print(count)
