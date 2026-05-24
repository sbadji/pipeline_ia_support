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

@track_performance
def fetch_and_analyze_support_email() -> None:
    """Simule la récupération et l'analyse d'un ticket de support par un LLM."""
    print("🤖 Requête envoyée au modèle d'IA pour analyse du ticket...")
    time.sleep(2)  # Simulation du délai d'attente de l'API
    print("✅ Analyse de l'IA complétée avec succès.")

# Point d'entrée du script pour test local
if __name__ == "__main__":
    fetch_and_analyze_support_email()