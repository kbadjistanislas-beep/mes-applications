import imaplib, smtplib, email, time
from email.mime.text import MIMEText

# ===== CONFIGURATION =====
EMAIL = "kbadjistanislas@gmail.com"
MDP = "pswl psyb padm bjen"  # Mot de passe d'application Gmail
IMAP = "imap.gmail.com"
SMTP = "smtp.gmail.com"
# Test de connexion
try:
    test = imaplib.IMAP4_SSL(IMAP)
    test.login(EMAIL, MDP)
    print("✅ Connexion IMAP réussie !")
    test.logout()
except Exception as e:
    print(f"❌ Erreur de connexion: {e}")
    exit()
# ===== ENVOYER =====
def envoyer(dest, sujet, corps):
    msg = MIMEText(corps)
    msg['From'] = EMAIL
    msg['To'] = dest
    msg['Subject'] = f"Re: {sujet}"
    s = smtplib.SMTP(SMTP, 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(EMAIL, MDP)
    s.send_message(msg)
    s.quit()
    print("✅ Envoyé !")

# ===== LIRE =====
def lire():
    mail = imaplib.IMAP4_SSL(IMAP)
    mail.login(EMAIL, MDP)
    mail.select('inbox')
    statut, msgs = mail.uid('search', None, '(UNSEEN)')
    uids = msgs[0].split()
    for uid in uids:
        statut, data = mail.uid('fetch', uid, '(BODY.PEEK[])')
        raw = data[0][1].decode('utf-8', errors='ignore')
        msg = email.message_from_string(raw)
        corps = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    corps = part.get_payload(decode=True).decode('utf-8', errors='ignore')
                    break
        else:
            corps = msg.get_payload(decode=True).decode('utf-8', errors='ignore')
        print(f"\n📩 De: {msg['From']}\n📎 Sujet: {msg['Subject']}\n📝 {corps[:200]}\n")
        if input("Répondre ? (o/n) : ").lower() == 'o':
            reponse = input("Votre réponse : ")
            envoyer(msg['From'], msg['Subject'], reponse)
    mail.close()
    mail.logout()

# ===== BOUCLE =====
print("📬 Surveille les emails... (Ctrl+C pour quitter)")
while True:
    try:
        lire()
        time.sleep(30)  # Vérifie toutes les 30 secondes
    except KeyboardInterrupt:
        print("\n👋 Bye !")
        break
    except Exception as e:
        print(f"⚠️ Erreur: {e}")
        time.sleep(60)