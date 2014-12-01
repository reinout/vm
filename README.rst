Vagrant VM directory
====================

The directory contains directories for vagrant/virtualbox/fusion virtual
machines and vagrant files.


Initial setup
-------------

A ``vagrantfile_django`` should be symlinked as ``django/Vagrantfile``. This
is done by the ``prepare.py`` script. Just run it and you're set. It also
checks certain things:

- Is the vagrant file symlinked? Same with other files named ``*_VMNAME*``. So
  ``provision_twaalf.yml`` ends up as ``twaalf/provision.yml``.

- Is there an ``ansible.cfg``? The symlinked one points at ``~/ansible/`` as a
  roles path, by default I keep my roles in there.

- Is there a symlink to ``~/utils/``? I always run zest.releaser (and other
  tools I maintain) as master checkouts.

- Is the vm dir in the ``.gitignore``?

- Is the hostname present in ``/etc/hosts``?


Network settings
----------------

I normally include a line like this in the ``Vagrantfile``::

    config.vm.network "private_network", ip: "10.0.0.12"

The IP address should be added to ``/etc/hosts`` with the vm name.
``prepare.py`` checks for this.


Provisioning
------------

Every VM should have a provision script. ``provision_VMNAME.yml``. No manual
steps, please.

I use some roles I made for my work (in an effort to make them a bit generic).
And I use https://github.com/reinout/reinoutible-vmsetup for my specific
custom VM setup.
