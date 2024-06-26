from nada_dsl import Party, SecretInteger, Input, Output

class ComputationProgram:
    def __init__(self, party_name):
        self.party = Party(name=party_name)
        self.input1 = self.create_input("my_int1")
        self.input2 = self.create_input("my_int2")

    def create_input(self, name):
        return SecretInteger(Input(name=name, party=self.party))

    def compute(self):
        # Implement your computation logic here using self.input1 and self.input2
        result = self.input1  # Example computation, replace with actual logic
        return result

    def get_output(self):
        result = self.compute()
        return [Output(result, "my_output", self.party)]

def nada_main():
    program = ComputationProgram("Party1")
    return program.get_output()
