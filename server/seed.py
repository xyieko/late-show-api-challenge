from server.app import create_app, db
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.user import User
from server.models.appearance import Appearance
from datetime import date

app = create_app()
with app.app_context():
    db.drop_all()
    db.create_all()

    guest = Guest(name="Trevor Noah", occupation="Comedian")
    episode = Episode(date=date(2023, 10, 1), number=1)
    appearance = Appearance(rating=5, guest=guest, episode=episode)

    db.session.add_all([guest, episode, appearance])
    db.session.commit()
    print("Seeded!")