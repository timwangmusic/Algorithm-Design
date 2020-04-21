def find_closest(arr, target):
    left, right = 0, len(arr)-1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid
        elif arr[mid] > target:
            right = mid

    return left if target - arr[left] <= arr[right] - target else right


if __name__ == "__main__":
    array = [1, 4, 5]
    print((find_closest(array, 3)))
