import jwt
from datetime import datetime, timedelta,timezone

def create_jwt_token(payload):
    # Your secret key (guard it with your life!)
    secret_key = 'supersecretkey'
    # Algorithm for token generation
    algorithm = 'HS256'
    token = jwt.encode(payload, secret_key, algorithm=algorithm)
    return token

def main():
    payload = {
        'user_id': 777,
        'username': 'tom',
        'role': 'mouse_catcher',
        'exp': datetime.now(timezone.utc) + timedelta(hours=1) # Token will expire in 1 hour
    }
    print("JWT TOKEN: ", create_jwt_token(payload))

if __name__ == "__main__":
    main()