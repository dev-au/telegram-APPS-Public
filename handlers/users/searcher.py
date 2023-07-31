from asyncio import sleep
from aiogram import types
from keyboards.inline.main_keyboards import *
from utils.movie_searcher import *
from loader import dp

@dp.inline_handler()
async def bot_search(query: types.InlineQuery):
    text=query.query
    i=1
    queries = []
    if len(text)==0:
        mains=main_movies()
        for names in mains[0]:
            img=mains[1][mains[0].index(names)]
            url=mains[2][mains[0].index(names)]
            queries.append(types.InlineQueryResultArticle(
                id=str(i),
                title=names,
                input_message_content=types.InputTextMessageContent(
                    message_text=f"{names}^{url}",
                ),
                thumb_url=img,
            ))
            i+=1
        await query.answer(queries)
    else:
        response = search(query.query)
        for res in response[0]:
            if len(response[0]) == 0:
                break
            url=f"http://www.taronatv.com{res['href']}"
            photo_url=f"http://www.taronatv.com{response[1][i-1]['href']}"
            txt=f"{i}.{res.get_text()}"

            queries.append(types.InlineQueryResultArticle(
                id=str(i),
                title=txt,
                input_message_content=types.InputTextMessageContent(
                    message_text=f"{txt}^{url}",
                ),
                thumb_url=photo_url,
                ))
            i+=1
        if len(response[0])!=0:
            await query.answer(queries)



@dp.message_handler()
async def search_movie(message:types.Message):
    via=message.via_bot
    if via!=None:
        await message.delete()
        text=list(message.text.split("^"))
        if len(text)!=2:
            await message.answer("Agar botdan foydalanishni bilmayotgan bo'lsangiz /help ni bosing.")
            await message.delete()
        url=text[1]
        response=result_search(url)
        msg = await dp.bot.send_message(chat_id=message.from_user.id,text="⏳ Iltimos biroz kuting...")
        await sleep(2)
        if len(response[1])>0:
            txt = "⏳Diqqat havola yuborilmoqda"
            await msg.edit_text("⏳Kino yuklash manzili topildi...")
            await sleep(2)
            await msg.edit_text("⏳Tayyorlanmoqda...")
            await sleep(2)
            await msg.edit_text(txt)
            i=0
            k=6
            j=1
            while k!=0:
                i += j
                dot_nik = "." * i
                await msg.edit_text(f"{txt}{dot_nik}")
                await sleep(0.1)
                if i==6:
                    j=-1
                    k-=1
                elif i==1:
                    j=1
                    k-=1
            photo=get_photo(url)
            await msg.delete()
            try:
                await dp.bot.send_photo(chat_id=message.from_user.id,photo=photo,
                                        caption=f"<b>{text[0]}</b>\n\n{response[0]}\n\n"
                                                f"Telegramning o'zidan yuklab olmoqchi bo'lsangiz qo'llanma uchun /t_help ni bosing.\n\n"
                                                f"!!! Agar yuklash bilan bog'liq muammo bo'lsa qo'lda yuklab olishingiz mumkin.",
                                        reply_markup=download_video(response[1],url))
            except:
                await dp.bot.send_photo(chat_id=message.from_user.id,
                                        photo=photo,
                                        caption=f"<b>{text[0]}</b>\n"
                                                f"Bu yerda qismlar kop ekan yaxshisi saytda ko'ra qoling!",
                                          reply_markup=enter_web(url))
        else:
            await msg.edit_text("Ushbu film saytga hali toliq yuklanmagan! Noqulaylik uchun uzr!")
    else:
        await message.answer("Pastdagi tugmani bosib kino qidirishingiz mumkin.",reply_markup=start_menu)
        await message.answer("Agar botdan foydalanishni bilmayotgan bo'lsangiz /help ni bosing.")