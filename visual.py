# Importar modulos
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st
import modulo_viisual as mv


# Establecer el estilo
sns.set_style("dark")
plt.style.use('dark_background')

# Configurar el tema oscuro
st.set_page_config(
    page_title="Distribución del valor de los equipos", 
    page_icon=":bar_chart:", layout="wide", theme="dark")

# Crear un título para el dashboard
st.title("Distribución del valor de los equipos")

# Crear un contenedor para el gráfico
with st.container():
    # Crear un gráfico de histograma con kde
    fig, ax = plt.subplots(figsize=(16, 10))
    sns.histplot(mv.df_22['Value'], bins=12, kde=True, color='blue', ax=ax)

    # Ajustar el rango del eje para comenzar en cero
    x_min, x_max = ax.get_xlim()  # Obtener el rango actual del eje
    ax.set_xlim(0, x_max)  # Ajustar el límite inferior del eje a cero

    # Personalizar las etiquetas del eje x
    xticks = ax.get_xticks()  # Obtener los ticks actuales del eje
    xticklabels = [mv.format_value(int(tick)) for tick in xticks]  # Aplicar formato a cada tick
    ax.set_xticks(xticks)  # Establecer los ticks del eje
    ax.set_xticklabels(xticklabels, fontsize=10)  # Establecer las etiquetas personalizadas

    # Personalizar las etiquetas del eje y
    yticks = ax.get_yticks()  # Obtener los ticks actuales del eje y
    yticklabels = [f'{int(tick)}%' for tick in yticks]  # Aplicar formato a cada tick
    ax.set_yticks(yticks)  # Establecer los ticks del eje y
    ax.set_yticklabels(yticklabels, fontsize=10)  # Establecer las etiquetas personalizadas

    # Añadir el nombre de cada equipo dentro de cada barra
    for p in ax.patches:
        height = p.get_height()
        # Usar el nombre del item como texto
        item_name = mv.df_22['Sports Team'][list(ax.patches).index(p)]
        ax.text( p.get_x() + p.get_width() / 2, height / 1.5, item_name, 
                color='white', ha='center', va='center',rotation=55, fontsize=7 )

    # Configurar el titulo y etiquetas
    ax.set_title('Distribución del valor de los equipos')
    ax.set_xlabel('Valor')
    ax.set_ylabel('Frecuencia en que los equipos caen en un intervalo de valor')

    # Mostrar el gráfico
    st.pyplot(fig)

# Agregar una descripción del gráfico
st.write("Este gráfico muestra la distribución del valor de los equipos deportivos. El histograma, acompañado por una línea de densidad (KDE), esta revela cómo se distribuyen los valores de los equipos en el conjunto de datos. En particular, el gráfico destaca que más del 25% de los equipos tienen un valor muy por debajo de la media, ofreciendo una visión clara sobre la dispersión de los valores.")



