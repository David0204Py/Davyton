import pandas as pd
import sqlite3

def conn_db():
    try:
        conn1 = sqlite3.connect('datos\MVST.db')
        df_22 = pd.read_sql_query('SELECT * FROM "Most Values Sports Team (2022)"', conn1)
        df_loc = pd.read_sql_query('SELECT * FROM "Most Values Sports Team (Location)"', conn1)
        return df_22, df_loc
    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None, None
    finally:
        conn1.close()

df_22, df_loc = conn_db()

def cord_fix(df_loc):
    if not any(c in df_loc['Longitude'] for c in ('°')):
        df_loc['Longitude'] = pd.to_numeric(df_loc['Longitude'].str.replace('°', ''))  
        df_loc['Latitude'] = pd.to_numeric(df_loc['Latitude'].str.replace('°', ''))
    return df_loc

df_loc = cord_fix(df_loc)

def format_value(value): # Función de formato personalizada
    if not any(c in value for c in ('B', 'M', 'K')):
        if value >= 1_000_000_000:
            return f"${value / 1_000_000_000:.0f}B"  # Billones
        elif value >= 1_000_000:
            return f"${value / 1_000_000:.0f}M"  # Millones
        elif value >= 1_000:
            return f"${value / 1_000:.0f}K"  # Miles
        else:
            return f"${value:.0f}"  # Valores menores a mil
    else:
        return value