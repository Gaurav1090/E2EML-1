from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="Gaurav1090",
    description="This project Demonstrate an End to End ML Pipeline involving varrious tech stacks.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Gaurav1090/EndToEndML",
    author_email="gauravsinghkaushik@gmail.com",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    licence="GNU",
    python_requires=">=3.6",
    install_require=[
        'dvc',
        'dvc[gdrive]',
        'dvc[s3]',
        'pandas',
        'scikit-learn'
    ]



)
