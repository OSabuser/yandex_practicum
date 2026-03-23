def get_sequence_len():
    return int(input())


def show_correct_sequence(seq_length):
    def generate_brackets_sequence(prefix, opened, closed):
        if opened == seq_length and closed == seq_length:
            # Количество закрывающих и открывающих скобок равны (seq_length) => имеем ПСП
            # Длина 2*seq_length
            print(prefix)
            return
        if opened < seq_length:
            generate_brackets_sequence(prefix + "(", opened + 1, closed)
        if closed < opened:
            generate_brackets_sequence(prefix + ")", opened, closed + 1)

    generate_brackets_sequence("", 0, 0)


if __name__ == "__main__":
    seq_length = get_sequence_len()
    prefix = ""
    show_correct_sequence(
        seq_length,
    )
