from setuptools import setup, find_packages

with open("docs/usage.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="random_interrupt",
    version="0.1.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "plyer==2.1.0",
    ],
    extras_require={
        "dev": [
            "pytest==8.3.3",
            "pytest-mock==3.14.0",
            "pytest-cov==5.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "random_interrupt=random_interrupt.main:main",
        ],
    },
    author="Endre Fülöp",
    author_email="gamesh411@gmail.com",
    description="A command-line tool that generates random interrupts throughout a specified time period, inspired by Andrew Huberman's research on productivity and focus.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gamesh411/random-interrupt",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.10",
)
