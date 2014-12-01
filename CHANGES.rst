Changelog for Reinout's vagrant VM setup
========================================

(Note: obviously I don't make releases as such. Versions are mostly for
documentation purposes.)


1.0 (unreleased)
----------------

- Moved the repo to github (https://github.com/reinout/vm) so that it might be
  useful as an example I can point to.

- Switched from a fabfile to an ansible setup.

- Added ``prepare.py`` file which prepares the vm subdirectories for use.
  Adding a bunch of symlinks and so.

- Using https://github.com/reinout/reinoutible-vmsetup for my custom VM setup
  stuff.
