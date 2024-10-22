from setuptools import setup, find_packages

setup(
    name='yinhe',
    version='1.3.12',
    description='A brief description of the package',
    author='yinhedata.com',
    vx='yhshuju',
    packages=['yinhepy'],
    package_data={
        'yinhepy': ['*.csv','*.pyc','*.dll']

    },
    install_requires=[
            'click',
            'pandas',
            'six',
            'cryptography',
            'akshare'
    ],
    python_requires='==3.9'
)
