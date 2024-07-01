from nada_dsl import *

def nada_main():
    party = Party("P1")
    result = sum(SecretInteger(Input(f"int{i}", party)) for i in "12")
    Output(result, "result", party)

if _name_ == "_main_":
    nada_main()