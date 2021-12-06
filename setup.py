from setuptools import setup

setup(
    name='jupyterhub-kyotta-jwt',
    version='0.1',
    description='JsonWebToken Authenticator for JupyterHub',
    url='https://github.com/guoziqin/kfe-code',
    author='guoziqin',
    author_email='gzq2132@163.com',
    license='Apache 2.0',
    tests_require = [
    'unittest2',
    ],
    test_suite = 'unittest2.collector',
    packages=['kfe-code'],
    install_requires=[
        'jupyterhub',
        'python-jose',
    ]
)
