import time
from typing import Callable, Any

def track_performance(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Décorateur mesurant le temps d'exécution d'une fonction de traitement.
    Utile pour monitorer la latence des appels API LLM (OpenAI, Mistral, etc.).
    """
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"\n📢 [LOG] Début d'exécution : {func.__name__}")
        start_time = time.time()
        
        # Exécution de la routine principale
        result = func(*args, **kwargs)
        
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"⏱️ [PERF] Tâche complétée en {execution_time:.2f} secondes.")
        return result
    return wrapper

import random  # On importe random pour simuler une panne aléatoire

@track_performance
def fetch_and_analyze_support_email() -> None:
    """
    Simule la récupération et l'analyse d'un ticket de support par un LLM.
    Intègre une gestion des erreurs (Error Handling) en cas de panne de l'API.
    """
    print("🤖 Connexion à l'API du modèle d'IA principal...")
    time.sleep(1)
    
    try:
        # Simuler une chance sur deux que l'API principale crash (Timeout ou Rate Limit)
        if random.choice([True, False]):
            raise ConnectionError("Le serveur d'IA principal ne répond pas (Timeout 504).")
            
        print("✅ Analyse de l'IA complétée avec succès par le modèle principal.")
        
    except ConnectionError as error:
        # Plan de continuité : On attrape la panne et on bascule sur le modèle de secours
        print(f"🚨 [ERROR] Échec critique : {error}")
        print("🔄 Bascule automatique sur le plan B : Exécution via le modèle de secours local...")
        time.sleep(1)
        print("✅ Analyse complétée avec succès par le modèle de secours.")

# Point d'entrée du script pour test local
if __name__ == "__main__":
    fetch_and_analyze_support_email()