# Automação de Cadastro de Produtos com PyAutoGUI e Pandas

Este script utiliza a biblioteca **PyAutoGUI** para automatizar o processo de login em um site e o cadastro de produtos a partir de uma planilha CSV. Ele abre o navegador, acessa um site específico, faz login e cadastra produtos em um formulário de forma repetida.

## Requisitos

Para rodar o script, é necessário ter as seguintes bibliotecas instaladas:

- `pyautogui`
- `pandas`

Você pode instalar essas dependências executando o seguinte comando:

```bash
pip install pyautogui pandas


```
## Como funciona

O script abre o navegador Chrome e acessa a página de login.
Faz o login no site com as credenciais fornecidas no código.
Carrega uma tabela CSV contendo os produtos a serem cadastrados.
Preenche os campos do formulário do site com as informações de cada produto (código, marca, tipo, categoria, preço unitário, custo, e observações) e os envia um a um.
Arquivo CSV

## A tabela de produtos deve estar em um arquivo chamado produtos.csv com a seguinte estrutura:
| codigo | marca  | tipo  | categoria | preco_unitario | custo | obs       |
|--------|--------|-------|-----------|----------------|-------|-----------|
| 12345  | MarcaX | Tipo1 | CategoriaA| 50.00          | 30.00 | Exemplo 1 |
| 67890  | MarcaY | Tipo2 | CategoriaB| 80.00          | 60.00 | Exemplo 2 |

## Observação

As coordenadas de clique (pyautogui.click) são específicas para o monitor usado no desenvolvimento. Para usar em outro monitor, pode ser necessário ajustar as coordenadas.
O tempo de espera entre as ações (como o uso de time.sleep e pyautogui.sleep) também pode precisar ser ajustado de acordo com a performance da sua máquina e a velocidade da conexão.

## Como usar

Certifique-se de que o arquivo produtos.csv esteja na mesma pasta que o script.
Execute o script em um ambiente Python:
```bash
python main.py
```
O navegador será aberto, o login será feito automaticamente e os produtos da tabela CSV serão cadastrados no site.

Aviso
Este script é um exemplo de automação simples com o PyAutoGUI e é altamente dependente de como a interface gráfica do usuário é exibida no monitor. Certifique-se de ajustar as coordenadas dos cliques para que funcione corretamente no seu ambiente.
"O PyAutoGUI possui uma trava de segurança para que você possa parar a automação sem problemas. Posicione o cursor do seu mouse no canto superior esquerdo do monitor e aguarde; isso fará com que a trava seja ativada e o seu código pare de rodar."
