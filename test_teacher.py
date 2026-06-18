from tools.ppt_generator import create_ppt

lesson = """
SLIDE:
TYPE: cover
TITLE: ⚽ El fútbol en Madrid
IMAGE: Real Madrid stadium
CONTENT:
- Nivel A1

SLIDE:
TYPE: warmup
TITLE: 🔥 Warm-up
IMAGE: football fans
CONTENT:
- ¿Te gusta el fútbol?
- ¿Qué equipos conoces?

SLIDE:
TYPE: image
TITLE: 🖼️ Observa la imagen
IMAGE: football supporters
CONTENT:
- ¿Qué ves?
- ¿Qué están haciendo?

SLIDE:
TYPE: vocab
TITLE: 📚 Vocabulario
IMAGE: football players
CONTENT:
- ⚽ gol
- 🏟 estadio
- 👥 aficionado

SLIDE:
TYPE: reading
TITLE: 📖 Lectura
CONTENT:
- Real Madrid ganó ayer.
- Muchos aficionados celebraron.

SLIDE:
TYPE: grammar
TITLE: ✏️ Gramática
CONTENT:
- ganar → ganó
- Completa: Ayer Madrid _____

SLIDE:
TYPE: speaking
TITLE: 🗣️ Hablemos
CONTENT:
- ¿Te gusta el fútbol?
- ¿Cuál es tu jugador favorito?

SLIDE:
TYPE: summary
TITLE: Resumen
CONTENT:
- Aprendimos vocabulario
- Hablamos sobre fútbol

SLIDE:
TYPE: homework
TITLE: Tarea
CONTENT:
- Escribe 5 frases sobre tu deporte favorito
"""

create_ppt(
    "Test",
    lesson,
    "output/ppt/test_notebooklm.pptx"
)