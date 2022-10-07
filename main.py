from crawler import ScrapperModule

obj = ScrapperModule()

date = obj.get_date_range()

print(date[0])
print(date[-1])

