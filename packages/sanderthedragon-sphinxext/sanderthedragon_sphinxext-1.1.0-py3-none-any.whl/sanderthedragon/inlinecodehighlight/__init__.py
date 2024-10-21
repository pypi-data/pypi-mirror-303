# SPDX-FileCopyrightText: 2021-2024 SanderTheDragon <sanderthedragon@zoho.com>
#
# SPDX-License-Identifier: MIT

from functools import partial
from typing import Any

from docutils.parsers.rst.states import Inliner
from docutils.parsers.rst import roles
from docutils import nodes
from sphinx.application import Sphinx
from sphinx.errors import ExtensionError
from sphinx.util.typing import ExtensionMetadata

import sanderthedragon as common


def make_code(name: str, raw: str, text: str, line: int, inliner: Inliner,
              options: dict[str, Any] = {}, content: list[str] = []) \
        -> tuple[list[nodes.Node], list[nodes.system_message]]:
    """
    Very simple wrapper around `code_role` to use 'short' syntax highlighting
    """

    inliner.document.settings.syntax_highlight = 'short'

    return roles.code_role(name, raw, text, line, inliner, options, content)


def setup(app: Sphinx) -> ExtensionMetadata:
    config = app.config._raw_config  # `raw_config` is available in setup

    inline_codes = config.get('inline_codes', {})
    if isinstance(inline_codes, dict):
        for ( key, value ) in inline_codes.items():
            app.add_role(key, partial(make_code, options={
                'language': value, 'classes': [ 'highlight' ]
            }))
    elif isinstance(inline_codes, ( list, tuple, set, frozenset )):
        for key in inline_codes:
            app.add_role(key, partial(make_code, options={
                'language': key, 'classes': [ 'highlight' ]
            }))
    else:
        raise ExtensionError(f'Invalid value type for \'inline_codes\'')

    return { 'version': common.__version__, 'parallel_read_safe': True }
