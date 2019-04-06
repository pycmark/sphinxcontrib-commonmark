"""
    sphinxcontrib.commonmark
    ~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: Copyright 2017-2019 by Takeshi KOMIYA
    :license: Apache License 2.0, see LICENSE for details.
"""

from typing import Any, Dict

from pycmark import CommonMarkParser
from sphinx.application import Sphinx

from sphinxcontrib.commonmark.version import __version__


def setup(app: Sphinx) -> Dict[str, Any]:
    app.add_source_suffix('.md', 'markdown')
    app.add_source_parser(CommonMarkParser)

    return {
        'version': __version__,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
