from src.model.renderer import render_html

class ParserBase(object):
    WEB_URL = None
    DATA_URL = None

    def __init__(self, render=None):
        self.render_data = None
        self.render_method = render

        if self.render_method=="html":
            self.render_data = render_html(self.DATA_URL)

    def parse(self, source):
        pass

    def get_data_html(self):
        if (self.render_method == "html") and (self.render_data):
            soup = self.render_data
        else:
            soup = render_html(self.DATA_URL)

        return self.parse(soup)
