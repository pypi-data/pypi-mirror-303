# coding utf8
import setuptools
from yxcompgen.versions import get_versions

with open('README.md') as f:
    LONG_DESCRIPTION = f.read()

setuptools.setup(
    name="yxcompgen",
    version=get_versions(),
    author="Yuxing Xu",
    author_email="xuyuxing@mail.kib.ac.cn",
    description="Xu Yuxing's personal comparative genomics tools",
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url="https://github.com/SouthernCD/yxcompgen",
    include_package_data=True,

    # entry_points={
    #     "console_scripts": ["yxcompgen = yxcompgen.cli:main"]
    # },

    packages=setuptools.find_packages(),

    install_requires=[
        "yxutil",
        "yxseq",
        "yxmath",
        "yxtree",
        "yxalign",
        "matplotlib>=3.5.0",
        "pandas>=1.0.1",
        "numpy>=1.18.1",
        "pyfaidx>=0.5.5.2",
        "interlap>=0.2.6",
        "biopython<=1.80",
        "bcbio-gff>=0.6.6",
        "tables",
    ],

    python_requires='>=3.5',
)
