def find_base_stack_energy(sequence):

    energies = {"AA": -4, "AT": -7, "AC": -5, "AG": -11, "TA": -7, "TT": -2, "TC": -3, "TG": -4, "CA": -9, "CT": -5, "CC": -6, "CG": -7, "GA": -9, "GT": -6, "GC": -4, "GG": -11}
    total_energy = 0
    for i in range(len(sequence)-2+1):
        dinucleotide = sequence[i:i+2]
        total_energy += energies[dinucleotide]
    avg_base_stack_energy = total_energy/(len(sequence)-2+1)
    return avg_base_stack_energy


test_seq = "CTCGGATTTGTAAAGATCATGATCTCATACATAGTACCTAGCCATTG"
print(find_base_stack_energy(test_seq))
