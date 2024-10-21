import datetime as dt
from datetime import datetime
import math
import re

class PoseidonDateTime(dt.datetime):
  """Class for representing dates on Poseidon. 
   Assumes Planetfall occurred at midnight on 3 January 2087, and is 
  represented by Colonial date 001.00."""

  # By definition
  planetfall = datetime.fromisoformat('2087-01-03 00:00')

  # By definition
  p_day_duration = dt.timedelta(hours=30, seconds=43)
  p_year_duration = p_day_duration * 330 + dt.timedelta(hours=13, minutes=2, seconds=17)

  def __new__(cls, year, month, day, hour=0, minute=0, second=0, 
               microsecond=0, tzinfo=None, *, fold=0):
    """Create a new PoseidonDateTime object, setting the attributes
    `p_year`, `p_day`, `p_hour`, `p_minute`, and `p_second` for the 
    Colonial datetime."""
    self = super(PoseidonDateTime, cls).__new__(cls, year, month, day, 
                  hour=hour, minute=minute, second=second, 
                  microsecond=microsecond, tzinfo=tzinfo, fold=fold)
    self.days_since_planetfall = self.since_planetfall() / PoseidonDateTime.p_day_duration
    self.count_years_days()
    self.set_hours()
    return self    

  def since_planetfall(self):
    return self - PoseidonDateTime.planetfall

  @classmethod
  def days_in_given_year(cls, year):
    """"Leap years are when the year number has an odd remainder when
    divided by seven."""
    if (year % 7) % 2 == 1:
      return 331
    else:
      return 330

  def count_years_days(self):
    """Find the number of years and days since Planetfall of the 
    current datetime."""
    if self.since_planetfall().days >= 0:
      self.p_year = 0
      self.p_day = 1 + self.since_planetfall() // PoseidonDateTime.p_day_duration
      while self.p_day > self.days_in_given_year(self.p_year):
        self.p_day -= self.days_in_given_year(self.p_year)
        self.p_year += 1

  def set_hours(self):
    """Set the hours, minutes, and seconds of a datetime."""
    if self.since_planetfall().days >= 0:
      full_days = self.since_planetfall() // PoseidonDateTime.p_day_duration
      part_days = (self.since_planetfall() / PoseidonDateTime.p_day_duration) - full_days
      seconds_in_day = (part_days * PoseidonDateTime.p_day_duration).total_seconds()
      self.p_hour = math.floor(seconds_in_day) // 3600
      seconds_in_hour = seconds_in_day - (self.p_hour * 3600)
      self.p_minute = math.floor(seconds_in_hour) // 60
      seconds_in_minutes = seconds_in_hour - (self.p_minute * 60)
      self.p_second = seconds_in_minutes

  def colonyformat(self, include_time=True):
    """Represent a date or datetime as the standard Colonial format, 
    like '150.63' or '150.63 28:45:13'"""
    if include_time:
      return f"{self.p_day:03d}.{self.p_year:02d} {self.p_hour:02d}:{self.p_minute:02d}:{round(self.p_second):02d}"
    else:
      return f"{self.p_day:03d}.{self.p_year:02d}"

  @classmethod
  def fromcolonyformat(cls, colonystring):
    """Create a PoseidonDateTime object from a Colonial format string, 
    like '150.63' or '150.63 28:45:13'"""
    m = re.match(r"(?P<day>\d{1,3})\.(?P<year>\d+)( (?P<hour>\d{2}):(?P<minute>\d{2})(:(?P<second>\d{2}))?)?", colonystring)
    if not m:
      raise ValueError(f"Invalid colonyformat string: '{colonystring}'")

    p_day = int(m.group('day'))
    if p_day <= 0:
      raise ValueError(f"Invalid colonyformat string: '{colonystring}'")
    p_year = int(m.group('year'))
    if p_day > PoseidonDateTime.days_in_given_year(p_year):
      raise ValueError(f"Invalid colonyformat string: '{colonystring}'")
    p_hour = None
    p_minute = None
    p_second = None
    if m.group('hour'):
      p_hour = int(m.group('hour'))
      p_minute = int(m.group('minute'))
    if m.group('second'):
      p_second = int(m.group('second'))

    p_datetime = PoseidonDateTime.planetfall
    for y in range(p_year):
      p_datetime += PoseidonDateTime.p_day_duration * PoseidonDateTime.days_in_given_year(y)
    p_datetime += PoseidonDateTime.p_day_duration * (p_day - 1)
    if p_hour:
      p_datetime += dt.timedelta(hours=p_hour)
    if p_minute:
      p_datetime += dt.timedelta(minutes=p_minute)
    if p_second:
      p_datetime += dt.timedelta(seconds=p_second)

    return p_datetime

# Now that the class has been defined, redefine PoseidonDateTime.planetfall
# as a PoseidonDateTime object
PoseidonDateTime.planetfall = PoseidonDateTime.fromisoformat(PoseidonDateTime.planetfall.isoformat())
