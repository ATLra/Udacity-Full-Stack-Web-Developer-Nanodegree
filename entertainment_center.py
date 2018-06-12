import fresh_tomatoes
import media

trainspotting = media.Movie("Trainspotting",
                            "R",
                            "Heroin addict Mark Renton stumbles through bad ideas and sobriety attempts with his unreliable friends",   # NOQA
                            "https://bit.ly/2HE2u0H",
                            "https://youtu.be/8LuxOYIpu-I")
heathers = media.Movie("Heathers",
                       "R",
                       "Best friends, social trends and occasional murder.",    # NOQA  
                       "https://bit.ly/2sKhdTw",
                       "https://www.youtube.com/watch?v=v5gHF3FNr78")
metropolis = media.Movie("Metropolis",
                         "PG",
                         "A futuristic city sharply divided between the working class and the city planners",   # NOQA
                         "https://bit.ly/2l3luwY",
                         "https://www.youtube.com/watch?v=on2H8Qt5fgA")
seven_brides = media.Movie("Seven Brides for Seven Brothers",
                           "G",
                           "When an Oregon trapper decides to marry, his six rowdy brothers aim to follow suit",    # NOQA
                           "https://bit.ly/2JtL6Sn",
                           "https://www.youtube.com/watch?v=W7IGzNUDZlg")
glengarry_glen_ross = media.Movie("Glengarry Glen Ross",
                                  "R",
                                  "An examination of the machinations behind the scenes at a real estate office",   # NOQA
                                  "https://bit.ly/2MfkT7N",
                                  "https://www.youtube.com/watch?v=QgAU2RJHfvE")
taxi_driver = media.Movie("Taxi Driver",
                          "R",
                          "Disturbed loner Travis Bickle takes a job as a New York City cabbie",    # NOQA
                          "https://bit.ly/2JsNSr0",
                          "https://www.youtube.com/watch?v=sLpMx8_TYOo")

movies = [trainspotting, heathers, metropolis, seven_brides, glengarry_glen_ross, taxi_driver]
fresh_tomatoes.open_movies_page(movies)
