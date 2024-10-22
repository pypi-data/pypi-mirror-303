from setuptools import setup, find_packages

setup(
    name='n2_utils',
    version='0.1.2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django>=3.2',
    ],
    description='N2 Common Area',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='N2Mobil',
    author_email='muslum.turk@n2mobil.com.tr',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
    ],
)
