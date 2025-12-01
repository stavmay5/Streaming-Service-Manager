from abc import ABC, abstractmethod
import functools

# --- חלק א': התשתית (OOP) ---

# 1. יורשים מ-ABC כדי שזה יהיה מופשט באמת
class Content(ABC):
    def __init__(self, title, rating, views):
        self.title = title
        self.rating = rating
        self.views = views

    @abstractmethod
    def play(self):
        pass

class Movie(Content):
    # הבנאי חייב לקבל את *כל* הנתונים
    def __init__(self, title, rating, views, duration):
        # מעבירים לאבא את מה ששייך לו
        super().__init__(title, rating, views)
        self.duration = duration

    def play(self):
        print(f"Playing movie: {self.title}, Duration: {self.duration}m")

class Series(Content):
    def __init__(self, title, rating, views, episodes):
        super().__init__(title, rating, views)
        self.episodes = episodes

    def play(self):
        print(f"Playing series: {self.title}, Episodes: {self.episodes}")


# --- חלק ב': הנתונים ---

# עכשיו אנחנו שולחים את כל הפרמטרים בסדר הנכון
library = [
    Movie("The Matrix", 9.5, 200000, 136),
    Series("Breaking Bad", 9.8, 500000, 62),
    Movie("Sharknado", 3.0, 500, 90),
    Series("Old Show", 6.5, 1000, 10),
    Movie("Inception", 8.8, 150000, 148)
]

# --- חלק ג': הלוגיקה (FP) ---

print("--- 1. Top Rated (> 8.0) ---")
# מסננים וממירים לרשימה כדי שנוכל להדפיס
top_rated = list(filter(lambda c: c.rating > 8.0, library))
for item in top_rated:
    print(item.title)


print("\n--- 2. Movie Marathon (Total Minutes) ---")
# שלב 1: מסננים רק סרטים (isinstance)
only_movies = filter(lambda x: isinstance(x, Movie), library)

# שלב 2: הופכים את הסרטים לרשימה של מספרים (רק הדקות)
movie_minutes = map(lambda m: m.duration, only_movies)

# שלב 3: סוכמים את המספרים
total_time = functools.reduce(lambda a, b: a + b, movie_minutes)
print(f"Total time: {total_time} minutes")


print("\n--- 3. Recommendations ---")
# שלב 1: מסננים רק את הנצפים ביותר
popular = filter(lambda x: x.views > 100000, library)

# שלב 2: הופכים אותם למשפטי המלצה
recommendations = list(map(lambda x: f"MUST WATCH: {x.title}", popular))

for rec in recommendations:
    print(rec)