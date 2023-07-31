from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
def set_keyboard(list_urls):
    results=InlineKeyboardMarkup(row_width=2)
    i=1
    for res in list_urls:
        results.insert(InlineKeyboardButton(text=f"{i}",callback=res))
        i+=1
    return results
def download_video(results,url):
    keyboard_dwn=InlineKeyboardMarkup(row_width=1)
    for res in results:
        keyboard_dwn.insert(InlineKeyboardButton(text=res[0],url=res[1]))
    keyboard_dwn.insert(InlineKeyboardButton(text="Qo'lda yuklash",url=url))
    return keyboard_dwn


start_menu=InlineKeyboardMarkup()
start_menu.insert(InlineKeyboardButton(text="Kino qidirish",switch_inline_query_current_chat=""))

def enter_web(url):
    web_menu=InlineKeyboardMarkup()
    web_menu.insert(InlineKeyboardButton(text="Web saytda ko'rish",url=url))
    return web_menu