# ============================================  
# 🌐 SolidarApp Global - Plataforma de Donaciones Inteligentes
# Ejecutable en VSCode con Streamlit
# ============================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="🌐 SolidarApp Global", layout="wide")

# ----------------------------
# Encabezado
# ----------------------------
st.title("🤝 SolidarApp Global - Plataforma de Donación Inteligente")
st.markdown("""
Esta app permite conectar a donantes con regiones de alta pobreza multidimensional (MPI) en todo el mundo,
visualizar el impacto de sus donaciones y apoyar directamente a comunidades vulnerables.
""")

# ----------------------------
# Datos globales simulados (sin CSV)
# ----------------------------
data = {
    "País": ["Afganistán", "Afganistán", "Afganistán", "Etiopía", "Etiopía", "Haití", "India", "India"],
    "Región": ["Baghlan", "Balkh", "Bamyan", "Tigray", "Amhara", "Artibonite", "Bihar", "Uttar Pradesh"],
    "MPI": [0.36, 0.32, 0.27, 0.42, 0.39, 0.48, 0.31, 0.35],
    "Población afectada (%)": [48.5, 45.3, 40.1, 60.2, 55.1, 67.3, 49.8, 51.4]
}
df = pd.DataFrame(data)

# ----------------------------
# Simulador de Donación
# ----------------------------
st.sidebar.header("💸 Simulador de Donación")
usuario = st.sidebar.text_input("Nombre del Donante", value="Anónimo")
montos = [5, 10, 25, 50, 100]
donacion = st.sidebar.selectbox("Elige un monto a donar ($)", montos)

# Selección de país y región
paises = df["País"].unique()
pais_elegido = st.sidebar.selectbox("🌍 País", paises)
regiones_disponibles = df[df["País"] == pais_elegido]["Región"].tolist()
region_elegida = st.sidebar.selectbox("📍 Región", regiones_disponibles)

# Botón de donación
if st.sidebar.button("Donar ahora"):
    st.sidebar.success(f"Gracias {usuario}, tu donación de ${donacion} fue enviada a {region_elegida}, {pais_elegido}.")

# ----------------------------
# Visualización: Mapa de calor
# ----------------------------
st.subheader("📊 Mapa de Calor - Índice de Pobreza Multidimensional (Simulado)")
fig = px.bar(
    df.sort_values("MPI"),
    x="MPI", y="Región", color="MPI", orientation='h',
    color_continuous_scale="Reds", facet_col="País", height=600
)
st.plotly_chart(fig, use_container_width=True)

# ----------------------------
# Estimación de impacto
# ----------------------------
st.subheader("📈 Impacto Estimado de tu Donación")
impacto_estimado = donacion * np.random.uniform(2, 5)
st.metric(label="Beneficiarios Estimados", value=f"{int(impacto_estimado)} personas")

# ----------------------------
# Transparencia y trazabilidad
# ----------------------------
st.subheader("🔍 Transparencia y Trazabilidad")
st.markdown("""
Cada donación es trazada a través de un sistema seguro y auditable. Puedes verificar el uso del dinero
en reportes mensuales públicos dentro de la plataforma.
""")

# ----------------------------
# Pie de página
# ----------------------------
st.markdown("---")
st.markdown("Desarrollado como parte del proyecto *Sistema Predictivo de Pobreza con IA* | Alineado al ODS 1")
