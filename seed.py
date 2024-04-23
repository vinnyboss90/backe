from app import app, db
from models import Authentication, Articles, User, Blog
import datetime

def seed_data():
    with app.app_context():
        
        auth1 = Authentication(name="mbuvijames29@gmail.com", password="1234567890")
        auth2 = Authentication(name="123@gmail.com", password="0987654321")

        # Seed Articles data
        article1 = Articles(title="Title 1", body="Body 1")
        article2 = Articles(title="Title 2", body="Body 2")

        # Seed Users data
        user1 = User(username="user1", image="user1.jpg")
        user2 = User(username="user2", image="user2.jpg")

        # Seed Blogs data
        blog1 = Blog(user=user1, content="Blog content 1")
        blog2 = Blog(user=user2, content="Blog content 2")

        # Add data to the session
        db.session.add(auth1)
        db.session.add(auth2)
        db.session.add(article1)
        db.session.add(article2)
        db.session.add(user1)
        db.session.add(user2)
        db.session.add(blog1)
        db.session.add(blog2)

        # Commit the changes to the database
        db.session.commit()

if __name__ == '__main__':
    seed_data()
