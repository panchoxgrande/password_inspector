
# 🔐 Password Strength Inspector

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Made with ❤️ by PanchoxGrande](https://img.shields.io/badge/made%20by-PanchoxGrande-red)

> ¿segui usando `123456` o `qwerty` como contraseña? Este script no solo te lo va a decir… ¡te va a volar la cabeza! 😉

---

## 🚀 ¿Qué es esto?

**Password Strength Inspector** es una herramienta simple escrita en Python que:
- Analiza contraseñas con criterios de seguridad realistas.
- Te da recomendaciones útiles (y algo sarcásticas).
- Consulta la API de [Have I Been Pwned](https://haveibeenpwned.com/) para saber si tu contraseña fue filtrada.

Ideal para:
- Concientización.
- Demo en portfolios.
- Gente que aún usa el nombre de su perro como password 🐶🔓

---

## 🧰 Tecnologías utilizadas

- `Python 3.8+`
- `rich` para impresión bonita en consola.
- `requests` para acceso a API web.
- `pytest` para tests automáticos.

---

## 📦 Instalación

```bash
git clone https://github.com/panchoxgrande/password_inspector.git
cd password_inspector
pip install -r requirements.txt
````

---

## 🕹️ Uso

```bash
python password_inspector.py
```

Ejemplo:

```
🔐 Password Strength Inspector 🔍
Ingresa tu contraseña: *********

📊 Evaluando seguridad...

Puntuación: 70/100
- Agregá mayúsculas
- Un símbolo no le vendría mal (#, @, %, etc)

¿Quieres revisar si fue filtrada en la web? (s/n): s
⚠️ Tu contraseña apareció en 15 filtraciones. Cámbiala urgente.
```

---

## 🧪 Ejecutar Tests

```bash
pytest tests/
```

---

## 📁 Estructura

```
password_inspector/
├── password_inspector.py
├── utils.py
├── requirements.txt
├── .gitignore
├── README.md
└── tests/
    └── test_utils.py
```

---

## ☂️ Licencia

Este proyecto está bajo licencia MIT. Usalo, modificalo, y compartilo libremente.

---

## 🙋‍♂️ Autor

PanchoxGrande
📫 [GitHub](https://github.com/panchoxgrande)

---

> Si este script te sacó una sonrisa o te salvó de un ciberpecado… ¡dejá una ⭐ en el repo!

```
