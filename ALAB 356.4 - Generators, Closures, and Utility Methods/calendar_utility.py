import calendar
import datetime


class MarkedCalendar(calendar.TextCalendar):
    """A text calendar that puts [brackets] around one chosen day."""

    def __init__(self, marked_day=None):
        # firstweekday=6 makes weeks start on Sunday
        super().__init__(firstweekday=6)
        self.marked_day = marked_day

    def formatday(self, day, weekday, width):
        """Format one day cell; mark it if it is the chosen day."""
        if day == 0:
            return " " * width  # blank cell for days outside the month
        text = f"[{day}]" if day == self.marked_day else str(day)
        return text.center(width)


def get_number(prompt, low, high):
    """Keep asking until the user types a whole number from low to high."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Please type a whole number.")
            continue
        if low <= value <= high:
            return value
        print(f"Please type a number from {low} to {high}.")


def main():
    """Run the calendar utility."""
    try:
        year = get_number("Enter a year (for example 2025): ", 1, 9999)
        month = get_number("Enter a month number (1-12): ", 1, 12)
    except EOFError:
        print("Error: no input was received.")
        return

    today = datetime.date.today()
    month_name = calendar.month_name[month]

    # Mark today's day only if today is inside the chosen month and year
    in_month = (today.year == year and today.month == month)
    marked_day = today.day if in_month else None

    print(f"\n=== Calendar for {month_name} {year} ===")
    print(MarkedCalendar(marked_day).formatmonth(year, month, w=4))

    print(f"Today's date: {today.strftime('%B')} {today.day}, {today.year}")
    if in_month:
        print(f"Today is {month_name} {today.day}, {year}, "
              "shown above in [brackets].")
    else:
        print(f"Today is not in {month_name} {year}.")


if __name__ == "__main__":
    main()