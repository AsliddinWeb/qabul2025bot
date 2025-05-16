from telegram import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from api import get_countries_api, get_regions_api, get_districts_api, get_branches_api, get_education_levels_api, get_education_forms_api, get_programs_api

BUTTON_HOME = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📝 Ariza topshirish")],
        [
            KeyboardButton(text="🏛 Universitet haqida"),
            KeyboardButton(text="📚 Yo'nalishlar")
        ],
        [
            KeyboardButton(text="📞 Bog‘lanish"),
            KeyboardButton(text="👨‍💻 Dasturchi")
        ]
    ],
    resize_keyboard=True
)

BUTTON_BACK_TO_MAIN = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🏠 Asosiy menyu")]
    ],
    resize_keyboard=True
)

BUTTON_SEND_PHONE = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📲 Telefon raqamni yuborish", request_contact=True)],
        [KeyboardButton(text="⬅️ Orqaga"), KeyboardButton(text="🏠 Asosiy menyu")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

BUTTON_NONE = ReplyKeyboardRemove()


BUTTON_VERIFY_CODE = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔁 Kodni qayta olish")],
        [KeyboardButton(text="⬅️ Orqaga"), KeyboardButton(text="🏠 Asosiy menyu")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

BUTTON_BACK_AND_HOME = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="⬅️ Orqaga"), KeyboardButton(text="🏠 Asosiy menyu")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)


def build_country_buttons():
    countries = get_countries_api()

    keyboard = []

    if countries:
        row = []
        for i, country in enumerate(countries, 1):
            row.append(KeyboardButton(text=country["name"]))
            if i % 2 == 0:
                keyboard.append(row)
                row = []
        if row:  # Agar oxirgi tugmalar 1 dona bo‘lsa
            keyboard.append(row)

    # Pastki navigatsiya tugmalari
    keyboard.append([
        KeyboardButton(text="⬅️ Orqaga"),
        KeyboardButton(text="🏠 Asosiy menyu")
    ])

    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        one_time_keyboard=True
    )

BUTTON_DAVLATLAR = build_country_buttons()


def build_region_buttons(country_id: int):
    regions = get_regions_api(country_id)

    keyboard = []

    if regions:
        row = []
        for i, region in enumerate(regions, 1):
            row.append(KeyboardButton(text=region["name"]))
            if i % 2 == 0:
                keyboard.append(row)
                row = []
        if row:  # Agar oxirgi qator to‘liq bo‘lmagan bo‘lsa
            keyboard.append(row)

    # Navigatsiya tugmalari
    keyboard.append([
        KeyboardButton(text="⬅️ Orqaga"),
        KeyboardButton(text="🏠 Asosiy menyu")
    ])

    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        one_time_keyboard=True
    )


def build_district_buttons(region_id: int) -> ReplyKeyboardMarkup:
    districts = get_districts_api(region_id)

    keyboard = []

    if districts:
        row = []
        for i, district in enumerate(districts, 1):
            row.append(KeyboardButton(text=district["name"]))
            if i % 2 == 0:
                keyboard.append(row)
                row = []
        if row:
            keyboard.append(row)

    # Pastki navigatsiya tugmalari
    keyboard.append([
        KeyboardButton(text="⬅️ Orqaga"),
        KeyboardButton(text="🏠 Asosiy menyu")
    ])

    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        one_time_keyboard=True
    )

def build_filial_buttons():
    filiallar = get_branches_api()

    keyboard = []

    if filiallar:
        row = []
        for i, filial in enumerate(filiallar, 1):
            row.append(KeyboardButton(text=filial["name"]))
            if i % 2 == 0:
                keyboard.append(row)
                row = []
        if row:  # Agar oxirgi qator to‘liq bo‘lmasa
            keyboard.append(row)

    # Pastki navigatsiya tugmalari
    keyboard.append([
        KeyboardButton(text="⬅️ Orqaga"),
        KeyboardButton(text="🏠 Asosiy menyu")
    ])

    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        one_time_keyboard=True
    )

BUTTON_BRANCHES = build_filial_buttons()



def build_education_levels_buttons():
    education_levels = get_education_levels_api()

    keyboard = []

    if education_levels:
        row = []
        for i, level in enumerate(education_levels, 1):
            row.append(KeyboardButton(text=level["name"]))
            if i % 2 == 0:
                keyboard.append(row)
                row = []
        if row:
            keyboard.append(row)

    # Pastki navigatsiya tugmalari
    keyboard.append([
        KeyboardButton(text="⬅️ Orqaga"),
        KeyboardButton(text="🏠 Asosiy menyu")
    ])

    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        one_time_keyboard=True
    )

BUTTON_EDUCATION_LEVELS = build_education_levels_buttons()



def build_education_type_buttons():
    education_forms = get_education_forms_api()

    keyboard = []

    if education_forms:
        row = []
        for i, form in enumerate(education_forms, 1):
            row.append(KeyboardButton(text=form["name"]))
            if i % 2 == 0:
                keyboard.append(row)
                row = []
        if row:
            keyboard.append(row)

    # Pastki navigatsiya tugmalari
    keyboard.append([
        KeyboardButton(text="⬅️ Orqaga"),
        KeyboardButton(text="🏠 Asosiy menyu")
    ])

    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        one_time_keyboard=True
    )

BUTTON_EDUCATION_TYPES = build_education_type_buttons()


def build_program_buttons(branch: str, education_level: str, education_form: str):
    programs = get_programs_api(branch, education_level, education_form)

    keyboard = []

    if programs:
        row = []
        for i, program in enumerate(programs, 1):
            row.append(KeyboardButton(text=program["name"]))
            if i % 2 == 0:
                keyboard.append(row)
                row = []
        if row:
            keyboard.append(row)

    # Navigatsiya tugmalari
    keyboard.append([
        KeyboardButton(text="⬅️ Orqaga"),
        KeyboardButton(text="🏠 Asosiy menyu")
    ])

    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        one_time_keyboard=True
    )

