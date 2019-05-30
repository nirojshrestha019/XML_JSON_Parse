import argparse


def input_agr():
    """

    :return:
    """
    parser = argparse.ArgumentParser(description='Convert XML file to csv')
    parser.add_argument(
            '-i',
            '--input_file',
            dest='input_file',
            default=None,
            required=True,
            help='Source XML file (mandatory)'
        )
    parser.add_argument(
            '-o',
            '--output_file',
            dest='output_file',
            default=None,
            required=True,
            help='Destination csv file (mandatory)'
        )
    parser.add_argument(
            '-e',
            '--element',
            dest='element',
            default=None,
            required=True,
            help='element to parse (mandatory)'
        )
    args = parser.parse_args()
    input_file  = args.input_file
    output_file = args.output_file
    element_to_parse = args.element

    return input_file, output_file, element_to_parse
