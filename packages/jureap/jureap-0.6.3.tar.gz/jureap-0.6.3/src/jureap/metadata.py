# --------------------------------------------------------------------------------------------------
# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2024 Jayesh Badwaik <j.badwaik@fz-juelich.de>
# --------------------------------------------------------------------------------------------------
import semver as SemVer
import enum


class major_version_type(enum.Enum):
    v0 = "0"
    v1 = "1"

    def __str__(self):
        return self.value


__version__ = "0.6.3"
semver = SemVer.VersionInfo.parse(__version__)
supported_input_version_array = [1]
supported_output_version_array = [1]
default_input_version = 1
default_output_version = 1
