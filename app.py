import streamlit as st

# Título de la aplicación
st.title("Calculadora de IMC")

# Entrada de datos
peso = st.number_input("Ingresa tu peso en kg:", min_value=0.0, format="%.2f")
altura = st.number_input("Ingresa tu altura en metros:", min_value=0.0, format="%.2f")

# Botón para calcular
if st.button("Calcular IMC"):
    if peso > 0 and altura > 0:
        # Calcular IMC
        imc = peso / (altura ** 2)
        
        # Mostrar resultado
        st.write(f"Tu IMC es: {imc:.2f}")
        
        # Interpretación del resultado
        if imc < 18.5:
            st.warning("Bajo peso")
        elif 18.5 <= imc < 24.9:
            st.success("Peso normal")
        elif 25 <= imc < 29.9:
            st.warning("Sobrepeso")
        else:
            st.error("Obesidad")
    else:
        st.error("Por favor ingresa valores válidos.")