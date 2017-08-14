import sys
import matplotlib.pyplot as plt
import operator
import argparse

# Get the first cmd line arg
def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-l", 
        "--list",
        nargs="+",
        dest="list",
        required=True,
        help="the word or list of the words to be compared."
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

    word_freq(args.list, args.filename)

def word_freq(wordArg, filename):
    doc = {}

    for line in open(filename, 'r', encoding="utf-8"):
        wordlist = line.split(' ')
        
        for entry in wordlist:
            if (doc.__contains__(entry)):
                doc[entry] = int(doc.get(entry)) + 1
            else:
                doc[entry] = 1

    sorted_doc = (sorted(doc.items(), key = operator.itemgetter(1)))[::-1]
    just_the_occur = []
    just_the_rank = []
    word_rank = 0
    word_frequency = 0
    entry_word = 1

    for i, word in enumerate(wordArg):
        if wordArg[i] not in str(doc):            
            sys.stderr.write("Error: " + wordArg[i] + " does not appear in " + filename)
            sys.exit(1)
            
        for entry in sorted_doc:
            if entry[0] in wordArg[i]:
                word_rank = entry_word
                word_frequency = entry[1]
                
            just_the_rank.append(entry_word)
            entry_word += 1
            just_the_occur.append(entry[1])

        plt.scatter(
            [word_rank],
            [word_frequency],
            color="r",
            marker=r"$ {} $".format(wordArg[i]),
            s=1000,
            label=wordArg[i]
        )
        plt.loglog(just_the_rank, just_the_occur, basex=10)    

    plt.title("Word Frequencies in " + filename)
    plt.ylabel("Total Number of Occurrences")    
    plt.grid(True)
    plt.show()
  
if __name__ == "__main__":
    main()
