=================
CloudtopiaaClient
=================

CloudtopiaaClient is a command-line client for Cloudtopiaa that brings
the command set for Compute, Identity, Image, Network, Object Store, and Block
Storage APIs together in a single shell with a uniform command structure.

The primary goal is to provide a unified shell command structure and a common
language to describe operations in Cloudtopiaa.

Getting Started
===============

Cloudtopiaa Client can be installed from PyPI using pip::

    pip install cloudtopiaaclient

There are a few variants on getting help. A list of global options and supported
commands is shown with ``--help``::

    cloudtopiaa --help

There is also a ``help`` command that can be used to get help text for a specific
command::

    cloudtopiaa help
    cloudtopiaa help server create
