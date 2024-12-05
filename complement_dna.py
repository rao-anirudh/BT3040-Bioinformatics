def complement(sequence):

    """
    Returns the complementary sequence (in 3' to 5' direction) of a given DNA sequence (in 5' to 3' direction)

    """

    complement = {"A": "T", "T": "A", "G": "C", "C": "G"}
    complementary = ""
    for base in sequence:
        complementary += complement[base]
    return complementary


test_seq = "CTCGGATTTGTAAAGATCATGATCTCATACATAGTACCTAGCCATTG"
ans = complement(test_seq)
print(ans)
