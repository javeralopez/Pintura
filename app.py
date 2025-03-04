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
