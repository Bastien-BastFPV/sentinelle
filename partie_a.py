def appliquer_remise(prix, niveau):
 if niveau == "gold":
  return prix * 0.8
 elif niveau == "silver":
  return prix * 0.9
 elif niveau == "bronze":
  return prix * 0.95
 else:
  return prix

print(f"prix: {appliquer_remise(2, "bronze")}")