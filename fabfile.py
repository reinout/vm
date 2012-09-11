from fabric.context_managers import cd
from fabric.contrib.files import exists
from fabric.decorators import hosts
from fabric.decorators import task
from fabric.operations import run
from fabric.operations import sudo


@task
@hosts('vagrant@33.33.33.20')
def initial_setup():
    sudo("apt-get install git python2.7-dev python-virtualenv")
    if not exists("tools"):
        run("git clone git@github.com:reinout/tools.git")
    if not exists("/Users"):
        sudo("mkdir /Users")
    if not exists("/Users/reinout"):
        with cd('/Users'):
            sudo("ln -s /home/vagrant reinout")
    with cd('tools'):
        run("virtualenv --system-site-packages .")
        run("bin/pip install . -r requirements.txt")
        run("./install_shell_scripts.sh")

    if not exists("Dotfiles"):
        run("git clone ssh://reinout@vanrees.org/~/git/Dotfiles")
        run("dotfiles --sync --force")
