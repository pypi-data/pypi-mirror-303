import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Kbrain",
    version="0.1",
    author="Siu",
    author_email="siukkokko@gmail.com",
    description="Kbrain is deeplearning package",
    long_description=long_description,
    url="https://github.com/Kbrain2/KBrain.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)