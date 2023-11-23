from collections import Counter, defaultdict

def get_vocab_from_corpus(corpus):
    """ Extracts a vocabulary from a given corpus, considering space as a token. """
    vocab = Counter(corpus.split())
    return {' '.join(word) + ' _': count for word, count in vocab.items()}

def get_stats(vocab):
    """ Get counts of pairs of consecutive symbols in the vocabulary. """
    pairs = defaultdict(int)
    for word, freq in vocab.items():
        symbols = word.split()
        for i in range(len(symbols)-1):
            pairs[symbols[i], symbols[i+1]] += freq
    return pairs

def merge_vocab(pair, v_in):
    """ Merges the most frequent pair of symbols in the vocabulary. """
    v_out = {}
    bigram = ' '.join(pair)
    replacement = ''.join(pair)
    for word in v_in:
        w_out = word.replace(bigram, replacement)
        v_out[w_out] = v_in[word]
    return v_out

def bpe(num_merges):
    """ Apply BPE to the input corpus for a fixed number of merges. """
    # Ask the user for the corpus
    corpus = input("Please enter the corpus: ")
    vocab = get_vocab_from_corpus(corpus)
    print(f"Original Vocabulary: {vocab}")
    for i in range(num_merges):
        pairs = get_stats(vocab)
        if not pairs:
            break
        best = max(pairs, key=pairs.get)
        vocab = merge_vocab(best, vocab)
        print(f"Step {i+1}: Merged {best} to {best[0]+best[1]}")
        print(f"Vocabulary: {vocab}")
    return vocab

# Define the number of merges - adjust this number based on your requirement
num_merges = 10

# Apply BPE
bpe_vocabulary = bpe(num_merges)
