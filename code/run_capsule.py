""" top level run script """
import os
import glob
from collections import defaultdict

def run():
    """ basic run function """
    data_dir = "/data/text"
    results_dir = "/results"
    
    # Create results directory if it doesn't exist
    os.makedirs(results_dir, exist_ok=True)
    
    # Dictionary to store lines grouped by first letter
    lines_by_letter = defaultdict(list)
    
    # Read all text files in /data folder
    text_files = glob.glob(os.path.join(data_dir, "*.txt"))
    
    for file_path in text_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.rstrip('\n\r')  # Remove trailing newlines
                    if line:  # Only process non-empty lines
                        # Get first character and convert to lowercase
                        first_char = line[0].lower()
                        # Only process if it's a letter
                        if first_char.isalpha():
                            lines_by_letter[first_char].append(line)
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
    
    # Write output files for each letter
    for letter, lines in sorted(lines_by_letter.items()):
        output_file = os.path.join(results_dir, f"{letter}.txt")
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                for line in lines:
                    f.write(line + '\n')
        except Exception as e:
            print(f"Error writing {output_file}: {e}")

if __name__ == "__main__": run()