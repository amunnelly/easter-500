# https://www.dr-mikes-math-games-for-kids.com/easter-date-tables.html?century=26

import pandas as pd

holder = []
df = pd.read_csv('dates.csv')
for a, b in df.iterrows():
    temp = b['date'].split(" ")
    day= temp[1][:-2]
    day = "{:02}".format(int(day))
    month = "03" if temp[0].strip() == "March" else "04"
    standard_date = "-".join([temp[2].strip(), month, day])
    nice_date = "".join([temp[0].strip()," ", day, ", ", temp[2].strip()])
    holder.append([temp[2], standard_date, nice_date])

df2 = pd.DataFrame(holder, columns=['Year', 'Date', 'Easter Sunday'])
df2.sort_values('Year', inplace=True)
# df2['Easter Sunday'] = df2['Date'].apply(lambda x: x.strftime('%B %d, %Y') if x else None)
print(df2.head())
print(df2.info())
df2.to_csv('right_dates.csv', index=False)