from setuptools import setup, find_packages

setup(
    name='yinhepy',
    version='1.3.13',
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
    ]
)
