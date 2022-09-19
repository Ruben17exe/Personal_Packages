from setuptools import setup, find_packages

setup(
    name="dlgpu_assistant",
    version="1.0",
    license="MIT",
    author="Rubén Hinojar",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[
        "tensorflow-gpu==2.9.0",
        "pandas==1.4.3",
        "numpy==1.23.1",
        "scikit-learn==1.1.2"
    ],
)
