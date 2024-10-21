import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="LoL.py",
    version="0.0.16",
    author="Blackcool70",
    author_email="blackcool70_cool7744@hotmail.com",
    description="A tiny Riot-league of legends Api wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Blackcool70/LoL.py",
    install_requires=[
        'requests',
    ],
    project_urls={
        "Bug Tracker": "https://github.com/Blackcool70/LoL.py/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['LoL'],
    python_requires=">=3.6",
)