
import os
import shutil
import cython

import subprocess as sp


def decode_byte(s):
    try:
        return s.decode('utf-8')
    except:
        return s.decode('')

def create_content(source='test'):
    content = """
import numpy as np

from distutils.core import setup
from Cython.Build import cythonize

setup(
    name = '{source}',
    ext_modules=cythonize('{source}.pyx'),
    include_dirs=[np.get_include()]
)
    """.format(source=source)

    return content



def create_setup(source='test'):

    content = create_content(source)
    file_name = 'setup_'+source+'.py'
    dir_abs_path = os.path.dirname(__file__)
    dir_name = os.path.basename(dir_abs_path)

    dir_ref = os.getcwd()
    os.chdir(dir_abs_path)

    with open(file_name,'w') as f:
        f.write(content)

    os.chdir(dir_ref)

    print('{} created'.format(os.path.join(dir_name, file_name)))



def run_setup(source='test', verbose=False):

    file_name = 'setup_'+source+'.py'
    dir_abs_path = os.path.dirname(__file__)
    dir_name = os.path.basename(dir_abs_path)

    dir_ref = os.getcwd()
    os.chdir(dir_abs_path)

    cmd = 'python {} build_ext --inplace'.format(file_name)
    print('compiling {} with cython v{}'.format(source+'.pyx', cython.__version__))
    process = sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    out = [line for line in process.stdout]
    err = [line for line in process.stderr]

    if verbose:
        if len(out) > 0:
            out = ''.join([line.decode('utf-8', 'replace') for line in out])
            print('\nstdout:\n', out)
        if len(err) > 0:
            err = ''.join([line.decode('utf-8', 'replace') for line in err])
            print('\nstderr:\n', err)

    os.chdir(dir_ref)

    # move up compile module one level
    li_file = [f for f in os.listdir(os.path.join(dir_name, dir_name)) if f.startswith(source)]
    for f in li_file:
        shutil.copy2(os.path.join(dir_name, dir_name, f), os.path.join(dir_name, f))


    print('done')
    print('if no error "from {} import {}"'.format(dir_name, source))
