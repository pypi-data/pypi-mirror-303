#!/usr/bin/env python3
#
#  _plt.py
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

# 3rd party
import matplotlib  # type: ignore[import]

current_backend = matplotlib.rcParams["backend"]

try:  # pragma: no cover
	# stdlib
	import tkinter  # noqa: F401  # lgtm [py/unused-import]
	matplotlib.use("TkAgg")
except ImportError:  # pragma: no cover
	pass

try:
	# 3rd party
	import matplotlib.pyplot  # type: ignore[import]  # noqa: E402
except ImportError:  # pragma: no cover
	matplotlib.rcParams["backend"] = current_backend

plt = matplotlib.pyplot
plt.style.use("default")

__all__ = ["plt"]
