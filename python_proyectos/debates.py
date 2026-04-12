# Mini simulador de debate izquierda vs derecha

argumentos_izquierda = {
    "economia": "Crecimiento en agro y turismo aumenta el PIB; precios podrían bajar; crecimiento inclusivo.",
    "empleo": "Bajos índices de desempleo muestran eficacia; empleo generado es positivo.",
    "transicion": "Es importante acelerar transición energética para reducir contaminación.",
    "seguridad": "Política de paz y desarme busca estabilidad social.",
    "turismo": "Incremento del turismo genera empleo e ingresos.",
    "agro": "Crecimiento del 30% en el sector agro fortalece economía y autosuficiencia alimentaria."
}

contraargumentos_derecha = {
    "economia": "Apoya crecimiento, pero pide equilibrio y sostenibilidad; cuidado con inflación o dependencia de sectores específicos.",
    "empleo": "Reconoce bajos índices actuales, pero alerta sobre sostenibilidad y calidad del empleo; no todos son formales o duraderos.",
    "transicion": "Apoya transición gradual; preocupación por pérdida de ingresos, empleos y estabilidad fiscal si se hace demasiado rápido.",
    "seguridad": "Preocupación por posibles vacíos de autoridad; seguridad debe ser fuerte para proteger inversión y ciudadanía.",
    "turismo": "Bien recibido, pero requiere planificación, infraestructura y regulación; importancia de inversión privada.",
    "agro": "Apoya crecimiento, pero pide diversificación y preparación ante riesgos climáticos o de mercado."
}

print("💬 Bienvenido al simulador de debate: izquierda vs derecha")
print("Temas disponibles:", ", ".join(argumentos_izquierda.keys()))

tema = input("Elige un tema para dar un argumento (escribe la palabra clave): ").lower()

if tema in argumentos_izquierda:
    print("\n👉 Argumento a favor (izquierda):")
    print(argumentos_izquierda[tema])
    print("\n⚔ Contraargumento (derecha):")
    print(contraargumentos_derecha[tema])
else:
    print("Tema no válido. Intenta de nuevo.")