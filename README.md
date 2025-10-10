Relatório de Laboratório: Exploração de Credenciais Fracas no Metasploitable (Protocolo FTP)
1. Preparação do Ambiente de Teste
O foco inicial foi estabelecer um ambiente de laboratório isolado e seguro. Utilize o Kali Linux (Atacante) e o Metasploitable (Alvo) no VirtualBox.

Isolamento de Rede: A VM Metasploitable foi configurada no modo Rede Interna (Internal Network), garantindo que a atividade de pentest ficasse isolada da rede hospedeira.

Identificação do Alvo: O Metasploitable recebeu o endereço IP [IP do Metasploitable] na interface eth0, estabelecendo a comunicação para o ataque.

2. Descoberta e Extração de Credenciais
Após a validação da conectividade, a etapa seguinte foi mapear os serviços vulneráveis.

Identificação de Serviço: Uma varredura de portas identificou o serviço FTP (File Transfer Protocol) rodando na porta 21 como um ponto de entrada potencial, devido à sua natureza insegura.

Obtenção de Hashes: Foi realizada a extração dos hashes de senha do sistema Metasploitable, essenciais para o ataque offline de quebra de senha.

3. Exploração via FTP com John the Ripper (Acesso Concedido)
O vetor de ataque foi a quebra das credenciais extraídas, confirmando a vulnerabilidade do sistema a ataques de dicionário.

Ataque de Força Bruta/Dicionário: A ferramenta John the Ripper (John) foi utilizada no Kali Linux, aplicando uma wordlist contra os hashes de senha obtidos.

Credencial Comprometida: O John decifrou com sucesso o hash, revelando a credencial do usuário [Nome do Usuário] como sendo [A Senha Descoberta].

Acesso Concedido: Utilizando as credenciais descobertas, foi estabelecido o acesso não autorizado ao sistema via FTP. Isso validou o controle da sessão e confirmou que a vulnerabilidade de credenciais fracas no sistema foi explorada com sucesso.

Conclusão: O teste demonstra que o Metasploitable estava vulnerável a um ataque de dicionário, permitindo o acesso à sua estrutura de arquivos via FTP. Isso ressalta a importância de desabilitar serviços legados e impor uma política de senhas fortes.
