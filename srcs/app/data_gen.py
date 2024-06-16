import os
import django
from PIL import Image

# Définir la variable d'environnement DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_basic_app.settings')

# Initialiser Django
django.setup()

from data_generation.user_factory import UserFactory
from data_generation.match_factory import MatchFactory, fill_match

def main():
	# UserFactory.create()
	users = UserFactory.create_batch(20)
	matchs = MatchFactory.create_batch(60)
	for match in matchs:
		fill_match(match)
	# print(users)
	# match = MatchFactory.create()
	# print(match)
	# match = MatchFactory.create()
	# fill_match(match, 4)

if __name__ == '__main__':
	main()
