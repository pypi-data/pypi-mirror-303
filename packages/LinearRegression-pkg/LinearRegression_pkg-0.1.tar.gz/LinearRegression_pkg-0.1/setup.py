from setuptools import setup, find_packages

setup(
    name='LinearRegression_pkg',
    version='0.1',
    packages=find_packages(),
    license='MIT',
    description='A simple linear regression model implemented from scratch.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/linear_regression_pkg',
    author='Said M Senhadji',
    author_email='saidsenhadji06@gmail.com',
    install_requires=['numpy'],  # Dependencies
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
