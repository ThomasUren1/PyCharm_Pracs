__Author__ = 'Thomas Uren'

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class Converter(App):
    def build(self):
        Window.size = (500,200)
        self.title = 'Convert Miles to Kilometers'
        self.root = Builder.load_file('task.kv')
        return self.root

    def convert_m_to_km(self):
        try:
            self.root.ids.km_label.text = str(int(self.root.ids.m_input.text)*1.60934)
        except ValueError:
            self.root.ids.km_label.text = '0.00'

    def handle_increment(self, increment_change):
        try:
            increment_value = int(self.root.ids.m_input.text)
            increment_value += increment_change
            self.root.ids.m_input.text = str(increment_value)
        except ValueError:
            self.root.ids.m_input.text = str(increment_change)

Converter().run()
