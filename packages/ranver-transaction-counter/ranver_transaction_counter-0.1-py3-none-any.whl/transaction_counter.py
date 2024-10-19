import argparse
import pandas as pd


def count_category(in_file, out_file):
    table = pd.read_csv(in_file, index_col='transaction_id')
    res = table.groupby(by='category').agg('sum').to_csv()
    print(res)

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--input_file',
        action='store',
        required=True
    )

    parser.add_argument(
        '--output_file',
        action='store',
        required=True
    )

    args = parser.parse_args()


if __name__ == '__main__':
    main()