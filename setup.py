from setuptools import setup, find_packages

setup(
    name='ft_package',
    version='0.0.1',
    description='A sample test package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='maserrie',
    author_email='maserrie@student.42perpignan.fr',
    url='https://github.com/TsRun/ft_package',
    packages=find_packages(),
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)
