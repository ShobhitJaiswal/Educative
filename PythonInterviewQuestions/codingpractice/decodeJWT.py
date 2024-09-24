import jwt

def validate_jwt_token(token_to_validate):
    secret_key = 'supersecretkey'
    algorithm = 'HS256'
    try:
        decoded_payload = jwt.decode(token_to_validate, secret_key, algorithms=[algorithm])
        return decoded_payload
    except jwt.ExpiredSignatureError:
        print("Token has expired. Please log in again.")
    except jwt.InvalidTokenError:
        print("Invalid token. Access denied.")
    return None

def main():
    token_to_validate = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo3NzcsInVzZXJuYW1lIjoidG9tIiwicm9sZSI6Im1vdXNlX2NhdGNoZXIiLCJleHAiOjE3MjQxNzc4MjJ9.UNxYIGgB3Y8Nw7LkoJVWJHhomjjHn63ZylL2k5ZYvGQ'
    # Validate and decode the token
    decoded_payload = validate_jwt_token(token_to_validate)
    if decoded_payload:
        # If the decoding is successful, you can trust the token!
        print("Decoded Payload:", decoded_payload)

if __name__ == "__main__":
    main()