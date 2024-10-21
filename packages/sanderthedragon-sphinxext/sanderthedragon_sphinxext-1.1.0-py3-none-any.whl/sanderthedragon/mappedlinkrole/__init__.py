# SPDX-FileCopyrightText: 2021-2024 SanderTheDragon <sanderthedragon@zoho.com>
#
# SPDX-License-Identifier: MIT

from functools import partial
from typing import Any, Optional

from docutils.parsers.rst.states import Inliner
from docutils.nodes import Node
from docutils import nodes
from sphinx.application import Sphinx
from sphinx.util.typing import ExtensionMetadata
from sphinx.util import logging, nodes as nodesutil

import sanderthedragon as common


def make_link(name: str, raw: str, text: str, line: int, inliner: Inliner,
              options: dict[str, Any] = {}, content: list[str] = [],
              mapping: dict[str, str] = {}, target: Optional[str] = None) \
        -> tuple[list[Node], list[nodes.system_message]]:
    # Split text into text, key and anchor
    anchor = None

    ( _, text, key ) = nodesutil.split_explicit_title(text)
    if ':' in key and key != ':':
        ( key, anchor ) = key.rsplit(':', maxsplit=1)

    no_key_anchor = (key == ':')
    if len(key) == 0 or no_key_anchor:
        key = text
        if ':' in key and not no_key_anchor:
            ( key, anchor ) = key.rsplit(':', maxsplit=1)

    # Get the URL
    value = mapping.get(key, None if target is None else key)
    if value is None:
        error = inliner.reporter.error(
            f'"{key}" is not defined for "{name}"', line=line
        )
        problematic = inliner.problematic(rawtext, rawtext, error)

        return ( [ problematic ], [ error ] )

    url = value
    if target is not None:
        url = target.format(value)

    # Append anchor (if given)
    if anchor is not None:
        if not url.startswith('http://') and not url.startswith('https://'):
            anchor = nodes.make_id(anchor)

        url += '#' + anchor

    node = nodes.reference(raw, text, refuri=url)

    return ( [ node ], [] )


def setup(app: Sphinx) -> ExtensionMetadata:
    config = app.config._raw_config  # `raw_config` is available in setup

    role_mapping = config.get('role_mapping', {})
    for ( key, value ) in role_mapping.items():
        item_mapping = config.get(key + '_mapping', {})
        if value is None:
            if len(item_mapping.keys()) == 0:
                logging.getLogger('mappedlinkrole').warning(
                    f'"{key}" is defined as `None`, but no mapping is defined'
                )

            app.add_role(key, partial(make_link, mapping=item_mapping))
        else:
            app.add_role(key, partial(make_link, mapping=item_mapping,
                                      target=value))

    return { 'version': common.__version__, 'parallel_read_safe': True }
