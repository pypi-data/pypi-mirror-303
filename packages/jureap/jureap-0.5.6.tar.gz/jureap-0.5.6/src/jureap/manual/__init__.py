# --------------------------------------------------------------------------------------------------
# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2024 Jayesh Badwaik <j.badwaik@fz-juelich.de>
# --------------------------------------------------------------------------------------------------

import jureap.detail
import shutil
import itertools
import os
import tempfile
import subprocess
import json
import sys
import matplotlib.pyplot
import math
import numpy


def compute_data_list(input_dir):
    data_name_list = []
    for file in os.listdir(input_dir):
        if file.endswith(".csv"):
            data_name_list.append(file.split(".")[0])

    return data_name_list


def extract_nodes_and_runtime(input_file):
    data = jureap.detail.csv_file_to_array(input_file)
    nodes = []
    runtime = []
    for row in data:
        nodes.append(int(row["nodes"]))
        runtime.append(float(row["runtime"]))

    runtime = [x for _, x in sorted(zip(nodes, runtime))]
    nodes = sorted(nodes)
    ideal_scaling_array = [runtime[0] / n * nodes[0] for n in nodes]
    low_scaling_array = [1.25 * i for i in ideal_scaling_array]

    return {
        "nodes": nodes,
        "runtime": runtime,
        "ideal_scaling": ideal_scaling_array,
        "low_scaling": low_scaling_array,
    }


def extract_data(input_dir):
    plot_data = []
    for file in os.listdir(input_dir):
        if file.endswith(".csv"):
            data = extract_nodes_and_runtime(os.path.join(input_dir, file))
            plot_data.append({"name": file.rsplit(".", 1)[0], "data": data})

    return plot_data


def prepare_output_dir(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
    shutil.copytree(input_dir, os.path.join(output_dir, "input"))


def compute_plot_info(plot_data):
    plot_info = {}
    node_range = [sys.maxsize, 0]
    runtime_range = [sys.float_info.max, 0]

    min_plot_name = plot_data[0]["name"]
    min_node = sys.maxsize

    node_array = []

    for keydata in plot_data:
        data = keydata["data"]
        name = keydata["name"]
        if min(data["nodes"]) < min_node:
            min_plot_name = name
            min_node = min(data["nodes"])
        node_array = node_array + data["nodes"]
        node_range[0] = min(node_range[0], min(data["nodes"]))
        node_range[1] = max(node_range[1], max(data["nodes"]))
        runtime_range[0] = min(runtime_range[0], min(data["runtime"]))
        runtime_range[1] = max(runtime_range[1], max(data["runtime"]))

    node_range = [node_range[0] * 0.75, node_range[1] * 1.25]
    runtime_range = [runtime_range[0] * 0.75, runtime_range[1] * 1.12]

    node_array = sorted(list(set(node_array)))

    plot_info["xticklabels"] = node_array
    yticklabel_range = [math.log(runtime_range[0]), math.log(runtime_range[1])]
    plot_info["yticklabels"] = numpy.logspace(
        yticklabel_range[0], yticklabel_range[1], num=6, base=math.e
    )
    plot_info["yticklabels"] = [int(p) if p > 1 else p for p in plot_info["yticklabels"]]
    plot_info["min_plot_name"] = min_plot_name
    plot_info["range_limits"] = {"node": node_range, "runtime": runtime_range}

    return plot_info


def generate_plot_file(output_dir, plot_data):
    plot = matplotlib.pyplot.figure()
    marker = itertools.cycle(("o"))

    ax = plot.subplots()

    plot_info = compute_plot_info(plot_data)
    for data in plot_data:
        print(data["name"])
        print(data)
        ax.plot(data["data"]["nodes"], data["data"]["runtime"], label=data["name"])
        ax.fill_between(
            data["data"]["nodes"],
            data["data"]["ideal_scaling"],
            data["data"]["low_scaling"],
            alpha=0.2,
            ls="--",
        )

    ax.set_xscale("log")
    ax.set_yscale("log")

    ax.set_xlim(plot_info["range_limits"]["node"])
    ax.set_ylim(plot_info["range_limits"]["runtime"])

    ax.set_xticks(plot_info["xticklabels"])
    ax.set_yticks(plot_info["yticklabels"])
    ax.set_xticklabels(plot_info["xticklabels"])
    ax.set_yticklabels(plot_info["yticklabels"])
    ax.set_xlabel("Nodes")
    ax.set_ylabel("Runtime")
    ax.set_title("Runtime vs Nodes")
    plot.savefig(os.path.join(output_dir, "plot.png"))
    plot.savefig(os.path.join(output_dir, "plot.pdf"))


def generate(input_dir, output_dir):
    prepare_output_dir(input_dir, output_dir)
    plot_data = extract_data(input_dir)
    generate_plot_file(output_dir, plot_data)
