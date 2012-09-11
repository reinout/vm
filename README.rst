Vagrant VM directory
====================

The directory contains directories for vagrant/virtualbox virtual machines and
vagrant files. A ``vagrantfile_django`` should be symlinked as
``django/Vagrantfile``.

And the ``django/`` directory, in that case, really really should be excluded
in the ``.gitignore`` file :-)

To set up a vm after creating it (it should be running!), run::

    $ fab initial_setup

This sets up reinout's user and installs the tools and dotfiles.
