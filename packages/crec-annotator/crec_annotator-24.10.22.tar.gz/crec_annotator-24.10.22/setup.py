from setuptools import setup, find_packages

setup(
    name='crec_annotator',
    version='24.10.22',
    author='Yichi Zhang',
    author_email='yichizhang2002@gmail.com',
    description='A tool to annotate and view congressional record text files.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/YZhang-Jeremy/crec_annotator/',
    packages=find_packages(),
    install_requires=[
        'tkinter',
    ],
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
    entry_points={
        'console_scripts': [
            'crec-annotator=crec_annotator.main:main',
        ],
    },
    include_package_data=True,
)
