import re

from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from states import BotState
import buttons
import api


async def messages_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    user = update.effective_user

    state = context.user_data.get('state', BotState.START)

    if state == BotState.START:
        if text == "📝 Ariza topshirish":
            context.user_data['state'] = BotState.ARIZA_TOPSHIRISH
            ariza_text = (
                "<b>📝 Ariza topshirish!</b>\n"
                "Iltimos, telefon raqamingizni <code>+998XXYYYYYYY</code> formatida yuboring yoki quyidagi tugma orqali jo'nating."
            )
            await update.message.reply_text(
                ariza_text, 
                parse_mode=ParseMode.HTML, 
                reply_markup=buttons.BUTTON_SEND_PHONE
            )

        elif text == "🏛 Universitet haqida":
            context.user_data['state'] = BotState.UNIVERSITET_HAQIDA
            university_text = (
                "<b>🏛 Xalqaro Innovatsion Universitet</b>\n"
                "Zamonaviy ta’lim, ilg‘or metodlar va xalqaro hamkorlik markazi.\n\n"

                "<b>👨‍🎓 Talabalar soni:</b>\n"
                "🌞 Kunduzgi — 1000+ talaba\n"
                "🌙 Sirtqi — 3200+ talaba\n\n"

                "<b>🏢 Infratuzilma:</b>\n"
                "• 🖥 Axborot texnologiyalari bilan jihozlangan binolar\n"
                "• 📚 Kutubxona va raqamli markazlar\n"
                "• 🏠 Yotoqxona\n"
                "• 🍽 Oshxona\n\n"

                "<b>👨‍🏫 O‘qituvchilar:</b> 86+ ilmiy darajali mutaxassislar\n"
                "<b>🤝 Hamkorlik:</b> Korxonalar, banklar, boshqarmalar bilan shartnomalar."
            )

            
            photo_path = "./images/xiu.jpg"

            await update.message.reply_photo(
                photo=open(photo_path, "rb"),
                caption=university_text,
                parse_mode=ParseMode.HTML,
                reply_markup=buttons.BUTTON_BACK_TO_MAIN
            )

        
        elif text == "📚 Yo'nalishlar":
            context.user_data['state'] = BotState.YONALISHLAR
            yonalish_text = (
                "<b>🎓 Bakalavriat yo‘nalishlari:</b>\n"
                "• 📊 Iqtisodiyot\n"
                "• 📘 Buxgalteriya hisobi va audit\n"
                "• 💳 Moliya va moliyaviy texnologiyalar\n"
                "• 👩‍🏫 Pedagogika va psixologiya\n"
                "• 🌍 Filologiya va tillarni o‘qitish\n"
                "• 🧒 Boshlang‘ich ta’lim\n"
                "• 🧸 Maktabgacha ta’lim\n"
                "• 🧠 Psixologiya\n"
                "• 🗞 Jurnalistika\n"
                "• 📚 Kutubxona-axborot faoliyati\n"
                "• 🏺 Tarix\n"
                "• 🤸‍♂️ Jismoniy madaniyat\n"
                "• 🧩 Maxsus pedagogika\n"
                "• 🏫 Pedagogika\n"
                "• 🔢 Matematika va informatika\n"
                "• 💻 Axborot tizimlari va texnologiyalari\n"
                "• 🏗 Shahar qurilishi va infratuzilma\n\n"

                "<b>🎓 Magistratura yo‘nalishlari:</b>\n"
                "• 📊 Iqtisodiyot\n"
                "• 🗣 Lingvistika (O‘zbek tili)\n"
                "• 🇷🇺 Lingvistika (Rus tili)\n"
                "• 🇬🇧 Lingvistika (Ingliz tili)\n"
                "• 👩‍🏫 Pedagogika va psixologiya"
            )
            await update.message.reply_text(yonalish_text, parse_mode=ParseMode.HTML, reply_markup=buttons.BUTTON_BACK_TO_MAIN)

        elif text == "📞 Bog‘lanish":
            context.user_data['state'] = BotState.BOGLANISH
            boglanish_text = (
                "<b>📞 Biz bilan bog‘laning:</b>\n\n"
                "📱 <b>Telefon:</b> <code>+998(55)406-15-15</code>\n"
                "📩 <b>Telegram:</b> @xiuedu_uz"
            )
            await update.message.reply_text(boglanish_text, parse_mode=ParseMode.HTML, reply_markup=buttons.BUTTON_BACK_TO_MAIN)

        elif text == "👨‍💻 Dasturchi":
            context.user_data['state'] = BotState.DASTURCHI
            dasturchi_text = (
                "👨‍💻 <b>Bot muallifi:</b> Asliddin Abdujabborov\n\n"
                "📲 Telegram: <a href='https://t.me/Asliddin_Abdujabborov'>@Asliddin_Abdujabborov</a>"
            )
            await update.message.reply_text(dasturchi_text, parse_mode=ParseMode.HTML, reply_markup=buttons.BUTTON_BACK_TO_MAIN)

        else:
            default_text = "❗ Iltimos, menyudan tugma tanlang."
            await update.message.reply_text(default_text, parse_mode=ParseMode.HTML, reply_markup=buttons.BUTTON_HOME)

    elif state == BotState.ARIZA_TOPSHIRISH:
        PHONE_REGEX = r'^\+998\d{9}$'
        if text == "🏠 Asosiy menyu":
            context.user_data['state'] = BotState.START
            await update.message.reply_html(
                text=(
                    "🏠 <b>Asosiy menyuga xush kelibsiz!</b>\n"
                    "<i>Iltimos, quyidagi tugmalardan birini tanlang:</i>"
                ),
                reply_markup=buttons.BUTTON_HOME
            )

        elif text == "⬅️ Orqaga":
            context.user_data['state'] = BotState.START
            await update.message.reply_html(
                text=(
                    "🔙 <b>Siz asosiy menyuga qaytdingiz.</b>\n"
                    "<i>Iltimos, quyidagi tugmalardan birini tanlang:</i>"
                ),
                reply_markup=buttons.BUTTON_HOME
            )

            
        else:
            if re.match(PHONE_REGEX, text):
                # Save Data
                context.user_data['user_phone'] = text

                # ⏳ Vaqtinchalik kutish xabari
                deleted_message = await update.message.reply_text(
                    "⏳ <i>Iltimos, kuting...</i>",
                    reply_markup=buttons.BUTTON_NONE,
                    parse_mode=ParseMode.HTML
                )

                # 📲 API so‘rov: telefon raqam va Telegram ID yuboriladi
                response = api.auth_api(
                    phone=text,
                    telegram_id=user.id
                )

                # 🧹 Vaqtinchalik xabarni o‘chirish
                await deleted_message.delete()

                # ✅ Javobga qarab foydalanuvchiga xabar berish
                if response:
                    await update.message.reply_html(
                        text="✅ <b>Telefon raqam qabul qilindi!</b>\n"
                        "🔐 <i>Endi sizga yuborilgan</i> <b>4 xonali kodni</b> kiriting:",
                        reply_markup=buttons.BUTTON_VERIFY_CODE
                    )

                    # Change State
                    context.user_data['state'] = BotState.ARIZA_KOD
                else:
                    await update.message.reply_text(
                        "❌ <b>Kod yuborishda xatolik yuz berdi!</b>\n\n"
                        "🔁 <i>Iltimos, telefon raqamni qayta yuboring yoki keyinroq urinib ko‘ring.</i>",
                        reply_markup=buttons.BUTTON_SEND_PHONE,
                        parse_mode=ParseMode.HTML
                    )

                await update.message.reply_html(
                    text=f"{response}"
                )
            else:
                await update.message.reply_text(
                    "❌ Noto‘g‘ri formatdagi telefon raqam.\n"
                    "Iltimos, telefon raqamni +998901234567 formatda kiriting."
                )
    
    elif state == BotState.ARIZA_KOD:
        code = text.strip()

        if text == "🔁 Kodni qayta olish":
            phone = context.user_data.get('user_phone')
            # ⏳ Vaqtinchalik kutish xabari
            deleted_message = await update.message.reply_text(
                "⏳ <i>Iltimos, kuting...</i>",
                reply_markup=buttons.BUTTON_NONE,
                parse_mode=ParseMode.HTML
                )

            response = api.auth_api(
                phone=phone,
                telegram_id=user.id
            )

            # 🧹 Vaqtinchalik xabarni o‘chirish
            await deleted_message.delete()

            # ✅ Javobga qarab foydalanuvchiga xabar berish
            if response:
                await update.message.reply_html(
                    "✅ <b>Kod qayta yuborildi!</b>\n"
                    "🔐 <i>Endi sizga yuborilgan</i> <b>4 xonali kodni</b> kiriting:",
                    reply_markup=buttons.BUTTON_VERIFY_CODE
                )
            else:
                await update.message.reply_text(
                    "❌ <b>Kod yuborishda xatolik yuz berdi!</b>\n\n",
                    reply_markup=buttons.BUTTON_VERIFY_CODE,
                    parse_mode=ParseMode.HTML
                )


            # Change state
            context.user_data['state'] = BotState.ARIZA_KOD

            return
        elif text == "⬅️ Orqaga":
            context.user_data['state'] = BotState.ARIZA_TOPSHIRISH

            ariza_text = (
                "<b>📝 Ariza topshirish!</b>\n"
                "Iltimos, telefon raqamingizni <code>+998XXYYYYYYY</code> formatida yuboring yoki quyidagi tugma orqali jo'nating."
            )
            await update.message.reply_text(
                ariza_text, 
                parse_mode=ParseMode.HTML, 
                reply_markup=buttons.BUTTON_SEND_PHONE
            )

            return
        elif text == "🏠 Asosiy menyu":
            # Change State
            context.user_data['state'] = BotState.START

            first_name = update.effective_user.first_name
            greeting_text = (
                f"👋 Salom, <b>{first_name}</b>!\n\n"
                "🎓 Bu — <b>Xalqaro Innovatsion Universitet</b>ning rasmiy <b>qabul bot</b>i.\n"
                "📝 Ariza topshirish va ma’lumot olish uchun menyudan foydalaning ⬇️"
            )
            await update.message.reply_text(text=greeting_text, reply_markup=buttons.BUTTON_HOME, parse_mode="HTML")
            
            return
        

        # 4 xonali raqammi yoki yo'qmi tekshiramiz
        if not code.isdigit():
            await update.message.reply_html(
                "❌ <b>Kod faqat raqamlardan iborat bo‘lishi kerak!</b>\n"
                "🔁 Iltimos, <b>4 xonali kodni</b> qayta kiriting:"
            )
            return

        if len(code) != 4:
            await update.message.reply_html(
                "⚠️ <b>Kod uzunligi noto‘g‘ri!</b>\n"
                "🔢 Iltimos, <b>aniq 4 xonali kod</b> kiriting:"
            )
            return

        phone = context.user_data.get("user_phone")
        if not phone:
            await update.message.reply_html(
                "⚠️ <b>Telefon raqam topilmadi!</b>\n"
                "❗️Iltimos, jarayonni boshidan boshlang."
            )
            context.user_data['state'] = BotState.START
            return

        # API orqali kodni tekshirish
        response = api.verify_code_api(phone=phone, code=code)

        if not response:
            await update.message.reply_html(
                "🚫 <b>Kod noto‘g‘ri yoki muddatidan o‘tib ketgan!</b>\n"
                "❗️Iltimos, <b>to‘g‘ri 4 xonali kodni</b> yana kiriting:"
            )
            return

        # Save Data
        context.user_data['access_token'] = response['access']
        context.user_data['refresh_token'] = response['refresh']
        
        # Change State
        context.user_data['state'] = BotState.ARIZA_PASSPORT_SERIYA

        await update.message.reply_html(
            "✅ <b>Kod muvaffaqiyatli tasdiqlandi!</b>\n\n"
            "📄 Endi iltimos, <b>pasport seriya va raqamingizni</b> kiriting (masalan: AA1234567):",
            reply_markup=buttons.BUTTON_BACK_TO_MAIN
        )

    elif state == BotState.ARIZA_PASSPORT_SERIYA:
        passport = text.strip().upper()

        if text == "🏠 Asosiy menyu":
            # Change State
            context.user_data['state'] = BotState.START

            first_name = update.effective_user.first_name
            greeting_text = (
                f"👋 Salom, <b>{first_name}</b>!\n\n"
                "🎓 Bu — <b>Xalqaro Innovatsion Universitet</b>ning rasmiy <b>qabul bot</b>i.\n"
                "📝 Ariza topshirish va ma’lumot olish uchun menyudan foydalaning ⬇️"
            )
            await update.message.reply_text(text=greeting_text, reply_markup=buttons.BUTTON_HOME, parse_mode="HTML")
            
            return

        if not re.match(r"^[A-Z]{2}\d{7}$", passport):
            await update.message.reply_html(
                "❌ <b>Pasport seriya va raqam formati noto‘g‘ri!</b>\n"
                "✅ To‘g‘ri format: <code>AA1234567</code>\n"
                "🔁 Iltimos, qayta urinib ko‘ring:"
            )
            return

        # Save Data
        context.user_data['passport'] = passport

        # Change State
        context.user_data['state'] = BotState.ARIZA_TUGILGAN_SANA

        await update.message.reply_html(
            "📅 <b>Tug‘ilgan sanangizni kiriting:</b>\n"
            "🗓 Format: <code>YYYY-MM-DD</code> (masalan: 2002-03-15)",
            reply_markup=buttons.BUTTON_BACK_AND_HOME
        )

    elif state == BotState.ARIZA_TUGILGAN_SANA:
        birth_date = text.strip()

        if text == "🏠 Asosiy menyu":
            # Change State
            context.user_data['state'] = BotState.START

            first_name = update.effective_user.first_name
            greeting_text = (
                f"👋 Salom, <b>{first_name}</b>!\n\n"
                "🎓 Bu — <b>Xalqaro Innovatsion Universitet</b>ning rasmiy <b>qabul bot</b>i.\n"
                "📝 Ariza topshirish va ma’lumot olish uchun menyudan foydalaning ⬇️"
            )
            await update.message.reply_text(text=greeting_text, reply_markup=buttons.BUTTON_HOME, parse_mode="HTML")
            
            return
        
        elif text == "⬅️ Orqaga":
            context.user_data['state'] = BotState.ARIZA_PASSPORT_SERIYA

            await update.message.reply_html(
                "📄 Iltimos, <b>pasport seriya va raqamingizni</b> kiriting (masalan: AA1234567):",
                reply_markup=buttons.BUTTON_BACK_TO_MAIN
            )

            return

        # Sana formatini tekshir
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", birth_date):
            await update.message.reply_html(
                "❌ <b>Sana formati noto‘g‘ri!</b>\n"
                "🗓 To‘g‘ri format: <code>YYYY-MM-DD</code>\n"
                "🔁 Masalan: <code>2002-03-15</code>\n"
                "Iltimos, qaytadan kiriting:"
            )
            return

        # ⏳ Vaqtinchalik xabar
        waiting_message = await update.message.reply_html(
            "⏳ <i>Ma’lumotlar tekshirilmoqda, iltimos kuting...</i>"
        )

        # Saqlash
        context.user_data['user_birth_date'] = birth_date

        # Pasport seriya va raqamni ajratib olish
        passport = context.user_data.get('passport', '')
        passport_series = passport[:2]
        passport_number = passport[2:]

        # Tokenni olish
        token = context.user_data.get('access_token')

        # API orqali tekshiruv
        passport_info = api.get_passport_info_api(
            series=passport_series,
            number=passport_number,
            birth_date=birth_date,
            token=token
        )

        # Vaqtinchalik xabarni o‘chirish
        await waiting_message.delete()

        if passport_info:
            # Save Data
            context.user_data['passport_info'] = passport_info

            # Change State
            context.user_data['state'] = BotState.ARIZA_DAVLAT

            # Reply Message
            info_text = (
                f"🪪 <b>Pasport maʼlumotlari:</b>\n"
                f"👤 <b>F.I.Sh:</b> {passport_info['full_name']}\n"
                f"🎂 <b>Tugʻilgan sana:</b> {passport_info['birth_date']}\n"
                f"🆔 <b>Pasport seriyasi:</b> {passport_info['passport_series']}\n"
                f"🧾 <b>JSHSHIR:</b> {passport_info['passport_number']}\n"
                f"🏢 <b>Berilgan sana:</b> {passport_info['given_by']}\n"
                f"📍 <b>Yashash manzili:</b> {passport_info['address']}\n"
            )

            await update.message.reply_html(info_text)

            # Save data
            context.user_data['countries'] = api.get_countries_api()

            # Reply Message
            await update.message.reply_html(
                "🌍 <b>Davlatingizni tanlang:</b>",
                reply_markup=buttons.BUTTON_DAVLATLAR
            )
        else:
            # State qaytariladi
            context.user_data['state'] = BotState.ARIZA_PASSPORT_SERIYA

            # Reply Message
            await update.message.reply_html(
                "❌ <b>Pasport yoki tug‘ilgan sana ma’lumotlari noto‘g‘ri!</b>\n"
                "📄 Iltimos, pasport seriya va raqamingizni qaytadan kiriting.\n"
                "Format: <code>AA1234567</code>"
            )

    elif state == BotState.ARIZA_DAVLAT:
        countries = context.user_data.get("countries", [])

        if text == "🏠 Asosiy menyu":
            # Change State
            context.user_data['state'] = BotState.START

            first_name = update.effective_user.first_name
            greeting_text = (
                f"👋 Salom, <b>{first_name}</b>!\n\n"
                "🎓 Bu — <b>Xalqaro Innovatsion Universitet</b>ning rasmiy <b>qabul bot</b>i.\n"
                "📝 Ariza topshirish va ma’lumot olish uchun menyudan foydalaning ⬇️"
            )
            await update.message.reply_text(text=greeting_text, reply_markup=buttons.BUTTON_HOME, parse_mode="HTML")
            
            return
        
        elif text == "⬅️ Orqaga":
            context.user_data['state'] = BotState.ARIZA_TUGILGAN_SANA

            await update.message.reply_html(
                "📅 <b>Tug‘ilgan sanangizni kiriting:</b>\n"
                "🗓 Format: <code>YYYY-MM-DD</code> (masalan: 2002-03-15)",
                reply_markup=buttons.BUTTON_BACK_AND_HOME
            )

            return

        selected_country = next((c for c in countries if c['name'] == text), None)

        if selected_country:
            # Save Data
            context.user_data["user_country_id"] = selected_country['id']
            context.user_data["user_country_name"] = selected_country['name']

            # Change State
            context.user_data["state"] = BotState.ARIZA_VILOYAT

            # Reply Message
            await update.message.reply_html(
                "🏙 <b>Viloyatingizni tanlang:</b>",
                reply_markup=buttons.build_region_buttons(selected_country['id'])
            )
        else:
            await update.message.reply_text("🚫 Davlat noto‘g‘ri tanlandi. Iltimos, tugmalar orqali tanlang.")


    elif state == BotState.ARIZA_VILOYAT:
        regions = api.get_regions_api(context.user_data.get('user_country_id'))

        if text == "🏠 Asosiy menyu":
            # Change State
            context.user_data['state'] = BotState.START

            first_name = update.effective_user.first_name
            greeting_text = (
                f"👋 Salom, <b>{first_name}</b>!\n\n"
                "🎓 Bu — <b>Xalqaro Innovatsion Universitet</b>ning rasmiy <b>qabul bot</b>i.\n"
                "📝 Ariza topshirish va ma’lumot olish uchun menyudan foydalaning ⬇️"
            )
            await update.message.reply_text(text=greeting_text, reply_markup=buttons.BUTTON_HOME, parse_mode="HTML")
            
            return
        
        elif text == "⬅️ Orqaga":
            context.user_data['state'] = BotState.ARIZA_DAVLAT

            # Reply Message
            await update.message.reply_html(
                "🌍 <b>Davlatingizni tanlang:</b>",
                reply_markup=buttons.BUTTON_DAVLATLAR
            )

            return
        
        selected_region = next((r for r in regions if r['name'] == text), None)

        if selected_region:
            # Save Data
            context.user_data["user_region_id"] = selected_region['id']
            context.user_data["user_region_name"] = selected_region['name']

            # Change State
            context.user_data["state"] = BotState.ARIZA_TUMAN

            # Reply Message
            await update.message.reply_html(
                "📍 <b>Tumaningizni tanlang:</b>",
                reply_markup=buttons.build_district_buttons(selected_region['id'])
            )
        else:
            await update.message.reply_text("🚫 Viloyat noto‘g‘ri tanlandi. Iltimos, tugmalar orqali tanlang.")


    elif state == BotState.ARIZA_TUMAN:
        districts = api.get_districts_api(context.user_data.get("user_region_id"))

        selected_district = next((d for d in districts if d['name'] == text), None)

        if selected_district:
            # Save Data
            context.user_data["user_district_id"] = selected_district["id"]
            context.user_data["user_district_name"] = selected_district["name"]

            # Create Applicant
            passport_info = context.user_data.get("passport_info", {})

            print(passport_info)

            create_applicant = api.create_applicant_profile_api(
                token=context.user_data.get('access_token'),
                payload = {
                    "last_name": passport_info.get("last_name"),
                    "first_name": passport_info.get("first_name"),
                    "other_name": passport_info.get("second_name"),
                    "birth_date": context.user_data.get('user_birth_date'),
                    "passport_series": passport_info.get("passport_series"),
                    "pinfl": passport_info.get("passport_number"),
                    "country": context.user_data.get("user_country_id"),
                    "region": context.user_data.get("user_region_id"),
                    "district": context.user_data.get("user_district_id"),
                    "address": passport_info.get("address"),
                    "gender": "",
                    "nationality": ""
                }
            )

            if create_applicant:
                # Applicant Created
                context.user_data["applicant_profile"] = create_applicant

                # Change State
                context.user_data["state"] = BotState.ARIZA_FILIAL

                # Reply Message
                await update.message.reply_html(
                    "🏫 <b>Filialni tanlang:</b>",
                    reply_markup=buttons.BUTTON_BRANCHES
                )
            else:
                # Error
                await update.message.reply_text(
                    "❌ Ariza yaratishda xatolik yuz berdi. Iltimos, qaytadan urinib ko‘ring.",
                    reply_markup=buttons.BUTTON_HOME
                )
                context.user_data["state"] = BotState.START
        else:
            await update.message.reply_text(
                "🚫 Tuman noto‘g‘ri tanlandi. Iltimos, tugmalar orqali tanlang."
            )

    elif state == BotState.ARIZA_FILIAL:
        branches = api.get_branches_api()

        if not branches:
            await update.message.reply_text(
                "🚫 Filial ro'yxati hozircha mavjud emas. Keyinroq urinib ko'ring.",
                reply_markup=buttons.BUTTON_HOME
            )
            context.user_data["state"] = BotState.START
            return

        selected_branch = next((b for b in branches if b['name'] == text), None)

        if selected_branch:
            # Saqlash
            context.user_data["user_branch_id"] = selected_branch['id']
            context.user_data["user_branch_name"] = selected_branch['name']

            # Keyingi state
            context.user_data["state"] = BotState.ARIZA_TALIM_DARAJASI

            # Javob xabari
            await update.message.reply_html(
                "🎓 <b>Ta‘lim darajasini tanlang:</b>",
                reply_markup=buttons.BUTTON_EDUCATION_LEVELS
            )
        else:
            await update.message.reply_text(
                "🚫 Filial noto‘g‘ri tanlandi. Iltimos, tugmalar orqali tanlang.",
                reply_markup=buttons.build_branch_buttons()
            )

    elif state == BotState.ARIZA_TALIM_DARAJASI:
        education_levels = api.get_education_levels_api()

        if not education_levels:
            await update.message.reply_text(
                "❌ Ta'lim darajalari ro'yxatini olishda xatolik yuz berdi. Iltimos, keyinroq urinib ko‘ring.",
                reply_markup=buttons.BUTTON_BACK_TO_MAIN
            )
            context.user_data["state"] = BotState.START
            return

        selected_level = next((el for el in education_levels if el['name'] == text), None)

        if selected_level:
            # Saqlash
            context.user_data["education_level_id"] = selected_level["id"]
            context.user_data["education_level_name"] = selected_level["name"]

            # Keyingi holatga o'tish
            context.user_data["state"] = BotState.ARIZA_TALIM_SHAKLI

            # Javob
            await update.message.reply_html(
                f"🎓 Tanlangan ta'lim darajasi: <b>{selected_level['name']}</b>\n\n"
                f"🏫 <b>Ta'lim turini tanlang:</b>",
                reply_markup=buttons.BUTTON_EDUCATION_TYPES
            )
        else:
            await update.message.reply_text(
                "🚫 Noto‘g‘ri tanlov. Iltimos, pastdagi tugmalar orqali tanlang.",
                reply_markup=buttons.BUTTON_EDUCATION_LEVELS
            )

    
    elif state == BotState.ARIZA_TALIM_SHAKLI:
        education_forms = api.get_education_forms_api()

        if not education_forms:
            await update.message.reply_text(
                "❌ Ta'lim shakllari ro'yxatini olishda xatolik yuz berdi. Iltimos, keyinroq urinib ko‘ring.",
                reply_markup=buttons.BUTTON_BACK_TO_MAIN
            )
            context.user_data["state"] = BotState.START
            return

        selected_form = next((form for form in education_forms if form['name'] == text), None)

        if selected_form:
            # Saqlash
            context.user_data["education_form_id"] = selected_form["id"]
            context.user_data["education_form_name"] = selected_form["name"]

            # Keyingi holatga o'tish
            context.user_data["state"] = BotState.ARIZA_YONALISH

            # Javob
            await update.message.reply_html(
                f"📘 Tanlangan ta'lim shakli: <b>{selected_form['name']}</b>\n\n"
                f"📚 <b>Yo‘nalishni tanlang:</b>",
                reply_markup=buttons.build_program_buttons(
                    branch=context.user_data.get("branch_id"),
                    education_level=context.user_data.get("education_level_id"),
                    education_form=selected_form["id"]
                )
            )
        else:
            await update.message.reply_text(
                "🚫 Noto‘g‘ri tanlov. Iltimos, pastdagi tugmalar orqali tanlang.",
                reply_markup=buttons.BUTTON_EDUCATION_TYPES
            )


    elif state == BotState.ARIZA_YONALISH:
        filial_id = context.user_data.get("user_branch_id")
        education_level_id = context.user_data.get("education_level_id")
        education_form_id = context.user_data.get("education_form_id")

        directions = api.get_programs_api(filial_id, education_level_id, education_form_id)
        selected_direction = next((d for d in directions if d['name'] == text), None)

        if selected_direction:
            # Save direction info
            context.user_data["user_direction_id"] = selected_direction["id"]
            context.user_data["user_direction_name"] = selected_direction["name"]

            # Prepare payload
            payload = {
                "admission_type": "regular",
                "branch": filial_id,
                "education_level": education_level_id,
                "education_form": education_form_id,
                "program": selected_direction["id"],
            }

            # Submit Application
            application_response = api.submit_application_api(
                token=context.user_data.get("access_token"),
                payload=payload
            )

            if application_response:
                await update.message.reply_html(
                    "✅ <b>Arizangiz muvaffaqiyatli yuborildi!</b>\n\n"
                    "Biz siz bilan tez orada bog‘lanamiz.",
                    reply_markup=buttons.BUTTON_HOME
                )
                context.user_data["state"] = BotState.START
            else:
                await update.message.reply_html(
                    "❌ <b>Ariza yuborishda xatolik yuz berdi.</b>\n"
                    "Iltimos, qaytadan urinib ko‘ring.",
                    reply_markup=buttons.BUTTON_HOME
                )
                context.user_data["state"] = BotState.START

        else:
            await update.message.reply_text("🚫 Yo‘nalish noto‘g‘ri tanlandi. Iltimos, tugmalar orqali tanlang.")



    elif state == BotState.UNIVERSITET_HAQIDA:
        if text == "🏠 Asosiy menyu":
            context.user_data['state'] = BotState.START
            welcome_back_text = "Asosiy menyuga xush kelibsiz! Quyidagilardan birini tanlang:"
            await update.message.reply_text(welcome_back_text, reply_markup=buttons.BUTTON_HOME)


    elif state == BotState.YONALISHLAR:
        if text == "🏠 Asosiy menyu":
            context.user_data['state'] = BotState.START
            welcome_back_text = "Asosiy menyuga xush kelibsiz! Quyidagilardan birini tanlang:"
            await update.message.reply_text(welcome_back_text, reply_markup=buttons.BUTTON_HOME)

    elif state == BotState.BOGLANISH:
        if text == "🏠 Asosiy menyu":
            context.user_data['state'] = BotState.START
            welcome_back_text = "Asosiy menyuga xush kelibsiz! Quyidagilardan birini tanlang:"
            await update.message.reply_text(welcome_back_text, reply_markup=buttons.BUTTON_HOME)

    elif state == BotState.DASTURCHI:
        if text == "🏠 Asosiy menyu":
            context.user_data['state'] = BotState.START
            welcome_back_text = "Asosiy menyuga xush kelibsiz! Quyidagilardan birini tanlang:"
            await update.message.reply_text(welcome_back_text, reply_markup=buttons.BUTTON_HOME)



async def contact_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    
    state = context.user_data.get('state', BotState.START)

    if state == BotState.ARIZA_TOPSHIRISH:
        phone = f"+{update.message.contact.phone_number}"
        
        # Save Data
        context.user_data['user_phone'] = phone

        # ⏳ Vaqtinchalik kutish xabari
        deleted_message = await update.message.reply_text(
            "⏳ <i>Iltimos, kuting...</i>",
            reply_markup=buttons.BUTTON_NONE,
            parse_mode=ParseMode.HTML
        )

        # 📲 API so‘rov: telefon raqam va Telegram ID yuboriladi
        response = api.auth_api(
            phone=phone,
            telegram_id=user.id
        )

        # 🧹 Vaqtinchalik xabarni o‘chirish
        await deleted_message.delete()

        # ✅ Javobga qarab foydalanuvchiga xabar berish
        if response:
            await update.message.reply_html(
                text="✅ <b>Telefon raqam qabul qilindi!</b>\n"
                "🔐 <i>Endi sizga yuborilgan</i> <b>4 xonali kodni</b> kiriting:",
                reply_markup=buttons.BUTTON_VERIFY_CODE
            )

            # Change State
            context.user_data['state'] = BotState.ARIZA_KOD
        else:
            await update.message.reply_text(
                "❌ <b>Kod yuborishda xatolik yuz berdi!</b>\n\n"
                "🔁 <i>Iltimos, telefon raqamni qayta yuboring yoki keyinroq urinib ko‘ring.</i>",
                reply_markup=buttons.BUTTON_SEND_PHONE,
                parse_mode=ParseMode.HTML
            )


        # Change state
        context.user_data['state'] = BotState.ARIZA_KOD
    
