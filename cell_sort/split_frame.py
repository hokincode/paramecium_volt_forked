import csv
import re
import json
import tqdm
import os
import os.path as osp
import argparse
import glob
import logging
import time
import os
import re

def logger_setup():
    """ logger_setup

    Returns:
        : logger
    """
    # create logger
    logger = logging.getLogger('Split into each frame')
    logger.setLevel(logging.CRITICAL)
    # create file handler which logs even debug messages
    log_name = '../log/{}.log'.format(time.strftime('%Y-%m-%d-%H-%M'))
    fh = logging.FileHandler(log_name)
    fh.setLevel(logging.CRITICAL)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)
    logger.disabled = True  # Disable the logger
    return logger

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-dir', type=str, default='../processed',help='directory of to be split files', dest='input_dir')
    parser.add_argument('--split-dir', type=str, default='../split_frame',help='directory to split files', dest='split_dir')
    return parser.parse_args()

if __name__ == "__main__":
    args = get_args()
    print(os.getcwd())
    out_path = args.split_dir
    input_path = args.input_dir