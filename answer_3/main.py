from http_requests.get import fetch_user_data
from interfaces.users import User
from helpers.database import SessionLocal
from sqlalchemy.orm import Session

def insert_data():
    # Obtener datos de usuarios desde la función fetch_user_data
    users_data = fetch_user_data()

    if not users_data:
        print("No se encontraron datos de usuarios.")
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
        # Confirmar los cambios
        db.commit()

        print("Usuarios insertados correctamente.")

    except Exception as e:
        print("Error al insertar usuarios:", e)

    finally:
        # Cerrar la sesión de SQLAlchemy
        db.close()

insertar_usuarios()
