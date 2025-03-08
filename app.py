import streamlit as st

def calcular_area_cubo(largo, ancho, alto):
  """Calcula el área de un cubo rectangular."""
  area = 2 * (largo * ancho + largo * alto + ancho * alto)
  return area

def calcular_area_rectangulo(largo, ancho):
  """Calcula el área de un rectángulo."""
  area = largo * ancho
  return area

def calcular_pintura(ancho, alto, precio_litro):
  """Calcula la cantidad de pintura y costo para pintar un rectángulo."""
  area = ancho * alto
  litros_necesarios = area / 9
  costo_total = litros_necesarios * precio_litro
  return litros_necesarios, costo_total

st.title("Calculadora de Áreas")

# Cálculo del área del cubo
st.header("Área de un Cubo Rectangular")
largo_cubo = st.number_input("Ingrese la longitud del cubo:", value=0.0)
ancho_cubo = st.number_input("Ingrese el ancho del cubo:", value=0.0)
alto_cubo = st.number_input("Ingrese la altura del cubo:", value=0.0)

if st.button("Calcular Área del Cubo"):
  area_cubo = calcular_area_cubo(largo_cubo, ancho_cubo, alto_cubo)
  st.write(f"El área del cubo rectangular es: {area_cubo}")

# Cálculo del área del rectángulo
st.header("Área de un Rectángulo")
largo_rectangulo = st.number_input("Ingrese la longitud del rectángulo:", value=0.0)
ancho_rectangulo = st.number_input("Ingrese el ancho del rectángulo:", value=0.0)

if st.button("Calcular Área del Rectángulo"):
  area_rectangulo = calcular_area_rectangulo(largo_rectangulo, ancho_rectangulo)
  st.write(f"El área del rectángulo es: {area_rectangulo}")

# Cálculo de pintura
st.header("Calculadora de Pintura")
ancho_pared = st.number_input("Ingrese el ancho de la pared (metros):", value=0.0)
alto_pared = st.number_input("Ingrese el alto de la pared (metros):", value=0.0)
precio_litro_pintura = st.number_input("Ingrese el precio por litro de pintura:", value=0.0)

if st.button("Calcular Pintura"):
  litros, costo = calcular_pintura(ancho_pared, alto_pared, precio_litro_pintura)
  st.write(f"Necesitará {litros:.2f} litros de pintura.")
  st.write(f"El costo total de la pintura será: {costo:.2f}")



import streamlit as st

# Título de la aplicación
st.title("Calculadora de Pintura")

# Descripción
st.write("Un litro de pintura cubre 9 metros cuadrados de pared. Ingresa las dimensiones de la pared para calcular la cantidad de pintura necesaria.")

# Entrada de usuario: Ancho y largo de la pared
ancho = st.number_input("Ingresa el ancho de la pared en metros:", min_value=0.0, step=0.1)
largo = st.number_input("Ingresa el largo de la pared en metros:", min_value=0.0, step=0.1)

# Cálculo del área y pintura necesaria
area = ancho * largo
litros_necesarios = area / 9

# Mostrar resultado
st.write(f"Para cubrir una pared de {ancho} metros de ancho y {largo} metros de largo (total {area:.2f} metros cuadrados), necesitas {litros_necesarios:.2f} litros de pintura.")
