from setuptools import setup, find_packages

setup(
    name='rishtedaar',
    version='1.0.3',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='A Django app to perform health checks for various services.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ramsuthar305/rishtedaar',  # Your GitHub repository URL
    author='Ram Suthar',
    author_email='ramsuthar305@gmail.com',
    python_requires='>=3.7',
    install_requires=[
        'kombu>=5.2.3',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.2',  # Specify the versions of Django you support
        'Framework :: Django :: 4.0',
        'Framework :: Django :: 4.1',
        'Framework :: Django :: 4.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
