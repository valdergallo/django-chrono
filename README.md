# django-chrono
Manager datetime registers to avoid duplicate date and time in database

# Usage

```
In [1]: from chrono.models import ChronoDateTime
In [2]: d = ChronoDateTime.get('2014-01-31 14:12', mask='%Y-%m-%d %H:%M')
In [3]: d
Out[3]: 2014-01-31 14:12:00
```
