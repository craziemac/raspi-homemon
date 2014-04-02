from distutils.core import setup

setup(
    name='RasPi-HomeMon',
    version='0.1.dev',
    description='Monitor your home',
    author='Marcus Jonsson',
    author_email='marcus.jonsson.mj+homemon@gmail.com',
    url='',
    license='LICENSE.txt',
    long_description=open('README.txt').read(),
    packages=[
        'homemon',
        'homemon.client',
        'homemon.core',
        'homemon.database',
        'homemon.external_cpp',
        'homemon.hardware',
        'homemon.web_service'
    ],
    install_requires=[
        "MySQL",
    ],
)
