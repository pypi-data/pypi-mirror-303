# --------------------------------------------------------------------------------------------------
# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2024 Jayesh Badwaik <j.badwaik@fz-juelich.de>
# --------------------------------------------------------------------------------------------------

import jureap.check
import os
import argparse
import csv
import json
import jureap.metadata
import pytest


def test_00_check_csv():
    input_filename = "test/share/check/00.input.csv"
    jureap.check.check(input_filename)


def test_01_check_csv_fail():
    input_filename = "test/share/check/01.input.fail.csv"

    with pytest.raises(ValueError, match="Empty value for column"):
        jureap.check.check(input_filename)


def test_02_check_csv_fail():
    input_filename = "test/share/check/02.input.fail.csv"

    with pytest.raises(ValueError, match="Column .* not found in the input file"):
        jureap.check.check(input_filename)
