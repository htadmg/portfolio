# Currículo Interativo | Agata Domingues

## Descrição do Projeto
Este é um projeto desenvolvido utilizando **Streamlit**, que gera um currículo interativo online, exibindo as principais informações de perfil, habilidades, histórico de trabalho e projetos. Ele também permite o download do currículo em PDF diretamente pela interface.

## Funcionalidades

- Exibição de foto e informações básicas de contato.
- Links para perfis de mídias sociais (LinkedIn e GitHub).
- Download do currículo em formato PDF.
- Apresentação das experiências profissionais e habilidades técnicas.
- Listagem de projetos e cursos com links diretos para os repositórios no GitHub.

## Tecnologias Utilizadas

- **Python**: Linguagem principal usada para desenvolver a aplicação.
- **Streamlit**: Framework utilizado para criar a interface do currículo.
- **Pillow (PIL)**: Biblioteca usada para manipulação e exibição da imagem.
- **CSS**: Customização da aparência da aplicação.

## Como Configurar o Projeto

Para executar este projeto localmente, siga os passos abaixo:

1. Clone o repositório:

- Usando HTTPS:
```bash
git clone https://github.com/htadmg/portfolio.git
```
- Usando SSH:
```bash
git clone git@github.com:htadmg/portfolio.git
```
- Navegue até o diretório do projeto:
```bash
cd .\portfolio
```

2. **Crie e Ative um Ambiente Virtual (opcional, mas recomendado)**
- **Para Linux/MacOS:**
```bash
python -m venv .venv
source venv/bin/activate
```
 
- **Para Windows:**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```   
3. **Instale as dependências**
```bash
pip install -r requirements.txt
```
### Iniciar o Servidor de Desenvolvimento

Inicie o servidor de desenvolvimento com o comando:

```bash
streamlit run .\app.py
```
### Acessar o Projeto
Abra um navegador e vá para http://localhost::8501 para ver o aplicativo em funcionamento.
