duration = int(input('Введите количество секунд: '))

if duration < 60:
    print((duration), ' сек')
elif duration < 60*60:
    print((duration // 60), ' мин', (duration % 60), ' сек')
elif duration < 24 * 60 * 60:
    print((duration // 3600), ' час', (duration % 3600 // 60), ' мин',(duration % 60), ' сек')


# days = duration // 86400
# hours = (duration - days * 86400) // 3600
# minutes = (duration - (days * 86400 + hours * 3600)) // 60
# seconds = duration - (days * 86400 + hours * 3600 + minutes * 60)
#
#
#
# print('duratin = ', duration, '\n', days, 'дн', hours, 'час', minutes, 'мин', seconds, 'сек')