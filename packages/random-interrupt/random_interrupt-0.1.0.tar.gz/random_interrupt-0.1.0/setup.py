from setuptools import setup, find_packages

setup(
    name="random_interrupt",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "plyer==2.1.0",
    ],
    extras_require={
        "dev": [
            "pytest==7.3.1",
            "pytest-mock==3.10.0",
            "pytest-cov==4.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "random_interrupt=random_interrupt.main:main",
        ],
    },
    tests_require=[
        "pytest==7.3.1",
        "pytest-mock==3.10.0",
        "pytest-cov==4.0.0",
    ],
    command_options={
        'test': {
            'pytest_args': ['tests/']
        }
    },
)
