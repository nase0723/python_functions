import calendar

class Date_operation:
    def get_first_date(dt):
        return dt.replace(day=1)
    def get_last_date(dt):
        return dt.replace(day=calendar.monthrange(dt.year, dt.month)[1])