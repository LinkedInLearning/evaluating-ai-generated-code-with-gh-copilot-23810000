"""Split a restaurant bill, including tax and tip, among friends."""


def main() -> None:
	bill = float(input("Bill amount: $"))
	tax_rate = float(input("Tax percentage: "))
	tip_rate = float(input("Tip percentage: "))
	people = int(input("Number of people: "))

	if bill < 0 or tax_rate < 0 or tip_rate < 0 or people <= 0:
		raise ValueError("Bill, tax, and tip must be non-negative; people must be positive.")

	tax = bill * tax_rate / 100
	tip = bill * tip_rate / 100
	total = bill + tax + tip

	print(f"Tax: ${tax:.2f}")
	print(f"Tip: ${tip:.2f}")
	print(f"Total: ${total:.2f}")
	print(f"Each person pays: ${total / people:.2f}")


if __name__ == "__main__":
	main()
