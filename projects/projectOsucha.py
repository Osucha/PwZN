import argparse
from collections import Counter
from ascii_graph import Pyasciigraph
from rich.progress import Progress
from rich import print
import rich.traceback
from rich.console import Console
from rich.text import Text
import re
import os
import collections
from _collections_abc import Iterable 
collections.Iterable = Iterable

rich.traceback.install()

console = Console() # rich console

# load file(s) and count words
def count_words(file_paths, min_length, ignore_words, exclude_chars, include_chars):
    word_counts = Counter() # special dict

    # for each file
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read().lower() # we do not care if letter are small or great

        words = re.findall(r'\b\w+\b', text)  # find all words - regular expression: \b = end of the word (space, dot, etc), ]w = some string
        filtered_words = []
        
        # word-by-word progress bar
        with Progress() as progress:
            task = progress.add_task(f"Processing {file_path}...", total=len(words))

            for word in words:
                # filters
                if len(word) >= min_length and word not in ignore_words:
                    if all(char not in word for char in exclude_chars) and all(char in word for char in include_chars):
                        filtered_words.append(word)

                progress.update(task, advance=1)
        
        word_counts.update(filtered_words)

    return word_counts

# display colorful histogram
def display_histogram(word_counts, top_n):
    most_common_words = word_counts.most_common(top_n)
    
    graph_data = [(word, count) for word, count in most_common_words]
    graph = Pyasciigraph()

    gradient_blue = 100
    
    # drawing histogram
    for index, line in enumerate(graph.graph("Word Frequency Histogram", graph_data)):
        blue = min(255, int(gradient_blue + ((index) / top_n) * 155)) # change value of blue to get a cOoL gRaDiEnT :DDD
        color = rgb_to_hex(0, 217, blue)
        console.print(line, style=color)

# gather all text files from directory
def get_files_from_directory(directory):
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.txt')]

def rgb_to_hex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

def main():
    # Arguments parsing
    parser = argparse.ArgumentParser(description="Script to display word frequency histogram from text file(s)")
    parser.add_argument('file', nargs='?', help="Path to text file or directory with text files")
    parser.add_argument('-n', '--number', type=int, default=10, help="Number of words to display (default: 10)")
    parser.add_argument('-m', '--min_length', type=int, default=0, help="Minimum word length (default: 0)")
    parser.add_argument('-i', '--ignore_words', nargs='*', default=[], help="List of words to ignore")
    parser.add_argument('-x', '--exclude_chars', nargs='*', default=[], help="Characters that words must not contain")
    parser.add_argument('-c', '--include_chars', nargs='*', default=[], help="Characters that words must contain")
    parser.add_argument('-d', '--directory', help="Directory to process all text files within")

    args = parser.parse_args()

    if args.directory:
        file_paths = get_files_from_directory(args.directory)
        print(f"Processing {len(file_paths)} files from directory: {args.directory}")
    else:
        file_paths = [args.file]
        print(f"Processing file: {args.file}")

    word_counts = Counter()


    for file_path in file_paths:
        # Count words for each file individually
        file_word_counts = count_words([file_path], args.min_length, args.ignore_words, args.exclude_chars, args.include_chars)
        
        # Update the global word_counts with the counts from the current file
        word_counts.update(file_word_counts)
        
        # Display the histogram for each file
        print(f"Displaying top {args.number} words for file: {file_path}")
        display_histogram(file_word_counts, args.number)
        print()

if __name__ == "__main__":
    main()
