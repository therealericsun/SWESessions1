# Import your function

from src.addition import add
# from src.subtraction import subtract
# from src.multiplication import multiply
# from src.division import divide
# from src.power import power
# from src.modulo import modulo
# from src.max import max_of_two
# from src.min import min_of_two
# from src.average import average
# from src.is_even import is_even

def main():
    """Main function to demonstrate the use of other functions."""
    print("Calling functions from the 'src' directory:")

    
    # After you write your function, print out its response below.
    print(add(5, 3))  # Example usage of the add function
    # i.e. print(function(input_1, input_2))

    print("All functions called successfully (though they do nothing yet).")

if __name__ == "__main__":
    main()
