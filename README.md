# BPE-Vocabulary-Builder
An implementation of Byte Pair Encoding (BPE), a data compression technique that can also be used for efficient subword tokenization in natural language processing tasks
# Byte Pair Encoding (BPE) Implementation

This repository contains a Python implementation of the Byte Pair Encoding (BPE) algorithm, which is widely used in Natural Language Processing for subword tokenization. BPE allows for the efficient representation of a corpus by iteratively merging the most frequent pairs of characters into single tokens.

## How it works

The BPE algorithm starts with a large corpus of text and performs the following steps:

1. Initialize the vocabulary with the unique characters from the corpus.
2. Count the frequency of adjacent character pairs (bigrams) in the corpus.
3. Merge the most frequent pair and update the corpus to replace occurrences of this pair with a single token.
4. Repeat steps 2 and 3 for a fixed number of iterations or until the vocabulary reaches a desired size.

## Usage

To use this code, simply run the script and enter the corpus when prompted. The script will output the vocabulary after each merge step.
