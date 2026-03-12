def get_number_of_commits(interns):
    if interns == 0 or interns == 1:
        return 1
    return get_number_of_commits(interns - 1) + get_number_of_commits(interns - 2)


if __name__ == "__main__":
    number_of_interns = int(input())
    print(get_number_of_commits(number_of_interns))
