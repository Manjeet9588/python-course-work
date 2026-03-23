'''The first line contains N and M separated by a space.
The next N lines each contain M elements.
The last line contains K .'''

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input().strip())

    arr.sort(key=lambda item: item[k])

    count = 0
       # products.sort(key=lambda item: item[1])
    for array in arr:
        for a in array:
            print(f"{a}",end=" ")
            count += 1
            if count % m == 0:
                print()
