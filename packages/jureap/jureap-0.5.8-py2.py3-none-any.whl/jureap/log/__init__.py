# --------------------------------------------------------------------------------------------------
# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2024 Jayesh Badwaik <j.badwaik@fz-juelich.de>
# --------------------------------------------------------------------------------------------------

import jureap.check
import jureap.detail
import json


def log(input_file, output_filename, environment, input_version, output_version):
    if input_version != 1 and output_version != 1:
        raise ValueError(
            "Version combination of "
            + str(input_version)
            + " and "
            + str(output_version)
            + " is not supported."
        )

    jureap.check.check(input_file)

    input_data = jureap.detail.csv_file_to_array(input_file)

    log_dict = {}
    log_dict["version"] = 1

    log_dict["reporter"] = {}
    log_dict["reporter"]["generator"] = "jureap-gitlab-exacb"
    reporter_info = jureap.detail.parse_reporter_info(environment)
    log_dict["reporter"]["info"] = reporter_info
    log_dict["parameter"] = {}

    log_dict["experiment"] = {}
    log_dict["experiment"]["system"] = reporter_info["system"]
    log_dict["experiment"]["version"] = reporter_info["version"]
    log_dict["experiment"]["variant"] = input_data[0]["variant"]
    log_dict["experiment"]["timestamp"] = reporter_info["timestamp"]

    data_dict = []

    special_data = [
        "system",
        "version",
        "variant",
        "success",
        "runtime",
        "nodes",
        "taskspernode",
        "threadspertask",
        "jobid",
        "queue",
    ]

    for data in input_data:
        data_copy = data.copy()
        data_entry = {}
        data_entry["success"] = data_copy["success"].lower()
        data_entry["runtime"] = data_copy["runtime"]
        data_entry["parameter"] = {}
        data_entry["parameter"]["nodes"] = data_copy["nodes"]
        data_entry["parameter"]["taskspernode"] = data_copy["taskspernode"]
        data_entry["parameter"]["threadspertask"] = data_copy["threadspertask"]
        data_entry["slurm_jobid"] = data_copy["jobid"]
        data_entry["queue"] = data_copy["queue"]

        data_entry["metrics"] = {}
        for key in data_copy:
            if key not in special_data:
                data_entry["metrics"][key] = data_copy[key]

        data_dict.append(data_entry)

    log_dict["data"] = data_dict

    with open(output_filename, "w") as output_file:
        json.dump(log_dict, output_file, indent=4)
