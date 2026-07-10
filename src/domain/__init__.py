"""Cœur métier d'Arcanum — python pur.

Règle d'or (ADR-002 §3) : ce paquet n'importe JAMAIS Django, `game` ni
`config`. La frontière est vérifiée par import-linter (ticket #30) et par
le test d'architecture `tests/domain/test_architecture.py`.
"""
