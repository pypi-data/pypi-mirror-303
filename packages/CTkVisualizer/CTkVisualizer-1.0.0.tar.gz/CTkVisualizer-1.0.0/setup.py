from setuptools import setup, find_packages

setup(
    name='CTkVisualizer',
    version='1.0.0',  # Update version as needed
    author='iLollek',
    author_email='loris_06@yahoo.de',
    description='A customtkinter widget for playing and visualizing Audio. ',
    long_description=open('README.md', encoding="utf-8").read(),  # Read from README
    long_description_content_type='text/markdown',
    url='https://github.com/iLollek/CTkVisualizer',  # Update with your GitHub URL
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',  # Update if using a different license
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',  # Specify your Python version requirement
)
