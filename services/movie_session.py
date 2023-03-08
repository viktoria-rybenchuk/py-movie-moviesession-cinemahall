from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> object:
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    movie = Movie.objects.get(id=movie_id)
    movie_session = MovieSession.objects.create(
        show_time=movie_show_time, movie=movie, cinema_hall=cinema_hall
    )
    return movie_session


def get_movies_sessions(
        session_string: str = None
) -> object:
    movie = MovieSession.objects.all()
    if session_string:
        return movie.filter(show_time__date=session_string)
    return movie


def get_movie_session_by_id(
        movie_session_id: int
) -> object:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
    session_id: int,
    cinema_hall_id: int = None,
    show_time: str = None,
    movie_id: int = None,
) -> object:
    movie_session = MovieSession.objects.filter(id=session_id)
    if cinema_hall_id:
        movie_session.update(cinema_hall=cinema_hall_id)
    if show_time:
        movie_session.update(show_time=show_time)
    if movie_id:
        movie_session.update(movie=movie_id)
    return movie_session


def delete_movie_session_by_id(
        session_id: int
) -> object:
    return MovieSession.objects.get(id=session_id).delete()
