from core.localization.translations.translations_pl import translations_pl
from core.localization.translations.translations_es import translations_es


class Localizations:

    __language_code: str | None = None

    @classmethod
    def language_code(cls) -> str | None:
        return cls.__language_code

    @classmethod
    def lang_initialization(cls, lang_code: str) -> None:
        if not cls.__language_code:
            cls.__language_code = lang_code

    @classmethod
    def translate(cls, msg: str) -> str:
        match cls.__language_code:
            case "en":
                return msg
            case "pl":
                return translations_pl.get(msg, msg)
            case "es":
                return translations_es.get(msg, msg)
            case _:
                return msg
