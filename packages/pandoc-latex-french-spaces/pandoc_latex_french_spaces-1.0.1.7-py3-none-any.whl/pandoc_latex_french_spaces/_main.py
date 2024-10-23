#!/usr/bin/env python3

"""
Pandoc filter for converting spaces to non-breakable spaces.

This filter is for use in LaTeX for french ponctuation.
"""
from __future__ import annotations

from panflute import Doc, Element, RawInline, Space, Str, run_filter


def spaces(elem: Element, doc: Doc) -> RawInline | None:
    """
    Add LaTeX spaces when needed.

    Arguments
    ---------
    elem
        A tree element.
    doc
        The pandoc document.

    Returns
    -------
    RawInline | None
        A RawInLine or None.
    """
    # Is it in the right format and is it a Space?
    if doc.format in ("latex", "beamer") and isinstance(elem, Space):
        if isinstance(elem.prev, Str) and elem.prev.text[-1] in ("«", "“", "‹"):
            return RawInline("\\thinspace{}", "tex")
        if isinstance(elem.next, Str):
            if elem.next.text[0] == ":":
                return RawInline("~", "tex")
            if elem.next.text[0] in (";", "?", "!", "»", "”", "›"):
                return RawInline("\\thinspace{}", "tex")
    return None


def main(doc: Doc | None = None) -> Doc:
    """
    Process conversion.

    Arguments
    ---------
    doc
        The pandoc document

    Returns
    -------
    Doc
        The modified document
    """
    return run_filter(spaces, doc=doc)


if __name__ == "__main__":
    main()
