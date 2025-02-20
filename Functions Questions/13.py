#13.Create a function to check if number is armstrong number or not.

def check_armstong(num):
    num_str = str(num)
    num_digit = len(num_str)
    sum = 0

    for digit in num_str:
        sum += int(digit)**num_digit
        if sum == num:
            return True
    return False

num = 153
print(check_armstong(num))


# second way
def check_armstong(num):
    num_str = str(num)
    num_digit = len(num_str)
    sum_powers = sum(int(digit)** num_digit for digit in num_str)

    return num == sum_powers

num = 153
print(check_armstong(num))