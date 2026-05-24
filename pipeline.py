import time
import random
from typing import Callable, Any, Generator

def track_performance(func: Callable[..., Any]) -> Callable[..., Any]:
    """Décorateur mesurant le temps d'exécution d'une fonction de traitement."""
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"\n📢 [LOG] Début d'exécution : {func.__name__}")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"⏱️ [PERF] Tâche complétée en {end_time - start_time:.2f} secondes.")
        return result
    return wrapper

# ⚙️ NOTRE GÉNÉRATEUR (Le flux d'e-mails de support)
def email_streamer(nombre_emails: int) -> Generator[dict[str, str], None, None]:
    """
    Générateur simulant un flux continu d'e-mails de support entrants.
    Utilise 'yield' pour distribuer les e-mails un par un sans surcharger la RAM.
    """
    for i in range(1, nombre_emails + 1):
        # Simulation d'une attente de réception d'e-mail
        time.sleep(0.5) 
        
        # On distribue (yield) l'e-mail actuel sous forme de dictionnaire
        yield {
            "id": f"TICKET-{i:04d}",
            "sujet": f"Panne technique ou anomalie de flux numéro {i}",
            "expediteur": f"utilisateur.{i}@renault-client.com"
        }

@track_performance
def analyze_ticket(ticket: dict[str, str]) -> None:
    """Analyse un ticket unique avec gestion des erreurs intégrée."""
    print(f"📥 Réception du {ticket['id']} de {ticket['expediteur']}")
    print(f"🤖 Analyse du contenu : '{ticket['sujet']}'")
    
    try:
        # Simulation d'une panne d'API aléatoire (1 chance sur 3)
        if random.choice([True, False, False]):
            raise ConnectionError("Timeout de l'API principale du LLM.")
            
        print(f"✅ {ticket['id']} : Analyse complétée par l'IA principale.")
        
    except ConnectionError as error:
        print(f"🚨 [ERROR] {ticket['id']} - Échec : {error}")
        print(f"🔄 [FALLBACK] {ticket['id']} - Traitement réussi par le LLM de secours local.")

# 🚀 POINT D'ENTRÉE DU SYSTEME
if __name__ == "__main__":
    print("🚀 DÉMARRAGE DU PIPELINE DE PRODUCTION EN FLUX CONTINU")
    
    # On initialise notre robinet pour générer 3 e-mails
    flux_tickets = email_streamer(nombre_emails=3)
    
    # On consomme le générateur un par un avec une boucle
    for ticket_entrant in flux_tickets:
        analyze_ticket(ticket_entrant)
        print("-" * 50)
        
    print("\n🏁 FIN DU TRAITEMENT DU FLUX. STATUT NOMINAL.")