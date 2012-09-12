from fabric.context_managers import cd
from fabric.contrib.files import exists
from fabric.decorators import hosts
from fabric.decorators import task
from fabric.operations import run
from fabric.operations import sudo

PACKAGES = [
    'binutils',
    'build-essential',
    'git',
    'libjpeg-dev',
    'lynx-cur',
    'memcached',
    'nginx',
    'python-dev',
    'python-gdal',
    'python-imaging',
    'python-lxml',
    # 'python-mapnik',
    'python-matplotlib',
    'python-psycopg2',
    'python-pyproj',
    'python-pysqlite2',
    'python-scipy',
    'python-setuptools',
    'python-virtualenv',
    'spatialite-bin',
    'subversion',
    'unzip',
    # TODO: check some of 'em for non-X-using packages. Too much is grabbed.
    ]


@task
@hosts('vagrant@33.33.33.20')
def initial_setup():
    sudo("apt-get update")
    sudo("apt-get install " + ' '.join(PACKAGES))
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
