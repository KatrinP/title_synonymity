#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys
import argparse

program_version = "1.0"


def parse_command_line():

    parser = argparse.ArgumentParser(description="Title Synonymy compares two newspaper titles "
                                                 "and gives a probability, that the two "
                                                 "articles are of the same topic."
                                     )

    parser.add_argument("-l", "--language",
                        help="Sorry, guy. Just English is supported right now...",
                        default="en"
                        )
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
    parser.add_argument("first_sentence", help="First sentence to compare")
    parser.add_argument("second_sentence", help="Second sentence to compare")

    return parser.parse_args()

if __name__ == '__main__':
    cl_args = parse_command_line()

