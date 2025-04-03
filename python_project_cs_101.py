import random
import time
import unicodedata

def normalizar_texto(texto):
    return ''.join(c for c in unicodedata.normalize('NFD', texto.lower().strip()) if unicodedata.category(c) != 'Mn')

# ASCII Art de bienvenida
BIENVENIDA = """
****************************************
*      🔮 BIENVENIDO AL TAROT 🔮       *
*  Descubre los misterios del destino  *
****************************************
"""

# Representación de una carta boca abajo
CARTA_BOCA_ABAJO = """
+---------+
|  *****  |
|  *****  |
|  *****  |
|  *****  |
+---------+
"""

# Representación de cartas reveladas
CARTA_ASCII = {
    "El Mago": """
+---------+
| 🌟MAGO🌟|
|          |
|  Poder   |
| Creativo |
+---------+
""",
    "La Sacerdotisa": """
+---------+
| 📖SAC📖 |
| Sabidur. |
| Misterio |
+---------+
""",
    "La Emperatriz": """
+---------+
| 👑EMP👑|
| Fértil. |
| Abund.  |
+---------+
""",
    "El Emperador": """
+---------+
| 🏛EMP🏛  |
| Orden   |
| Estabil.|
+---------+
""",
    "El Papa": """
+---------+
| ✝️PAP✝️ |
| Sabidur. |
| Consejo |
+---------+
""",
    "Los Enamorados": """
+---------+
| ❤️ENAM❤️|
| Unión   |
| Decisión|
+---------+
""",
    "El Carro": """
+---------+
| 🛞CARRO🛞|
| Avance  |
| Victoria|
+---------+
""",
    "La Justicia": """
+---------+
| ⚖️JUST⚖️|
| Equilib.|
| Verdad  |
+---------+
""",
    "El Ermitaño": """
+---------+
| 🕯️ERMI🕯️|
| Intros. |
| Sabidur.|
+---------+
""",
    "La Rueda de la Fortuna": """
+---------+
| 🔄RUEDA🔄|
| Cambio  |
| Ciclos  |
+---------+
""",
    "La Fuerza": """
+---------+
| 🦁FUER🦁 |
| Coraje  |
| Dominio |
+---------+
""",
    "El Colgado": """
+---------+
| 🪢COLG🪢 |
| Sacrif. |
| Perspec.|
+---------+
""",
    "La Muerte": """
+---------+
| ☠️MUER☠️ |
| Cambio  |
| Renacer |
+---------+
""",
    "La Templanza": """
+---------+
| 🌈TEMP🌈 |
| Armonía |
| Pacienc.|
+---------+
""",
    "El Diablo": """
+---------+
| 😈DIAB😈 |
| Tentac. |
| Atadura |
+---------+
""",
    "La Torre": """
+---------+
| 🏰TORR🏰 |
| Ruptura |
| Cambio  |
+---------+
""",
    "La Estrella": """
+---------+
| ⭐ESTR⭐ |
| Esperan.|
| Inspir. |
+---------+
""",
    "La Luna": """
+---------+
| 🌙LUNA🌙 |
| Ilus.   |
| Intuic. |
+---------+
""",
    "El Sol": """
+---------+
| 🌞SOL🌞 |
| Éxito   |
| Felicid.|
+---------+
""",
    "El Juicio": """
+---------+
| 🎺JUIC🎺 |
| Renacer |
| Decisión|
+---------+
""",
    "El Mundo": """
+---------+
| 🌍MUND🌍 |
| Comple. |
| Logro   |
+---------+
"""
}

# Definimos la clase CartaTarot
class CartaTarot:
    def __init__(self, nombre, significado_amor, significado_dinero, numerologia):
        self.nombre = nombre
        self.significado_amor = significado_amor
        self.significado_dinero = significado_dinero
        self.numerologia = numerologia

    def mostrar_carta(self, categoria):
        significado = self.significado_amor if categoria == "amor" else self.significado_dinero
        return f"{CARTA_ASCII[self.nombre]}\n{self.nombre} (#{self.numerologia}): {significado}"

# Definimos la clase LectorTarot
class LectorTarot:
    def __init__(self, nombre, pregunta, categoria):
        self.nombre = nombre
        self.pregunta = pregunta
        self.categoria = categoria

# Definimos la clase TiradaTarot
class TiradaTarot:
    def __init__(self, tipo, categoria):
        self.tipo = tipo
        self.categoria = categoria
        self.cartas = self.generar_cartas()

    def generar_cartas(self):
        cartas_disponibles = [
            CartaTarot("El Mago", "Un amor lleno de posibilidades y transformación personal.", "Grandes oportunidades en negocios y creatividad.", 1),
            CartaTarot("La Sacerdotisa", "Un amor profundo, misterioso y lleno de sabiduría.", "Paciencia y conocimiento son clave en tus finanzas.", 2),
            CartaTarot("La Emperatriz", "Fertilidad en relaciones, crecimiento y amor abundante.", "Éxito financiero, riqueza y prosperidad material.", 3),
            CartaTarot("El Emperador", "Relación estable, estructurada y con bases sólidas.", "Logro de metas económicas con disciplina.", 4),
            CartaTarot("El Papa", "Consejos valiosos que guían el amor sincero.", "Sabiduría financiera, estabilidad y buenos negocios.", 5),
            CartaTarot("Los Enamorados", "Decisiones importantes en el amor, unión y armonía.", "Asociaciones exitosas y decisiones financieras clave.", 6),
            CartaTarot("El Carro", "Avance en relaciones, éxito y determinación en el amor.", "Triunfo en proyectos financieros y metas alcanzadas.", 7),
            CartaTarot("La Justicia", "Relaciones equilibradas y decisiones justas en el amor.", "Éxito financiero basado en la honestidad y el equilibrio.", 8),
            CartaTarot("El Ermitaño", "Reflexión y búsqueda de sabiduría en el amor.", "Tiempo para analizar y planificar tus finanzas.", 9),
            CartaTarot("La Rueda de la Fortuna", "Cambios inesperados en el amor, ciclos que se renuevan.", "Suerte y cambios positivos en tus finanzas.", 10),
            CartaTarot("La Fuerza", "Coraje y paciencia para superar desafíos en el amor.", "Dominio y control sobre tus finanzas.", 11),
            CartaTarot("El Colgado", "Sacrificio y cambio de perspectiva en relaciones amorosas.", "Decisiones financieras que requieren paciencia y reflexión.", 12),
            CartaTarot("La Muerte", "Transformación profunda y renacimiento en el amor.", "Cambios significativos en tu situación financiera.", 13),
            CartaTarot("La Templanza", "Armonía y equilibrio en relaciones amorosas.", "Gestión cuidadosa y equilibrada de tus finanzas.", 14),
            CartaTarot("El Diablo", "Relaciones intensas, cuidado con la dependencia emocional.", "Evita ataduras financieras y decisiones impulsivas.", 15),
            CartaTarot("La Torre", "Rupturas y cambios inesperados en el amor.", "Crisis financiera que lleva a nuevas oportunidades.", 16),
            CartaTarot("La Estrella", "Esperanza y renovación en relaciones amorosas.", "Inspiración y éxito en proyectos financieros.", 17),
            CartaTarot("La Luna", "Confusión e intuición en el amor, cuidado con ilusiones.", "Precaución en decisiones financieras, confusión temporal.", 18),
            CartaTarot("El Sol", "Felicidad y éxito en relaciones amorosas.", "Éxito financiero y logros importantes.", 19),
            CartaTarot("El Juicio", "Renacimiento y decisiones importantes en el amor.", "Evaluación y renovación en tus finanzas.", 20),
            CartaTarot("El Mundo", "Plenitud y realización en relaciones amorosas.", "Logro de metas financieras y éxito global.", 21)
        ]
        return random.sample(cartas_disponibles, 3 if self.tipo == "basica" else 5)

    def realizar_tirada(self):
        print("\n🌙🌟 Realizando la tirada... 🌟🌙\n")
        time.sleep(2)
        for i, _ in enumerate(self.cartas, 1):
            print(f"Carta {i}:\n{CARTA_BOCA_ABAJO}")
        print("\nEscoge una carta por su número para revelar su significado.")
        reveladas = []
        while len(reveladas) < len(self.cartas):
            if len(reveladas) == len(self.cartas) - 1:
                # Automáticamente revelar la última carta
                ultima_carta = [i for i in range(1, len(self.cartas) + 1) if i not in reveladas][0]
                print(f"\n✨ Y para finalizar, la última carta sería la número {ultima_carta}. ✨")
                reveladas.append(ultima_carta)
                print("\n🔮 Revelando la carta... 🔮")
                time.sleep(1)
                print(self.cartas[ultima_carta - 1].mostrar_carta(self.categoria))
                break

            print("\nCartas disponibles para voltear:")
            for i in range(1, len(self.cartas) + 1):
                if i not in reveladas:
                    print(f"Carta {i}")
            try:
                eleccion = int(input("Número de carta: "))
                if 1 <= eleccion <= len(self.cartas) and eleccion not in reveladas:
                    reveladas.append(eleccion)
                    print("\n🔮 Revelando la carta... 🔮")
                    time.sleep(1)
                    print(self.cartas[eleccion - 1].mostrar_carta(self.categoria))
                else:
                    print("Selección inválida o carta ya revelada.")
            except ValueError:
                print("Ingresa un número válido.")
        
        print("\n🌟 Resumen de tu lectura 🌟")
        for num in reveladas:
            carta = self.cartas[num - 1]
            significado = carta.significado_amor if self.categoria == "amor" else carta.significado_dinero
            print(f"{carta.nombre} (#{carta.numerologia}): {significado}")

# Función principal
if __name__ == "__main__":
    print(BIENVENIDA)
    nombre = input("Ingresa tu nombre: ")
    print(f"\n✨ Hola, {nombre.title()}! Prepárate para descubrir los misterios del Tarot. ✨\n")
    categoria = ""
    while categoria not in ["amor", "dinero"]:
        categoria = normalizar_texto(input("¿Tu pregunta es sobre amor o dinero?: "))
        if categoria not in ["amor", "dinero"]:
            print("Por favor, elige entre 'amor' o 'dinero'.")
    pregunta = input("Escribe tu pregunta: ")
    lector = LectorTarot(nombre, pregunta, categoria)
    
    tipo_tirada = ""
    while tipo_tirada not in ["basica", "inglesa"]:
        tipo_tirada = normalizar_texto(input("Elige el tipo de tirada ('básica' o 'inglesa'): "))
        if tipo_tirada not in ["basica", "inglesa"]:
            print("Por favor, elige 'basica' o 'inglesa'.")
    
    tirada = TiradaTarot(tipo_tirada, categoria)
    tirada.realizar_tirada()
    print(f"\n🔮 Gracias por participar en la lectura del Tarot, {nombre.title()}! 🔮")

