import datetime as dt

class Record:
    def __init__(self, amount, date=None, comment=None):
        date_format= '%d.%m.%Y'
        now = dt.datetime.now()
        self.amount = amount
        self.date = date
        if self.date is None:
            self.date = now.date()
        else:
            self.date = dt.datetime.strptime(self.date, date_format).date()
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
        stats_day = 0
        for record in self.records:
            now = dt.datetime.now()
            if record.date == now.date():
                stats_day += record.amount
        return stats_day
 
    #how much already taken/eaten for week

    def get_week_stats(self):
        stats_week = 0
        week = dt.datetime.now() - dt.timedelta(days=7)
        for record in self.records:
            now = dt.datetime.now()
            if week.date() < record.date <= now.date():
                stats_week += record.amount
        return stats_week

    def today_remained(self): 
        to_have = self.limit - self.get_today_stats()
        return to_have


class CashCalculator(Calculator):
        USD_RATE = 72.93
        EURO_RATE = 88.58
        
        def get_today_cash_remained(self, currency):

            rates_dict = {"rub" : (1, 'руб'), "usd" : (self.USD_RATE, 'USD'), "eur" : (self.EURO_RATE, 'Euro')}
            if self.today_remained() == 0:
                return 'Денег нет, держись'
            elif self.today_remained() > 0:
                cash_remained = round(self.today_remained()/rates_dict[currency][0], 2)
                return f'На сегодня осталось {cash_remained} {rates_dict[currency][1]}'
            else:
                cash_remained = -round(self.today_remained()/rates_dict[currency][0], 2)
                return f'Денег нет, держись: твой долг - {cash_remained} {rates_dict[currency][1]}'


class CaloriesCalculator(Calculator):

        def get_calories_remained(self):

            if self.today_remained() > 0:
                return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {self.today_remained()} кКал' 
            return 'Хватит есть!'
            