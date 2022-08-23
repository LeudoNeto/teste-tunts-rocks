import requests
import xlsxwriter


response = requests.get("https://restcountries.com/v3.1/all")

workbook = xlsxwriter.Workbook('countries_list.xlsx')

title_style = workbook.add_format({'bold': True, 'align': 'center', 'font_color' : '#4F4F4F'})

worksheet = workbook.add_worksheet()

worksheet.merge_range('A1:D1', 'Merged Range')

worksheet.write('A1:A4', 'Countries List', title_style) 
workbook.close()


# for country in response.json():

#     name = country['name']['common']

#     try:
#         capital = country['capital'][0]
#     except KeyError:
#         capital = '-'

#     try:
#         area = country['area']
#     except KeyError:
#         area = '-'

#     try:
#         currencies = ','.join(list(country['currencies'].keys()))
#     except KeyError:
#         currencies = '-'

#     print(f"{name:<50} {capital:<20} {area:<10} {currencies}")