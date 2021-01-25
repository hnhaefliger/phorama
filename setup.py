import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="phorama",
    version="0.0.1",
    author="Henry Haefliger",
    author_email="code@henryhaefliger.com",
    description="A package for neural image enhancement",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hnhaefliger/placeholder",
    license='GPLv3+',
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.0',
)
