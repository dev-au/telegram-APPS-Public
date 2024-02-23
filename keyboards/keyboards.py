class KeyboardSetter:
    from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

    async def search_result_keyboard(self, search_result, search_term=None):
        tracks_list = search_result[0][0]
        is_next_url = search_result[0][1]
        if is_next_url and search_term == None:
            return "No name! Please give me search term!"
        now_page = search_result[1]
        main_keyboard = self.InlineKeyboardMarkup(row_width=5)

        line = 1
        for track in tracks_list:
            name = f"{track[0][1]}+{track[0][0]}"
            music_id = track[1]
            main_keyboard.insert(self.InlineKeyboardButton(text=str(line), callback_data=f"{line}^{music_id}"))
            line += 1
        if len(tracks_list) == 10 and is_next_url or now_page != 0:
            next = self.InlineKeyboardButton(text="➡", callback_data=f"{now_page + 1}~{search_term}")
            back = self.InlineKeyboardButton(text="⬅", callback_data=f"{now_page - 1}~{search_term}")
            if now_page == 0:
                main_keyboard.insert(next)
            elif is_next_url and now_page != 0:
                main_keyboard.insert(back)
                main_keyboard.insert(next)
            elif now_page != 0 and not is_next_url:
                main_keyboard.insert(back)
        return main_keyboard
