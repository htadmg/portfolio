from pathlib import Path
import streamlit as st
from PIL import Image

# configuracoes estruturais #

diretorio = Path(__file__).parent if "__file__" in locals() else Path.cwd()
arquivo_css = diretorio / "styles" / "geral.css"
arquivo_pdf = diretorio / "assets" / "agata_domingues.pdf"
arquivo_img = diretorio / "assets" / "foto.jpeg"

# configuracoes geral das informacoes #

TITULO = "Currículo | Agata Domingues"

NOME = "Agata Domingues"

DESCRICAO = """
    Desenvolvedora | C# | Python | HTML | CSS | JavaScript | SQL
"""

EMAIL = "agatadominguestec@hotmail.com"

MIDIA_SOCIAL = {
    "LinkedIn": "https://www.linkedin.com/in/agatadominguesfarias/",
    "GitHub": "https://github.com/htadmg"
}

PROJETOS_CURSOS = {
    "Análise de Dados e Previsão de Sobrevivência": "https://github.com/htadmg/dataset_titanic",
    "Dashboard de Vendas": "https://github.com/htadmg/projeto_streamilt_dash",
    "Dashboard de Vendas com Dash e Flask": "https://github.com/htadmg/dashboard_com_dash",
    "Lista de Tarefas com Django": "https://github.com/htadmg/lista_de_tarefas",    
}

st.set_page_config(
    page_title=TITULO
)

# carregando Assets #

with open(arquivo_css) as c:
    st.markdown(f"<style>{c.read()}</style>", unsafe_allow_html=True)

with open(arquivo_pdf, "rb") as arquivo_pdf:
    pdf_leitura = arquivo_pdf.read()

imagem = Image.open(arquivo_img)

col1, col2 = st.columns(2, gap="small")

with col1:
    st.image(imagem, width=250)

with col2:
    st.title(NOME)
    st.write(DESCRICAO)
    st.download_button(
        label="Download Currículo",
        data=pdf_leitura,
        file_name=arquivo_pdf.name,
        mime="application/octet-stream"
    )
    st.write(EMAIL)

# Midias sociais #

colunas = st.columns(len(MIDIA_SOCIAL))

for indice, (plataforma, link) in enumerate(MIDIA_SOCIAL.items()):
    colunas[indice].write(f"[{plataforma}]({link})")

# experiencias #

st.subheader("Experiências")
st.write(
    """
    - Desenvolvimento de Aplicações com .NET e C#
    - Desenvolvimento WEB com Flask em Python
    - Criação de dashboards interativos com Streamlit e Plotly
    - Integração com a API do Mercado Livre
    - Desenvolvimento de aplicações para gerenciamento de salões de beleza
    """
)

# skills #

st.subheader("Skills")
st.write(
    """
    - Programação: Python | C# | JavaScript 
    - Desenvolvimento Web: Flask | Streamlit | Dash | HTML | CSS
    - Banco de Dados: SQL | PostgreSql
    - Ferramentas: Git | Visual Studio | PyCharm
    - Soft Skills: Trabalho em equipe | Comunicação eficaz | Resolução de problemas
    """
)

# Historico de trabalho #

st.subheader("Histórico de Trabalho")
st.write("**Desenvolvedor de Sistemas | Conecta Marketplaces**")
st.write("05/2024 - o momento")
st.write(
    """
        Atualmente, estou trabalhando em um projeto de integração com o Mercado Livre, 
        onde desenvolvemos uma solução robusta utilizando a API do Mercado Livre. 
        O projeto abrange várias funcionalidades, incluindo o gerenciamento de faturamento, 
        busca e acompanhamento de pedidos, consulta e atualização de preços de anúncios, 
        além de monitoramento da manutenção de anúncios. Implementamos um sistema de login e autenticação de usuários, 
        garantindo segurança e eficiência, utilizando Flask e Python como base para a arquitetura do sistema.
    """
)

st.write("**Desenvolvedor de Sistemas | Techmillen Consultoria e Projetos**")
st.write("06/2023 - 05/2024")
st.write(
    """
        Trabalhei no desenvolvimento de uma aplicação para o gerenciamento de salões de beleza utilizando C# e .NET, 
        com interface responsiva construída com Bootstrap e interatividade aprimorada com jQuery. 
        A aplicação permitia o controle de agendamentos, cadastro de clientes, 
        gerenciamento de funcionários e serviços, oferecendo uma solução eficiente 
        para otimizar as operações do negócio.
    """
)

# cursos # 
st.subheader("Projetos")
for curso, link in PROJETOS_CURSOS.items():
    st.write(f"[{curso}]({link})")