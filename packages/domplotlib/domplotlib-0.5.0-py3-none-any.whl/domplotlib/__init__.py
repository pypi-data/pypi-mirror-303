#!/usr/bin/env python3
#
#  __init__.py
"""
Dom's extensions to matplotlib.
"""
#
#  Copyright © 2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#  DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
#  OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
#  OR OTHER DEALINGS IN THE SOFTWARE.
#
#  "save_svg" based on matplotlib
#  |  1. This LICENSE AGREEMENT is between the Matplotlib Development Team
#  |  ("MDT"), and the Individual or Organization ("Licensee") accessing and
#  |  otherwise using matplotlib software in source or binary form and its
#  |  associated documentation.
#  |
#  |  2. Subject to the terms and conditions of this License Agreement, MDT
#  |  hereby grants Licensee a nonexclusive, royalty-free, world-wide license
#  |  to reproduce, analyze, test, perform and/or display publicly, prepare
#  |  derivative works, distribute, and otherwise use matplotlib
#  |  alone or in any derivative version, provided, however, that MDT's
#  |  License Agreement and MDT's notice of copyright, i.e., "Copyright (c)
#  |  2012- Matplotlib Development Team; All Rights Reserved" are retained in
#  |  matplotlib  alone or in any derivative version prepared by
#  |  Licensee.
#  |
#  |  3. In the event Licensee prepares a derivative work that is based on or
#  |  incorporates matplotlib or any part thereof, and wants to
#  |  make the derivative work available to others as provided herein, then
#  |  Licensee hereby agrees to include in any such work a brief summary of
#  |  the changes made to matplotlib .
#  |
#  |  4. MDT is making matplotlib available to Licensee on an "AS
#  |  IS" basis.  MDT MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR
#  |  IMPLIED.  BY WAY OF EXAMPLE, BUT NOT LIMITATION, MDT MAKES NO AND
#  |  DISCLAIMS ANY REPRESENTATION OR WARRANTY OF MERCHANTABILITY OR FITNESS
#  |  FOR ANY PARTICULAR PURPOSE OR THAT THE USE OF MATPLOTLIB
#  |  WILL NOT INFRINGE ANY THIRD PARTY RIGHTS.
#  |
#  |  5. MDT SHALL NOT BE LIABLE TO LICENSEE OR ANY OTHER USERS OF MATPLOTLIB
#  |  FOR ANY INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES OR
#  |  LOSS AS A RESULT OF MODIFYING, DISTRIBUTING, OR OTHERWISE USING
#  |  MATPLOTLIB , OR ANY DERIVATIVE THEREOF, EVEN IF ADVISED OF
#  |  THE POSSIBILITY THEREOF.
#  |
#  |  6. This License Agreement will automatically terminate upon a material
#  |  breach of its terms and conditions.
#  |
#  |  7. Nothing in this License Agreement shall be deemed to create any
#  |  relationship of agency, partnership, or joint venture between MDT and
#  |  Licensee.  This License Agreement does not grant permission to use MDT
#  |  trademarks or trade name in a trademark sense to endorse or promote
#  |  products or services of Licensee, or any third party.
#  |
#  |  8. By copying, installing or otherwise using matplotlib ,
#  |  Licensee agrees to be bound by the terms and conditions of this License
#  |  Agreement.
#

# stdlib
import itertools
from io import StringIO
from typing import IO, Iterable, Optional, Tuple, TypeVar, Union

# 3rd party
from domdf_python_tools.iterative import chunks
from domdf_python_tools.pagesizes import PageSize
from domdf_python_tools.paths import PathPlus, clean_writer
from domdf_python_tools.typing import PathLike
from matplotlib.artist import Artist  # type: ignore[import]
from matplotlib.axes import Axes  # type: ignore[import]
from matplotlib.figure import Figure  # type: ignore[import]
from matplotlib.legend import Legend  # type: ignore[import]
from typing_extensions import Literal

__all__ = ["create_figure", "horizontal_legend", "save_svg", "transpose"]

__author__: str = "Dominic Davis-Foster"
__copyright__: str = "2020 Dominic Davis-Foster"
__license__: str = "MIT License"
__version__: str = "0.5.0"
__email__: str = "dominic@davis-foster.co.uk"

_T = TypeVar("_T")


def save_svg(
		figure: Figure,
		fname: Union[PathLike, IO],
		*,
		dpi: Union[float, Literal["figure"], None] = None,
		facecolor: Union[str, Literal["auto"]] = 'w',
		edgecolor: Union[str, Literal["auto"]] = 'w',
		orientation: Literal["portrait", "landscape"] = "portrait",
		transparent: bool = False,
		bbox_inches: Optional[str] = None,
		pad_inches: float = 0.1,
		**kwargs,
		) -> None:
	r"""
	Save the given figure as an SVG.

	:param figure:
	:param fname: The file to save the SVG as.
		If ``format`` is set, it determines the output format, and the file is saved as ``fname``.
		Note that ``fname`` is used verbatim, and there is no attempt to make the extension,
		if any, of ``fname`` match ``format``, and no extension is appended.

		If ``format`` is not set, then the format is inferred from the extension of ``fname``, if there is one.

	:param dpi: The resolution in dots per inch. If ``'figure'``, use the figure's dpi value.
	:param facecolor: The facecolor of the figure. If ``'auto'``, use the current figure facecolor.
	:param edgecolor: The edgecolor of the figure.  If ``'auto'``, use the current figure edgecolor.
	:param orientation: Currently only supported by the postscript backend.

	:param transparent: If :py:obj:`True`, the axes patches will all be transparent;
		the figure patch will also be transparent unless ``facecolor`` and/or ``edgecolor`` are specified.
		This is useful, for example, for displaying a plot on top of a colored background on a web page.
		The transparency of these patches will be restored to their original values upon exit of this function.

	:param bbox_inches: Bounding box in inches: only the given portion of the figure is saved.
		If 'tight', try to figure out the tight bbox of the figure.

	:param pad_inches: Amount of padding around the figure when bbox_inches is 'tight'.

	:param \*\*kwargs: Additional keyword arguments passed to :meth:`~.Figure.savefig`.
	"""

	buf = StringIO()

	figure.savefig(
			fname=buf,
			format="svg",
			dpi=dpi,
			facecolor=facecolor,
			edgecolor=edgecolor,
			orientation=orientation,
			transparent=transparent,
			bbox_inches=bbox_inches,
			pad_inches=pad_inches,
			**kwargs,
			)

	# need this if 'transparent=True' to reset colors
	figure.canvas.draw_idle()

	if isinstance(fname, IO):
		clean_writer(buf.getvalue(), fname)
	else:
		PathPlus(fname).write_clean(buf.getvalue())


def transpose(iterable: Iterable[_T], ncol: int) -> Iterable[_T]:
	"""
	Transposes the contents of ``iterable`` so they are ordered right to left rather than top to bottom.

	:param iterable:
	:param ncol:

	:returns: An :class:`~typing.Iterable` contaning elements of the same type as ``iterable``.
	"""

	return itertools.chain.from_iterable(itertools.zip_longest(*chunks(tuple(iterable), ncol)))


def horizontal_legend(
		fig: Figure,
		handles: Optional[Iterable[Artist]] = None,
		labels: Optional[Iterable[str]] = None,
		*,
		ncol: int = 1,
		**kwargs,
		) -> Legend:
	"""
	Place a legend on the figure, with the items arranged to read right to left rather than top to bottom.

	:param fig: The figure to plot the legend on.
	:param handles:
	:param labels:
	:param ncol: The number of columns in the legend.
	:param kwargs: Addition keyword arguments passed to :meth:`matplotlib.figure.Figure.legend`.
	"""

	if handles is None and labels is None:
		handles, labels = fig.axes[0].get_legend_handles_labels()

	# Rearrange legend items to read right to left rather than top to bottom.
	if handles:
		handles = list(filter(None, transpose(handles, ncol)))
	if labels:
		labels = list(filter(None, transpose(labels, ncol)))

	return fig.legend(handles, labels, ncol=ncol, **kwargs)


def create_figure(
		pagesize: PageSize,
		left: float = 0.2,
		bottom: float = 0.14,
		right: float = 0.025,
		top: float = 0.13,
		) -> Tuple[Figure, Axes]:
	"""
	Creates a figure with the given margins,
	and returns a tuple of the figure and its axes.

	:param pagesize:
	:param left: Left margin
	:param bottom: Bottom margin
	:param right: Right margin
	:param top: Top margin
	"""  # noqa: D400

	# 3rd party
	from matplotlib import pyplot  # type: ignore[import]

	# Import here to avoid clobbering theme and backend choices.

	fig = pyplot.figure(figsize=pagesize)

	# [left, bottom, width, height]
	ax = fig.add_axes([left, bottom, 1 - left - right, 1 - top - bottom])

	return fig, ax
