from data_for_change.active_finance import (
    RRODUCTION_LINK,
    SOCIAL_LINK,
    LEASING_LINK, CREDIT_LINK, TOURISM_LINK, YOUNG_LINK, FOLK_LINK, FAIR_LINK,
    CERTIFICATE_LINK
)

ACTIVE: dict[int, str] = {
    1: '<b>Приобретение оборудования для развития производства</b>\n\n'
        '<b><i>Кто может получить:</i></b>\n'
        'субъект МСП - производитель товаров, зарегистрированный и '
        'осуществляющий деятельность в Ленинградской области\n'
        '<b><i>Размер субсидии:</i></b>\n'
        'до 5 млн руб., но не более 50% затрат\n'
        '<b><i>На что можно потратить:</i></b>\n'
        'Оборудование - устройства, механизмы, станки, приборы, аппараты, '
        'агрегаты, установки, машины; транспортные средства (за исключением '
        'легковых автомобилей и воздушных судов)\n'
        '<b><i>Дополнительные условия:</i></b>\n'
        'Оборудование должно быть приобретено не ранее двух лет назад и '
        'полностью оплачено',
    2: '<b>Субсидия для социальных предпринимателей</b>\n\n'
        '<b><i>Кто может получить:</i></b>\n'
        'субъект МСП, признанные социальными предприятиями\n'
        '<b><i>Размер субсидии:</i></b>\n'
        'до 1 млн руб., но не более 75% затрат\n'
        '<b><i>На что можно потратить:</i></b>\n'
        'аренда, ремонт, покупка оборудования, участие в конкурсах и '
        'чемпионатах, приобретение технических средств, механизмов, '
        'оборудования, устройств, санитарной техники, '
        'изготовление мебели и инвентаря, компьютерное оборудование и т.д.',
    3: '<b>Компенсация затрат, связанных с лизингом</b>\n\n'
        '<b><i>Кто может получить:</i></b>\n'
        'субъект МСП, осуществляющий деятельность в Ленинградской области\n'
        '<b><i>Размер субсидии:</i></b>\n'
        'до 1.5 млн руб., но не более 95% затрат\n'
        '<b><i>На что можно потратить:</i></b>\n'
        'возмещение затрат, связанных с уплатой лизинговых платежей, '
        'кроме первого взноса\n'
        '<b><i>Дополнительные условия:</i></b>\n'
        'Предмет лизинга должен относиться ко второй и выше амортизационным '
        'группам Классификации основных средств;\n'
        'Предмет лизинга не может быть физически изношенным или морально '
        'устаревшим',
    4: '<b>Компенсация процентной ставки по кредитам для бизнеса</b>\n\n'
        '<b><i>Кто может получить:</i></b>\n'
        'субъект МСП, осуществляющий деятельность в Ленинградской области\n'
        '<b><i>Размер субсидии:</i></b>\n'
        'до 2.5 млн руб., но не более 75% затрат\n'
        '<b><i>На что можно потратить:</i></b>\n'
        'возмещение затрат, связанных с уплатой процентов по действующим на '
        'дату подачи заявки на получение субсидии, кредитам, '
        'полученным в российских кредитных организациях в целях приобретения '
        'и(или) модернизации основных средств и(или) пополнения оборотных '
        'средств, произведенных не ранее года, предшествующего году подачи '
        'заявки',
    #5: '<b>Субсидия для развитие туризма</b>\n\n'
    #   '<b><i>Кто может получить:</i></b>\n'
    #   'субъект МСП, осуществляющий деятельность в Ленинградской области;\n'
    #   'cоискатель должен иметь действующий договор страхования на средство '
    #   'размещения, являющееся объектом недвижимости;\n'
    #   'Соискатель должен иметь документы, свидетельствующие о наличии права '
    #   'собственности на средства размещения, являющиеся объектом '
    #   'недвижимости;\n'
    #   'Соискатель должен иметь документ, свидетельствующий о наличии '
    #   'зарегистрированных прав на земельный участок, в границах которого '
    #   'расположены объекты туристской индустрии\n'
    #   '<b><i>Размер субсидии:</i></b>\n'
    #   'до 1.5 млн руб., но не более 80% затрат\n'
    #   '<b><i>На что можно потратить:</i></b>\n'
    #   'возмещение затрат, связанных с приобретением оборудования, '
    #   'мебели, техники, благоустройством территории, создание кемпинга, '
    #   'продвижением сайта, оборудованием беседок, скамеек и т.д.',
    5: '<b>Грант для предпринимателей до 25 лет включительно</b>\n\n'
       '<b><i>Кто может получить:</i></b>\n'
       'субъект МСП, организованный предпринимателем до 25 лет включительно\n'
       '<b><i>Размер субсидии:</i></b>\n'
       'до 500 тыс. руб., необходимо софинансирование  - 25%\n'
       '<b><i>На что можно потратить:</i></b>\n'
       'аренда, ремонт помещения, оборудование, услуги связи, ПО, '
       'расходные материалы и др.',
    6: '<b>Субсидия для народных художественных промыслов</b>\n\n'
       '<b><i>Кто может получить:</i></b>\n'
       'субъект МСП, осуществляющий деятельность в Ленинградской области;\n'
       'деятельность соискателя (ОКВЭД) отнесена к ремесленной деятлеьности\n'
       '<b><i>Размер субсидии:</i></b>\n'
       'до 700 тыс. руб., но не более 90% затрат\n'
       '<b><i>На что можно потратить:</i></b>\n'
       'расходные материалы, инструменты, торговое оборудование, '
       'расходы на экспорт готовой продукции и др.',
    7: '<b>Субсидия для участия в выставках и ярмарках</b>\n\n'
       '<b><i>Кто может получить:</i></b>\n'
       'субъект МСП, осуществляющий деятельность в Ленинградской области;\n'
       '<b><i>Размер субсидии:</i></b>\n'
       'не более 90% затрат\n'
       '<b><i>На что можно потратить:</i></b>\n'
       'компенсация затрат, связанных с уплатой регистрационных сборов, '
       'арендой выставочных площадей (в том числе с учетом особенностей '
       'расположения стендов) и выставочного оборудования, работами по '
       'изготовлению, монтажу и демонтажу стендов, арендой дополнительного '
       'оборудования (в том числе фризовые надписи), подключением к '
       'источникам электропитания, арендой костюмов и аксессуаров для участия '
       'в чемпионатах, конкурсах, транспортными расходами по доставке '
       'выставочных экспонатов, командировочными расходами в части '
       'транспортных расходов, расходов по проживанию представителей '
       'соискателей, расходами на оплату услуг переводчика, расходами на '
       'производство презентационных материалов, буклетов',
    8: '<b>Субсидия для получения сертификатов</b>\n\n'
       '<b><i>Кто может получить:</i></b>\n'
       'субъект МСП, осуществляющий деятельность в Ленинградской области;\n'
       '<b><i>Размер субсидии:</i></b>\n'
       'не более 90% затрат\n'
       '<b><i>На что можно потратить:</i></b>\n'
       'компенсация затрат, связанных с обязательным или добровольным '
       'подтверждением соответствия продукции, с получением международных '
       'сертификатов (присвоение знака "CE"), получением (продлением) '
       'сертификатов соответствия.',
}

ACTIVE_LINKS: dict[int, str] = {
    1: RRODUCTION_LINK,
    2: SOCIAL_LINK,
    3: LEASING_LINK,
    4: CREDIT_LINK,
    #5: TOURISM_LINK,
    5: YOUNG_LINK,
    6: FOLK_LINK,
    7: FAIR_LINK,
    8: CERTIFICATE_LINK,
}