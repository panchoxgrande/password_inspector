import re
import hashlib
import requests

def evaluate_password(password):
    score = 0
    feedback = []

    length = len(password)
    if length >= 12:
        score += 30
    elif length >= 8:
        score += 20
        feedback.append("Podrías hacerla más larga 💪")
    else:
        score += 5
        feedback.append("Muy corta... así no protegés ni una bici 😅")

    if re.search(r'[A-Z]', password): score += 10
    else: feedback.append("Agregá mayúsculas")

    if re.search(r'[a-z]', password): score += 10
    else: feedback.append("Agregá minúsculas")

    if re.search(r'\d', password): score += 10
    else: feedback.append("Le falta algún numerito")

    if re.search(r'\W', password): score += 10
    else: feedback.append("Un símbolo no le vendría mal (#, @, %, etc)")

    if password.lower() in ['password', '123456', 'qwerty']:
        feedback.append("No uses contraseñas típicas. No sos el único que lo pensó.")
        score = max(score - 20, 0)

    return score, feedback or ["Buena contraseña 👌"]

def check_pwned(password):
    sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1[:5], sha1[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    if response.status_code != 200:
        return None

    hashes = (line.split(':') for line in response.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return int(count)
    return 0
