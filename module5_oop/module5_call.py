from module5_mod import IntegerStore

def main():
    store = IntegerStore()
    try:
        total_number_of_ints = int(input("Enter N number of ints: "))
        if total_number_of_ints <= 0:
            print("Only positive numbers allowed.")
            return

        for i in range(total_number_of_ints):
            num = int(input(f"Enter number {i+1}: "))
            store.add_num(num)

        x = int(input("Enter the number to search for: "))
        result = store.find_num(x)
        if result == -1:
            print("-1")
        else:
            print(f"Found at position: {result}")

    except ValueError:
        print("Invalid input. Please enter only integers.")

if __name__ == "__main__":
    main()

