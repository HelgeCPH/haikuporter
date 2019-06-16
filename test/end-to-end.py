# This test expects that `haikuporter` and `haikuports` are both cloned into
# /bin/home
# Additionally, it expects that `python` is available on the path and defaults 
# to Python 2.7 and that `python3` is available on the path and it defaults to
# Python 3.7

import os
import shutil
import hashlib
import subprocess as sbp


py2_build_cmd = '/boot/home/haikuporter/haikuporter which-2.21'
py2_clean_cmd = '/boot/home/haikuporter/haikuporter --clean which-2.21'
py3_build_cmd = 'python3 /boot/home/haikuporter_port/haikuporter --debug which-2.21'

which_recipe_dir = '/boot/home/haikuports/sys-apps/which/'
tmp_dir = '/tmp'
result_pkg = '/boot/home/haikuports/packages/which_source-2.21-5-source.hpkg'
result_pkg_bkp = '/tmp/which_source-2.21-5-source.hpkg'


def build_with_python2():
    os.chdir(which_recipe_dir)
    sbp.run(py2_build_cmd, shell=True)
    assert os.path.isfile(result_pkg)


def build_with_python3():
    os.chdir(which_recipe_dir)
    sbp.run(py3_build_cmd, shell=True)
    assert os.path.isfile(result_pkg)


def cleanup():

    sbp.run(py2_clean_cmd, shell=True)
    # This file is pickled and it confuses the different Python versions
    shutil.remove('/boot/home/haikuports/repository/hpkgInfoCache')


def compute_hash(filepath):
    with open(filepath, 'rb') as fp:
        content = fp.read()
    return hashlib.sha256(content).hexdigest()


if __name__ == '__main__':
    start_dir = os.getcwd()

    build_with_python2()

    shutil.move(result_pkg, tmp_dir)

    build_with_python3()

    os.chdir(start_dir)

    assert compute_hash(result_pkg_bkp) == compute_hash(result_pkg)


# TODO: There is something wrong in: "/boot/home/haikuporter_port/HaikuPorter/Package.py", line 292, in createBuildPackage
# ['/bin/package', 'create', '-bi', '/build-packages/which-2.21-5-build.PackageInfo', '-I', '/packaging/which', '/build-packages/which-2.21-5-build.hpkg']

# ['/bin/package', 'create', '-bi', u'/build-packages/which-2.21-5-build.PackageInfo', '-I', u'/packaging/which', u'/build-packages/which-2.21-5-build.hpkg']
# ['/bin/package', 'create', '-bi', u'/build-packages/which_debuginfo-2.21-5-build.PackageInfo', '-I', u'/packaging/which_debuginfo', u'/build-packages/which_debuginfo-2.21-5-build.hpkg']

