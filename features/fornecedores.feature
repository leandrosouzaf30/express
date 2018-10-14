# language: pt 

Funcionalidade: Cadastro fornecedores
    Cenario: Efetuar cadastro com sucesso
    Dado que o usuario esteja na pagina "http://localhost:4200/fornecedores"
    Quando inserir o "nome" "Shoppin Benfica"
    E inserir o "endereco" "Av. Senador Carlos Jereissati"
    E inserir o "cidade" "Maracanau"
    E inserir o "uf" "CE"
    E inserir o "telefone" "30114-2855"
    Entao clicar no botao "Adicionar"