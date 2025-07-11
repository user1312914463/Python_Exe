Compilador Python para EXE

Introdução:
O compilador Python para EXE é uma ferramenta fácil de usar que permite aos usuários compilar scripts Python em arquivos executáveis (EXE) separados. A ferramenta fornece uma interface gráfica intuitiva (GUI) que facilita a escolha de arquivos Python, diretórios de saída, arquivos de ícones e configuração de opções de compilação. Ao mesmo tempo, para garantir a segurança e o uso autorizado das ferramentas, foi adicionado um mecanismo de verificação de chaves.
Características
Verificação da chave: antes de usar a ferramenta, é necessário inserir uma chave válida para verificar se somente os usuários autorizados podem usá-la.
Interface gráfica do usuário: fornece uma GUI intuitiva para facilitar a seleção de arquivos e configuração de opções de compilação.
Configurações de opções de compilação: suporta várias opções de compilação como modo de arquivo único, modo de janela e modo de depuração.
Salvar e carregar configurações: os usuários podem salvar e carregar configurações de compilação para facilitar seu próximo uso.
Saída de registro em tempo real: durante o processo de compilação, a saída de registro de compilação em tempo real facilita ao usuário monitorar o progresso da compilação.

Instalação e dependência
Dependência:
Python 3.x
PyInstaller: para compilar scripts Python em arquivos EXE.
Passos de instalação
Certifique-se de ter o Python 3.x instalado, que pode ser baixado e instalado no site oficial do Python.
Instalar o PyInstaller: Abra o terminal da linha de comando e execute o seguinte comando:
pip install pyinstaller

Clone ou baixe este código do projeto localmente.

Uso (inicialização):
Abra o terminal da linha de comando e vá para o diretório raiz do projeto.
Execute o seguinte iniciador de comandos:
python main.py

Verificação da chave:
Quando o programa é iniciado pela primeira vez, aparece uma janela de verificação de chave.
Digite uma chave válida e clique no botão "Verificar" para verificar.
Se a verificação for bem sucedida, o programa será iniciado automaticamente; Se a autenticação falhar, será solicitado com base no número de tentativas restantes e o número de erros excedentes do limite bloqueará o arquivo de chave.

Configurações de compilação:
Arquivos Python: clique no botão "Procurar..." para selecionar o arquivo Python a compilar.
Diretório de saída: clique no botão "Procurar..." para selecionar o diretório de saída do arquivo EXE compilado.
Arquivo de ícone (opcional): clique no botão "Procurar..." para selecionar o arquivo de ícone (com extensão .ico) que você deseja definir para o arquivo EXE.
Opções de compilação:
Modo de arquivo único: empacota todas as dependências em um arquivo EXE separado.
Modo de janela (sem console): o arquivo EXE compilado não mostra a janela do console quando executado.
Modo de depuração: Habilite o modo de depuração para facilitar o processo de compilação de depuração.
Limpar arquivos temporários: limpa os arquivos temporários após a compilação.
Codificação do console: selecione o formato de codificação para a saída do console.
Salvar e carregar configurações
Salvar configurações: clique no botão "Salvar configurações" para salvar as configurações de compilação atuais no arquivo py_to_exe_config.json.
Configurações de carregamento: clique no botão "Configurações de carregamento" para carregar as configurações de compilação salvas anteriormente do arquivo py_to_exe_config.json.
Iniciar a compilação
Depois de concluir as configurações de compilação, clique no botão "Iniciar compilação" e o programa iniciará o processo de compilação.
Durante a compilação, o registro de compilação é exibido em tempo real na área de registro e a barra de progresso mostra o progresso da compilação.
Quando a compilação for concluída, a caixa de instruções correspondente aparecerá para informar o resultado da compilação.

Estrutura do arquivo:
plaintext:
exe/
main.py # ponto de entrada do programa
key_verification.py # Módulo de verificação de chaves
â—— compiler_gui.py # Módulo principal da interface de compilação
 ── compilation_engine.py # Módulo do motor de compilação
config_manager.py # Configuração do módulo de gerenciamento
├── resources/
keys.json # Perfil da chave
 ─ py_to_exe_config.json # Compilar configurações para salvar arquivos

Atenção!
Certifique-se de que a chave digitada é válida, caso contrário a ferramenta poderá não funcionar corretamente.
O processo de compilação pode levar algum tempo, dependendo da complexidade do script Python e do desempenho do sistema.
Se você tiver problemas durante a compilação, verifique a saída do log para resolver com base nas mensagens de erro.
Contribuições e feedback
Se você encontrar um bug ou sugerir melhorias, adicione QQ:1312914463. Ao mesmo tempo, você é bem-vindo a compartilhar suas experiências e apresentar novas necessidades de recursos.