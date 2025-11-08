class StringUtils:
    @staticmethod
    def capitalize_text(text: str) -> str:
        if not text:
            return ""
        return text[0].upper() + text[1:]

    @staticmethod
    def add_period(text: str) -> str:
        if not text:
            return "."
        if not text.endswith('.'):
            return text + '.'
        return text

    @staticmethod
    def replace_spaces(text: str, char: str = "_") -> str:
        if not text:
            return ""
        return text.replace(" ", char)