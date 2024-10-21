# About the class

This class implements date conversion for the fictitous sci-fi world of **Poseidon** from the tabletop role-playing game [Blue Planet](https://www.biohazardgamespublishing.com/blueplanet) published by [Biohazard Games](https://www.biohazardgamespublishing.com/).

See the Blue Planet wiki for more about the [Colonial calendar](https://bp-rpg.org/Colonial_calendar).

# Usage

This is a sample session of using the `PoseidonDateTime` class.

New objects are created with the `fromcolonyformat` or `fromisoformat` methods.

Pretty formatting of dates is with the `colonyformat` or `isoformat` methods.

The attributes `p_year`, `p_day`, `p_hour`, `p_minute`, and `p_second` give the components of the Colonial datetime. Similarly, the attributes `year`. `day`, `hour`, `minute`, and `second` give the components of the CE datetime.

You can use `timedelta` objects for changes in time; `PoseidonDateTime.p_day_duration` is one Poseidon day and `PoseidonDateTime.p_year_duration` is one Poseidon year.

```
>>> import poseidon_datetime as pdt
>>> import datetime as dt
>>> p_atlantis = pdt.PoseidonDateTime.fromisoformat('2124-08-07')
>>> p_atlantis.colonyformat()
'076.33 18:51:43'
>>> p_atlantis.colonyformat(include_time=True)
'076.33 18:51:43'
>>> p_atlantis.colonyformat(include_time=False)
'076.33'
>>> p_birthday = pdt.PoseidonDateTime.fromcolonyformat('023.99 28:15:00')
>>> p_birthday
PoseidonDateTime(2199, 1, 30, 23, 14, 22)
>>> p_birthday.isoformat()
'2199-01-30T23:14:22'
>>> p_birthday.p_day
23
>>> p_birthday.day
30
>>> p_after_birthday = p_birthday + dt.timedelta(days=1)
>>> p_after_birthday.isoformat()
'2199-01-31T23:14:22'
>>> p_after_birthday.colonyformat()
'024.99 22:14:17'
>>> p_after_birthday = p_birthday + pdt.PoseidonDateTime.p_day_duration
>>> p_after_birthday.colonyformat()
'024.99 28:15:00'
>>> p_after_birthday.isoformat()
'2199-02-01T05:15:05'
```