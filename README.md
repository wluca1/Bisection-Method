<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
</head>
<body>
    <h1>Método da Bisseção em Python</h1>
    <p>Este é um código Python que implementa o Método da Bisseção para encontrar raízes de uma função matemática. O método da bisseção é uma técnica numérica que divide repetidamente um intervalo ao meio até encontrar uma raiz com uma tolerância aceitável.</p>

<h2>Instruções de Uso</h2>
    <ol>
        <li>Para executar o programa, você precisa de um ambiente Python instalado em seu computador.</li>
        <li>Abra o código em um editor de texto ou ambiente de desenvolvimento Python.</li>
        <li>Execute o código e a interface gráfica será aberta.</li>
        <li>Insira a função que deseja analisar (use 'x' como variável), o intervalo inicial [a, b], a tolerância e o número máximo de iterações.</li>
        <li>Clique no botão "Executar Método da Bisseção" para iniciar o cálculo.</li>
        <li>Os resultados serão exibidos na interface, incluindo a raiz encontrada, uma tabela com os detalhes das iterações e um gráfico da função.</li>
    </ol>

<h2>Estrutura do Código</h2>
    <p>O código Python é dividido em várias partes:</p>
    <ul>
        <li><strong>Função `bissecao(a, b, tol, max_iter, funcao)`: </strong> Esta função implementa o método da bisseção para encontrar uma raiz da função `funcao` dentro do intervalo `[a, b]` com uma tolerância `tol` e um número máximo de iterações `max_iter`.</li>

<li><strong>Função `criar_interface_grafica()`: </strong> Esta função cria a interface gráfica onde o usuário pode inserir os parâmetros para o método da bisseção e visualizar os resultados.</li>

<li><strong>Interface Gráfica: </strong> A interface gráfica inclui campos para inserir a função, o intervalo, a tolerância e o número máximo de iterações. Também há botões para executar o método e limpar a interface. Os resultados são exibidos em uma tabela e em um gráfico Matplotlib na interface.</li>

<li><strong>Iterações do Método da Bisseção: </strong> O método da bisseção divide o intervalo `[a, b]` ao meio repetidamente até encontrar uma raiz. A cada iteração, o código calcula o ponto médio, avalia a função nesse ponto e decide qual metade do intervalo contém a raiz.</li>
    </ul>

<p>Em resumo, este código combina programação Python com o método matemático da bisseção para encontrar raízes de funções, proporcionando uma interface gráfica amigável para entrada de dados e visualização de resultados. É útil para resolver problemas de matemática e engenharia que envolvem a busca por raízes de funções.</p>
</body>
</html>
