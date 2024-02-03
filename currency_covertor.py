def main():
    print("this program converts us dollar to pound sterling")
    print()

    dollars=eval(input("Enter amount in dollars: "))

    pounds=convert_to_pounds(dollars)

    print("that is ",pounds, "pounds.")

convert_to_pounds=lambda dollars: dollars*0.82

main()
