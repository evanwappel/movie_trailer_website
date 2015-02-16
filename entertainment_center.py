import fresh_tomatoes
import media

swingers = media.Movie("Swingers",
    "Wannabe actors become regulars in the stylish neo-lounge scene; Trent teaches his friend Mike the unwritten rules of the scene.",
    "http://upload.wikimedia.org/wikipedia/en/9/91/Swingers_ver2.jpg",
    "www.youtube.com/watch?v=zHT2zOnutCA")

i_love_you_man = media.Movie("I Love You Man",
    "Friendless Peter Klaven goes on a series of man-dates to find a Best Man for his wedding.",
    "http://upload.wikimedia.org/wikipedia/en/d/dd/I_love_you%2C_Man.jpg",
    "http://www.youtube.com/watch?v=um5DuTLzw-I")

it_might_get_loud = media.Movie("It Might Get Loud",
    "A documentary on the electric guitar from the point of view of three significant rock musicians: the Edge, Jimmy Page and Jack White.",
    "http://upload.wikimedia.org/wikipedia/en/thumb/b/b9/Itmightgetloud.PNG/320px-Itmightgetloud.PNG",
    "http://www.youtube.com/watch?v=Bo6C6K01PgQ")

sound_city = media.Movie("Sound City",
    "A documentary on the fabled recording studio that was located in Van Nuys, California.",
    "http://upload.wikimedia.org/wikipedia/en/0/0a/Sound-City-poster.png",
    "http://www.youtube.com/watch?v=HQoOfiLz1G4")

crazy_stupid_love = media.Movie("Crazy Stupid Love",
    "A middle-aged husband's life changes dramatically when his wife asks him for a divorce. He seeks to rediscover his manhood with the help of a newfound friend, Jacob, learning to pick up girls at bars.",
    "http://upload.wikimedia.org/wikipedia/en/7/78/CrazyStupidLovePoster.jpg",
    "http://www.youtube.com/watch?v=aDLhjm-0rJQ")

black_hawk_down = media.Movie("Black Hawk Down",
    "123 elite U.S. soldiers drop into Somalia to capture two top lieutenants of a renegade warlord and find themselves in a desperate battle with a large force of heavily-armed Somalis.",
    "http://upload.wikimedia.org/wikipedia/en/0/0c/Black_hawk_down_ver1.jpg",
    "www.youtube.com/watch?v=tnV6wM-vd9s")

movies = [swingers, i_love_you_man, it_might_get_loud, sound_city, crazy_stupid_love, black_hawk_down]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__doc__)
