# --------------------------------------------------------------------------------------------------
# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2024 Jayesh Badwaik <j.badwaik@fz-juelich.de>
# --------------------------------------------------------------------------------------------------

import jureap
import json


def test_log_01():

    input_file = "test/share/log/01.input.csv"
    output_file = "test/share/log/01.output.json"
    environment = "test/share/log/01.env.file"
    input_version = 1
    output_version = 1

    env_json = jureap.detail.env_file_to_dict(environment)
    jureap.log.log(input_file, output_file, env_json, input_version, output_version)

    with open(output_file, "r") as file:
        output = json.load(file)

    with open("test/share/log/01.expected.json", "r") as file:
        expected = json.load(file)

    assert output == expected


def test_log_02():

    input_file = "test/share/log/02.input.csv"
    output_file = "test/share/log/02.output.json"
    environment = "test/share/log/02.env.file"
    input_version = 1
    output_version = 1

    env_json = jureap.detail.env_file_to_dict(environment)
    jureap.log.log(input_file, output_file, env_json, input_version, output_version)

    with open(output_file, "r") as file:
        output = json.load(file)

    with open("test/share/log/02.expected.json", "r") as file:
        expected = json.load(file)

    assert output == expected


def test_log_03():

    input_file = "test/share/log/03.input.csv"
    output_file = "test/share/log/03.output.json"
    environment = "test/share/log/03.env.file"
    input_version = 1
    output_version = 1

    env_json = jureap.detail.env_file_to_dict(environment)
    jureap.log.log(input_file, output_file, env_json, input_version, output_version)

    with open(output_file, "r") as file:
        output = json.load(file)

    with open("test/share/log/03.expected.json", "r") as file:
        expected = json.load(file)

    assert output == expected
