from setuptools import setup


def get_version():
    version = {}
    with open("handouter/version.py") as f:
        exec(f.read(), version)
    return version["__version__"]


long_description = """Handouter is a script that wraps tectonic
to generate handouts for [Chgk](https://en.wikipedia.org/wiki/What%3F_Where%3F_When%3F)

Project home on gitlab: https://gitlab.com/peczony/handouter
"""


setup(
    name="handouter",
    version=get_version(),
    author="Alexander Pecheny",
    author_email="ap@pecheny.me",
    description="Handouter is a script that wraps tectonic to generate handouts for [Chgk](https://en.wikipedia.org/wiki/What%3F_Where%3F_When%3F)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/peczony/handouter",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["handouter"],
    entry_points={"console_scripts": [
        "hndt = handouter.__main__:main",
        "hndt-gen = handouter.gen:main",
        "hndt-pack = handouter.pack:main",
    ]},
    install_requires=["pecheny_utils"],
    extras_require={
        "full": ["chgksuite", "pypdf"],
    }
)
