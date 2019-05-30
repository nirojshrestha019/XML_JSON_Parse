from __future__ import print_function
import sys
import pandas as pd
import csv
import os

dict_list = []
counter = 1


def travel_element(row_dict, element, tag):
    """

    :param row_dict:
    :param element:
    :param tag:
    :return:
    """
    for child in element:
        if len(child) == 0:
            key = str(tag + '##' + child.tag)
            value = child.text if child.text is not None else ''
            if key not in row_dict.keys():
                row_dict[key] = value
            else:
                row_dict[key] = row_dict[key] + '||' + value
        else:
            travel_element(row_dict, child, tag + '##' + child.tag)
    return row_dict


def parse_from_root(each_item, total_element):
    """

    :param each_item:
    :param total_element:
    :return:
    """
    row_dict = {}
    global dict_list, counter
    row_dict = travel_element(row_dict, each_item, each_item.tag)
    print(">>>  Progress:  {} %   ".format(int((counter/total_element)*100)), end='\r')
    sys.stdout.flush()
    counter += 1
    dict_list.append(row_dict)


def output_csv(output_path, output_file):
    """

    :param output_path:
    :param output_file:
    :return:
    """
    main_df = pd.DataFrame(dict_list)
    # main_df = main_df.rename(columns={col: col.rsplit('##',1)[-1] for col in main_df.columns})
    main_df.to_csv(os.path.join(output_path, output_file), index=False, quoting=csv.QUOTE_ALL, encoding='utf-8')
