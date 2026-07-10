"""Garde-fou d'architecture : domain/ doit rester du python pur (ADR-002 §3).

Ces tests tournent sans base de données. La vérification exhaustive des
frontières d'import est faite par import-linter (ticket #30) ; ce test est
le filet minimal exécutable dès la Phase 0.
"""

import subprocess
import sys


def test_importer_domain_ne_charge_pas_django() -> None:
    code = (
        "import sys, domain; "
        "offenders = [m for m in sys.modules "
        "if m == 'django' or m.startswith('django.')]; "
        "sys.exit(1 if offenders else 0)"
    )
    result = subprocess.run(
        [sys.executable, "-c", code],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
