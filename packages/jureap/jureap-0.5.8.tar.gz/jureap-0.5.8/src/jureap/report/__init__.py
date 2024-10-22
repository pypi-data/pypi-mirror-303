# --------------------------------------------------------------------------------------------------
# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2024 Jayesh Badwaik <j.badwaik@fz-juelich.de>
# --------------------------------------------------------------------------------------------------

import os
import tempfile
import shutil
import subprocess
import csv
import json
import jureap
import jureap.report.jedi
import jureap.report.scaling


def generate(
    report_type,
    input_dir,
    pipeline_array,
    prefix_array,
    workload_factor_array,
    output_dir,
    share_dir,
    tmp_dir,
):
    experiment_array = parse_experiments(
        input_dir, pipeline_array, prefix_array, workload_factor_array
    )

    if report_type == "jedi":
        jureap.report.jedi.generate(input_dir, experiment_array, output_dir, share_dir, tmp_dir)
    elif report_type == "scaling":
        jureap.report.scaling.generate(input_dir, experiment_array, output_dir, share_dir, tmp_dir)
    else:
        raise ValueError(f"Report type {report_type} not implemented yet.")


def parse_experiments(input_dir, pipeline_array, prefix_array, workload_factor_array):
    experiment_array = []
    for index, pipeline in enumerate(pipeline_array):
        pipeline_dir_array = [f for f in os.listdir(input_dir) if f.startswith(pipeline)]
        if len(pipeline_dir_array) == 0:
            raise ValueError(f"Pipeline {pipeline} not found in {input_dir}")
        elif len(pipeline_dir_array) > 1:
            raise ValueError(f"Multiple directories found for pipeline {pipeline} in {input_dir}")

        pipeline_reldir = pipeline_dir_array[0]
        pipeline_dir = os.path.join(input_dir, pipeline_reldir)
        prefix = prefix_array[index]
        workload_factor = workload_factor_array[index]
        csv_file = os.path.join(pipeline_dir, f"{prefix}.csv")
        json_file = os.path.join(pipeline_dir, f"{prefix}.json")

        csv_data = jureap.detail.csv_file_to_array(csv_file)
        with open(json_file) as json_filepath:
            json_data = json.load(json_filepath)

        experiment_array.append(
            experiment(pipeline_reldir, pipeline, prefix, workload_factor, csv_data, json_data)
        )

    return experiment_array


class experiment:
    def __init__(self, pipeline_dir, pipeline, prefix, workload_factor, csv_data, json_data):
        self._pipeline_dir = pipeline_dir
        self._pipeline = pipeline
        self._prefix = prefix
        self._workload_factor = workload_factor
        self._csv_data = csv_data
        self._json_data = json_data

    def pipeline_dir(self):
        return self._pipeline_dir

    def pipeline(self):
        return self._pipeline

    def prefix(self):
        return self._prefix

    def csv_data(self):
        return self._csv_data

    def output_pipeline_dir(self):
        return self._pipeline + "." + self._prefix

    def json_data(self):
        return self._json_data

    def workload_factor(self):
        return self._workload_factor

    def json_repr(self):
        return {
            "pipeline": self._pipeline,
            "prefix": self._prefix,
            "csv_data": self._csv_data,
            "json_data": self._json_data,
            "workload_factor": self._workload_factor,
        }

    def __repr__(self):
        return json.dumps(self.json_repr(), indent=4)

    def __str__(self):
        return self.__repr__()
