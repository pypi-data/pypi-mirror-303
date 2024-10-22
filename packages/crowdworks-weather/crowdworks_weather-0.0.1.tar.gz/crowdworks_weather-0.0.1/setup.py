import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="crowdworks_weather",
    version="0.0.1",
    author="interlude0112",
    author_email="interlude0112@gmail.com",
    description="interlude0112 weather bot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "weather"},
    packages=setuptools.find_packages(where="weather"),
    python_requires=">=3.10",
)