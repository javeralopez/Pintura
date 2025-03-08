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




import streamlit as st

# Título de la aplicación
st.title("Calculadora de Pintura (RECTANGULO)")

# Descripción
st.write("Un litro de pintura cubre 9 metros cuadrados de pared. Ingresa las dimensiones de la pared y otros detalles para calcular la cantidad de pintura y thinner necesarios, y el costo total.")

# Entrada de usuario: Ancho y largo de la pared
ancho = st.number_input("Ingresa el ancho de la pared en metros:", min_value=0.0, step=0.1)
largo = st.number_input("Ingresa el largo de la pared en metros:", min_value=0.0, step=0.1)

# Entrada de usuario: Costo por litro de pintura y tipo de pintura
costo_pintura = st.number_input("Ingresa el costo por litro de pintura en tu moneda local:", min_value=0.0, step=0.1)
tipo_pintura = st.text_input("Ingresa el tipo de pintura:")

# Entrada de usuario: Cantidad de thinner necesario y su costo
litros_thinner = st.number_input("Ingresa la cantidad de thinner necesaria en litros:", min_value=0.0, step=0.1)
costo_thinner = st.number_input("Ingresa el costo por litro de thinner en tu moneda local:", min_value=0.0, step=0.1)

# Cálculo del área y pintura necesaria
area = ancho * largo
litros_pintura_necesarios = area / 9
costo_total_pintura = litros_pintura_necesarios * costo_pintura
costo_total_thinner = litros_thinner * costo_thinner
costo_total = costo_total_pintura + costo_total_thinner

# Mostrar resultados
st.write(f"Para cubrir una pared de {ancho} metros de ancho y {largo} metros de largo (total {area:.2f} metros cuadrados), necesitas {litros_pintura_necesarios:.2f} litros de pintura.")
st.write(f"Tipo de pintura: {tipo_pintura}")
st.write(f"El costo total de la pintura es: {costo_total_pintura:.2f} en tu moneda local.")
st.write(f"El costo total del thinner es: {costo_total_thinner:.2f} en tu moneda local.")
st.write(f"El costo total de la pintura y thinner es: {costo_total:.2f} en tu moneda local.")
