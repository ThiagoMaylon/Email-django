from django import forms
from django.core.mail.message import EmailMessage

class Emailform(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_email(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMenssagem: {mensagem}'

        mail = EmailMessage(
            subject='Email enviado pelo sistema email_django',
            body=conteudo,
            from_email='contato@seudominio.com',
            to=['contato@seudominio.com', ],
            headers={'Reply_to':email}
        )
        mail.send()