from data_for_change.start_finance import START_LINK, TERM_START, CSZN_LINK

START: dict[int, str] = {
    1: '<b>Стартовая субсидия</b>\n\n'
        '<b><i>Кто может получить:</i></b>\n'
        'субъект МСП, зарегистрированный менее 2х лет назад и '
        'осуществляющий деятельность в Гатчинском районе\n'
        '<b><i>Размер субсидии: до 700 тыс. руб.</i></b>\n'
        '<b><i>Размер софинансирования: 20% от общей стоимости проекта</i></b>\n'
        '<b><i>На что можно потратить:</i></b>\n'
        'оборудование, техника, мебель, коммунальные платежи, ПО,  '
        'основные средства, сырье и расходные материалы\n'
        f'<b><i>Срок подачи документов:</i></b> {TERM_START}',
    2: '<b>Социальный контракт</b>\n\n'
        '<b><i>Кто может получить:</i></b>\n'
        'официальный доход за 3 последних месяца '
        'составляет менее прожиточного минимума на '
        'одного члена семьи\n'
        '<b><i>Размер поддержки: до 350 тыс. руб.</i></b>\n'
        '<b><i>На что можно потратить:</i></b>\n'
        'оборудование, мебель, реклама, образование',
    3: '<b>Субсидия Центра занятости населения</b>\n\n'
        '<b><i>Кто может получить:</i></b>\n'
        'безработный, который состоит на учете '
        'в Центре занятости населения\n'
        '<b><i>Размер поддержки: до 100 тыс. руб.</i></b>\n'
        '<b><i>На что можно потратить:</i></b>\n'
        'оборудование, мебель, техника',
}

START_LINKS: dict[int, str] = {
    1: START_LINK,
    2: CSZN_LINK,
    3: CSZN_LINK,
}
