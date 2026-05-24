import unittest
from pipeline import analyze_ticket

class TestPipelineIA(unittest.TestCase):
    """Fiche de test unitaire pour valider les composants du pipeline."""

    def test_analyze_ticket_execution(self) -> None:
        """Vérifie qu'un ticket standard est traité sans lever d'exception."""
        ticket_test = {
            "id": "TICKET-TEST",
            "sujet": "Test unitaire du pipeline CI/CD",
            "expediteur": "test@renault.com"
        }
        
        # Le test passe si la fonction s'exécute jusqu'au bout sans crasher
        try:
            analyze_ticket(ticket_test)
            execution_valide = True
        except Exception:
            execution_valide = False
            
        self.assertTrue(execution_valide, "L'analyse du ticket a généré une erreur critique non gérée.")

if __name__ == "__main__":
    unittest.main()