def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    nums = input()
    nums = nums.split(",")
    nums = [float(i) for i in nums]
    return nums

def calc_average_temperature(nums):
    avg_temp = 0
    for i in nums:
        avg_temp += i/len(nums)
    return avg_temp

def calc_min_max_temperature(nums):
    min_temp = nums[0]
    max_temp = nums[0]
    for i in nums:
        if i < min_temp:
            min_temp = i
        if i > max_temp:
            max_temp = i

    return [min_temp, max_temp]

def sort_temperature(nums):
    nums.sort()
    return nums

def calc_median_temperature(nums):
    n = len(nums)
    if n % 2 == 1:
        return nums[n//2]
    return (nums[n//2] + nums[n//2 - 1])/2
     
def main():
    display_main_menu()
    nums = get_user_input()
    print("Average is " + str(calc_average_temperature(nums)))
    sorted_nums = sort_temperature(nums)
    print("Sorted list is " + str(sorted_nums))
    min_max = calc_min_max_temperature(sorted_nums)
    print("Minimum is " + str(min_max[0]))
    print("Maximum is " + str(min_max[1]))
    print("Median is " + str(calc_median_temperature(sorted_nums)))

if __name__ == "__main__":
    main()