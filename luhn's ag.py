def check_algo(card_no):
    sum_odd = 0
    sum_even = 0
    #reverse and take the input
    card_no = card_no.replace(" ", "") 
    card_no = card_no.replace("-", "")
    card_no = card_no[::-1]

    for x in card_no[::2]:
        sum_odd += int(x)

    for x in card_no[1::2]:
        x = int(x) * 2
        if x >= 10:
            sum_even += (1 + (x % 10))
    else:
        sum_even += x

    total = sum_odd + sum_even

    if total % 10 == 0:
        print("Valid  number")
    else:
        print("Invalid  number")
    return total % 10 == 0
card_no = input("Enter card number: ")
check_algo(card_no)
