import re
import sys
import os.path
import argparse

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "filename",
        help="the path to the text file to be searched through"
    )

    parser.add_argument(
        "-l",
        "--lowercase",
        help="translate words to the lowercase",
        default="true"
    )

    args = parser.parse_args()

    try:
        open(args.filename)
    except FileNotFoundError:
        sys.stderr.write("Error: " + args.filename + " does not exist!")
        sys.exit(1)

    parse_file(args.filename, -l)

def parse_file(filename, lowercaseArg):
    # Create 'output' directory inside current
    current_directory = os.getcwd()
    destination_directory = os.path.join(current_directory, 'output')
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory, exist_ok=True)
            
    with open(filename, 'r', encoding="utf-8") as in_file:
        # Russian text
        for text in re.findall(r"[а-яА-яёЁ]+", in_file.read()):
            if (lowercaseArg == true):
                with open("output/output_lwc.txt", 'a', encoding="utf-8") as out_file:
                    # Write lowercase word to the file
                    out_file.write(text.lower() + " ")
                out_file.closed
            else:
                with open("output/output.txt", 'a', encoding="utf-8") as out_file:
                    out_file.write(text + " ")
                out_file.closed

        in_file.seek(0)
        
        # English text
        for text in re.findall(r"[a-zA-z]+", in_file.read()):     
            if (lowercaseArg == true):
                with open("output/output_lwc.txt", 'a', encoding="utf-8") as out_file:
                    # Write lowercase word to the file
                    out_file.write(text.lower() + " ")
                out_file.closed
            else:
                with open("output/output.txt", 'a', encoding="utf-8") as out_file:
                    out_file.write(text + " ")
                out_file.closed
    in_file.closed
       
if __name__ == "__main__":
    main()