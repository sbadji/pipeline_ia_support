import time

# Voici notre papier cadeau (Décorateur)
def chronometrer(fonction_originale):
    def enveloppe(*args, **kwargs):
        print(f"\n📢 [LOG] Démarrage de la tâche : {fonction_originale.__name__}")
        temps_debut = time.time()
        
        # Ici, on laisse la vraie fonction s'exécuter
        resultat = fonction_originale(*args, **kwargs)
        
        temps_fin = time.time()
        print(f"⏱️ Fin de la tâche. Durée : {temps_fin - temps_debut:.2f} secondes")
        return resultat
    return enveloppe

# Testons-le sur une fausse fonction d'IA qui prend du temps
@chronometrer
def appeler_ia_support():
    print("🤖 L'IA est en train d'analyser l'email de panne...")
    time.sleep(2) # On simule une attente de 2 secondes
    print("✅ Analyse terminée !")

# On lance le test
appeler_ia_support()