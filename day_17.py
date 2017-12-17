

def spinlock(step=3, range_=1):
    # step_forward
    # insert value
    # user insert value location as current_pos

    current = 0
    spinner = [0]
    for index in range(1, range_):
        current = (current + step) % index + 1
        spinner.insert(current, index)

    return spinner


def get_spinlock_result_at_index(step=3, range_=1, index_at=0):
    current = 0
    spinner = [0]
    for index in range(1, range_):
        current = (current + step) % index + 1
        if current == index_at:
            spinner.insert(current, index)

        # feedback -- taking a long time...
        if index % 5_000_000 == 0:
            print('currently at: ', index)
    return spinner


if __name__ == "__main__":
    input = 3
    results = spinlock(step=input, range_=2018)
    print("Part One: ", results[results.index(2017) + 1])  # 638

    input = 394
    element = 1
    results = get_spinlock_result_at_index(step=input, range_=50_000_000, index_at=element)
    print("Part Two: ", results[1])  # 10150888
