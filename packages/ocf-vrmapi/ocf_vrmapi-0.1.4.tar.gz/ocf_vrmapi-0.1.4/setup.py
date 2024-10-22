from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='ocf_vrmapi',
    packages=find_packages(),
    version='0.1.4',
    description='Victron python api',
    license='MIT',
    long_description=readme,
    long_description_content_type='text/markdown',
    install_requires=['requests'],
)
