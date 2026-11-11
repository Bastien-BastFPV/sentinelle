import sys
import platform
import datetime
print("")
print("===================================================")
print("VERIFICATION DE L'INSTALLATiON PYTHON")
print("===================================================")
print("")
print("[1] Version de Python")
if sys.version_info.major == 3:
    print(f"    python {sys.version_info.major}.{sys.version_info.minor} détecté - OK")
else:
    print(f"    python {sys.version_info.major}.{sys.version_info.minor} détecté - Mauvaise version")
print("")
print("[2] interpréteur utilisé")
print(f"    {sys.executable}")
print("")
print("[3] Système d'exploitation")
print(f"    {platform.system()} {platform.release()} ({platform.machine()})")
print("")
print("[4] date et heure d'exploitation")
print(f"    {datetime.datetime.now().strftime("%d.%m.%Y à %H:%M:%S")}") #utilisation de l'ia sur cette ligne
print("")
print("test de calcul")
somme = 0;
for k in range(11):
    somme = somme + k
print(f"    somme des nombres de 1 à 10 = {somme}")
print("")
print("===================================================")
if (sys.version_info.major == 3 and somme == 55):
    print(" RESULTAT: Installation OK - tu peux continuer")
else:
    print(" RESULTAT: Installation pas OK - tu peux pas continuer.")
print("===================================================")