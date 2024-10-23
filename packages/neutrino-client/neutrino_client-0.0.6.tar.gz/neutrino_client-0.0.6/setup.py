from setuptools import find_packages, setup

setup(
    name='neutrino_client',
    packages=find_packages(include=['neutrino_client']),
    version='0.0.6',
    description='Neutrino client SDK',
    author='dpdzero',
    install_requires=['grpcio', 'grpcio-tools', 'protobuf', 'pydantic'],
    setup_requires=[],
    tests_require=['pytest'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
    ],
)

# python3 setup.py sdist bdist_wheel
