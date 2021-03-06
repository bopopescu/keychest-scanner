import sys

from setuptools import setup
from setuptools import find_packages

version = '0.1.17'

# Please update tox.ini when modifying dependency version requirements
install_requires = [
    'pycrypto>=2.6',
    'cryptography>=1.9',
    'PyOpenSSL>=17.2.0',
    'requests',
    'setuptools>=1.0',
    'sarge>=0.1.4',
    'psutil',
    'pid>=2.0.1',
    'coloredlogs',
    'six',
    'future',
    'SQLAlchemy>=1.1',
    'shellescape',
    'flask>=0.12',
    'lxml',
    'MarkupSafe>=0.23',  # problem with deps
    'redis',
    'hiredis',
    'phpserialize',
    'pymysql',
    'tldextract',
    'ph4-python-whois>=0.6.8',
    'IPy',
    'python-dateutil',
    'idna>=2.5',
    'eventlet',
    'gevent',
    'flask-socketio',
    'flask-sse',
    'websocket-client',
    'sseclient-py',
    'socketIO-client',
    'roca-detect',
    'events',
    'certbot-external-auth>=0.0.5',
    'pylru',
    'PyYAML',
]

if sys.version_info < (3,):
    install_requires.append('scapy-ssl_tls')
else:
    install_requires.append('scapy-python3')

# env markers in extras_require cause problems with older pip: #517
# Keep in sync with conditional_requirements.py.
if sys.version_info < (2, 7):
    install_requires.extend([
        # only some distros recognize stdlib argparse as already satisfying
        'argparse',
        'mock<1.1.0',
    ])
else:
    install_requires.append('mock')


dev_extras = [
    'nose',
    'pep8',
    'tox',
]

docs_extras = [
    'Sphinx>=1.0',  # autodoc_member_order = 'bysource', autodoc_default_flags
    'sphinx_rtd_theme',
    'sphinxcontrib-programoutput',
]


setup(
    name='keychest-scanner',
    version=version,
    description='Keychest scanner',
    url='https://github.com/EnigmaBridge/keychest-scanner',
    author="Dusan Klinec (ph4r05) @ enigmabridge",
    author_email='dusan.klinec@gmail.com',
    license=open('LICENSE').read(),
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Security',
    ],

    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    extras_require={
        'dev': dev_extras,
        'docs': docs_extras,
    },

    entry_points={
        'console_scripts': [
            'keychest-server = keychest.server:main',
            'keychest-setup = keychest.cmd_setup:main',
            'keychest-ansible-inventory = keychest.ansible_inventory:main',
        ],
    }
)
