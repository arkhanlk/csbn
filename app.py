import streamlit as st
import json

# Configurar a página
st.set_page_config(page_title="Menu Interativo - SbN", layout="wide")

# Carregar dados do JSON
@st.cache_data
def carregar_dados():
    with open('dados.json', 'r', encoding='utf-8') as f:
        return json.load(f)

dados = carregar_dados()

# Título da aplicação
st.title("🌱 Catálogo de Soluções Baseadas na Natureza (SbN)")
st.markdown("---")

# Extrair lista de tópicos para a selectbox
topicos_list = [f"{t['id']} - {t['titulo']}" for t in dados['topicos']]
topico_selecionado_index = st.selectbox(
    "Selecione um Tópico:",
    range(len(topicos_list)),
    format_func=lambda x: topicos_list[x]
)

# Obter dados do tópico selecionado
topico_dados = dados['topicos'][topico_selecionado_index]

# Exibir informações do tópico
st.subheader(f"📋 {topico_dados['id']} - {topico_dados['titulo']}")
st.markdown("---")

# Criar expanders para cada eixo
for eixo in topico_dados['eixos']:
    with st.expander(f"**Eixo {eixo['numero']}** - {eixo['titulo']}", expanded=False):
        for item in eixo['conteudo']:
            st.markdown(f"• {item}")

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: gray; font-size: 12px;'>
    Catálogo de Soluções Baseadas na Natureza | Desenvolvido com Streamlit
    </div>
""", unsafe_allow_html=True)
