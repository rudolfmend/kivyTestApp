from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField

class CurrencyConverterApp(MDApp):
    title = "Zmenáreň"
    def build(self):
        layout = MDBoxLayout(orientation="vertical", padding="48dp", spacing="12dp")

        self.input_field = MDTextField(hint_text="Amount in EUR", helper_text="Enter the amount in EUR",
                                       helper_text_mode="on_focus")
        layout.add_widget(self.input_field)

        self.output_field = MDTextField(hint_text="Amount in CZK", readonly=True)
        layout.add_widget(self.output_field)

        convert_button = MDRaisedButton(
            text="Zmeniť", on_release=self.convert_currency)
        layout.add_widget(convert_button)

        return layout

    def convert_currency(self, instance):
        try:
            amount_eur = float(self.input_field.text)
            amount_czk = amount_eur * 25.5  # Conversion rate: 1 EUR = 25.5 CZK
            self.output_field.text = str(amount_czk)
        except ValueError:
            self.output_field.text = "Invalid input"

CurrencyConverterApp().run()
 