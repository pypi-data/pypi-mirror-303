from setuptools import find_namespace_packages, setup

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='sr.comp.scorer',
    version='1.5.0',
    project_urls={
        'Code': 'https://github.com/PeterJCLaw/srcomp-scorer',
        'Issue tracker': 'https://github.com/PeterJCLaw/srcomp-scorer/issues',
    },
    packages=find_namespace_packages(include=['sr.*']),
    namespace_packages=['sr', 'sr.comp'],
    description="Student Robotics Competition Score Entry Application",
    long_description=long_description,
    include_package_data=True,
    zip_safe=False,
    author="Student Robotics Competition Software SIG",
    author_email="srobo-devel@googlegroups.com",
    install_requires=[
        'Flask >=1.0, <4',
        'sr.comp >=1.2, <2',
    ],
    extras_require={
        # When deploying at an event, libproton is very useful as it allows
        # running compstate scoring of match files standalone (i.e: outside
        # srcomp).
        'deploy': ['libproton'],
    },
    python_requires='>=3.9',
    classifiers=[
        'Intended Audience :: Information Technology',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
)
