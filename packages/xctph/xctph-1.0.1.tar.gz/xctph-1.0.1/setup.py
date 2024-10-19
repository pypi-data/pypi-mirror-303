from setuptools import setup

setup(
    name='xctph',
    version='1.0.1',
    packages=['xctph'],
    url='',
    license='',
    install_requires=['numpy', 'scipy', 'h5py', 'xmltodict', "setuptools"],
    author='jonah haber',
    author_email='',
    description='Package for computing exciton phonon matrix elements.',
    scripts=[
        'xctph/write_eph_h5.py',
        'xctph/write_xct_h5.py',
        'xctph/compute_xctph.py',
        'xctph/print_eph.py',
        'xctph/print_xctph.py',
        ]
)
