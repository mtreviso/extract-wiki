import argparse
import os

import preprocess

parser = argparse.ArgumentParser()
parser.add_argument("input", type=str, help="Path to an input directory containing dirs of extracted articles")
parser.add_argument("-o", "--output", type=str, help="Path to an output directory or a single file")
parser.add_argument("-m", "--merge", action="store_true", help="Whether to merge all files in a single txt file")
parser.add_argument("-w", "--min-nb-words", type=int, default=1, help="Min number of words in a sentence")


def normalize(text):
    text = preprocess.remove_tags(text)
    text = preprocess.remove_newlines(text)
    text = preprocess.trim(text)
    return text.strip()


def clean_corpus(args):
    output_file = None
    if args.merge:
        output_path = args.output if args.output.endswith('.txt') else os.path.join(args.output, '.txt')
        output_file = open(output_path, 'w', encoding='utf8')
    for dname in sorted(os.listdir(args.input)):
        d_path = os.path.join(args.input, dname)
        if args.output is not None:
            o_path = os.path.join(args.output, dname)
        else:
            o_path = os.path.join(args.input, dname)
        if not args.merge and not os.path.exists(o_path):
            os.makedirs(o_path, exist_ok=True)
        for fname in sorted(os.listdir(d_path)):
            input_path = os.path.join(d_path, fname)
            output_path = os.path.join(o_path, fname)
            if not args.merge:
                output_file = open(output_path, 'w', encoding='utf8')
            with open(input_path, 'r', encoding='utf8') as f:
                print('Processing {}'.format(input_path), end='\r')
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    line = normalize(line)
                    if not line or line.count(' ') + 1 < args.min_nb_words:
                        continue
                    output_file.write(line + '\n')
            if not args.merge:
                output_file.close()
    if args.merge:
        output_file.close()
    print('Processing complete!')


if __name__ == '__main__':
    args = parser.parse_args()
    clean_corpus(args)
