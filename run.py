
# Question 1

nums = [1,1,3,4,5]

def check_duplicates(list):
    """
    Converts list to set and compares lengths of list and set
    to evaluate if duplicates are present. 
    If duplicates are present the set will be shorter.
    """
    compare = set(nums)

    if len(compare) == len(nums):
        return True
    else:
        return False

# Question 3 

def reverse_order(string):
    """
    Takes input of list, reverse list 
    and converts to string
    """
    reversed_list = string[::-1]
    convert_to_string = ""
    final = convert_to_string.join(reversed_list)
    return(final)

test = ["s","t","r","i","n","g"]
print(reverse_order(test))

# Question 4

def palindrome(word):
    """
    Takes string as input and ingores non alpha
    characters.
    Compares equality between inputted word and reversed word
    to determine if palindrome
    """
    remove_special_chars = ""

    for charachter in word:
        if charachter.isalpha():
            remove_special_chars += charachter

    forward = remove_special_chars.lower()
    backward = remove_special_chars[::-1].lower()

    if forward == backward:
        print(f"The word: {remove_special_chars} is a palindrome")
    else:
        print(f"The word: {remove_special_chars} is not a palindrome")


palindrome("navan123")

# Question 5:

def fizz_buzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "Fizzbuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n 

print(fizz_buzz(15))

# Question 6:

def optimus_prime(n):
    """
    Takes each number up to elected integer
    and check if it is prime. 
    If it is it is counted if not it is skipped.
    """
    count = 0
    for num in range(1,n):
        if num <= 1:
            continue
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            count += 1
    print(count)

optimus_prime(7)

# Question 7

def swap_numbers(number):
    """
    converts number to string,
    reverses number.
    Then converts number back to int
    """
    new_number = str(number)
    print(int(new_number[::-1]))

swap_numbers(2557)