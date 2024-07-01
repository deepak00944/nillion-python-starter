from nada_dsl import *

def nada_main():
    # Define the party involved in the computation
    party1 = Party(name="Party1")
    
    # Define the secret integer inputs for the party
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))
    
    # Perform the desired computation using the secret integers
    # Example: Compute the sum of my_int1 and my_int2
    sum_result = my_int1 + my_int2
    
    # Return the result of the computation as an output
    return [Output(sum_result, "sum_output", party1)]