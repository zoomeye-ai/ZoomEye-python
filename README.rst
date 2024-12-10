ZoomEye-python
--------------

``ZoomEye`` is a cyberspace search engine, users can search for
network devices using a browser https://www.zoomeye.ai.

``ZoomEye-python`` is a Python library developed based on the
``ZoomEye API``. It provides the ``ZoomEye command line`` mode and can
also be integrated into other tools as an ``SDK``. The library allows
technicians to **search**, **filter**, and **export** ``ZoomEye`` data
more conveniently.



0x01 installation
~~~~~~~~~~~~~~~~~

It can be installed directly from ``pypi``:

::

   pip3 install zoomeyeai

or installed from ``github``:

::

   pip3 install git+https://github.com/zoomeye-ai/ZoomEye-python

0x02 how to use cli
~~~~~~~~~~~~~~~~~~~

After successfully installing ``ZoomEye-python``, you can use the
``zoomeyeai`` command directly, as follows:

::

   $ zoomeyeai -h
   usage: zoomeyeai [-h] [-v] {init,info,search} ...
    positional arguments:
      {init,info,search}
        init                Initialize the token for ZoomEye-python
        info                Show ZoomEye account info
        search              Search the ZoomEye database

    optional arguments:
      -h, --help            show this help message and exit
      -v, --version         show program's version number and exit


1.initialize token
^^^^^^^^^^^^^^^^^^

Before using the ``ZoomEye-python cli``, the user ``token`` needs to be
initialized. The credential is used to verify the user’s identity to
query data from ``ZoomEye``; only support API-KEY authentication methods.

You can view the help through ``zoomeyeai init -h``, and use ``APIKEY`` to
demonstrate below:

::

   $ zoomeyeai init -apikey "01234567-acbd-00000-1111-22222222222"
   successfully initialized
   Role: developer
   Quota: 10000

Users can login to ``ZoomEye`` and obtain ``APIKEY`` in personal
information (https://www.zoomeye.ai/profile); ``APIKEY`` will not
expire, users can reset in personal information according to their
needs.


2.query quota
^^^^^^^^^^^^^

Users can query personal information and data quota through the ``info``
command, as follows:

::

   $ zoomeyeai info
    "email": "",
    "username:": "",
    "phone", "",
    "created_at:": ""
    quota: {
        "plan": "" ,                # service level
        "end_date": "",             # service end date
        "points": "",               # This month remaining free amount
        "zoomeye_points": "",       # Amount of remaining payment this month
    }

3.search
^^^^^^^^

Search is the core function of ``ZoomEye-python``, which is used through
the ``search`` command. the ``search`` command needs to specify the
search keyword (``dork``), let's perform a simple search below:

::

   $ zoomeyeai search "telnet"
    ip                  port             domain               update_time
    192.53.120.134      7766             [unknown]            2024-12-06T15:20:08

   total: 1

Using the ``search`` command is as simple as using a browser to search
in ``ZoomEye``. by default, we display five more important fields. users
can use these data to understand the target information:

::

   1.ip             ip address
   2.port           port
   3.domain         domain of the target
   4.update_time    update time of the target

In the above example, the number to be displayed is specified using the
``-pagesize`` parameter. in addition, ``search`` also supports the following
parameters (``zoomeyeai search -h``) so that users can handle the data. we
will explain and demonstrate below.

::

  -h, --help            show this help message and exit
  -facets facets        if this parameter is specified, the corresponding data
                        will be displayed at the end of the returned result.
                        supported : 'product', 'device', 'service', 'os',
                        'port', 'country', 'subdivisions', 'city'
  -fields field=regexp  display data based on input fields please see:
                        https://www.zoomeye.ai/doc/
  -sub_type {v4,v6,web,all}
                        specify the type of data to search
  -page page            view the page of the query result
  -pagesize pagesize    specify the number of pagesize to search
  -figure {pie,hist}    Pie chart or bar chart showing data，can only be used
                        under facet and stat

4.graphical data
^^^^^^^^^^^^^^^^

The ``-figure`` parameter is a data visualization parameter. This parameter provides two display methods: ``pie (pie chart)`` and ``hist (histogram)``. The data will still be displayed without specifying it. When ``-figure`` is specified , Only graphics will be displayed. The pie chart is as follows:

.. figure:: https://raw.githubusercontent.com/knownsec/ZoomEye-python/master/images/image-20210205004653480.png
    :width: 500px

.. figure:: https://raw.githubusercontent.com/knownsec/ZoomEye-python/master/images/image-20210205005016399.png
    :width: 500px

The histogram is as follows:

.. figure:: https://raw.githubusercontent.com/knownsec/ZoomEye-python/master/images/image-20210205004806739.png
    :width: 500px

.. figure:: https://raw.githubusercontent.com/knownsec/ZoomEye-python/master/images/image-20210205005117712.png
    :width: 500px


0x03 use SDK
~~~~~~~~~~~~

.. _initialize-token-1:

1.initialize token
^^^^^^^^^^^^^^^^^^

Similarly, the SDK also supports API-KEY authentication methods,
``APIKEY``, as follows:

**APIKEY**

.. code:: python

   from zoomeye.sdk import ZoomEye

   zm = ZoomEye(api_key="01234567-acbd-00000-1111-22222222222")

.. _sdk-api-1:

2.SDK API
^^^^^^^^^

The following are the interfaces and instructions provided by the SDK:

::
   1.userinfo()
     get current user information
   2.search(dork, qbase64='', page=1, pagesize=20, sub_type='all', fields='', facets='')
     get network asset information based on query conditions.

.. _sdk-example-1:

3.SDK example
^^^^^^^^^^^^^

.. code:: python

   $ python3
      >>> import zoomeyeai.sdk as zoomeye
      >>> # Use API-KEY search
      >>> zm = zoomeye.ZoomEye(api_key="01234567-acbd-00000-1111-22222222222")
      >>> data = zm.search('country=cn')
      ip                            port                          domain                        update_time
      192.53.120.134                7766                          [unknown]                     2024-12-06T15:20:08
   ...



0x04 issue
~~~~~~~~~~

| **1.How to enter dork with quotes?**
| When using cli to search, you will encounter dork with quotes, for example: ``"<body style=\"margin:0;padding:0\"> <p align=\"center\"> <iframe src=\ "index.xhtml\""``, when dork contains quotation marks or multiple quotation marks, the outermost layer of dork must be wrapped in quotation marks to indicate a parameter as a whole, otherwise command line parameter parsing will cause problems. Then the correct search method for the following dork should be: ``'"<body style=\"margin:0;padding:0\"> <p align=\"center\"> <iframe src=\"index.xhtml\" "'``.

.. figure:: https://raw.githubusercontent.com/knownsec/ZoomEye-python/master/images/image-20210205131713799.png
    :width: 500px


.. figure:: https://raw.githubusercontent.com/knownsec/ZoomEye-python/master/images/image-20210205131802799.png
    :width: 500px



--------------

| References:
| https://www.zoomeye.ai/doc

| Zoomeye Team
| Time: 2024.12.05

.. |asciicast| image:: https://asciinema.org/a/qyDaJw9qQc7UjffD04HzMApWa.svg
   :target: https://asciinema.org/a/qyDaJw9qQc7UjffD04HzMApWa




















