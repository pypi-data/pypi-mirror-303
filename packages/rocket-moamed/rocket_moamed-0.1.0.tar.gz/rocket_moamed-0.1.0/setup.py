from setuptools import setup, find_packages

setup(
    name='rocket-moamed',
    version='0.1.0',
    author='Boufafa MOhamed',
    author_email='boufafa.moamed@gmail.com',
    description='A package for simulating rockets and shuttles.',
    packages=find_packages(),
    install_requires=[
        # List your package dependencies here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
