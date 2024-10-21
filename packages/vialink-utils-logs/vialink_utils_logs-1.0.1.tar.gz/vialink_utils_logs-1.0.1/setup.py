import setuptools

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name='vialink-utils-logs',
    version='1.0.1',
    packages=setuptools.find_namespace_packages(include=['vialink.utils.*']),
    url='',
    license='Apache 2.0',
    author='yurananatul.m',
    author_email='yurananatul.m@via.link',
    python_requires='>=3.7',
    description='Vialink Utils',
    install_requires=requirements,
)
