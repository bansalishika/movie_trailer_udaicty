
import webbrowser

class Movie():
	"""
	class movie helps to make instances of different movies without repeating the code.
	This class helps to write information for different movies and show trailer for the same.
	"""

	VALID_RATINGS = ["G", "PG", "PG-13", "R"]
# the above variable includes the valid ratings for any movie.

	"""
	with the help of __init__ function we get to know about valid information for movies.

	"""
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

	"""
	with the help of show_trailer funnction a movie trailer is shown.

	"""




# creates space to write information and details.
