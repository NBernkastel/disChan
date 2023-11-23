import os
from datetime import datetime, timedelta
from hashlib import scrypt

import jwt
from fastapi import HTTPException
from jwt import encode, decode

from .config import SECRET_KEY


def auth_user(token: str):
    try:
        username = verify_token(token)
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="wrong token")
    return username


def generate_salt():
    return os.urandom(16).hex()


def hash_password(password: str, salt: str, hash_length=64) -> str:
    hashed_password = scrypt(
        password.encode('utf-8'),
        salt=salt.encode('utf-8'),
        n=16384,
        r=8,
        p=1,
        dklen=hash_length
    )
    return hashed_password.hex()


def generate_token(userid: int, del_time: int = 30) -> str:
    """Time in seconds"""
    if not isinstance(userid, int):
        raise ValueError("user.id should be int")
    expiration = datetime.utcnow() + timedelta(hours=del_time)
    payload = {
        'user.id': userid,
        'exp': expiration
    }
    token: str = encode(payload, SECRET_KEY, algorithm='HS256')
    return token


def verification(password: str, pass_hash: str, salt: str) -> bool:
    if hash_password(password, salt) == pass_hash:
        return True
    return False


def verify_token(token: str) -> bool or str:
    try:
        payload = decode(token, SECRET_KEY, algorithms=['HS256'])
        if payload['exp'] < datetime.utcnow().timestamp():
            return False
    except (jwt.DecodeError, jwt.ExpiredSignatureError):
        return False
    return payload['user.id']
