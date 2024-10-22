#!/usr/bin/env python

"""Pandoc filter for adding admonition in LaTeX."""
from __future__ import annotations

import contextlib

from panflute import (
    Doc,
    Element,
    MetaInlines,
    MetaList,
    Plain,
    RawInline,
    convert_text,
    debug,
    run_filter,
)


def x11colors() -> dict[str, str]:  # noqa: CFQ001
    """
    Get the x11 colors.

    Returns
    -------
    dict[str, str]
        The x11 colors
    """
    # See https://www.w3.org/TR/css-color-3/#svg-color
    return {
        "aliceblue": "F0F8FF",
        "antiquewhite": "FAEBD7",
        "aqua": "00FFFF",
        "aquamarine": "7FFFD4",
        "azure": "F0FFFF",
        "beige": "F5F5DC",
        "bisque": "FFE4C4",
        "black": "000000",
        "blanchedalmond": "FFEBCD",
        "blue": "0000FF",
        "blueviolet": "8A2BE2",
        "brown": "A52A2A",
        "burlywood": "DEB887",
        "cadetblue": "5F9EA0",
        "chartreuse": "7FFF00",
        "chocolate": "D2691E",
        "coral": "FF7F50",
        "cornflowerblue": "6495ED",
        "cornsilk": "FFF8DC",
        "crimson": "DC143C",
        "cyan": "00FFFF",
        "darkblue": "00008B",
        "darkcyan": "008B8B",
        "darkgoldenrod": "B8860B",
        "darkgray": "A9A9A9",
        "darkgreen": "006400",
        "darkgrey": "A9A9A9",
        "darkkhaki": "BDB76B",
        "darkmagenta": "8B008B",
        "darkolivegreen": "556B2F",
        "darkorange": "FF8C00",
        "darkorchid": "9932CC",
        "darkred": "8B0000",
        "darksalmon": "E9967A",
        "darkseagreen": "8FBC8F",
        "darkslateblue": "483D8B",
        "darkslategray": "2F4F4F",
        "darkslategrey": "2F4F4F",
        "darkturquoise": "00CED1",
        "darkviolet": "9400D3",
        "deeppink": "FF1493",
        "deepskyblue": "00BFFF",
        "dimgray": "696969",
        "dimgrey": "696969",
        "dodgerblue": "1E90FF",
        "firebrick": "B22222",
        "floralwhite": "FFFAF0",
        "forestgreen": "228B22",
        "fuchsia": "FF00FF",
        "gainsboro": "DCDCDC",
        "ghostwhite": "F8F8FF",
        "gold": "FFD700",
        "goldenrod": "DAA520",
        "gray": "808080",
        "green": "008000",
        "greenyellow": "ADFF2F",
        "grey": "808080",
        "honeydew": "F0FFF0",
        "hotpink": "FF69B4",
        "indianred": "CD5C5C",
        "indigo": "4B0082",
        "ivory": "FFFFF0",
        "khaki": "F0E68C",
        "lavender": "E6E6FA",
        "lavenderblush": "FFF0F5",
        "lawngreen": "7CFC00",
        "lemonchiffon": "FFFACD",
        "lightblue": "ADD8E6",
        "lightcoral": "F08080",
        "lightcyan": "E0FFFF",
        "lightgoldenrodyellow": "FAFAD2",
        "lightgray": "D3D3D3",
        "lightgreen": "90EE90",
        "lightgrey": "D3D3D3",
        "lightpink": "FFB6C1",
        "lightsalmon": "FFA07A",
        "lightseagreen": "20B2AA",
        "lightskyblue": "87CEFA",
        "lightslategray": "778899",
        "lightslategrey": "778899",
        "lightsteelblue": "B0C4DE",
        "lightyellow": "FFFFE0",
        "lime": "00FF00",
        "limegreen": "32CD32",
        "linen": "FAF0E6",
        "magenta": "FF00FF",
        "maroon": "800000",
        "mediumaquamarine": "66CDAA",
        "mediumblue": "0000CD",
        "mediumorchid": "BA55D3",
        "mediumpurple": "9370DB",
        "mediumseagreen": "3CB371",
        "mediumslateblue": "7B68EE",
        "mediumspringgreen": "00FA9A",
        "mediumturquoise": "48D1CC",
        "mediumvioletred": "C71585",
        "midnightblue": "191970",
        "mintcream": "F5FFFA",
        "mistyrose": "FFE4E1",
        "moccasin": "FFE4B5",
        "navajowhite": "FFDEAD",
        "navy": "000080",
        "oldlace": "FDF5E6",
        "olive": "808000",
        "olivedrab": "6B8E23",
        "orange": "FFA500",
        "orangered": "FF4500",
        "orchid": "DA70D6",
        "palegoldenrod": "EEE8AA",
        "palegreen": "98FB98",
        "paleturquoise": "AFEEEE",
        "palevioletred": "DB7093",
        "papayawhip": "FFEFD5",
        "peachpuff": "FFDAB9",
        "peru": "CD853F",
        "pink": "FFC0CB",
        "plum": "DDA0DD",
        "powderblue": "B0E0E6",
        "purple": "800080",
        "red": "FF0000",
        "rosybrown": "BC8F8F",
        "royalblue": "4169E1",
        "saddlebrown": "8B4513",
        "salmon": "FA8072",
        "sandybrown": "F4A460",
        "seagreen": "2E8B57",
        "seashell": "FFF5EE",
        "sienna": "A0522D",
        "silver": "C0C0C0",
        "skyblue": "87CEEB",
        "slateblue": "6A5ACD",
        "slategray": "708090",
        "slategrey": "708090",
        "snow": "FFFAFA",
        "springgreen": "00FF7F",
        "steelblue": "4682B4",
        "tan": "D2B48C",
        "teal": "008080",
        "thistle": "D8BFD8",
        "tomato": "FF6347",
        "turquoise": "40E0D0",
        "violet": "EE82EE",
        "wheat": "F5DEB3",
        "white": "FFFFFF",
        "whitesmoke": "F5F5F5",
        "yellow": "FFFF00",
        "yellowgreen": "9ACD32",
    }


# pylint: disable=inconsistent-return-statements,too-many-branches,too-many-statements
def tikz(elem: Element, doc: Doc) -> RawInline | None:
    """
    Add admonition to elem.

    Arguments
    ---------
    elem
        The current element
    doc
        The pandoc document

    Returns
    -------
    RawInline | None
        The modified element or None
    """
    # Is it in the right format and is it Div or a CodeBlock?
    if doc.format in ("beamer") and elem.tag in ("Span"):
        # Is there a latex-admonition-color attribute?
        if "beamer-arrow-node" in elem.classes:
            text = convert_text(
                Plain(*elem.content), input_format="panflute", output_format="latex"
            )

            options = ["anchor=base"]

            color = get_color(elem, doc)
            if color:
                options.append(f"fill={color}")

            (from_value, to_value) = get_range(elem, doc)
            if from_value or to_value:
                display = f"\\only<{from_value}-{to_value}>"
            else:
                display = ""

            return RawInline(
                f"\\tikz[baseline]{{"
                f"{display}{{\\node[{','.join(options)}] "
                f"({elem.identifier}) "
                f"{{{text}}}"
                f";}}}}",
                format="tex",
            )

        if "beamer-arrow-edge" in elem.classes:
            angles = []
            if "angle_src" in elem.attributes:
                try:
                    angle = elem.attributes["angle_src"]
                    angle = int(angle)
                    angles.append(f"out={angle}")
                except ValueError:
                    debug(f"pandoc-beamer-arrow: angle_src '{angle}' is not correct")

            if "angle_dest" in elem.attributes:
                try:
                    angle = elem.attributes["angle_dest"]
                    angle = int(angle)
                    angles.append(f"in={angle}")
                except ValueError:
                    debug(f"pandoc-beamer-arrow: angle_dest '{angle}' is not correct")

            options = ["->"]

            color = get_color(elem, doc)
            if color:
                options.append(color)

            if "linewidth" in elem.attributes:
                try:
                    linewidth = elem.attributes["linewidth"]
                    linewidth = int(linewidth)
                    options.append(f"line width={linewidth}pt")
                except ValueError:
                    debug(
                        f"pandoc-beamer-arrow: linewidth '{linewidth}' is not correct"
                    )

            (from_value, to_value) = get_range(elem, doc)
            if from_value or to_value:
                display = f"<{from_value}-{to_value}>"
            else:
                display = ""

            return RawInline(
                f"\\begin{{tikzpicture}}[overlay]"
                f"\\path[{','.join(options)}]{display} "
                f"({elem.attributes['src']}) "
                f"edge "
                f"[{','.join(angles)}] "
                f"({elem.attributes['dest']});"
                f"\\end{{tikzpicture}}",
                format="tex",
            )
    return None


def get_range(elem: Element, _) -> tuple[str, str]:
    """
    Get the range of display for an element.

    Arguments
    ---------
    elem
        A pandoc element.

    Returns
    -------
    tuple[str, str]
        A range represented by a couple.
    """
    from_value = elem.attributes.get("from", "")
    if bool(from_value):
        try:
            from_value = max(1, int(from_value))
        except ValueError:
            debug(f"pandoc-beamer-arrow: from value '{from_value}' is not " f"correct")
            from_value = ""
    else:
        from_value = ""

    to_value = elem.attributes.get("to", "")
    if bool(to_value):
        try:
            to_value = max(1, int(to_value))
        except ValueError:
            debug(f"pandoc-beamer-arrow: to value '{to_value}' is not " f"correct")
            to_value = ""
    else:
        to_value = ""

    with contextlib.suppress(TypeError):
        if to_value < from_value:
            debug(
                f"pandoc-beamer-arrow: from value '{from_value}' and "
                f" to value '{to_value}' are incompatible"
            )
            from_value = ""
            to_value = ""

    return (from_value, to_value)


def get_color(elem: Element, doc: Doc) -> str:
    """
    Get the color of display for an element.

    Arguments
    ---------
    elem
        A pandoc element
    doc
        The pandoc document.

    Returns
    -------
    str
        The color.
    """
    if "color" in elem.attributes:
        color = elem.attributes["color"]
        if color in doc.x11colors:
            return color  # type: ignore
        debug(f"pandoc-beamer-arrow: color '{color}' is not correct")
    return ""


def prepare(doc: Doc) -> None:
    """
    Prepare the document.

    Arguments
    ---------
    doc
        The pandoc document
    """
    doc.x11colors = x11colors()


def finalize(doc: Doc) -> None:
    """
    Finalize the pandoc document.

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

    # Add useful LaTexPackage
    doc.metadata["header-includes"].append(
        MetaInlines(RawInline("\\usepackage{tikz}", "tex"))
    )
    doc.metadata["header-includes"].append(
        MetaInlines(RawInline("\\tikzstyle{every picture}+=[remember picture]", "tex"))
    )
    doc.metadata["header-includes"].append(
        MetaInlines(RawInline("\\usetikzlibrary{positioning}", "tex"))
    )
    doc.metadata["header-includes"].append(
        MetaInlines(
            RawInline(
                "\\tikzset{onslide/.code args={<#1>#2}{\\only<#1>{\\pgfkeysalso{#2}}}}",
                "tex",
            )
        )
    )

    # Define x11 colors
    tex = [
        f"\\definecolor{{{name.lower()}}}{{HTML}}{{{color}}}"
        for name, color in doc.x11colors.items()
    ]
    doc.metadata["header-includes"].append(
        MetaInlines(RawInline("\n".join(tex), "tex"))
    )


def main(doc: Doc | None = None) -> Doc:
    """
    Convert the document.

    Arguments
    ---------
    doc
        The pandoc document

    Returns
    -------
    Doc
        The modified pandoc document
    """
    return run_filter(tikz, prepare=prepare, finalize=finalize, doc=doc)


if __name__ == "__main__":
    main()
