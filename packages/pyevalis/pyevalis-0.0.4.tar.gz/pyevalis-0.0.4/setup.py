import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="pyevalis",
    version="0.0.4",
    description="Python package for PyEvalis",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Guryansh/temp7",
    author="Guryansh",
    author_email="guryanshsingla@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["PyEvalis"],
    include_package_data=True,
    install_requires=['pandas', 'numpy', 'matplotlib', 'ipython', 'ipywidgets', 'seaborn', 'tabulate'],
    entry_points={"console_scripts": ["pyevalis=pyevalis.__main__:main"]},
)
