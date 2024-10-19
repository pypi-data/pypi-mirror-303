![PyPI](https://img.shields.io/pypi/v/work-calendar?label=pypi%20work-calendar)
![ruff](https://github.com/Polyrom/work-calendar/actions/workflows/linter.yml/badge.svg) ![tests](https://github.com/Polyrom/work-calendar/actions/workflows/tests.yml/badge.svg)

# work calendar

A simple no-nonsense library to find out whether a day is a working day in Russia.

Data obtained from [consultant.org](https://www.consultant.ru). I try to parse it as soon as the official calendar for the following year is published, which is normally late summer or early autumn.

Data available **for years 2015-2025**.

Feel free to use the [raw json file](work_calendar/total.json).

## Installation

```bash
pip install work-calendar
```

## Basic (and only) usage

```python
from datetime import date
import work_calendar

dt = date(year=2021, month=1, day=2)
work_calendar.is_workday(dt) # False


dt_out_of_bounds = date(year=2090, month=1, day=2)
try:
    work_calendar.is_workday(dt_out_of_bounds)
except work_calendar.NoDataForYearError:
    print('woopsy!')

woopsy!
```
