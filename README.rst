amtTimer
========

|license| |python| |pypi| |build| |coverage|

----

*amtTimer* is a Python 3 package that provides a class to measure
code performances.

Time points are tagged with a name and multiple measurements of
the same time point are aggregated.
Statistics on measurements can be built and used for analysis.

----

Basic Usage
-----------

Install with pip:

.. code:: bash

    pip install amtTimer

Import the ``Timer`` and ``TimerSingleton`` class in your python code,
and instanciate it

.. code:: python

    from amtTimer import Timer, TimerSingleton

    myTimer = Timer()

The TimerSingleton class can be used to create a global Timer object.

Adding a new time point can be done inside or outside a context manager.

.. code:: python

    # new time point with context manager
    with myTimer("point_1"):
        # do something

    # new time point outside a context manager
    point_2 = myTimer("point_2")
    point_2.start()
    # do something
    point_2.stop()

Retrieving the list of time points already defined:

.. code:: python

    for name in myTimer.names():
        print(f"Time Point {name} is defined")


Statistics are provided by the `amtStats`_ module.
The values for a particular time point can be obtained with:

.. code:: python

    results = myTimer.stats("point_1")


Tests
-----

Run tests:

.. code:: bash

    $ tox

License
-------

This package is released under the Apache License 2.0. See the bundled
`LICENSE`_ file for details.


.. _amtStats: https://https://github.com/aimktech/amtStats

.. _LICENSE: https://github.com/aimktech/amtTimer/blob/master/LICENSE.txt

.. |python| image:: https://img.shields.io/static/v1?label=python&message=3%2e7%2b&color=blue&style=flat-square
    :target: https://www.python.org
    :alt: Python 3.7+

.. |pypi| image:: https://img.shields.io/pypi/v/amttimer?color=blue&style=flat-square
    :target: https://pypi.org/project/amttimer
    :alt: Latest version released on PyPI

.. |build| image:: https://img.shields.io/travis/aimktech/amtTimer/master.svg?style=flat-square
    :target: https://travis-ci.org/aimktech/amtTimer
    :alt: Travis build

.. |coverage| image:: https://img.shields.io/coveralls/github/aimktech/amtTimer/master?style=flat-square
    :alt: Tests coverage

.. |license| image:: https://img.shields.io/badge/license-Apache--2.0-blue.svg?style=flat-square
    :target: https://raw.githubusercontent.com/aimktech/amtTimer/master/LICENSE.txt
    :alt: Package license
