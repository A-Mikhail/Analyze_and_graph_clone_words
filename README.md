## What is it?
The scripts were my first attempt to work with python, so they have a hundred of problems that I hope to fix if not forget about them.

## How to use it?
**formatText.py** -- take from the file with text English and Russian words and write them into an output.txt file in output folder.

    Example: python formatText.py "file_with_text.ext"

    Output: /output/output.txt -- where words separated by a space
    
With optional *-lowercase* argument:

    Example: python formatText.py "file_with_text.ext" -lowercase

    Output: /output/output_lwc.txt -- words separated by a space, and transfer in lowercase

**word_freq.py** -- compare two words together in a given file from the previous script output or just a word separated by a space.

    Example: python word_freq.py firstWord secondWord "file_with_words.ext"
    
    Output: A graph where a word with higher frequency appears a top of the graph.
