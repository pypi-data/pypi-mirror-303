#!/usr/bin/env python

"""
Pandoc filter for adding complex figures.
"""

from panflute import (
    Caption,
    Div,
    Doc,
    Element,
    Figure,
    Plain,
    convert_text,
    debug,
    run_filter,
)


# pylint: disable=broad-exception-caught
def figure(elem: Element, doc: Doc) -> Figure | None:
    """
    Transform a div element into a figure element.

    Arguments
    ---------
    elem
        The pandoc element
    doc
        The pandoc document

    Returns
    -------
    Figure | None
        Figure or None.
    """
    if (
        doc.api_version >= (1, 23)
        and isinstance(elem, Div)
        and "figure" in elem.classes
        and "caption" in elem.attributes
    ):
        try:
            caption = convert_text(elem.attributes["caption"])
            del elem.attributes["caption"]
            elem.classes.remove("figure")
            return Figure(
                *elem.content,
                caption=Caption(Plain(*caption[0].content)),
                identifier=elem.identifier,
                classes=elem.classes,
                attributes=elem.attributes,
            )
        except Exception as error:  # noqa: B902
            debug(f"[WARNING] pandoc-figure: {error}")
    return None


def prepare(doc: Doc) -> None:
    """
    Prepare the pandoc document.

    Arguments
    ---------
    doc
        The pandoc document
    """
    if doc.api_version < (1, 23):
        debug(
            f"[WARNING] pandoc-figure: pandoc api version "
            f"{'.'.join(str(value) for value in doc.api_version)} "
            "is not compatible"
        )


def main(doc: Doc | None = None) -> Doc:
    """
    Convert the pandoc document.

    Arguments
    ---------
    doc
        The pandoc document

    Returns
    -------
    Doc
        The modified pandoc document
    """
    return run_filter(figure, prepare=prepare, doc=doc)


if __name__ == "__main__":
    main()
