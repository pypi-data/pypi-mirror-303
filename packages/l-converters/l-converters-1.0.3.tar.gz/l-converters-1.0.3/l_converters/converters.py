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

    @staticmethod
    def text_to_file(md_text: str, html_file: str):
        """
        - html file from md text \n
        - md_text must be str and in 3 double " \n
        - html_file is name of html file \n
        :return: True if file created
        """
        import markdown
        md = markdown.markdown(md_text)
        with open(html_file, 'w') as html_file:
            html_file.write(md)
        return True
