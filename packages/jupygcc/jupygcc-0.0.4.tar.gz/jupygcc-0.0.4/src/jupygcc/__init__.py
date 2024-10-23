# SPDX-FileCopyrightText: 2024-present Benjamin Abel <dev.abel@free.fr>
#
# SPDX-License-Identifier: MIT

from .gcc_magic import GccMagic


def load_ipython_extension(ipython):
    ipython.register_magics(GccMagic)
