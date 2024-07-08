from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    party3 = Party(name="Party3")
    party4 = Party(name="Party4")

    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party2))
    my_int3 = SecretInteger(Input(name="my_int3", party=party3))

    # Basic arithmetic operations
    sum_result = my_int1 + my_int2
    product_result = my_int1 * my_int2
    difference_result = my_int1 - my_int2
    quotient_result = my_int1 / my_int2

    # Conditional logic
    max_result = (my_int1 < my_int2).if_else(my_int2, my_int1)

    # Custom function using the @nada_fn decorator
    @nada_fn
    def custom_operation(a: SecretInteger, b: SecretInteger, c: SecretInteger) -> SecretInteger:
        return (a + b) * (a - c) + (b * c)

    custom_result = custom_operation(my_int1, my_int2, my_int3)

    # Function to calculate the square of a number
    @nada_fn
    def square(a: SecretInteger) -> SecretInteger:
        return a * a

    square_result1 = square(my_int1)
    square_result2 = square(my_int2)
    square_result3 = square(my_int3)

    # Function to compute the minimum of three numbers
    @nada_fn
    def min_value(a: SecretInteger, b: SecretInteger, c: SecretInteger) -> SecretInteger:
        min_ab = (a < b).if_else(a, b)
        return (min_ab < c).if_else(min_ab, c)

    min_result = min_value(my_int1, my_int2, my_int3)

    # Additional complex operation involving all three inputs
    @nada_fn
    def complex_operation(a: SecretInteger, b: SecretInteger, c: SecretInteger) -> SecretInteger:
        return (a * b) + (b / c) - (c % a)

    complex_result = complex_operation(my_int1, my_int2, my_int3)

    # Return all results as outputs
    return [
        Output(sum_result, "sum_output", party4),
        Output(product_result, "product_output", party4),
        Output(difference_result, "difference_output", party4),
        Output(quotient_result, "quotient_output", party4),
        Output(max_result, "max_output", party4),
        Output(custom_result, "custom_output", party4),
        Output(square_result1, "square_output1", party4),
        Output(square_result2, "square_output2", party4),
        Output(square_result3, "square_output3", party4),
        Output(min_result, "min_output", party4),
        Output(complex_result, "complex_output", party4)
    ]
