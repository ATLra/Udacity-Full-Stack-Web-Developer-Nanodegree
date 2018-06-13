import webbrowser


class Movie():
    """ This class provides a way to store movie-related \
    information using the defined attributes"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_rating, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title                    # Movie Title
        self.rating = movie_rating                  # Movie Rating
        self.storyline = movie_storyline            # Movie Storyline
        self.poster_image_url = poster_image        # Movie Poster Image
        self.trailer_youtube_url = trailer_youtube  # Movie Trailer Link

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
