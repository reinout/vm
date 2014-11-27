#!/usr/bin/python
import glob
import os

ANSIBLE_CFG_FILENAME = 'ansible.cfg'


def main():
    vagrantfiles = glob.glob('vagrantfile_*')
    vm_names = [vagrantfile.split('_')[-1] for vagrantfile in vagrantfiles]
    ignore_contents = [line.strip() for line in open('.gitignore')]
    hostsfile_contents = [line.strip() for line in open('/etc/hosts')
                          if line.strip()]
    known_hostnames = [line.split()[-1] for line in hostsfile_contents]

    for vm_name in vm_names:
        if not os.path.exists(vm_name):
            os.mkdir(vm_name)
        relevant_filenames = glob.glob('*_%s*' % vm_name)
        os.chdir(vm_name)
        print("Working in %s" % os.getcwd())
        for relevant_filename in relevant_filenames:
            filename_inside_vm = relevant_filename.replace('_%s' % vm_name,
                                                           '')
            if filename_inside_vm == 'vagrantfile':
                filename_inside_vm = 'Vagrantfile'  # Just making sure.
            if not os.path.exists(filename_inside_vm):
                src = '../%s' % relevant_filename
                os.symlink(src, filename_inside_vm)
                print("Linked %s to %s" % (src, filename_inside_vm))

            if not os.path.exists(ANSIBLE_CFG_FILENAME):
                src = '../%s' % ANSIBLE_CFG_FILENAME
                os.symlink(src, ANSIBLE_CFG_FILENAME)
                print("Linked %s to %s" % (src, ANSIBLE_CFG_FILENAME))

            for to_symlink in ['utils', 'Dotfiles']:
                if not os.path.exists(to_symlink):
                    src = '/Users/reinout/%s' % to_symlink
                    os.symlink(src, to_symlink)
                    print("Linked %s to %s" % (src, to_symlink))

        #   config.vm.network "private_network", ip: "10.0.0.12"
        if vm_name not in ignore_contents:
            print("%s should be added to .gitignore" % vm_name)
        if vm_name not in known_hostnames:
            print("%s should be added to /etc/hosts" % vm_name)
            print("private_network lines from the vagrant file:")
            for line in open('Vagrantfile'):
                if 'private_network' in line:
                    print(line)
            print('')

        os.chdir('..')


if __name__ == '__main__':
    main()
