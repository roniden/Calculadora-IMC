from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFillRoundFlatButton, MDRaisedButton
from kivymd.uix.gridlayout import MDGridLayout

class IMCCalculator(MDBoxLayout):
    pass

class CalculadoraApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        layout = IMCCalculator(orientation='vertical', padding=20, spacing=30)

        self.title = "Calculadora IMC"

        reset_button = MDRaisedButton(
            text="Resetar",
            size_hint=(None, None),
            size=("200dp", "50dp"),
            pos_hint={"center_x": 0.5},
            on_release=self.resetar,
            md_bg_color=(0.2, 0.2, 0.2, 1)
        )
        layout.add_widget(reset_button)

        title_label = MDLabel(
            text="Calculadora de IMC",
            halign="center",
            font_style="H3",
            font_name="fonts/LexendDeca-Regular.ttf"
        )
        layout.add_widget(title_label)

        self.peso_input = MDTextField(
            hint_text="Digite seu peso (kg)",
            hint_text_color=(0, 0, 0, 1),
            helper_text="Ex: 70",
            helper_text_mode="on_focus",
            mode="rectangle",
            line_color_focus=(0, 0, 0, 1),
        )
        layout.add_widget(self.peso_input)

        self.altura_input = MDTextField(
            hint_text="Digite sua altura (m)",
            helper_text="Ex: 1.75",
            helper_text_mode="on_focus",
            mode="rectangle",
            line_color_focus=(0, 0, 0, 1),
        )
        layout.add_widget(self.altura_input)

        button_layout = MDBoxLayout(
            orientation='horizontal',
            padding=[400, 0],
            pos_hint={"center_x": 0.5},
            spacing=10
        )
        
        button_layout.add_widget(MDFillRoundFlatButton( 
            text="Calcular",
            on_release=self.calcular_imc,
            font_size="20sp",
            md_bg_color=(0, 0, 0, 1),
            width='200dp'
        ))

        button_layout.add_widget(MDRaisedButton(
            text="Tema",
            on_release=self.toggle_theme,
            pos_hint={"center_x": 0.5},
            size=(200, 50),
            md_bg_color=(0.2, 0.2, 0.2, 1)
        ))

        layout.add_widget(button_layout)

        self.result_label = MDLabel(
            text="",
            halign="center"
        )
        layout.add_widget(self.result_label)
 
        self.classificacao_label = MDLabel(
            text="",
            halign="center",
            font_style="Subtitle1"
        )
        layout.add_widget(self.classificacao_label)

        tabela_imc = MDGridLayout(cols=2, size_hint_y=None, height='100dp')
        tabela_imc.add_widget(MDLabel(text="Abaixo do peso", halign="center"))
        tabela_imc.add_widget(MDLabel(text="< 18.5", halign="center"))
        tabela_imc.add_widget(MDLabel(text="Peso saudável", halign="center"))
        tabela_imc.add_widget(MDLabel(text="18.5 - 24.9", halign="center"))
        tabela_imc.add_widget(MDLabel(text="Sobrepeso", halign="center"))
        tabela_imc.add_widget(MDLabel(text="25 - 29.9", halign="center"))
        tabela_imc.add_widget(MDLabel(text="Obesidade", halign="center"))
        tabela_imc.add_widget(MDLabel(text="≥ 30", halign="center"))

        layout.add_widget(tabela_imc)

        self.set_default_font(layout)

        return layout
    
    def set_default_font(self, widget):
        for child in widget.children:
            if hasattr(child, 'font_name'):
                child.font_name = "fonts/LexendDeca-Regular.ttf"
            if isinstance(child, MDBoxLayout):
                self.set_default_font(child)

    def calcular_imc(self, instance):
        try:
            peso = float(self.peso_input.text)
            altura = float(self.altura_input.text)
            imc = peso / (altura ** 2)
            self.result_label.text = f"Seu IMC é: {imc:.2f}"
            self.classificacao_label.text = self.classificar_imc(imc)
        except ValueError:
            self.result_label.text = "Por favor, insira valores válidos."

    def classificar_imc(self, imc):
        if imc < 18.5:
            return "Você está abaixo do peso"
        elif 18.5 <= imc < 24.9:
            return "Seu peso é ideal"
        elif 25 <= imc < 29.9:
            return "Você está Sobrepeso"
        else:
            return "Você está Obeso"

    def resetar(self, instance):
        self.peso_input.text = ""
        self.altura_input.text = ""
        self.result_label.text = ""
        self.classificacao_label.text = ""

    def toggle_theme(self, instance):
        self.theme_cls.theme_style = "Dark" if self.theme_cls.theme_style == "Light" else "Light"

if __name__ == '__main__':
    CalculadoraApp(icon="img/icon.png").run()