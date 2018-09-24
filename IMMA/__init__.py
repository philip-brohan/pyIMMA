# (C) British Crown Copyright 2018, Met Office
#
# This code is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This code is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#

"""
This module provides a python API to `IMMA files <http://icoads.noaa.gov/e-doc/imma>`.

IMMA files are not necessarily consistent in their contents - each line can have a different set of extensions. So we can't treat the file as a table of data - instead we treat it as a list of records, and read those records one at a time.

So an IMMA file is best thought of as an `iterator <https://anandology.com/python-practice-book/iterators.html>`_. Set up a file as an iterator with the  :func:`get` function:

.. code-block:: python

    import IMMA
    iobs=IMMA.get('some_file.imma')

Then every time you call ```iobs.next()``` you will get the next record from ```some_file.imma```.

Each record is returned as a :obj:`dict` where vthe keys are the IMMA variable names. So after ```rec=iobs.next()```, the sea-surface temperature is in ```rec['SST']```.

|
"""


from structure import attachment
from structure import parameters
from structure import definitions
from read import *

