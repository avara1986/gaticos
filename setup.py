from setuptools import find_packages, setup

install_requires = [
    'click>=8.0.3',
]

setup(
    name="gaticos",
    version="0.0.2",
    author="Alberto Vara",
    author_email="avara1986 <a.vara.1986@gmail.com>",
    description="Librería de ejemplo",
    long_description="",
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    license="License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    platforms=["any"],
    keywords="",
    url='',
    packages=find_packages(
        exclude=[
            '*.tests',
            '*.tests.*',
            'tests.*',
            'tests',
            '*.examples',
            '*.examples.*',
            'examples.*',
            'examples',
        ]
    ),
    install_requires=install_requires,
    include_package_data=True,
    entry_points={'console_scripts': ['gaticos = gaticos.main:main']},
    zip_safe=True,
)
