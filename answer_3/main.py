from http_requests.get import fetch_user_data, fetch_post_data
from interfaces.users import User
from interfaces.posts import Post
from helpers.database import SessionLocal
from sqlalchemy.orm import Session

def insert_data():
    #! API USE 
    users_data = fetch_user_data()

    if not users_data:
        print("No se encontraron datos de usuarios.")
        return

    #! API USE 
    posts_data = fetch_post_data()

    if not posts_data:
        print("No se encontraron datos de publicaciones.")
        return

    # Crear una sesión de SQLAlchemy
    db: Session = SessionLocal()

    try:
        # Recorremos los datos de usuarios y crear instancias de User usando el método de clase
        for user_data in users_data:
            user = User.from_dict(user_data)
            db.add(user)

        # Recorremos los datos de publicaciones y creamos en base a método de la clase 
        for post_data in posts_data:
            post = Post.from_dict(post_data)
            db.add(post)

        # Confirmar los cambios
        db.commit()

        print("Usuarios y publicaciones insertados correctamente.")

    except Exception as e:
        db.rollback()
        print("Error al insertar datos:", e)

    finally:
        db.close()

# Execute  
insert_data()
