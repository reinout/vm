#!/usr/bin/python
import glob
import os

ANSIBLE_CFG_FILENAME = 'ansible.cfg'


def main():
    vagrantfiles = glob.glob('vagrantfile_*')
    vm_names = [vagrantfile.split('_')[-1] for vagrantfile in vagrantfiles]
    for vm_name in vm_names:
        if not os.path.exists(vm_name):
            os.mkdir(vm_name)
        relevant_filenames = glob.glob('*_%s*' % vm_name)
        os.chdir(vm_name)
        print("Working in %s" % os.getcwd())
        for relevant_filename in relevant_filenames:
            filename_inside_vm = relevant_filename.replace('_%s' % vm_name,
                                                           '')
            if not os.path.exists(filename_inside_vm):
                src = '../%s' % relevant_filename
                os.symlink(src, filename_inside_vm)
                print("Linked %s to %s" % (src, filename_inside_vm))

            if not os.path.exists(ANSIBLE_CFG_FILENAME):
                src = '../%s' % ANSIBLE_CFG_FILENAME
                os.symlink(src, ANSIBLE_CFG_FILENAME)
                print("Linked %s to %s" % (src, ANSIBLE_CFG_FILENAME))

            if not os.path.exists('utils'):
                src = '/Users/reinout/utils'
                os.symlink(src, 'utils')
                print("Linked %s to %s" % (src, 'utils'))

        os.chdir('..')


if __name__ == '__main__':
    main()
