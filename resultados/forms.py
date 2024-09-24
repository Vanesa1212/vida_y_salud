from django import forms

class loginForm(forms.Form): 

    TIPO_ID = [
        ('CC', 'Cédula de ciudadanía'),
        ('TI', 'Tarjeta de identidad'),
        ('CE', 'Cédula de extranjería'),
        ('RC', 'Registro civil'),
        ('PA', 'Pasaporte', ),
        ('AS', 'Adulto sin identificación'),
        ('MS', 'Menor sin identificación'),
        ('NU', 'Número único de identificación'),
        ('NV', 'Certificado de nacido vivo'),
        ('SC', 'Salvoconducto'),
        ('NIT', 'Nit'),
        ('CD', 'Carnet diplomático')
        ('PE', 'Permiso especial de permanencia'),
        ('RE', 'Residente especial para la paz'),
        ('PT', 'Permiso por protección temporal')
        ('DE', 'Documento extranjero'),

    ]

    tipo_id =forms.ChoiceField(
            choices = TIPO_ID,
        )
    numero_identificacion = forms.CharField(max_length=20)
    fecha_nacimiento = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2025)))

    def clean(self):
        cleaned_data = super().clean()

