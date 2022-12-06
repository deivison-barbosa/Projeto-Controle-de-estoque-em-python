from PyQt5 import uic, QtWidgets
import mysql.connector #importa a coneção com banco
from fpdf import Template


#connect o banco dados
conexao = mysql.connector.connect(

    host = "localhost",
    user ="root",
    password = "",
    database = "cadastro_produtos"

)
numero_id = 0 #variavel global

def imprimir():
    elements = [
        { 'name': 'company_name', 'type': 'T', 'x1': 17.0, 'y1': 32.5, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
        { 'name': 'box', 'type': 'B', 'x1': 15.0, 'y1': 15.0, 'x2': 185.0, 'y2': 260.0, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': None, 'priority': 0, },
        { 'name': 'box_x', 'type': 'B', 'x1': 95.0, 'y1': 15.0, 'x2': 105.0, 'y2': 25.0, 'font': 'Arial', 'size': 0.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': None, 'priority': 2, },
        { 'name': 'line1', 'type': 'L', 'x1': 100.0, 'y1': 25.0, 'x2': 100.0, 'y2': 57.0, 'font': 'Arial', 'size': 0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': None, 'priority': 3, },
        { 'name': 'barcode', 'type': 'BC', 'x1': 20.0, 'y1': 246.5, 'x2': 140.0, 'y2': 254.0, 'font': 'Interleaved 2of5 NT', 'size': 0.75, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '200000000001000159053338016581200810081', 'priority': 3, },
    ]

    #here we instantiate the template and define the HEADER
    f = Template(format="A4", elements=elements,
                title="Sample Invoice")
    f.add_page()

    #we FILL some of the fields of the template with the information we want
    #note we access the elements treating the template instance as a "dict"
    f["company_name"] = "Sample Company"

    #and now we render the page
    f.render("./template.pdf")

    
def deletar():
    remover = lista.tableWidget.currentRow()
    lista.tableWidget.removeRow(remover)

    cursor = conexao.cursor()
    cursor.execute("SELECT id FROM produtos")
    leitura_banco = cursor.fetchall()
    valor_id = leitura_banco[remover][0]
    cursor.execute("DELETE FROM produtos WHERE id="+str(valor_id))#seleciona so o valor especifico do id e deleta

    conexao.commit()


def editarL():
    global numero_id
    dados = lista.tableWidget.currentRow()#informa qual a linha ativa/linha selecionada
    cursor = conexao.cursor()
    cursor.execute("SELECT id FROM produtos")
    leitura_banco = cursor.fetchall()
    valor_id = leitura_banco [dados][0]
    cursor.execute("SELECT * FROM produtos WHERE id="+str(valor_id))#seleciona so o valor especifico do id
    leitura_banco = cursor.fetchall()
    
    editar.show()#execulta a tela
    numero_id = valor_id #estou dando o valor da variavel valor_id  para numero_id

    editar.txtAlterarId.setText(str(leitura_banco[0][0]))
    editar.txtAlterarProduto.setText(str(leitura_banco[0][1]))
    editar.txtAlterarPreco.setText(str(leitura_banco[0][2]))
    editar.txtAlterarEstoque.setText(str(leitura_banco[0][3]))

def salvar_dados():
    global numero_id

    id = editar.txtAlterarId.text()
    produto = editar.txtAlterarProduto.text()
    preco = editar.txtAlterarPreco.text()
    estoque = editar.txtAlterarEstoque.text()

    cursor = conexao.cursor()
    cursor.execute("UPDATE produtos SET id='{}', produto='{}', preco='{}', estoque='{}' WHERE id={}".format(id, produto, preco, estoque, numero_id))

    editar.close()
    lista.close()
    formulario.show()
    
    conexao.commit()#garante que a estrutura esta correta

#cria a função lista para tela lista
def lista():
    lista.show()
    cursor = conexao.cursor()
    comando_SQL = "SELECT * FROM produtos"
    cursor.execute(comando_SQL)
    leitura_banco = cursor.fetchall()


    #faz uma contagem de linha e chama a tabela da lista
    lista.tableWidget.setRowCount(len(leitura_banco))# le as linhas usamos len para achar o final dos dados
    lista.tableWidget.setColumnCount(4)#le a coluna id, produtos, precos, estoque
    
    
    for i in range(0, len(leitura_banco)):#conta do 0 e o len porque não sabemos onde é o fim
        for j in range(0, 4):#conta do 0 ao 4 da coluna
            lista.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(leitura_banco[i][j])))#altera os itens



#cria a funçao inserir
def inserir():
    produto = formulario.txtProduto.text()
    preco = formulario.txtPreco.text()
    estoque = formulario.txtEstoque.text()

    cursor = conexao.cursor()#permite o uso de comando_SQL em python
    comando_SQL = " INSERT INTO produtos (produto, preco, estoque) VALUES (%s, %s, %s)"
    dados = (str(produto), str(preco), str(estoque))
    cursor.execute(comando_SQL, dados)#execulta o comando SQL
    conexao.commit()#confere se as informação está existe

    #zera caixa de texto
    formulario.txtProduto.setText("")
    formulario.txtPreco.setText("")
    formulario.txtEstoque.setText("")




app = QtWidgets.QApplication([])

formulario = uic.loadUi("formulario.ui")#vincula a tela formulario
formulario.btnCadastrar.clicked.connect(inserir)#faz com que ao clikcar no botão cadstrar chame a função inserir
formulario.btnRelatorio.clicked.connect(lista)


lista = uic.loadUi("lista.ui")#vincula a tela lista
lista.btnAlterarRegistro.clicked.connect(editarL)#chama a função editar
lista.btnDeletarRegistro.clicked.connect(deletar)#chama a função deletar
lista.btnImprimir.clicked.connect(imprimir)#chama a função deletar

editar = uic.loadUi("editar.ui")#vincula a tela editar
editar.btnConfirmar.clicked.connect(salvar_dados)

formulario.show()#chama a tela formulario
app.exec()#execulta a tela formulario