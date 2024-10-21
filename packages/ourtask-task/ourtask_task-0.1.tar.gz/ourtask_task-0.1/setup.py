from setuptools import setup, find_packages

setup(
    name='ourtask_task',
    version='0.1',
    packages=find_packages(),
    description='A simple JSON processing package',
    author='Willem van Heemstra',
    author_email='wvanheemstra@icloud.com',
    url='https://github.com/OurTask/task',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
