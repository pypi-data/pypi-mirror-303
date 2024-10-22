# Random Interrupt Helper

Random Interrupt Helper is a command-line tool that generates random interrupts throughout a specified time period. It's inspired by Andrew Huberman's research on productivity and focus.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/random-interrupt-helper.git
   cd random-interrupt-helper
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the Random Interrupt Helper from the command line with the following options:

```
python src/random_interrupt/main.py --overall-time <minutes> --number-of-interrupts <count> [--min-gap <minutes>] [--notification-title <title>] [--notification-message <message>] [--notification-timeout <seconds>]
```

Arguments:
- `--overall-time`: Total time period in minutes (required)
- `--number-of-interrupts`: Total number of interrupts (required)
- `--min-gap`: Minimum time between interrupts in minutes (optional)
- `--notification-title`: Title for the notification (optional, default: "Random Interrupt")
- `--notification-message`: Message for the notification (optional, default: "Time for a break!")
- `--notification-timeout`: Notification timeout in seconds (optional, default: 10)

Example:
```
python src/random_interrupt/main.py --overall-time 60 --number-of-interrupts 5 --min-gap 5 --notification-title "Focus Break" --notification-message "Take a moment to relax" --notification-timeout 15
```

This will generate 5 random interrupts over a 60-minute period, with at least 5 minutes between each interrupt, and custom notification settings.

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
