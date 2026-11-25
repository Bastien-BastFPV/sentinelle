# generer_log.py
# Génère un fichier exemple.log avec des incidents variés.
# À exécuter UNE FOIS par l'enseignant : python generer_log.py

import random
from datetime import datetime, timedelta

# Configuration
NOMBRE_LIGNES = 600
FICHIER_SORTIE = "exemple.log"

# Motifs d'incident que les élèves devront détecter
INCIDENTS = [
    "ERROR Connexion refusée pour user {user}",
    "ERROR Timeout de la base de données après {ms}ms",
    "ERROR Fichier introuvable : /var/log/{fichier}",
    "Failed password for {user} from 192.168.1.{ip}",
    "Failed password for root from 10.0.0.{ip}",
    "timeout waiting for response from {host}",
    "timeout during handshake with {host}",
]

# Lignes normales (bruit de fond)
NORMALES = [
    "INFO Connexion réussie pour user {user}",
    "INFO Fichier {fichier} sauvegardé",
    "INFO Service {service} démarré",
    "INFO Requête traitée en {ms}ms",
    "WARN Utilisation mémoire à {pct}%",
    "WARN Certificat expire dans {jours} jours",
]

USERS = ["admin", "alice", "bob", "root", "webmaster", "backup"]
FICHIERS = ["access.log", "error.log", "auth.log", "syslog", "backup.tar.gz"]
HOSTS = ["db-primary", "db-replica", "cache-01", "api-gateway", "storage-02"]
SERVICES = ["nginx", "postgresql", "redis", "ssh", "cron"]

def generer_ligne(timestamp):
    """Génère une ligne de log, avec ~30% de chance d'être un incident."""
    if random.random() < 0.30:  # 30% d'incidents
        modele = random.choice(INCIDENTS)
    else:
        modele = random.choice(NORMALES)

    return modele.format(
        user=random.choice(USERS),
        ip=random.randint(1, 254),
        ms=random.randint(100, 5000),
        fichier=random.choice(FICHIERS),
        host=random.choice(HOSTS),
        service=random.choice(SERVICES),
        pct=random.randint(60, 99),
        jours=random.randint(1, 30),
    )

def main():
    lignes = []
    # Commencer il y a 2 heures, avancer de quelques secondes à chaque ligne
    timestamp = datetime.now() - timedelta(hours=2)

    for _ in range(NOMBRE_LIGNES):
        # Avancer le temps de 5 à 20 secondes
        timestamp += timedelta(seconds=random.randint(5, 20))
        moment = timestamp.strftime("%Y-%m-%d %H:%M:%S")
        contenu = generer_ligne(timestamp)
        lignes.append(f"{moment} {contenu}")

    with open(FICHIER_SORTIE, "w", encoding="utf-8") as f:
        f.write("\n".join(lignes) + "\n")

    print(f"Fichier '{FICHIER_SORTIE}' généré : {len(lignes)} lignes.")

if __name__ == "__main__":
    main()