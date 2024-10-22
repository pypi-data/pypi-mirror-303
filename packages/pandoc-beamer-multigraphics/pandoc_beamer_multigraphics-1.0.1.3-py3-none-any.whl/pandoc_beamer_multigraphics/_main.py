#!/usr/bin/env python

"""
Pandoc filter for using beamer multi-graphics ability.
"""
from __future__ import annotations

from panflute import (
    Doc,
    Element,
    Image,
    MetaInlines,
    MetaList,
    RawInline,
    run_filter,
)


def image(elem: Element, doc: Doc) -> RawInline | None:
    """
    Transform image element.

    Arguments
    ---------
    elem
        current element
    doc
        pandoc document

    Returns
    -------
    RawInline | None
        RawInline or None
    """
    if doc.format == "beamer" and isinstance(elem, Image):
        classes = frozenset(elem.classes)

        # Loop on all multi-graphics definition
        for definition in doc.defined:
            # Are the classes correct?
            if classes >= definition["classes"]:
                graphics: list[str] = []

                if "height" in elem.attributes:
                    graphics.append(f"height={elem.attributes['height']}")
                elif "height" in definition:
                    graphics.append(f"height={definition['height']}")

                if "width" in elem.attributes:
                    graphics.append(f"width={elem.attributes['width']}")
                elif "width" in definition:
                    graphics.append(f"width={definition['width']}")

                options = []

                if "start" in elem.attributes:
                    options.append(f"start={int(elem.attributes['start']):d}")

                if "end" in elem.attributes:
                    options.append(f"end={int(elem.attributes['end']):d}")

                options.append(
                    f"format={elem.attributes.get('format', definition['format'])}"
                )

                return RawInline(
                    (
                        f"\\multiinclude"
                        f"[graphics={{{','.join(graphics)}}},{','.join(options)}]"
                        f"{{{elem.url}}}"
                    ),
                    "tex",
                )

    return None


def prepare(doc: Doc) -> None:
    """
    Prepare the document.

    Arguments
    ---------
    doc
        The pandoc document
    """
    # Prepare the definitions
    doc.defined = []

    # Get the meta data
    meta = doc.get_metadata("pandoc-beamer-multigraphics")

    if isinstance(meta, list):
        # Loop on all definitions
        for definition in meta:
            # Verify the definition
            if (
                isinstance(definition, dict)
                and "classes" in definition
                and isinstance(definition["classes"], list)
            ):
                definition["classes"] = frozenset(definition["classes"])
                definition["format"] = str(definition.get("format", "pdf"))
                if "width" in definition:
                    definition["width"] = str(definition["width"])
                if "height" in definition:
                    definition["height"] = str(definition["height"])

                doc.defined.append(definition)


def finalize(doc: Doc) -> None:
    """
    Finalize the document.

    Arguments
    ---------
    doc
        The pandoc document
    """
    # Add header-includes if necessary
    if "header-includes" not in doc.metadata:
        doc.metadata["header-includes"] = MetaList()
    # Convert header-includes to MetaList if necessary
    elif not isinstance(doc.metadata["header-includes"], MetaList):
        doc.metadata["header-includes"] = MetaList(doc.metadata["header-includes"])

    doc.metadata["header-includes"].append(
        MetaInlines(RawInline("\\usepackage{xmpmulti}", "tex"))
    )


def main(doc: Doc | None = None) -> Doc:
    """
    Transform the document.

    Arguments
    ---------
    doc
        pandoc document

    Returns
    -------
    Doc
        The transformed document.
    """
    return run_filter(image, doc=doc, prepare=prepare, finalize=finalize)


if __name__ == "__main__":
    main()
