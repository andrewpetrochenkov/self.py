import setuptools

setuptools.setup(
    name='self',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
