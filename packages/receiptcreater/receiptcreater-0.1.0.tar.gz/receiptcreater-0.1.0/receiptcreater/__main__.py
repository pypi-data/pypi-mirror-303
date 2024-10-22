import argparse
from csvreportcreater import create_receipt



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument( '--input-file')
    parser.add_argument('--output-file')

    args = parser.parse_args()
    if args.input_file and args.output_file:
        create_receipt(args.input_file,args.output_file)



if __name__ == '__main__':
    main()