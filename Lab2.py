def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    nums = input()
    nums = nums.split(",")
    nums = [float(i) for i in nums]
    return nums

def calc_average_temperature(nums):
    avg = 0
    for i in nums:
        avg += i/len(nums)
    return avg

def calc_min_max_temperature(nums):
    min_temp = nums[0]
    max_temp = nums[0]
    for i in range(1,len(nums)):
        if nums[i] < min_temp:
            min_temp = nums[i]
        if nums[i] > max_temp:
            max_temp = nums[i]
    return [min_temp, max_temp]

def main():
    display_main_menu()
    nums = get_user_input()
    print("Average is " + str(calc_average_temperature(nums)))
    print("Minimum is " + str(calc_min_max_temperature(nums)[0]))
    print("Maximum is " + str(calc_min_max_temperature(nums)[1]))

if __name__ == "__main__":
    main()