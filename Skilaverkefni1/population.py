currentpop = 307357870

seconds_year = 3600*24*365

births_year = seconds_year / 7
deaths_year = seconds_year / 13
immigr_year = seconds_year / 35

years_str = input("Years: ")
years_int = int(years_str)

if years_int < 0:
    print("Invalid input!")
else:
    futurepop = currentpop + years_int*(births_year + immigr_year - deaths_year )
    print("New population after", years_int, "years is", int(futurepop))