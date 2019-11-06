// given an array of integer and a range, peudo-sort the array so that the numbers
// to the left of the last number are less than or equals the last number (pivot)
// and the numbers to the right are larger than the last number
func quickSelect(nums []int, i int, j int) int {
    pivot := nums[j]
    for k := i; k < j; k++ {
        if nums[k] <= pivot {
            swap(nums, i, k)
            i++
        }
    }
    swap(nums, i, j)
    return i
}

func swap(nums []int, i int, j int) {
    temp := nums[j]
    nums[j] = nums[i]
    nums[i] = temp
}
