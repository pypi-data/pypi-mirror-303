import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="pollination-io",
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    author="Pollination",
    author_email="info@pollination.solutions",
    description="A Pollination extension to facilitate working with Pollination SDK.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pollination/pollination-io",
    packages=setuptools.find_packages(exclude=["tests"]),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent"
    ],
    license="Apache-2.0 License"
)
