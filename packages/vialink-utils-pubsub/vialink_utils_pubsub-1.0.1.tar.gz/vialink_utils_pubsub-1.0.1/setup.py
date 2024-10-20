import setuptools

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name='vialink-utils-pubsub',
    version='1.0.1',
    packages=setuptools.find_namespace_packages(include=['vialink.utils.*']),
    url='',
    license='Apache 2.0',
    author='SSripilaipong',
    author_email='santhapon.s@siametrics.com',
    python_requires='>=3.7',
    description='ViaLink Utils PubSub',
    install_requires=requirements,
)
