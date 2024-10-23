from setuptools import setup, find_packages


VERSION = '0.0.23' 
DESCRIPTION = 'a pip-installable package with function for Arenz Group'
LONG_DESCRIPTION = 'My first Python package with a slightly longer description'

#Setting up
setup(
    name='Arenz_Group_Python',
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    license='MIT',
    package_dir={"arenz_group_python": "src/arenz_group_python"},
    packages=find_packages("src"),
    #packages=['ArenzGroupPython'],
    author='Gustav Wiberg',
    author_email='gustav.wiberg@unibe.ch',
    keywords=['python', 'arenz group', 'tdms'],
    url='https://github.com/guswib/arenz_group_python',
    install_requires=['nptdms','matplotlib', 'pathlib','scipy','numpy','pandas']
)
