import sys
import matplotlib.pyplot as plt
import operator
import argparse

# Get the first cmd line arg
def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "wordOne",
        help="the word to be compared with the second."
    )

    parser.add_argument(
        "wordTwo",
        help="the word to be compared with the first."
    )

    parser.add_argument(
        "filename",
        help="the path to the text file to be searched through."
    )

    args = parser.parse_args()

    try:
        open(args.filename)
    except FileNotFoundError:

        sys.stderr.write("Error: " + args.filename + " does not exist!")
        sys.exit(1)

    word_freq(args.wordOne, args.wordTwo, args.filename)

def word_freq(wordOne, wordTwo, filename):
    doc = {}

    for line in open(filename, 'r', encoding="utf-8"):
        wordlist = line.split(' ')

        for entry in wordlist:
            if (doc.__contains__(entry)):
                doc[entry] = int(doc.get(entry)) + 1
            else:
                doc[entry] = 1

    if (wordOne not in doc):
        sys.stderr.write("Error: " + wordOne + " does not appear in " + filename)
        sys.exit(1)
    elif (wordTwo not in doc):
        sys.stderr.write("Error: " + wordTwo + " does not appear in " + filename)
        sys.exit(1)

    sorted_doc = (sorted(doc.items(), key = operator.itemgetter(1)))[::-1]
    just_the_occur = []
    just_the_rank = []
    wordOne_rank, wordTwo_rank = 0, 0
    word_frequency = 0

    entry_numOne, entry_numTwo = 1, 1

    for entry in sorted_doc:
        if(entry[0] == wordOne):
            wordOne_rank = entry_numOne
            wordOne_frequency = entry[1]
        elif (entry[0] == wordTwo):
            wordTwo_rank = entry_numTwo
            wordTwo_frequency = entry[1]

        just_the_rank.append(entry_numOne)
        entry_numOne += 1
        entry_numTwo += 1
        just_the_occur.append(entry[1])
    
    plt.title("Word Frequencies in " + filename)
    plt.ylabel("Total Number of Occurrences")
    plt.xlabel("Rank of word(\"" + wordOne + "\" is rank " + str(wordOne_rank) + ")" 
    + "\n" + "Rank of word(\"" + wordTwo + "\" is rank " + str(wordTwo_rank) + ")")
    
    plt.loglog(just_the_rank, just_the_occur, basex=10)
    # First word
    plt.scatter(
        [wordOne_rank],
        [wordOne_frequency],
        color="r",
        marker=r"$ {} $".format(wordOne),
        s=1000,
        label=wordOne
        )
    # Second word
    plt.scatter(
        [wordTwo_rank],
        [wordTwo_frequency],
        color="g",
        marker=r"$ {} $".format(wordTwo),
        s=1000,
        label=wordTwo
    )
    plt.grid(True)
    plt.show()
  
if __name__ == "__main__":
    main()
