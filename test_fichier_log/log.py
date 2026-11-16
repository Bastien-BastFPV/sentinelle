fichier = "exemple.log"
num_ligne = 0
nb_error = 0
nb_failed = 0
nb_timeout = 0
nb_warning = 0
nb_info = 0
#verifier les erreurs:
def error_test(ligne, num_ligne):
    global nb_error, nb_warrning, nb_critical
    if "error connexion refusée" in ligne.lower():
        nb_error += 1
        print(f"l.{num_ligne}: {ligne}")
    elif "error timeout de la base de données" in ligne.lower():
        nb_error += 1
        print(f"l.{num_ligne}: {ligne}")
    elif "error fichier introuvable" in ligne.lower():
        nb_error += 1
        print(f"l.{num_ligne}: {ligne}")

#verifier les failed:
def failed_test(ligne, num_ligne):
    global nb_error, nb_warrning, nb_critical
    if "failed password for root" in ligne.lower():
        nb_failed += 1
        print(f"l.{num_ligne}: {ligne}")
    elif "failed password" in ligne.lower():
        nb_failed += 1
        print(f"l.{num_ligne}: {ligne}")

#verifier les timeout:
def timeout_test(ligne, num_ligne):
    global nb_error, nb_warrning, nb_critical
    if "timeout waiting for response" in ligne.lower():
        nb_timeout += 1
        print(f"l.{num_ligne}: {ligne}")
    elif "timeout during handshake" in ligne.lower():
        nb_timeout += 1
        print(f"l.{num_ligne}: {ligne}")

#verifier les warn:
def warn_test(ligne, num_ligne):
    global nb_error, nb_warrning, nb_critical
    if "warn utilisation mémoire" in ligne.lower():
        nb_warning += 1
        print(f"l.{num_ligne}: {ligne}")
    elif "warn certificat expire" in ligne.lower():
        nb_warning += 1
        print(f"l.{num_ligne}: {ligne}")

#verifier les info:
def info_test(ligne, num_ligne):
    global nb_error, nb_warrning, nb_critical
    if "info connexion réussie" in ligne.lower():
        nb_info += 1
        print(f"l.{num_ligne}: {ligne}")
    elif "info fichier" in ligne.lower():
        nb_info += 1
        print(f"l.{num_ligne}: {ligne}")
    elif "info service" in ligne.lower():
        nb_info += 1
        print(f"l.{num_ligne}: {ligne}")
    elif "info requête traitée" in ligne.lower():
        nb_info += 1
        print(f"l.{num_ligne}: {ligne}")

with open("exemple.log", "r", encoding="utf-8") as fichier:
    for ligne in fichier:
        num_ligne += 1
        error_test(ligne, num_ligne)
        failed_test(ligne, num_ligne)
        timeout_test(ligne, num_ligne)
        warn_test(ligne, num_ligne)
        info_test(ligne, num_ligne)


print(f"le fichier contient: {nb_error} erreurs, {nb_warning} warnings")