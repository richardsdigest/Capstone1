import requests
from app import db
from models import User, Genre, UserGenre

def fetch_api_data():
    # Example: Replace with actual API endpoint
    api_url = "http://www.omdbapi.com/?i=tt3896198&apikey=22b0e85c"
    response = requests.get(api_url)
    data = response.json()

    # Assuming API returns a JSON list of users with genres
    for user_data in data['users']:
        user = User(username=user_data['username'], password='password', email=user_data['email'])
        db.session.add(user)
        db.session.commit()

        for genre_name in user_data['genres']:
            genre = Genre.query.filter_by(type=genre_name).first()
            if not genre:
                genre = Genre(type=genre_name)
                db.session.add(genre)
                db.session.commit()
            
            user_genre = UserGenre(user_id=user.id, genre_id=genre.id)
            db.session.add(user_genre)
            db.session.commit()

if __name__ == "__main__":
    db.create_all()
    fetch_api_data()
