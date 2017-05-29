import fresh_tomatoes
import media

# An instance of a class!
# Below are the six movies with the information starting from title to raiting.
star_wars_ep_5 = media.Movie("Star Wars EP 5",
                     "The adventure continues in this Star Wars sequel.",
                     "https://images-na.ssl-images-amazon.com/images"
                     "/I/51C0cpp4d%2BL._AC_UL320_SR208,320_.jpg",
                     "https://www.youtube.com/watch?v=SSfactF_SDo",
                     "PG")

iorn_giant = media.Movie("Iorn Giant",
                     "A story of a boy who friends a giant robot",
                     "http://www.impawards.com/1999"
                     "/posters/iron_giant_ver1.jpg",
                     "https://www.youtube.com/watch?v=xzK8ut_6ZQE",
                     "PG")

the_incredibles = media.Movie("The Incredibles",
                     "A family of superheros",
                     "http://www.impawards.com/2004/posters/incredibles.jpg",
                     "https://www.youtube.com/watch?v=eZbzbC9285I",
                     "G")

the_grand_budapest_hotel = media.Movie(
                     "The Grand Budapest Hotel",
                     "A legendary concierge at a famous"
                     "European hotel between the wars",
                     "http://cdni.condenast.co.uk/1280x1920/g_j"
                     "/Grand-Budapest-Hotel-poster-Vogue-8Jan15-pr_b.jpg",
                     "https://www.youtube.com/watch?v=1Fg5iWmQjwk",
                     "R")

battle_los_angles = media.Movie("Battle: Los Angeles",
                     "Marines counter an alien attack on Los Angeles",
                     "http://www.thaimokit.com/photo/Poster"
                     "/Movie/SP-UF0137-bi-Battle-Los-Angeles.jpg",
                     "https://www.youtube.com/watch?v=-Pd-uuDi28U",
                     "PG-13")

back_to_the_future = media.Movie("Back To The Future",
                     "Teenager is sent 30 years into the past",
                     "https://images-na.ssl-images-amazon.com"
                     "/images/I/51a3mzh6ymL.jpg",
                     "https://www.youtube.com/watch?v=qvsgGtivCgs",
                     "PG")

movies = [star_wars_ep_5, iorn_giant, the_incredibles,
the_grand_budapest_hotel, battle_los_angles, back_to_the_future]
fresh_tomatoes.open_movies_page(movies)
