from http_requests.get import  fetch_post_data, fetch_user_data
from interfaces.users import User  # Clase User  | interface layer
from interfaces.post import Post # Clase Post | interface layer


# test
results1 = fetch_user_data()
print(f'  USER?? {results1}') 
results2 = fetch_post_data()
print(f' POST?? {results2}') 