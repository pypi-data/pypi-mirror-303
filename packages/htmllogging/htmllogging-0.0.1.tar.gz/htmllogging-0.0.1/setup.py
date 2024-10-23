import setuptools
import re

# Load description from the README
with open("README.md", "r") as fh:
    long_description = fh.read()

# Load version from teh module
with open("htmllogging/__init__.py", 'r', encoding='utf-8') as fh:
    content = fh.read()
    reg = re.compile(r"__version__\s*=\s*['\"]([\d\.]+)['\"]")
    version = reg.search(content).group(1)
    print(version)

setuptools.setup(
    name="htmllogging",
    version=version,
    author="Bender Robotics",
    author_email="kumpan@benderrobotics.com",
    description="Logging into HTML format.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.benderrobotics.com",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'Pillow>=6.2.1'
    ]
)
