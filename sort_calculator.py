def swap(IN, i, j):
    IN[i], IN[j] = IN[j], IN[i]

def partition(IN, left, right):
    low = left
    high = right + 1 #while문 안에서 1 감소하기 때문에 1더함
    pivot = IN[left] #피벗은 일단 리스트 첫번째 요소   5 1 9' 6 7 3' -> 5 1 3 6 7 //9

    while True:
        while True:
            low += 1
            if low > right or IN[low] >= pivot:
                break

        while True:
            high -= 1
            if high < left or IN[high] <= pivot:
                break

        if low < high: # low와 high 가 교차하지 않았다면 swap
            swap(IN, low, high)
        else:
            break

    swap(IN, left, high)
    return high

def quick_sort(IN, left, right):
    if left < right:
        q = partition(IN, left, right)
        quick_sort(IN, left, q - 1)
        quick_sort(IN, q + 1, right)

# 사용자 입력
while True:
    try:
        IN = input("숫자 입력: ").split()
        IN = [float(x) for x in IN]
        if not IN:
            raise ValueError("empty input.")
        break
    except ValueError:
        print("invalid input.")

quick_sort(IN, 0, len(IN) - 1)

for x in IN:
    print("%0.1f " % x, end = '')
