def main():
	int_store = []
	total_number_of_ints = int(input("Enter N number of ints: "))
	if total_number_of_ints < 0:
		print("Only positive numbers bro!")
	elif total_number_of_ints == 0:
		print("You inputted 0, goodbye")
		return
	else:	
		print("Getting nums from 1->N")
		for num in range(total_number_of_ints):
			curr_num = input("Enter number: ")
			int_store.append(curr_num)
		num_to_test = input("Enter test number: ")
		if num_to_test in int_store:
			print(f"FOUND IT AT index: {int_store.index(num_to_test)}")
		else:
			print(-1)


if __name__ == "__main__":
	main()
