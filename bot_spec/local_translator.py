class LanguageTranslator:
    from typing import List
    from loguru import logger
    all_text: dict
    all_languages: list

    def __init__(self, languages: List[str], all_text: dict):
        for lang in languages:
            if lang not in ["uz", "ru", "en", "any1", "any2", "any3", "any4", "any5", "any6", "any7"]:
                self.logger.info(f"LangError: Does not support language - '{lang}'")
                return
        self.all_languages = languages
        self.all_text = all_text

    def uz(self, text_key):
        if "uz" in self.all_languages:
            txt_ind = self.all_languages.index("uz")
            return self.all_text[text_key][txt_ind]
        else:
            self.logger.info(f"LangError: Does not give language - 'uz'")

    def ru(self, text_key):
        if "ru" in self.all_languages:
            txt_ind = self.all_languages.index("ru")
            return self.all_text[text_key][txt_ind]
        else:
            self.logger.info(f"LangError: Does not give language - 'ru'")

    def en(self, text_key):
        if "en" in self.all_languages:
            txt_ind = self.all_languages.index("en")
            return self.all_text[text_key][txt_ind]
        else:
            self.logger.info(f"LangError: Does not give language - 'en'")

    def any1(self, text_key):
        if "en" in self.all_languages:
            txt_ind = self.all_languages.index("any1")
            return self.all_text[text_key][txt_ind]
        else:
            self.logger.info(f"LangError: Does not give language - 'any1'")

    def any2(self, text_key):
        if "en" in self.all_languages:
            txt_ind = self.all_languages.index("any2")
            return self.all_text[text_key][txt_ind]
        else:
            self.logger.info(f"LangError: Does not give language - 'any2'")

    def any3(self, text_key):
        if "en" in self.all_languages:
            txt_ind = self.all_languages.index("any3")
            return self.all_text[text_key][txt_ind]
        else:
            self.logger.info(f"LangError: Does not give language - 'any3'")

    def any4(self, text_key):
        if "en" in self.all_languages:
            txt_ind = self.all_languages.index("any4")
            return self.all_text[text_key][txt_ind]
        else:
            self.logger.info(f"LangError: Does not give language - 'any4'")

    def any5(self, text_key):
        if "en" in self.all_languages:
            txt_ind = self.all_languages.index("any5")
            return self.all_text[text_key][txt_ind]
        else:
            self.logger.info(f"LangError: Does not give language - 'any5'")

    def any6(self, text_key):
        if "en" in self.all_languages:
            txt_ind = self.all_languages.index("any6")
            return self.all_text[text_key][txt_ind]
        else:
            self.logger.info(f"LangError: Does not give language - 'any6'")

    def any7(self, text_key):
        if "en" in self.all_languages:
            txt_ind = self.all_languages.index("any7")
            return self.all_text[text_key][txt_ind]
        else:
            self.logger.info(f"LangError: Does not give language - 'any7'")
