def print_square(n=5):
    for _ in range(n):
        print("*" * n)

def print_left_pyramid(n=5):
    for i in range(n):
        print("*" * (i+1))


if __name__ == "__main__":
    print_square(5)
    print()
    print_left_pyramid(5)
