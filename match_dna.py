def find_match(sequence, string):

    match_count = 0
    match_positions = []
    for i in range(len(sequence) - len(string) + 1):
        if sequence[i:i+len(string)] == string:
            match_count += 1
            match_positions.append(str(i))
    positions = ", ".join(match_positions)
    print(f"Enter the string: {string}")
    print(f"Total matches: {match_count}")
    print(f"Positions of matches: {positions}\n")


test_seq = "GACATTGTGAACAGTAAAAAAGTCCATGCAATGCGCAAGGAGCAGAAGAGGAAGCAGGGCAAGCAGCGCTCCATGGGCTCTCCCATGGACTACTCTCCTCTGCCCATCGACAAGCATGAGCCTGAATTTGGTCCATGCAGAAGAAAACTGGATGGG"
test_strings = ["AAG", "GTC", "GAG", "ACTA", "ATAT"]
for test_string in test_strings:
    find_match(test_seq, test_string)
