from datetime import datetime
import test_fichier_log

moment = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

resultats = {
    "ERROR": test_fichier_log.nb_error,
    "Failed password": test_fichier_log.nb_failed,
    "timeout": test_fichier_log.nb_timeout,
    "WARNING": test_fichier_log.nb_warning,
    "INFO": test_fichier_log.nb_info
}

with open("rapport.txt", "w", encoding="utf-8") as fichier:
    for motif, nombre in resultats.items():
        fichier.write(f"[{moment}] {motif} : {nombre} occurrence(s)\n")
        print(f"[{moment}] {motif} : {nombre} occurrence(s)\n")

print("Rapport écrit dans rapport.txt")