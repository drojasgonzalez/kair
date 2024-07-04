from http_requests.get import fetch_user_data, fetch_post_data
from interfaces.users import User
from interfaces.posts import Post
from helpers.database import SessionLocal
from sqlalchemy.orm import Session

def insert_data():
    # Obtener datos de usuarios desde la función fetch_user_data
    users_data = fetch_user_data()

    if not users_data:
        print("No se encontraron datos de usuarios.")
        return

    # Obtener datos de publicaciones desde la función fetch_post_data
    posts_data = fetch_post_data()

    if not posts_data:
        print("No se encontraron datos de publicaciones.")
        return

    # Crear una sesión de SQLAlchemy
    db: Session = SessionLocal()

    try:
        # Recorrer los datos de usuarios y crear instancias de User
        for user_data in users_data:
            user = User(
                user_id=user_data['id'],
                name=user_data['name'],
                username=user_data['username'],
                email=user_data['email'],
                address=str(user_data['address']),
                phone=user_data['phone'],
                website=user_data['website'],
                company=user_data['company']['name']
            )
            db.add(user)

        # Recorrer los datos de publicaciones y crear instancias de Post
        for post_data in posts_data:
            post = Post(
                user_id=post_data['userId'],
                post_id=post_data['id'],
                title=post_data['title'],
                body=post_data['body']
            )
            db.add(post)

        # Confirmar los cambios
        db.commit()

        print("Usuarios y publicaciones insertados correctamente.")

    except Exception as e:
        db.rollback()
        print("Error al insertar datos:", e)

    finally:
        # Cerrar la sesión de SQLAlchemy
        db.close()

# Ejecutar la función para insertar los datos
insert_data()
