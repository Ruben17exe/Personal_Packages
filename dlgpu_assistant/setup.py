from setuptools import setup, fins_packages

setup(
    name="dlgpu_assistant",
    version="0.1.0",
    license="MIT",
    author="Rubén Hinojar",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[
        "logging==0.5.1.2",
        "tensorflow==2.9.0",
        "pandas==1.4.3",
        "numpy==1.23.2",
        "sklearn=1.1.2"
    ],
)
