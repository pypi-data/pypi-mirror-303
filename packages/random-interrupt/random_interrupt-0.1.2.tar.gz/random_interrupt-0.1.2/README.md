# Random Interrupt Helper

Random Interrupt Helper is a command-line tool that generates random interrupts throughout a specified time period. It's inspired by Andrew Huberman's research on productivity and focus.

## Installation

You can install Random Interrupt Helper using pip:

```
pip install random-interrupt
```

For development purposes, you can clone the repository and install it in editable mode:

1. Clone the repository:
   ```
   git clone https://github.com/gamesh411/random-interrupt.git
   cd random-interrupt
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the package in editable mode with development dependencies:
   ```
   pip install -e .[dev]
   ```

## Usage

For detailed usage instructions, please refer to the [Usage Guide](docs/usage.md).

## Dependencies

- Python 3.10+
- plyer==2.1.0

For development and testing:
- pytest==8.3.3
- pytest-mock==3.14.0
- pytest-cov==5.0.0

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

This tool is inspired by the research of Dr. Andrew Huberman on productivity and focus. For more information, visit [Huberman Lab](https://hubermanlab.com/).
