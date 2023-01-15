class Hour:
    def __init__(self, time=None, hour=None, minutes=None):
        if time:
            hour, minutes = time.split(':')
        self.hour = int(hour)
        self.minutes = int(minutes)

    def __str__(self):
        return f"{self.hour:02d}:{self.minutes:02d}"

    def __repr__(self):
        return f"{self.hour:02d}:{self.minutes:02d}"

    def __sub__(self, other):
        minutes = self.minutes
        hours = self.hour
        if other.minutes > minutes:
            minutes += 60
            hours -= 1
        minutes -= other.minutes
        hours -= other.hour
        return Hour(hour=hours, minutes=minutes)

    def __gt__(self, other):
        if self.hour != other.hour:
            return self.hour > other.hour
        return self.minutes > other.minutes

    def __lt__(self, other):
        if self.hour != other.hour:
            return self.hour < other.hour
        return self.minutes < other.minutes

    def get_total_minutes(self):
        return self.hour * 60 + self.minutes