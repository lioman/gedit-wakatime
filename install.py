#!/usr/bin/env python3

import sys
import shutil
from os import path

base_path = path.dirname(path.abspath(__file__))
home_dir = path.expanduser('~')
gedit_plugins_dir = home_dir + '/.local/share/gedit/plugins'

plugin_module_name = 'gedit_wakatime'
plugin_module_src_dir = path.join(base_path, plugin_module_name)
plugin_module_dst_dir = path.join(gedit_plugins_dir, plugin_module_name)

plugin_descriptor_fname = 'wakatime.plugin'
plugin_descriptor_file = path.join(base_path, plugin_descriptor_fname)


try:
    assert PermissionError
except:
    class PermissionError(Exception):
        pass


def check_wakatime():
    try:
        import wakatime
        assert wakatime
    except:
        import pip
        pip.main(['install', 'wakatime'])


def install():
    check_wakatime()
    if path.exists(plugin_module_dst_dir):
        shutil.rmtree(plugin_module_dst_dir)
    shutil.copytree(plugin_module_src_dir, plugin_module_dst_dir)
    shutil.copy(plugin_descriptor_file, gedit_plugins_dir)
    print('Wakatime plugin installation successful.')
    print('Now activate it in gedit Edit > Preferences > Plugins.')


if __name__ == '__main__':
    try:
        install()
    except (PermissionError, IOError, OSError):
        print('ERROR: You must be root.')
        print('Try: sudo {}'.format(' '.join(sys.argv)))
