""" Generate random secure token of 64 bytes and random URL """
import secrets
print(secrets.token_bytes(64))
print(secrets.token_urlsafe(64))