# --------------------------------------------------------------------------------------------------
# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2024 Jayesh Badwaik <j.badwaik@fz-juelich.de>
# --------------------------------------------------------------------------------------------------

import csv
import os
import jureap.detail

column_array = [
    "system",
    "version",
    "queue",
    "variant",
    "jobid",
    "nodes",
    "taskspernode",
    "threadspertask",
    "runtime",
    "success",
]

supported_systemname_array = ["jurecadc", "juwelsbooster", "jedi"]
supported_variant_array = [
    "single",
    "full",
    "strong.starter",
    "strong.tiny",
    "strong.small",
    "strong.medium",
    "strong.large",
    "weak.micro",
    "weak.tiny",
    "weak.small",
    "weak.medium",
    "strong.standalone",
    "jedi.evaluation.jureca",
    "jedi.evaluation.juwels_booster",
    "jedi.evaluation.jedi",
]


def check(input_filename):
    matrix = []
    with open(input_filename, "r") as input_file:
        reader = csv.reader(input_file)
        for row in reader:
            matrix.append(row)

    try:
        title_row = matrix[0]
        for column in column_array:
            if column not in title_row:
                raise ValueError("Column " + column + " not found in the input file.")

        for row in matrix[1:]:
            for index, value in enumerate(row):
                if value == "":
                    raise ValueError(
                        "Empty value for column " + column_array[index] + " in the input file."
                    )

        array = jureap.detail.csv_file_to_array(input_filename)
        for data in array:
            if data["system"] not in supported_systemname_array:
                raise ValueError("System name " + data["system"] + " is not supported.")
            if data["variant"] not in supported_variant_array:
                raise ValueError("Variant name " + data["variant"] + " is not supported.")

    except ValueError as e:
        error_string = "Error in input csv file " + input_filename + str("\n")
        error_string = error_string + str(e)
        raise ValueError(error_string)
