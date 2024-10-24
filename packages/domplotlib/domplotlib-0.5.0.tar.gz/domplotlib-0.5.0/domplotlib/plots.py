#!/usr/bin/env python3
#
#  plots.py
"""
Custom plotting functions.

.. versionadded:: 0.2.0
"""
#
#  Copyright © 2021 Dominic Davis-Foster <dominic@davis-foster.co.uk>
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

# stdlib
from typing import Collection, List, Optional, Tuple, overload

# 3rd party
from cawdrey.tally import SupportsMostCommon, Tally
from matplotlib.patches import Wedge  # type: ignore[import]
from matplotlib.text import Text  # type: ignore[import]

__all__ = ["pie_from_tally"]


@overload
def pie_from_tally(
		tally: "Tally[str]",
		explode: Collection[str] = (),
		*,
		percent: bool = ...,
		reverse: bool = ...,
		autopct: None = ...,
		**kwargs,
		) -> Tuple[List[Wedge], List[Text]]: ...


@overload
def pie_from_tally(
		tally: Tally[str],
		explode: Collection[str] = (),
		*,
		percent: bool = ...,
		reverse: bool = ...,
		autopct: str,
		**kwargs,
		) -> Tuple[List[Wedge], List[Text], List[Text]]: ...


def pie_from_tally(
		tally: Tally[str],
		explode: Collection[str] = (),
		*,
		percent: bool = False,
		reverse: bool = False,
		autopct: Optional[str] = None,
		**kwargs,
		) -> Tuple[List, ...]:
	r"""
	Construct a pie chart from :class:`cawdrey.tally.Tally`.

	:param tally:
	:param explode: A list of key names to explode the segments for.
	:param percent: If :py:obj:`True`, shows the percentage of each element out of the sum of all elements.
	:param reverse: Order the wedges clockwise rather than anticlockwise..
	:param \*\*kwargs: Other keyword arguments taken by :meth:`matplotlib.axes.Axes.pie`.

	:return:

		* patches (:class:`list`\) -- A sequence of `matplotlib.patches.Wedge` instances
		* texts (:class:`list`\) -- A list of the label `.Text` instances.
		* autotexts (:class:`list`\) -- A list of `.Text` instances for the numeric labels. This will only
		  be returned if the parameter *autopct* is not *None*.
	"""

	if "ax" in kwargs:
		ax = kwargs.pop("ax")
	else:  # pragma: no cover

		# 3rd party
		from matplotlib import pyplot  # type: ignore[import]
		ax = pyplot.gca()

	kwargs.pop("labels", None)
	kwargs["autopct"] = autopct

	data: SupportsMostCommon[str]
	if percent:
		data = tally.as_percentage()
	else:
		data = tally

	if reverse:
		labels, sizes = list(zip(*reversed(data.most_common())))
	else:
		labels, sizes = list(zip(*data.most_common()))

	if explode:
		kwargs["explode"] = tuple(0.1 if label in explode else 0.0 for label in labels)
	else:
		kwargs.pop("explode", None)

	return ax.pie(sizes, labels=labels, **kwargs)
