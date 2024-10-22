from setuptools import setup, find_packages

setup(
    name="phoneshift",
    version="0.0.5",
    packages=find_packages(),
    install_requires=[],
    author="Phoneshift",
    author_email="dev@phoneshift.ing",
    description="A simple example private package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    # url="https://github.com/nydasco/package_publishing",  # TODO TODO TODO
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
