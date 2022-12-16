import math



def main():
    lst = [4,101,10,18,17,13,2,37]

    for n in lst:
        print(n,": ", 4*n % 12)

if __name__ == "__main__":
    main()