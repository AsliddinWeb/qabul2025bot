import requests

from config import BASE_URL

def auth_api(phone: str, telegram_id: str) -> dict | None:
    """
    Telefon raqamni yuborib, foydalanuvchini ro‘yxatdan o‘tkazish yoki avtorizatsiya qilish.
    :param phone: +998 bilan boshlanuvchi telefon raqam
    :return: API javobi yoki None
    """
    url = f"{BASE_URL}/auth/"
    payload = {"phone": phone, "telegram_id": telegram_id}

    try:
        response = requests.post(url, json=payload)
        if response.status_code in [200, 201]:
            return response.json()
        else:
            print(f"[ERROR] Auth API status: {response.status_code} | Body: {response.text}")
            return None
    except Exception as e:
        print("[EXCEPTION] Auth API Error:", e)
        return None


def verify_code_api(phone: str, code: str) -> dict | None:
    """
    Tasdiqlash kodini yuborib, foydalanuvchini avtorizatsiya qiladi (JWT token oladi).
    :param phone: +998 bilan telefon raqam
    :param code: 4 xonali tasdiqlash kodi
    :return: JWT tokenlar yoki None
    """
    url = f"{BASE_URL}/auth/verify/"
    payload = {
        "phone": phone,
        "code": code
    }

    try:
        response = requests.post(url, json=payload)
        if response.status_code in [200, 201]:
            return response.json()
        else:
            print(f"[ERROR] Verify API status: {response.status_code} | Body: {response.text}")
            return None
    except Exception as e:
        print("[EXCEPTION] Verify API Error:", e)
        return None


def get_branches_api() -> list[dict] | None:
    """
    API orqali filiallar (branches) ro‘yxatini olish
    :return: list of branches yoki None
    """
    url = f"{BASE_URL}/programs/branches/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"[ERROR] Branch API: {response.status_code} | {response.text}")
            return None
    except Exception as e:
        print("[EXCEPTION] Branch API Error:", e)
        return None


def get_education_levels_api() -> list[dict] | None:
    """
    Ta'lim darajalari (bakalavr, magistr) ro'yxatini olish
    :return: [{"id": 1, "name": "Bakalavriat"}, ...] ko'rinishida yoki None
    """
    url = f"{BASE_URL}/programs/education-levels/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"[ERROR] Education levels API: {response.status_code} | {response.text}")
            return None
    except Exception as e:
        print("[EXCEPTION] Education levels API error:", e)
        return None
    

def get_education_forms_api() -> list[dict] | None:
    """
    Ta'lim shakllari (kunduzgi, sirtqi va h.k.) ro'yxatini olib keladi
    """
    url = f"{BASE_URL}/programs/education-forms/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"[ERROR] Education forms API: {response.status_code} | {response.text}")
            return None
    except Exception as e:
        print("[EXCEPTION] Education forms API error:", e)
        return None
    

def get_programs_api(branch: str, education_level: str, education_form: str) -> list[dict] | None:
    """
    Filtrlangan yo‘nalishlar ro‘yxatini olib keladi
    """
    url = f"{BASE_URL}/programs/programs/"
    params = {
        "branch": branch,
        "education_level": education_level,
        "education_form": education_form
    }

    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"[ERROR] Programs API: {response.status_code} | {response.text}")
            return None
    except Exception as e:
        print("[EXCEPTION] Programs API error:", e)
        return None
    

def submit_application_api(token: str, payload: dict) -> dict | None:
    """
    Ariza yuborish (applications/)
    """
    url = f"{BASE_URL}/applications/"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code in [200, 201]:
            return response.json()
        else:
            print(f"[ERROR] Submit Application: {response.status_code} | {response.text}")
            return None
    except Exception as e:
        print("[EXCEPTION] Application submission error:", e)
        return None


def refresh_token_api(refresh_token: str):
    import requests
    url = f"{BASE_URL}/auth/token/refresh/"
    response = requests.post(url, data={"refresh": refresh_token})
    if response.status_code == 200:
        return response.json()
    return None


def get_passport_info_api(series: str, number: str, birth_date: str, token: str) -> dict | None:
    """
    Pasport seriya, raqam va tug‘ilgan sana orqali shaxsiy ma’lumotlarni olish.
    """
    url = f"{BASE_URL}/auth/get-passport-info/"

    params = {
        "series": series,
        "number": number,
        "birth_date": birth_date
    }
    headers = {
        "Authorization": f"Bearer {token}"
    }

    try:
        response = requests.get(url, params=params, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"[ERROR] Passport Info API: {response.status_code} | {response.text}")
            return None
    except Exception as e:
        print("[EXCEPTION] Passport Info API error:", e)
        return None


def create_applicant_profile_api(token: str, payload: dict) -> dict | None:
    """
    Applicant profili yaratish (auth/profile/create/)
    """
    url = f"{BASE_URL}/auth/profile/create/"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code in [200, 201]:
            return response.json()
        else:
            print(f"[ERROR] Profile Create: {response.status_code} | {response.text}")
            return None
    except Exception as e:
        print("[EXCEPTION] Profile Create API error:", e)
        return None

def get_countries_api() -> list[dict] | None:
    """
    Davlatlar ro'yxatini olish.
    :return: [{"id": 1, "name": "O'zbekiston"}, ...] ko'rinishida yoki None
    """
    url = f"{BASE_URL}/regions/countries/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"[ERROR] Countries API: {response.status_code} | {response.text}")
            return None
    except Exception as e:
        print("[EXCEPTION] Countries API error:", e)
        return None


def get_regions_api(country_id: int) -> list[dict] | None:
    """
    Tanlangan davlatga tegishli viloyatlar ro'yxatini olish.
    :param country_id: Davlat IDsi (masalan, 2)
    :return: [{"id": 1, "name": "Toshkent"}, ...] ko'rinishida yoki None
    """
    url = f"{BASE_URL}/regions/regions/?country={country_id}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"[ERROR] Regions API: {response.status_code} | {response.text}")
            return None
    except Exception as e:
        print("[EXCEPTION] Regions API error:", e)
        return None


def get_districts_api(region_id: int) -> list[dict] | None:
    """
    Tanlangan viloyatga tegishli tumanlar ro'yxatini olish.
    :param region_id: Viloyat IDsi (masalan, 3)
    :return: [{"id": 5, "name": "Olmazor"}, ...] ko‘rinishida yoki None
    """
    url = f"{BASE_URL}/regions/districts/?region={region_id}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"[ERROR] Districts API: {response.status_code} | {response.text}")
            return None
    except Exception as e:
        print("[EXCEPTION] Districts API error:", e)
        return None
