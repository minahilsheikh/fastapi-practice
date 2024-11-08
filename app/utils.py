from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str): 
    return pwd_context.hash(password)

def verify(plain_password, hashed_password): 
    try: 
        print(f"Plain password: {plain_password}")
        print(f"Hashed password: {hashed_password}")
        return pwd_context.verify(plain_password, hashed_password)
    
    except:
        print("Error: The provided hash could not be identified")
        return False
