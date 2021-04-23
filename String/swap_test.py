
str = input("Enter ")

def swap_case(str):
    result = " "
    for letter in str:
        if letter == letter.upper():
            result += letter.lower()
        else:
            result += letter.upper()
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)