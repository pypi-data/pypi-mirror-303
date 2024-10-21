# SPDX-FileCopyrightText: 2021-2024 SanderTheDragon <sanderthedragon@zoho.com>
#
# SPDX-License-Identifier: MIT

from pygments.lexer import inherit
from pygments.lexers.javascript import JavascriptLexer
from pygments.token import Comment
from sphinx.application import Sphinx
from sphinx.util.typing import ExtensionMetadata

import sanderthedragon as common


class LLVMJSONLexer(JavascriptLexer):
    """
    The LLVM JSON parser uses '#' instead of '//' for comments.
    This lexer adds it as comment prefix.
    """

    name: str = 'LLVMJSON'
    aliases: list[str] = [ 'llvmjson' ]
    filenames: list[str] = [ '*.imp' ]

    tokens: dict[str, list] = {
        'commentsandwhitespace': [
            ( r'#.*?\n', Comment.Single ),
            inherit
        ]
    }


def setup(app: Sphinx) -> ExtensionMetadata:
    for lexer in [ LLVMJSONLexer ]:
        for alias in [ lexer.name, *lexer.aliases ]:
            app.add_lexer(alias, lexer)

    return { 'version': common.__version__, 'parallel_read_safe': True }
