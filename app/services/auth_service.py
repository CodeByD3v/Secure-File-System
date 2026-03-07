from app.models.user_model import User
import bcrypt

def hash_password(password):
    return bcrypt.hashpw(password.encode() , bcrypt.gensalt()).decode()

def register_user(user_data , db):

    if user_data.password != user_data.confirm_password:
        return {"error":"Passwords does not match"}
    
    hashed_password = hash_password(user_data.password)

    new_user = User(
        username = user_data.username,
        email = user_data.email,
        password_hash = hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message":"User registered successfully"}