from setuptools import find_packages, setup

setup(
    name="smallbench",
    version="0.2.13",
    packages=find_packages(),
    install_requires=[
        "zyk>=0.2.17",
        "apropos==0.4.5"
    ],
    author="Josh Purtell",
    author_email="jmvpurtell@gmail.com",
    description="",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/JoshuaPurtell/SmallBench",
    license="MIT",
)
