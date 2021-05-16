if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)

    maximum = max(arr)
    while maximum in arr:
        arr.remove(max(arr))
    print(max(arr))
