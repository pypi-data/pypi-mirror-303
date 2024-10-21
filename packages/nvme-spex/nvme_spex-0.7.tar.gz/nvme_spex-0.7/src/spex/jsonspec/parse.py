# SPDX-FileCopyrightText: 2023 Samsung Electronics Co., Ltd
#
# SPDX-License-Identifier: BSD-3-Clause

import io
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from spex.jsonspec.document import DocumentParser
from spex.jsonspec.parserargs import ParserArgs
from spex.jsonspec.quirks import QUIRKS_MAP, QuirksMap
from spex.xml import ElementTree, Xpath, etree


@dataclass(frozen=True)
class SpecDocument:
    tree: ElementTree
    key: str
    rev: str

    def get_parser(
        self, args: ParserArgs, quirks_map: Optional[QuirksMap] = None
    ) -> DocumentParser:
        if quirks_map is None:
            quirks_map = QUIRKS_MAP

        quirks_key = (self.key, self.rev)
        dp = quirks_map.get(quirks_key, DocumentParser)(
            args, self.tree, self.key, self.rev
        )
        return dp


# TODO determine what to return
def open_doc(spec: Path) -> SpecDocument:
    return html_to_spec_doc(spec.absolute().read_text())


def html_to_spec_doc(html_doc: str) -> SpecDocument:
    """Html to SpecDocument

    This creates a SpecDocument from a raw string containing html
    from a second stage run.

    Args:
        html (str): Full html document to parse as a string

    Returns:
        SpecDocument: A wrapper that returns a parser and holds meta data on the
        specification
    """
    doc = etree.parse(io.StringIO(html_doc))

    doc_spec = Xpath.attr_first_req(doc, "./head/meta/@data-spec").lower()
    doc_rev = Xpath.attr_first_req(doc, "./head/meta/@data-revision").lower()
    return SpecDocument(tree=doc, key=doc_spec, rev=doc_rev)
