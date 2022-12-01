def main():
    with open("2020_Day_10/input.txt") as f:
        rows = [int(r) for r in f.read().split("\n")]

    print(sorted(rows))
    last = max(rows)

    index = [1] + [0] * last + [0, 0]
    print(index)

    for r in sorted(rows):
        index[r] = index[r-1] + index[r-2] + index[r-3]
        if r == last:
            print(f"{r=} {index[r]=}")
            break


if __name__ == '__main__':
    main()