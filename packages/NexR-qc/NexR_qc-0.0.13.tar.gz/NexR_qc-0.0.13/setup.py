from setuptools import find_packages, setup

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="NexR_qc",
    version="0.0.13",
    long_description=long_description,
    long_description_content_type="text/markdown",
    description="PYPI package creation written by NexR-qc",
    author="mata.lee",
    author_email="ldh3810@gmail.com",
    url="https://github.com/mata-1223/NexR_qc",
    install_requires=[
        "numpy",
        "pandas",
        "openpyxl",
    ],
    packages=find_packages(exclude=[]),
    keywords=["qc", "NexR", "mata.lee", "NexR_qc", "python", "python tutorial", "pypi"],
    python_requires=">=3.6",
    package_data={},
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
