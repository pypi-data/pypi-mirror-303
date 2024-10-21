# --------------------------------------------------------------------------------------------------
# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2024 Jayesh Badwaik <j.badwaik@fz-juelich.de>
# --------------------------------------------------------------------------------------------------

import jureap.detail
import csv


def env_file_to_dict(env_file):
    """
    Convert the environment file to a dictionary.
    :param env_file: Path to the environment file.
    :return: Dictionary containing the environment variables.
    """
    env_dict = {}
    with open(env_file, "r") as f:
        for line in f:
            if line.strip() == "":
                continue
            key, value = line.strip().split("=", 1)
            env_dict[key] = value
    return env_dict


def csv_file_to_array(input_filename):
    matrix = []

    with open(input_filename, "r") as input_file:
        reader = csv.reader(input_file)
        for row in reader:
            matrix.append(row)

    output = []
    column_array = matrix[0]

    for row in matrix[1:]:
        if len(row) == 0:
            continue
        row_dict = {}
        for index, value in enumerate(row):
            row_dict[column_array[index]] = value
        output.append(row_dict)
    return output


def parse_reporter_info(environment):
    reporter_info = {}
    reporter_info["pipeline"] = environment["CI_PIPELINE_ID"]
    reporter_info["job"] = environment["CI_JOB_ID"]
    reporter_info["commit"] = environment["CI_COMMIT_SHA"]
    reporter_info["username"] = environment["GITLAB_USER_LOGIN"]
    reporter_info["project"] = environment["PROJECT"]
    reporter_info["budget"] = environment["BUDGET_ACCOUNTS"]
    reporter_info["system"] = environment["SYSTEMNAME"]
    reporter_info["version"] = "2024.12"
    reporter_info["timestamp"] = environment["CI_JOB_STARTED_AT"]
    return reporter_info
