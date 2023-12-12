# DNA to RNA Conversion
# For example:
# "GCAT"  =>  "GCAU"
def dna_to_rna(dna):
    my_str = dna.replace("T", "U")
    return my_str

    dna1 = ""
    for i in dna:
        dna1 += i
    return dna1.replace("T", "U")
# test.assert_equals(dna_to_rna("TTTT"), "UUUU")
# test.assert_equals(dna_to_rna("GCAT"), "GCAU")
# test.assert_equals(dna_to_rna("GACCGCCGCC"), "GACCGCCGCC")
