import argparse
import random
import time
from typing import List
from plyer import notification

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Random Interrupt Helper inspired by Andrew Huberman's research")
    parser.add_argument("--overall-time", type=int, required=True, help="Total time period in minutes")
    parser.add_argument("--number-of-interrupts", type=int, required=True, help="Total number of interrupts")
    parser.add_argument("--min-gap", type=float, help="Minimum time between interrupts in minutes")
    parser.add_argument("--notification-title", type=str, default="Random Interrupt", help="Title for the notification")
    parser.add_argument("--notification-message", type=str, default="Time for a break!", help="Message for the notification")
    parser.add_argument("--notification-timeout", type=int, default=10, help="Notification timeout in seconds")
    return parser.parse_args()

def validate_input(args: argparse.Namespace) -> None:
    if args.overall_time <= 0:
        raise ValueError("Overall time must be positive")
    if args.number_of_interrupts <= 0:
        raise ValueError("Number of interrupts must be positive")
    if args.min_gap is not None:
        if args.min_gap < 0:
            raise ValueError("Minimum gap must be non-negative")
        if args.min_gap * args.number_of_interrupts > args.overall_time:
            raise ValueError("Minimum gap is too large for the given number of interrupts and overall time")

def generate_interrupt_times(args: argparse.Namespace) -> List[float]:
    def generate_times():
        return sorted([random.uniform(0, args.overall_time) for _ in range(args.number_of_interrupts)])

    interrupt_times = generate_times()
    if args.min_gap is None:
        return interrupt_times

    while not all(j-i >= args.min_gap for i, j in zip(interrupt_times[:-1], interrupt_times[1:])):
        interrupt_times = generate_times()
    return interrupt_times

def send_notification(title: str, message: str, timeout: int):
    notification.notify(
        title=title,
        message=message,
        app_icon=None,
        timeout=timeout,
    )

def main():
    args = parse_arguments()
    validate_input(args)
    interrupt_times = generate_interrupt_times(args)
    
    print(f"Generated {len(interrupt_times)} interrupts:")
    for t in interrupt_times:
        print(f"  {t:.2f} minutes")

    start_time = time.time()
    for t in interrupt_times:
        wait_time = t * 60 - (time.time() - start_time)
        if wait_time > 0:
            time.sleep(wait_time)
        send_notification(args.notification_title, args.notification_message, args.notification_timeout)

if __name__ == "__main__":
    main()

# Expose functions for testing
__all__ = ['parse_arguments', 'validate_input', 'generate_interrupt_times', 'send_notification', 'main']
