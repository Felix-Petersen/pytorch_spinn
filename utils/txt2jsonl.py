import argparse
import jsonlines


def main():
    assert len(open(args.txt1).readlines()) == len(open(args.txt2).readlines())

    with open(args.txt1) as txt1:
        with open(args.txt2) as txt2:
            with jsonlines.open(args.out, mode='w') as writer:
                for line1, line2 in zip(txt1.readlines(), txt2.readlines()):
                    line = {
                        'sentence1_binary_parse': line1,
                        'sentence2_binary_parse': line2,
                        'sentence1': line1.replace('`', '').replace('?', ''),
                        'sentence2': line2.replace('`', '').replace('?', ''),
                        'gold_label': 'neutral',
                    }
                    writer.write(line)
                writer.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--txt1', required=True, help='first file')
    parser.add_argument('--txt2', required=True, help='second file')
    parser.add_argument('--out', required=True, help='path to save output .jsonl file')
    args = parser.parse_args()
    main()
