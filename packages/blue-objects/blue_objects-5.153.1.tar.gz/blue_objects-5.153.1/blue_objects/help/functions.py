from typing import List

from abcli.help.functions import help_pytest as help_abcli_pytest


def help_pytest(
    tokens: List[str],
    mono: bool,
) -> str:
    return help_abcli_pytest(
        tokens,
        mono=mono,
        plugin_name="@objects",
    )


help_functions = {
    "pytest": help_pytest,
}
