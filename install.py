import os

exclude = ['install.py']

home = os.path.expanduser('~')
here = os.path.dirname(os.path.realpath(__file__))

# symlink all the files in this repo in the home directory
for f in os.listdir('.'):
    if f in exclude or f[0] == '.':
        continue

    local_file = "%s/%s" % (here, f)
    install_file = "%s/.%s" % (home, f)
    if os.path.exists(install_file):
        backup_file = '%s_bak' % install_file
        cmd = 'mv %s %s' % (install_file, backup_file)
        print(cmd)
        os.system(cmd)

    cmd = 'ln -sf %s %s' % (local_file, install_file)
    print(cmd)
    os.system(cmd)

