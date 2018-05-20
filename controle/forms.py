from django import forms
from controle.models import Produto
from controle.models import ItemVendido

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['descricao', 'preco', 'unidades_compradas', 'categoria', 'fornecedor']

    def __init__(self, *args, **kwargs):
        super(ProdutoForm, self).__init__(*args, **kwargs)

        self.fields['descricao'].widget.attrs['class'] = 'form-control'
        self.fields['preco'].widget.attrs['class'] = 'form-control'
        self.fields['categoria'].widget.attrs['class'] = 'form-control'
        self.fields['unidades_compradas'].widget.attrs['class'] = 'form-control'
        #self.fields['unidades_no_estoque'].widget.attrs['class'] = 'form-control'
        self.fields['fornecedor'].widget.attrs['class'] = 'form-control'

class VendaForm(forms.ModelForm):
    class Meta:
        model = ItemVendido
        fields = ['produto', 'cliente', 'quantidade', 'desconto']

    def __init__(self, *args, **kwargs):
        super(VendaForm, self).__init__(*args, **kwargs)

        self.fields['produto'].widget.attrs['class'] = 'form-control'
        self.fields['cliente'].widget.attrs['class'] = 'form-control'
        # self.fields['preco_unitario'].widget.attrs['class'] = 'form-control'
        self.fields['quantidade'].widget.attrs['class'] = 'form-control'
        self.fields['desconto'].widget.attrs['class'] = 'form-control'
        # self.fields['data_venda'].widget.attrs['class'] = 'form-control'
        
    