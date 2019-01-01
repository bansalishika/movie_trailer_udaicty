import fresh_tomatoes
import media

    #import media conects this python file with media.py and fresh_tomatoes import connects it to fresh_tomatoes.py

    # below, the different movies use the class Movie to write the information.

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys which come to lfe ",
                        "https://68.media.tumblr.com/131db9b5de3cbb3e7e1fc60221f2a4b2/tumblr_o30l4bk4Z01qi8pxqo2_1280.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                      "A marine on an alien planet",
                      "http://www.impawards.com/2009/posters/avatar_xlg.jpg",
                      "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

alligant = media.Movie("Alligant",
                      "Third part of divergent dealing with discovery of a new world",
                      "http://www.impawards.com/2016/posters/divergent_series_allegiant_ver17.jpg",
                      "https://www.youtube.com/watch?v=tE8LEPSTK6A")


raabta = media.Movie("Raabta",
                      "Discovering the true love ",
                      "http://www.filmibeat.com/img/2017/04/14-1492148799-raa1.jpg",
                      "https://www.youtube.com/watch?v=YXjYfpqg8Z0")


divergent = media.Movie("Divergent",
                      "Getting to know who divergents are and fighting for the loved ones.",
                      "https://ae01.alicdn.com/kf/HTB1mOehRXXXXXcSXXXXq6xXFXXX4/-font-b-DIVERGENT-b-font-font-b-poster-b-font-Home-Decoration-Wall-font-b.jpg",
                      "https://www.youtube.com/watch?v=sutgWjz10sMhttps://www.youtube.com/watch?v=sutgWjz10sM")


insurgent = media.Movie("Insurgent",
                      "Second part of divergent and the continous fight for the loved ons.",
                      "http://www.heyuguys.com/images/2015/01/Insurgent-Poster.png",
                      "https://www.youtube.com/watch?v=IR-l_TSjlEo")

    # the below code connects fresh_tomatoes to entertainment_center.py . The code helps to connect HTML page to python files.
movies = [toy_story, avatar,alligant,raabta,divergent,insurgent]
fresh_tomatoes.open_movies_page(movies)



print(media.Movie.VALID_RATINGS)
    #print (avatar.storyline)
    #avatar.show_trailer()
