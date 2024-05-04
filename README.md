# Alexson - Assistente de Voz

Alexson é um assistente de voz desenvolvido em Python que realiza comandos de voz e fornece respostas curtas e concisas. Ele é capaz de reconhecer comandos de voz, responder a perguntas e realizar interações baseadas em texto.

## Funcionalidades

- Reconhecimento de comandos de voz: Alexson pode ouvir comandos de voz do usuário.
- Respostas curtas e concisas: As respostas de Alexson são curtas, geralmente com cerca de 100 caracteres, mas são formuladas de forma clara e compreensível.
- Reconhecimento de nome: Alexson responde a várias variantes de seu nome, incluindo "Alexson", "Alekso" e "Alex".

## Como usar

Para usar Alexson, basta executar o arquivo Python `main.py`. Ele começará a ouvir comandos de voz assim que for ativado pelo nome "Alexson" ou suas variantes. Após reconhecer um comando de voz, Alexson processa o comando, fornece uma resposta e aguarda o próximo comando.

## Dependências

- Python 3.x
- Bibliotecas Python: `speech_recognition`, `pyttsx3`, `google.generativeai`, `os`, `time`, `dotenv`, `re`, `winsound`

## Configuração

Antes de usar Alexson, é necessário configurar a API do Google para reconhecimento de voz. Você precisa obter uma chave de API válida e configurá-la em um arquivo `.env` no diretório raiz do projeto.

Exemplo de arquivo `.env`:
```
GOOGLE_API_KEY=SuaChaveDeAPIAqui
```
## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para enviar sugestões, correções de bugs ou melhorias por meio de pull requests.
