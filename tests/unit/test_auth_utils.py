# tests/unit/test_auth_utils.py

import pytest
from app.auth import validate_credentials

def test_validate_credentials_ok():
    """Doit retourner True pour les bons identifiants."""
    assert validate_credentials('tomsmith', 'SuperSecretPassword!')

def test_validate_credentials_wrong_user():
    """Doit retourner False pour un nom d’utilisateur incorrect."""
    assert not validate_credentials('wronguser', 'SuperSecretPassword!')

def test_validate_credentials_wrong_password():
    """Doit retourner False pour un mot de passe incorrect."""
    assert not validate_credentials('tomsmith', 'wrongpassword')

def test_validate_credentials_empty():
    """Doit retourner False si l’un des champs est vide."""
    assert not validate_credentials('', 'SuperSecretPassword!')
    assert not validate_credentials('tomsmith', '')
