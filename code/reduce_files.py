""" Script to reduce/merge multiple files with the same name from different subdirectories """
import os
import sys
from pathlib import Path

def reduce_files(input_files, output_file):
    """
    Reduce/merge multiple input files into a single output file.
    
    This function can be customized to perform complex merging logic beyond
    simple concatenation (e.g., deduplication, sorting, aggregation, etc.)
    
    Args:
        input_files: List of input file paths
        output_file: Path to output file
    """
    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(output_file)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    
    # For now, simple concatenation
    # This can be replaced with more complex logic (deduplication, sorting, etc.)
    lines_seen = set()  # For potential deduplication
    all_lines = []
    
    print(f"Processing {len(input_files)} input files...")
    
    for input_file in sorted(input_files):
        if not os.path.exists(input_file):
            print(f"Warning: Input file not found: {input_file}")
            continue
            
        print(f"Reading from: {input_file}")
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.rstrip('\n\r')
                    if line:  # Only process non-empty lines
                        # Example: Could add deduplication here
                        # if line not in lines_seen:
                        #     lines_seen.add(line)
                        #     all_lines.append(line)
                        
                        # For now, just collect all lines
                        all_lines.append(line)
        except Exception as e:
            print(f"Error reading {input_file}: {e}")
    
    # Write output file
    print(f"Writing {len(all_lines)} lines to: {output_file}")
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            for line in all_lines:
                f.write(line + '\n')
        print(f"Successfully created output file: {output_file}")
    except Exception as e:
        print(f"Error writing {output_file}: {e}")
        sys.exit(1)

def main():
    """Main entry point"""
    if len(sys.argv) < 3:
        print("Usage: reduce_files.py <output_file> <input_file1> [input_file2] ...")
        sys.exit(1)
    
    output_file = sys.argv[1]
    input_files = sys.argv[2:]
    
    print(f"Output file: {output_file}")
    print(f"Input files: {input_files}")
    
    reduce_files(input_files, output_file)

if __name__ == "__main__":
    main()

