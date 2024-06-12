from django.test import TestCase
from django.utils import timezone
from fahrten.models import Pfadfinderfahrt


class PfadfinderfahrtModelTest(TestCase):
    def setUp(self):
        self.fahrt = Pfadfinderfahrt.objects.create(
            titel="Sommerlager",
            ziel="Schwarzwald",
            start_zeit=timezone.now(),
            end_zeit=timezone.now() + timezone.timedelta(days=7),
            start_ort="Berlin",
            end_ort="Berlin",
            beschreibung="Lagerfeuer und Wanderungen",
            motto="Gemeinsam Abenteuer erleben",
        )

    def test_fahrt_erstellen(self):
        """Test, ob eine Fahrt korrekt erstellt werden kann."""
        self.assertEqual(self.fahrt.titel, "Sommerlager")
        self.assertEqual(self.fahrt.ziel, "Schwarzwald")
        self.assertTrue(self.fahrt.start_zeit < self.fahrt.end_zeit)
        self.assertEqual(self.fahrt.start_ort, "Berlin")
        self.assertEqual(self.fahrt.end_ort, "Berlin")
        self.assertEqual(self.fahrt.beschreibung, "Lagerfeuer und Wanderungen")
        self.assertEqual(self.fahrt.motto, "Gemeinsam Abenteuer erleben")

    def test_string_darstellung(self):
        """Test, ob die __str__-Methode des Modells korrekt funktioniert."""
        erwartete_darstellung = f"Pfadfinderfahrt: {self.fahrt.titel} ({self.fahrt.start_zeit.strftime('%Y-%m-%d')})"
        self.assertEqual(str(self.fahrt), erwartete_darstellung)

    def test_ziel_und_motto_optional(self):
        """Test, ob Ziel und Motto optional sind."""
        fahrt_ohne_ziel_und_motto = Pfadfinderfahrt.objects.create(
            titel="Testfahrt",
            start_zeit=timezone.now(),
            end_zeit=timezone.now() + timezone.timedelta(days=3),
            start_ort="München",
            end_ort="München",
        )
        self.assertIsNone(fahrt_ohne_ziel_und_motto.ziel)
        self.assertIsNone(fahrt_ohne_ziel_und_motto.motto)
