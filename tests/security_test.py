from ..app.core.security import hash_password, verify_password, create_access_token, decode_access_token
from datetime import timedelta


def test_password_hashing_and_verification():
    password = "my_secure_password"
    hashed = hash_password(password)
    assert verify_password(password, hashed) is True
    assert verify_password("wrong_password", hashed) is False


def test_jwt_token_creation_and_decoding():
    data = {"sub": "test_user", "role": "admin", "id": 123}
    expires = timedelta(minutes=15)

    token = create_access_token(data, expires_delta=expires)

    decoded = decode_access_token(token)
    
    assert decoded is not None
    assert decoded.get("sub") == "test_user" 
    assert decoded.get("role") == "admin"
    assert decoded.get("id") == 123


def test_jwt_token_expiration():
    data = {"sub": "test_user"}
    expires = timedelta(seconds=-1)  # Token already expired
    token = create_access_token(data, expires_delta=expires)

    decoded = decode_access_token(token)
    
    assert decoded is None  # Token should be invalid due to expiration


def test_jwt_token_with_invalid_signature():
    data = {"sub": "test_user"}
    token = create_access_token(data)

    invalid_token = token + "tampered"

    decoded = decode_access_token(invalid_token)
    
    assert decoded is None  # Token should be invalid due to signature error  

# Note: These tests assume that the SECRET_KEY and ALGORITHM in the config are set to known values.