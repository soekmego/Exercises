import calendar

def main():
    hc = calendar.HTMLCalendar(calendar.SUNDAY)
    sc = hc.formatmonth(2017, 1)
    print(sc)


if __name__ == "__main__":
    main()
