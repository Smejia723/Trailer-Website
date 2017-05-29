import webbrowser

# class = blueprint that have data and methods
class Movie():
    """ This class provides a way to store movie related information"""
    
    # constructor this is the init method and analyze the data.
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube, valid_ratings):
        # the four below are instance variables
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.valid_ratings = valid_ratings 

    # instance methods!
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
 
