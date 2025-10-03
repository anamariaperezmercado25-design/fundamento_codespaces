import streamlit as st

st.title('Calculadora de Número de Reynolds')
st.write('Ingresa los valores para calcular el número de Reynolds y determinar el tipo de flujo:')

# Entradas del usuario
velocidad = st.number_input('Velocidad del fluido (m/s)', min_value=0.0, format="%f")
diametro = st.number_input('Diámetro del tubo (m)', min_value=0.0, format="%f")
densidad = st.number_input('Densidad del fluido (kg/m³)', min_value=0.0, format="%f")
viscosidad = st.number_input('Viscosidad dinámica (Pa·s)', min_value=0.0, format="%f")

if st.button('Calcular'):
	if viscosidad == 0:
		st.error('La viscosidad no puede ser cero.')
	else:
		reynolds = (densidad * velocidad * diametro) / viscosidad
		st.write(f'**Número de Reynolds:** {reynolds:.2f}')

		# Determinar tipo de flujo
		if reynolds < 2000:
			tipo = 'Flujo laminar'
		elif reynolds < 4000:
			tipo = 'Flujo transitorio'
		else:
			tipo = 'Flujo turbulento'
		st.write(f'**Tipo de flujo:** {tipo}')
