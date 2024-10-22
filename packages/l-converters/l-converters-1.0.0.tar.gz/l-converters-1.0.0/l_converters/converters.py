class FromMDtoHTML:
    def __init__(self):
        pass

    @staticmethod
    def text_to_text(md_text: str):
        """
        md_text must be str and in 3 double "
        :return: html text from md text
        """
        import markdown
        md = markdown.markdown(md_text)
        return md
