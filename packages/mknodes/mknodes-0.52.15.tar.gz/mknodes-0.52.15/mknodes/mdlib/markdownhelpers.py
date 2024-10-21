from __future__ import annotations

from typing import TYPE_CHECKING

from mknodes.utils import log


if TYPE_CHECKING:
    import markdown


logger = log.get_logger(__name__)


class CustomFence:
    """Formatter wrapper."""

    def __init__(self, extensions: list):
        self.extensions = extensions

    def custom_formatter(
        self,
        source,
        language,
        css_class,
        options,
        md: markdown.Markdown,
        classes=None,
        id_value="",
        attrs=None,
        **kwargs,
    ):
        # import mknodes as mk

        # node_kls = getattr(mk, language)
        print(f"{language=} {css_class=} {options=} {classes=} {id_value=} {attrs=}")
        try:
            return md.convert(source)
        except Exception:
            logger.exception("Error for custom fence %s", language)
            raise


def generate_fences():
    import mknodes as mk

    dcts = []
    for node_name in mk.__all__:
        dct = {"name": node_name, "class": node_name, "format": fence.custom_formatter}
        dcts.append(dct)
    return dcts


if __name__ == "__main__":
    from mknodes.mdlib import mdconverter

    fence = CustomFence(extensions=[])
    fences = generate_fences()
    md = mdconverter.MdConverter(extensions=["attr_list"], custom_fences=fences)
    text = "```{.MkText shift_header_levels=1}\ntest\n```"
    result = md.convert(text)
    print(result)
