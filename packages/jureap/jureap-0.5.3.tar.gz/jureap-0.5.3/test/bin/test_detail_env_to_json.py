# --------------------------------------------------------------------------------------------------
# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2024 Jayesh Badwaik <j.badwaik@fz-juelich.de>
# --------------------------------------------------------------------------------------------------

import jureap
import pytest


def test_env_file_to_dict():
    env_file = "test/share/env/booster.env.file"
    env_dict = jureap.detail.env_file_to_dict(env_file)

    assert env_dict["CI_COMMIT_SHORT_SHA"] == """b2af1b22"""
    assert env_dict["SCRATCH_cjsc"] == """/p/scratch/cjsc"""
    assert env_dict["CI_RUNNER_EXECUTABLE_ARCH"] == """linux/amd64"""
    assert env_dict["CI_COMMIT_TITLE"] == """- fix errors"""
    assert (
        env_dict["LD_LIBRARY_PATH"]
        == """/p/software/juwelsbooster/stages/2024/software/CUDA/12/nvvm/lib64:/p/software/juwelsbooster/stages/2024/software/CUDA/12/extras/CUPTI/lib64:/p/software/juwelsbooster/stages/2024/software/CUDA/12/lib:/p/software/juwelsbooster/stages/2024/software/binutils/2.40-GCCcore-12.3.0/lib:/p/software/juwelsbooster/stages/2024/software/zlib/1.2.13-GCCcore-12.3.0/lib:/p/software/juwelsbooster/stages/2024/software/GCCcore/12.3.0/lib64"""
    )
    assert env_dict["CI_DEPENDENCY_PROXY_SERVER"] == """gitlab.jsc.fz-juelich.de:443"""
    assert env_dict["CI_PROJECT_TITLE"] == """jacamar-tester"""
    assert env_dict["CI_RUNNER_TAGS"] == """["shell", "jacamar", "login", "juwels_booster"]"""
    assert (
        env_dict["CI_PIPELINE_URL"]
        == """https://gitlab.jsc.fz-juelich.de/exacb/examples/jacamar-tester/-/pipelines/221082"""
    )
