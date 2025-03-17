def text_to_wordlist(filename):
    with open(filename) as f:
        example_paragraph = f.read()
        ex_par_lowered = example_paragraph.lower()
        ex_par_lower_no_punc = ex_par_lowered.replace(".", "").replace(";", "").replace(",", "").replace("(", "").replace('"', '').replace(")", "").replace("\n", " ").split(" ")
        return ex_par_lower_no_punc


def count_frequencies(_list):
    wordDCT = {}
    for word in _list:
        if word not in wordDCT:
            wordDCT[word] = 1
        else:
            wordDCT[word] += 1
    return wordDCT

