import requests
import xlsxwriter

response = requests.get("https://restcountries.com/v3.1/all")

workbook = xlsxwriter.Workbook('countries_list.xlsx')

titulo_style = workbook.add_format({'bold': True, 'align': 'center', 'font_color' : '#4F4F4F', 'font_size' : 16})
cabecalho_style = workbook.add_format({'bold': True, 'font_color' : '#808080', 'font_size' : 12})

worksheet = workbook.add_worksheet()

worksheet.merge_range('A1:D1', 'Merged Range')

worksheet.write('A1', 'Countries List', titulo_style)
worksheet.write('A2', 'Name', cabecalho_style)
worksheet.write('B2', 'Capital', cabecalho_style)
worksheet.write('C2', 'Area', cabecalho_style)
worksheet.write('D2', 'Currencies', cabecalho_style)

for pos,country in enumerate(response.json()):
    name = country['name']['common']

    try:
        capital = country['capital'][0]
    except KeyError:
        capital = '-'

    try:
        area = country['area']
    except KeyError:
        area = '-'

    try:
        currencies = ','.join(list(country['currencies'].keys()))
    except KeyError:
        currencies = '-'

    worksheet.write(f'A{pos+3}', name)
    worksheet.write(f'B{pos+3}', capital)
    worksheet.write(f'C{pos+3}', area)
    worksheet.write(f'D{pos+3}', currencies)

workbook.close()