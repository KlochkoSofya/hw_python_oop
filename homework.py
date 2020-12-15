import datetime as dt

class Record:
    def __init__(self, amount, date=None, comment=None):
        date_format= '%d.%m.%Y'
        now = dt.datetime.now()
        self.amount = amount
        self.date = date
        if self.date is None:
            self.date=now.date()
        else:
            self.date= dt.datetime.strptime(self.date, date_format).date()
        self.comment = comment
    

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []
    #new record:
    def add_record(self, record):
        self.records.append(record)
    #how much already taken/eaten for day
    def get_today_stats(self):
        stats_day=0
        for record in self.records:
            now=dt.datetime.now()
            print(record.date, ' = ', now.date(), ' = ', record.amount)
            if record.date == now.date():
                stats_day +=record.amount
        return stats_day
 #how much already taken/eaten for week
    def get_week_stats(self):
        stats_week = 0
        week = dt.datetime.now() - dt.timedelta(days=7)
        for record in self.records:
            now=dt.datetime.now()
            print(record.date, ' = ', week.date(), ' = ', record.amount)
            if record.date >= week.date() and record.date<=now.date():
                stats_week +=record.amount
        return stats_week


class CashCalculator(Calculator):
    USD_RATE = 72.93
    EURO_RATE = 88.58
    def get_today_cash_remained(self, currency):
        if currency == 'rub':
            rate = 1
            currency_cash = 'руб'
        elif currency == 'usd':
            rate = CashCalculator.USD_RATE
            currency_cash = 'USD'
        else:
            rate = CashCalculator.EURO_RATE
            currency_cash = 'Euro'
        if self.limit > self.get_today_stats():
            cash_remained = round(self.limit/rate-self.get_today_stats()/rate, 2)
            return f'На сегодня осталось {cash_remained} {currency_cash}'
        elif self.limit == self.get_today_stats():
            return f'Денег нет, держись'
        else:
            cash_remained = round(self.get_today_stats()/rate-self.limit/rate, 2)
            return f'Денег нет, держись: твой долг - {cash_remained} {currency_cash}'


class CaloriesCalculator(Calculator):
        def get_calories_remained(self):
            if self.limit > self.get_today_stats():
                you_can_eat = self.limit-self.get_today_stats()
                return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {you_can_eat} кКал' 
            else:
                return f'Хватит есть!'
            

