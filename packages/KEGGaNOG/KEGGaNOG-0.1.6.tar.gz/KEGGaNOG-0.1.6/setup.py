from setuptools import setup, find_packages

setup(
    name="KEGGaNOG",
    version="0.1.6",
    description="A tool for generating KEGG heatmaps from eggnog-mapper outputs.",
    long_description=open("README_PyPI.md").read(),
    long_description_content_type="text/markdown",
    author="Ilia Popov",
    author_email="iljapopov17@gmail.com",
    url="https://github.com/iliapopov17/KEGGaNOG",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "KEGGaNOG=kegg_a_nog.kegg_a_nog:main",  # Maps the command to the main function
        ],
    },
    install_requires=open("requirements.txt").read().splitlines(),
    python_requires=">=3.6",
)
