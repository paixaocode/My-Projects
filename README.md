O programa foi desenvolvido para atender a seguinte necessidade:

Eu sempre criei documentos para os desenvolvimentos de projetos, ou de alguma implantação realizada. E esses documentos são anexados em uma pasta compartilhada no Sharepoint (Ferramenta da Microsoft), portanto toda a equipe tem acesso a essas documentações.

O problema é que ningúem sabia, quando um documento era incluso na pasta, a verificação tinha que ser manual, para saber se tinha alguma novidade ou não.

Pensando nisso, criei esse script que verifica automaticamente a quantidade de documentos na pasta compartilhada, e caso tenha algum documento novo ele envia uma mensagem no Whatsapp da equipe dizendo que foi incluso um novo documento, passando também a URL do site na mensagem.


O programa segue os seguintes passos:

1. Verifica a quantidade de arquivos (documentos) na pasta do Sharepoint (obs: A pasta do sharepoint tem que estar sincronizada no computador ou no servidor de onde o programa irá rodar.) O programa grava a quantidade de arquivos em um arquivo TXT, caso a pasta do sharepoint tenha mais arquivos que o TXT, ele entende que está desatualizado, faz a comparação e dispara um aviso no whatsapp. E logo em seguida atualiza o arquivo TXT.

Sugestão: 
1. Colocar o programa para rodar via Job/Schedule do windows a cada 3/6/12 horas.
2. Colocar o programa para rodar em um servidor VM our Fisico.


Atualizações:

Data da ultima atualização: 01/08/2022

O programa futuramente vai ser integrado no Microsoft via Teams, e também não terá a necessidade da pasta está local na maquina.
E também enviará a notificação via Windows para todos os usuários que estão no grupo do OneDrive ou Sharepoint.

Assim que atualizado, será versionado no meu Github.

Obrigado!