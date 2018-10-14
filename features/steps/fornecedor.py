from behave import when, given, then
from selenium import webdriver

gc = webdriver.Chrome(executable_path=r'../../chrome/chromedriver')

dic = {
        'nome'    : 'nome',
        'endereco': 'endereco',
        'cidade'  : 'cidade',
        'uf'      : 'uf',
        'telefone': 'telefone',
        'Adicionar': 'adicionar'
        }

@given('que o usuario esteja na pagina "{page}"')
def acess_page(context, page):
    gc.get(page)

@when('inserir o "{field}" "{value}"')
def insert_values_on_fields(context, field, value):
    gc.find_element_by_id(dic[field]).send_keys(value)
    
@then('clicar no botao "{btn}"')
def click_btn(context, btn):
    gc.find_element_by_id(dic[btn]).click()  
