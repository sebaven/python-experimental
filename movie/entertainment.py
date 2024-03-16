from movie import movie
from movie import index

karate_kid = movie.Movie("The Karate Kid", 
                         "The story of a kid learning Karate to defend himself at school.",
                         "https://upload.wikimedia.org/wikipedia/en/a/a9/Karate_kid.jpg",
                         "https://www.youtube.com/watch?v=n7JhKCQnEqQ")

belier_family = movie.Movie("The Bélier Family",
                            "In the Bélier family, sixteen-year-old Paula is an indispensable interpreter for her deaf parents and brother on a daily basis.",
                            "https://upload.wikimedia.org/wikipedia/en/2/23/La_Famille_B%C3%A9lier_%28poster%29.jpg",
                            "https://www.youtube.com/watch?v=tEgw97vpkDM")


leon = movie.Movie("Léon",
                   "The friendship of a hitman and an orphan girl",
                   "https://upload.wikimedia.org/wikipedia/en/0/03/Leon-poster.jpg",
                   "https://www.youtube.com/watch?v=yRABrgRcn5Y")

intouchables = movie.Movie("Intouchables",
                          "The Friendship of a young rebel man and a rich quadriplegic.",
                          "https://upload.wikimedia.org/wikipedia/en/9/93/The_Intouchables.jpg",
                          "https://www.youtube.com/watch?v=R8wUIez--WE")

indiana_jones = movie.Movie("Indiana Jones and the temple of Doom",
                            "Indiana Jones helps an Indian community to recover its sacred stone.",
                            "https://upload.wikimedia.org/wikipedia/en/1/10/Indiana_Jones_and_the_Temple_of_Doom_PosterB.jpg",
                            "https://www.youtube.com/watch?v=5uWBc96vfOo")

wild = movie.Movie("Wild",
                   "A perturbed lady goes hiking the Pacific Crest Trail and find herself.",
                   "https://upload.wikimedia.org/wikipedia/en/3/37/Wild2014Poster.jpg",
                   "https://www.youtube.com/watch?v=MvDT42x_NBk")                       
                          

movies = [karate_kid, belier_family, leon, intouchables, indiana_jones, wild]
index.open_movies_page(movies)