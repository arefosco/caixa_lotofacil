

# caixa_lotofacil (Português)
Algoritmo para criar jogos filtrados e melhorados com base em padrões conhecidos

<h4>Detalhes</h4>
<ul> Arquivos principais
  <li>banco_de_dados/banco.py</li>
  <li>banco_de_dados/do_2001_ao_3000.py</li>
  <li>executavel/exe.py</li>
  <li>executavel/exe_loop.py</li>
  <li>testes/tests.py</li>
</ul>

<ol>
  <li><b>banco_de_dados/banco.py</b> guarda os dados do banco usado pelo algoritmo, armazenado na variável <b>dtb</b></li>
  <li><b>banco_de_dados/banco.py</b> é uma concatenação de todos os jogos desmembrados em grupos de <b>1000 índices</b></li>
  <li><b>banco_de_dados</b> armazena arquivos, onde cada um guarda um array de tuplas com 1000 índices</li>
  <li><b>A cada 1000 jogos</b>, será criado um novo arquivo ao escopo da pasta (atualmente entre 2000 a 3000 jogos)</li>
  <li>O único procedimento a ser feito é adicionar cada jogo novo lançado (em forma de tupla) ao arquivo de banco de dados atual</li>
  <li>O arquivo de banco de dados atual: <b>banco_de_dados/do_2001_ao_3000.py</b> (adicionar tupla ao fundo do array)</li>
</ol>

<h4>Versões do Algoritmo</h4>
<ol>
  <li>O algoritmo está respectivamente em <b>executavel/exe.py</b> e <b>executavel_exe_loop.py</b></li>
  <li><b>executavel/exe.py</b> é a versão do algoritmo usada para testes</li>
  <li><b>executavel_exe_loop.py</b> é a versão oficial do algoritmo</li>
  <li><b>executavel/exe.py</b> é usada em <b>testes.py</b></li>
  <li>MOTIVO: testes com input tornam sua execução manual e limitada</li>
</ol>

<h4>Testes</h4>
<ol>
  <li>Ir ao módulo <b>testes/testes.py</b> e executar o botão próximo à classe</li>
</ol>

# caixa_lotofacil (English)
Algorithm to create filtered and improved games based on known patterns

<h4>Details</h4>
<ul> Main files
  <li>banco_de_dados/banco.py</li>
  <li>banco_de_dados/do_2001_ao_3000.py</li>
  <li>executavel/exe.py</li>
  <li>executavel/exe_loop.py</li>
  <li>testes/tests.py</li>
</ul>

<ol>
  <li><b>banco_de_dados/banco.py</b> holds the database data used on the algorithm, stored by the variable <b>dtb</b></li>
  <li><b>banco_de_dados/banco.py</b> is a concatenation of all dismembered games in groups of <b>1000 indexes</b></li>
  <li><b>banco_de_dados</b> stores files, where each one keeps an array of tuples with 1000 indexes</li>
  <li><b>After each 1000 games</b>, a new file will be created in the scope of the folder (currently at 2000 to 3000 games)</li>
  <li>The only procedure to be done is to add each new game released (as a tuple) to the current target database file </li>
  <li>The current target database file is: <b>banco_de_dados/do_2001_ao_3000.py</b> (add tuple to the bottom of the array)</li>
</ol>

<h4>Versões do algoritmo</h4>
<ol>
  <li>The algorithm is respectively at <b>executavel/exe.py</b> and <b>executavel_exe_loop.py</b></li>
  <li><b>executavel/exe.py</b> holds the alternative version of the algorithm used for making tests</li>
  <li><b>executavel/exe.py</b> is directly used at <b>testes/testes.py</b></li>
  <li><b>executavel_exe_loop.py</b> is the official version of the algorithm</li>
  <li>JUSTIFICATION: tests holding inputs turn them manual and limited</li>
</ol>

<h4>Tests</h4>
<ol>
  <li>Go to the module <b>testes/testes.py</b> and execute the button next to the class</li>
</ol>