def multiplication_table(number):
    """
    Ex. multiplication_table(6) returns "6 12 18 24 30 36 42 48 54 60 66 72 "
    :param number: An integer
    :return: A string of 12 values representing the mulitiplication table of the parameter number.
    """
    table = [(str(number * x)) for x in range(1, 13)]
    return table
def main():
    try:

        the_opps = int(input("Select a number to create a multiplication table for: "))
        if the_opps > 0:
            print(multiplication_table(the_opps))
    except ValueError:
            print("Error, please enter a positive integer.")
            main()
if __name__ == "__main__":
    main()