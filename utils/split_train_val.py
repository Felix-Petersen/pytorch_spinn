import argparse


def main():
    with open(args.input+'.train', mode='w') as train:
        with open(args.input+'.val', mode='w') as val:
            with open(args.input) as input:
                lines = input.readlines()
                val.write(''.join(lines[:int(len(lines)*float(args.val_size))]))
                train.write(''.join(lines[int(len(lines)*float(args.val_size)):]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True, help='first file')
    parser.add_argument('--val_size', default=0.2, help='relative size of validation set')
    args = parser.parse_args()
    main()
