from fpdf import FPDF

# Crear la clase para el PDF
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Comparación de Tipos de Datos: Python vs JavaScript', ln=True, align='C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', align='C')

# Datos de comparación
datos = [
    ["Característica", "Python", "JavaScript"],
    ["Enteros", "int", "Number"],
    ["Cadenas", "str", "String"],
    ["Booleanos", "bool", "Boolean"],
    ["Listas/Arreglos", "list", "Array"],
    ["Diccionarios/Objetos", "dict", "Object"],
]

# Crear y configurar el PDF
pdf = PDF()
pdf.add_page()
pdf.set_font('Arial', '', 12)

# Crear la tabla
for i, fila in enumerate(datos):
    for item in fila:
        pdf.cell(63, 10, item, border=1, align='C')
    pdf.ln()

# Guardar el archivo PDF
pdf.output("Comparacion_Tipos_Datos.pdf")

print("PDF generado exitosamente.")