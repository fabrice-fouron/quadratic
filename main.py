from quadratic import SecondDegree
import time


def main():
    command = input("Enter a command: ")

    if command == 'solve':
        a_val = int(input("Enter the a value: "))
        b_val = int(input("Enter the b value: "))
        c_val = int(input("Enter the c value: "))
        equation = SecondDegree(a_val, b_val, c_val)
        
        print("The standard form of the quadratic is: ", equation.__str__())
        print("Solving eqution...")
        time.sleep(5)
        print(equation.solve())


if __name__ == "__main__":
    main()