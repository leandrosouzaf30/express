from django import forms
from controle.models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['descricao', 'preco', 'unidades_no_estoque', 'unidades_pedidas', 'categoria', 'fornecedor']

    def __init__(self, *args, **kwargs):
        super(ProdutoForm, self).__init__(*args, **kwargs)

        self.fields['descricao'].widget.attrs['class'] = 'form-control'
        self.fields['preco'].widget.attrs['class'] = 'form-control'
        self.fields['categoria'].widget.attrs['class'] = 'form-control'
        self.fields['unidades_pedidas'].widget.attrs['class'] = 'form-control'
        self.fields['unidades_no_estoque'].widget.attrs['class'] = 'form-control'
        self.fields['fornecedor'].widget.attrs['class'] = 'form-control'
    