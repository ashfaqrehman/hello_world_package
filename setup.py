import setuptools

setuptools.setup(
    name='hello-world',
    version='0.0.1',
    author='George Costanza',
    description='This is my hello world program!',
    packages=['hello_world'],
    entry_points={
        'console_scripts': ['hello=hello_world.hello:main']
    },
    install_requires=[
        "requests>=2"
    ]
)
