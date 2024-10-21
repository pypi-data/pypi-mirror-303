from setuptools import setup, Extension
from Cython.Build import cythonize
import os
import sys

include_path = os.path.abspath(os.path.dirname(__file__))

# Modify extra_compile_args based on platform
if sys.platform == 'win32':
    extra_compile_args = ["/std:c++11", "/W3", "/O2"]  # MSVC compatible flags
    extra_link_args = ["/DEBUG"]
else:
    extra_compile_args = ["-std=c++11", "-Wall", "-Wextra", "-O3"]
    extra_link_args = ["-g"]

extensions = [
    Extension(
        name="thinelc",  
        sources=["thinelc/thinelc.pyx"],
        language="c++",   
        extra_compile_args=extra_compile_args,
        extra_link_args=extra_link_args,
    )
]

setup(
    name="thinelc",
    author="Bolun Zhang",
    author_email="bolun_zhangzbl@outlook.com",
    description="A thin ELC Wrapper for Python",
    url="https://github.com/BolunZhangzbl/thinelc",
    packages=["thinelc"],
    ext_modules=cythonize(
        extensions, 
        compiler_directives={"language_level": "3"},  
        gdb_debug=True,
        force=True
    ),
    setup_requires=["setuptools>=42", "wheel", "Cython"], 
    install_requires=["Cython"],
)   