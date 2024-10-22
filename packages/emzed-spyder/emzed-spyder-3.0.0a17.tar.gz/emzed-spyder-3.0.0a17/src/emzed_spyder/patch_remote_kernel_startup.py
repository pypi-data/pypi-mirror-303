#! /usr/bin/env python
# Copyright 2020 Uwe Schmitt <uwe.schmitt@id.ethz.ch>

from datetime import datetime


from .utils import (
    active_python_exe,
    get_active_project,
    get_project_folder,
    is_project,
    python_executable_in,
    update_active_project,
    update_message
)


def set_emzed_spyder_kernels():
    import spyder.plugins.ipythonconsole.utils.kernelspec as kernelspec

    class PatchedKernelSpec(kernelspec.SpyderKernelSpec):
        def __init__(self, is_cython=False, is_pylab=False, is_sympy=False, **kwargs):
            kernelspec.KernelSpec.__init__(self, **kwargs)
            self.is_cython = is_cython
            self.is_pylab = is_pylab
            self.is_sympy = is_sympy

            self.display_name = "Python 3 (emzed.spyder)"
            self.language = "python3"
            self.resource_dir = ""

        @property
        def argv(self):
            result = super().argv

            update_active_project()
            active_project = get_active_project()
            if active_project and is_project(active_project):
                project_folder = get_project_folder(active_project)
                python_exe = python_executable_in(project_folder / ".venv")
                result[0] = str(python_exe)
            result[2] = "emzed_spyder_kernels"
            return result

        @property
        def env(self):
            result = super().env
            active_project = get_active_project()
            if active_project and is_project(active_project):
                project_folder = get_project_folder(active_project)
                result["EMZED_ACTIVE_PROJECT"] = str(project_folder)
            return result

    kernelspec.SpyderKernelSpec = PatchedKernelSpec


ITALICS = "\033[0;3m"
RESET = "\033[0;0m"
BLUE_FG = "\033[0;34m"
RED_FG = "\033[0;31m"

LIGHT_GREEN_FG = "\033[1;32m"
WHITE_FG = "\033[1;37m"

WELCOME = r"""{FG_LOGO}                                 _
                                | |
     _____ ____  _____ _____  __| |
    | ___ |    \(___  ) ___ |/ _  |
    | ____| | | |/ __/| ____( (_| |
    |_____)_|_|_(_____)_____)\____|
{FG_TEXT}
{ITALICS}
      Copyright (c) 2020 ETH Zurich
             Scientific IT Services
              https://emzed.ethz.ch
{RESET}
run {ITALICS}emzed_help(){RESET} for an overview of available functions.
"""

latest_version_check = None


def set_banner(remote_interpreter):
    from spyder.plugins.ipythonconsole.widgets.shell import (
        ShellWidget,
        create_qss_style,
    )

    def _banner_default(self, _orig=ShellWidget._banner_default):
        _, dark_fg = create_qss_style(self.syntax_style)
        if dark_fg:
            FG_LOGO = RED_FG
            FG_TEXT = BLUE_FG
        else:
            FG_LOGO = LIGHT_GREEN_FG
            FG_TEXT = WHITE_FG

        global latest_version_check

        active_project_exe = active_python_exe()
        if active_project_exe is not None:
            remote_interpreter = active_project_exe

        # only check versions at startup or at max once per day when one opens a new
        # console:
        if (
            latest_version_check is None
            or (datetime.now() - latest_version_check).days >= 1
        ):
            try:
                extra = "\n".join(update_message(remote_interpreter, FG_LOGO, FG_TEXT))
            except Exception:
                import traceback

                extra = traceback.format_exc()
            latest_version_check = datetime.now()
        else:
            extra = ""

        return (
            WELCOME.format(
                FG_LOGO=FG_LOGO, FG_TEXT=FG_TEXT, ITALICS=ITALICS, RESET=RESET
            )
            + extra
        )

    ShellWidget._banner_default = _banner_default
