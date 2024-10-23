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
    workload_factor = read_workload_factor(input_dir)
    min_workload_factor = min(workload_factor.values())
    for key in workload_factor:
        workload_factor[key] = workload_factor[key] / min_workload_factor

    plot_data = []
    for file in os.listdir(input_dir):
        if file.endswith(".csv"):
            data = extract_nodes_and_runtime(os.path.join(input_dir, file))
            name = file.rsplit(".", 1)[0]
            plot_data.append(
                {
                    "name": file.rsplit(".", 1)[0],
                    "data": data,
                    "workload_factor": workload_factor[name],
                }
            )

    return plot_data


def read_workload_factor(input_dir):
    workload_factor = {}
    for file in os.listdir(input_dir):
        if file.endswith(".csv"):
            basename = file.rsplit(".", 1)[0]
            workload_filename = file.rsplit(".", 1)[0] + ".workload"
            with open(os.path.join(input_dir, workload_filename), "r") as f:
                workload_factor[basename] = float(f.read().strip())

    return workload_factor


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

    for plot in plot_data:
        if plot["name"] == min_plot_name:
            base_expected_runtime = plot["workload_factor"] * plot["data"]["runtime"][0]

    expected_runtime_array = {}
    for plot in plot_data:
        name = plot["name"]
        data = plot["data"]
        expected_runtime_array[name] = (
            base_expected_runtime * plot["workload_factor"] / data["nodes"][0] * min_node
        )

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

    plot_info["min_plot_name"] = min_plot_name
    plot_info["expected_runtime_array"] = expected_runtime_array
    return plot_info


def generate_plot_file(output_dir, plot_data):
    plot = matplotlib.pyplot.figure()
    marker = itertools.cycle(("o"))

    ax = plot.subplots()
    ax.ticklabel_format(useOffset=False)

    cmap = matplotlib.colormaps["rainbow"]
    colorgen = iter(cmap(numpy.linspace(0, 1, len(plot_data))))
    plot_info = compute_plot_info(plot_data)

    error_yaxis = []
    xaxis_point = []
    yaxis_point = []

    for data in plot_data:
        color = next(colorgen)
        ax.plot(
            data["data"]["nodes"],
            data["data"]["runtime"],
            label=data["name"],
            marker=next(marker),
            color=color,
        )
        ax.fill_between(
            data["data"]["nodes"],
            data["data"]["ideal_scaling"],
            data["data"]["low_scaling"],
            alpha=0.2,
            ls="--",
            color=color,
        )
        if data["name"] != plot_info["min_plot_name"]:
            expected_runtime = plot_info["expected_runtime_array"][data["name"]]
            error_yaxis_positive = 0.25 * expected_runtime
            error_yaxis_negative = 0
            error_yaxis.append([error_yaxis_negative, error_yaxis_positive])
            xaxis_point.append(data["data"]["nodes"][0])
            yaxis_point.append(expected_runtime)

    error_yaxis_transpose = [[], []]
    for point in error_yaxis:
        for i in range(2):
            error_yaxis_transpose[i].append(point[i])

    minimum_error_bar_ymin = min(
        [yxp - yerr for yxp, yerr in zip(yaxis_point, error_yaxis_transpose[0])]
    )
    max_error_bar_ymax = max(
        [yxp + yerr for yxp, yerr in zip(yaxis_point, error_yaxis_transpose[1])]
    )

    if minimum_error_bar_ymin < plot_info["range_limits"]["runtime"][0]:
        plot_info["range_limits"]["runtime"][0] = minimum_error_bar_ymin
    if max_error_bar_ymax > plot_info["range_limits"]["runtime"][1]:
        plot_info["range_limits"]["runtime"][1] = max_error_bar_ymax


    error_bar_ymin = min(min(yaxis_point), min(error_yaxis_transpose[0]))
    eb = ax.errorbar(
        xaxis_point,
        yaxis_point,
        yerr=error_yaxis_transpose,
        fmt="none",
        capsize=4.0,
        ls="-",
        alpha=0.7,
    )
    eb[-1][0].set_linestyle("dashed")

    ax.set_xscale("log")
    ax.set_yscale("log")

    ax.set_xlim(plot_info["range_limits"]["node"])
    ax.set_ylim(plot_info["range_limits"]["runtime"])

    ax.set_xticks(plot_info["xticklabels"])
    ax.set_yticks(plot_info["yticklabels"])
    ax.minorticks_off()
    ax.set_xticklabels(plot_info["xticklabels"])
    ax.set_yticklabels(plot_info["yticklabels"])
    ax.tick_params(axis="x", labelrotation=90)
    ax.set_xlabel("Nodes (log-scale)")
    ax.set_ylabel("Runtime / s (log-scale)")
    ax.set_title("Runtime vs Nodes")
    plot.savefig(os.path.join(output_dir, "plot.png"), bbox_inches="tight")
    plot.savefig(os.path.join(output_dir, "plot.pdf"), bbox_inches="tight")


def generate(input_dir, output_dir):
    prepare_output_dir(input_dir, output_dir)
    plot_data = extract_data(input_dir)
    generate_plot_file(output_dir, plot_data)
