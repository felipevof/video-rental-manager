from sqlalchemy import Column, String, Integer, Date, ForeignKey, Float, Boolean

from .base import Base


class Rentable(Base):
    __tablename__ = 'rentables'
    __mapper_args__ = {
        'polymorphic_on': 'rentable_type',
        'polymorphic_identity': 'rentable',
        'with_polymorphic': '*'
    }

    id = Column(Integer, primary_key=True)
    title = Column(String, info={'label': 'Title'})
    description = Column(String, nullable=True, info={'label': 'Description'})
    language = Column(String, info={'label': 'Language'})
    age_restriction = Column(Integer, info={'label': 'Age Restriction'})
    rent_price = Column(Float, info={'label': 'Rent Price'})
    poster_image = Column(String, info={'label': 'Poster Image (URL)'})

    # just for class table inheritance shenanigans
    rentable_type = Column(String(20))

    def __str__(self):
        return self.getTitle()

    def getTitle(self):
        return self.title

    def setTitle(self, value):
        self.title = value

    def getDescription(self):
        return self.description

    def setDescription(self, value):
        self.description = value

    def getLanguage(self):
        return self.language

    def setLanguage(self, value):
        self.language = value

    def getAgeRestriction(self):
        return self.age_restriction

    def setAgeRestriction(self, value):
        self.age_restriction = value

    def getRentPrice(self):
        return self.rent_price

    def setRentPrice(self, value):
        self.rent_price = value

    def getPosterImage(self):
        return self.poster_image

    def setPosterImage(self, value):
        self.poster_image = value

# ---

class SeriesSeason(Rentable):
    __tablename__ = 'series_seasons'
    __mapper_args__ = {'polymorphic_identity': 'series_season'}

    id = Column(Integer, ForeignKey('rentables.id'), primary_key=True)

    season_number = Column(Integer, info={'label': 'Season Number'})
    episode_count = Column(Integer, info={'label': 'Episode Count'})
    episode_duration_minutes = Column(Integer, info={'label': 'Episode Duration Minutes'})
    network = Column(String, nullable=True, info={'label': 'Network'})
    genre = Column(String, info={'label': 'Genre'})

    def getSeasonNumber(self):
        return self.season_number

    def setSeasonNumber(self, value):
        self.season_number = value

    def getEpisodeCount(self):
        return self.episode_count

    def setEpisodeCount(self, value):
        self.episode_count = value

    def getEpisodeDurationMinutes(self):
        return self.episode_duration_minutes

    def setEpisodeDurationMinutes(self, value):
        self.episode_duration_minutes = value

    def getNetwork(self):
        return self.network

    def setNetwork(self, value):
        self.network = value

    def getGenre(self):
        return self.genre

    def setGenre(self, value):
        self.genre = value


class LiveActionSeries(SeriesSeason):
    __tablename__ = 'live_action_series'
    __mapper_args__ = {'polymorphic_identity': 'live_action_series'}

    id = Column(Integer, ForeignKey('rentables.id'), ForeignKey('series_seasons.id'), primary_key=True)

    cast = Column(String, info={'label': 'Cast'})
    director = Column(String, info={'label': 'Director'})
    writer = Column(String, info={'label': 'Writer'})
    emmy_nominee = Column(Boolean, info={'label': 'Emmy Nominee'})
    emmy_winner = Column(Boolean, info={'label': 'Emmy Winner'})

    def getCast(self):
        return self.cast

    def setCast(self, value):
        self.cast = value

    def getDirector(self):
        return self.director

    def setDirector(self, value):
        self.director = value

    def getWriter(self):
        return self.writer

    def setWriter(self, value):
        self.writer = value

    def getEmmyNominee(self):
        return self.emmy_nominee

    def setEmmyNominee(self, value):
        self.emmy_nominee = value

    def getEmmyWinner(self):
        return self.emmy_winner

    def setEmmyWinner(self, value):
        self.emmy_winner = value


class AnimatedSeries(SeriesSeason):
    __tablename__ = 'animated_series'
    __mapper_args__ = {'polymorphic_identity': 'animated_series'}

    id = Column(Integer, ForeignKey('rentables.id'), ForeignKey('series_seasons.id'), primary_key=True)

    animation_studio = Column(String, info={'label': 'Animation Studio'})
    original_author = Column(String, info={'label': 'Original Author'})
    has_2d = Column(Boolean, info={'label': 'Has 2D'})
    has_3d = Column(Boolean, info={'label': 'Has 3D'})
    adult_content = Column(Boolean, info={'label': 'Adult Content'})

    def getAnimationStudio(self):
        return self.animation_studio

    def setAnimationStudio(self, value):
        self.animation_studio = value

    def getOriginalAuthor(self):
        return self.original_author

    def setOriginalAuthor(self, value):
        self.original_author = value

    def getHas2D(self):
        return self.has_2d

    def setHas2D(self, value):
        self.has_2d = value

    def getHas3D(self):
        return self.has_3d

    def setHas3D(self, value):
        self.has_3d = value

    def getAdultContent(self):
        return self.adult_content

    def setAdultContent(self, value):
        self.adult_content = value


class DocumentarySeries(SeriesSeason):
    __tablename__ = 'documentary_series'
    __mapper_args__ = {'polymorphic_identity': 'documentary_series'}

    id = Column(Integer, ForeignKey('rentables.id'), ForeignKey('series_seasons.id'), primary_key=True)

    director = Column(String, info={'label': 'Director'})
    narrator = Column(String, info={'label': 'Narrator'})
    locations = Column(String, info={'label': 'Locations'})
    guests = Column(String, nullable=True, info={'label': 'Guests'})
    low_budget = Column(Boolean, info={'label': 'Low Budget'})

    def getDirector(self):
        return self.director

    def setDirector(self, value):
        self.director = value

    def getNarrator(self):
        return self.narrator

    def setNarrator(self, value):
        self.narrator = value

    def getLocations(self):
        return self.locations

    def setLocations(self, value):
        self.locations = value

    def getGuests(self):
        return self.guests

    def setGuests(self, value):
        self.guests = value

    def getLowBudget(self):
        return self.low_budget

    def setLowBudget(self, value):
        self.low_budget = value

# ---

class FeatureFilm(Rentable):
    __tablename__ = 'feature_films'
    __mapper_args__ = {'polymorphic_identity': 'feature_film'}

    id = Column(Integer, ForeignKey('rentables.id'), primary_key=True)

    duration_minutes = Column(Integer, info={'label': 'Duration Minutes'})
    publisher = Column(String, info={'label': 'Publisher'})
    producer = Column(String, info={'label': 'Producer'})
    release_year = Column(Integer, info={'label': 'Release Year'})
    genre = Column(String, info={'label': 'Genre'})

    def getDurationMinutes(self):
        return self.duration_minutes

    def setDurationMinutes(self, value):
        self.duration_minutes = value

    def getPublisher(self):
        return self.publisher

    def setPublisher(self, value):
        self.publisher = value

    def getProducer(self):
        return self.producer

    def setProducer(self, value):
        self.producer = value

    def getReleaseYear(self):
        return self.release_year

    def setReleaseYear(self, value):
        self.release_year = value

    def getGenre(self):
        return self.genre

    def setGenre(self, value):
        self.genre = value


class StandUpComedySpecial(FeatureFilm):
    __tablename__ = 'stand_up_comedy_specials'
    __mapper_args__ = {'polymorphic_identity': 'stand_up_comedy_special'}

    id = Column(Integer, ForeignKey('rentables.id'), ForeignKey('feature_films.id'), primary_key=True)

    headliner_comedian = Column(String, info={'label': 'Headliner Comedian'})
    opener_comedian = Column(String, nullable=True, info={'label':'Opener Comedian'})
    venue = Column(String, info={'label': 'Venue'})
    offensive_language = Column(Boolean, info={'label': 'Offensive Language'})
    additional_entertainers = Column(String, nullable=True, info={'label': 'Additional Entertainers'})  # some comedians use DJs, bands, etc

    def getHeadlinerComedian(self):
        return self.headliner_comedian

    def setHeadlinerComedian(self, value):
        self.headliner_comedian = value

    def getOpenerComedian(self):
        return self.opener_comedian

    def setOpenerComedian(self, value):
        self.opener_comedian = value

    def getVenue(self):
        return self.venue

    def setVenue(self, value):
        self.venue = value

    def getOffensiveLanguage(self):
        return self.offensive_language

    def setOffensiveLanguage(self, value):
        self.offensive_language = value

    def getAdditionalEntertainers(self):
        return self.additional_entertainers

    def setAdditionalEntertainers(self, value):
        self.additional_entertainers = value


class LiveActionMovie(FeatureFilm):
    __tablename__ = 'live_action_movies'
    __mapper_args__ = {'polymorphic_identity': 'live_action_movie'}

    id = Column(Integer, ForeignKey('rentables.id'), ForeignKey('feature_films.id'), primary_key=True)

    lead = Column(String, nullable=True, info={'label': 'Lead'})
    cast = Column(String, info={'label': 'Cast'})
    director = Column(String, info={'label': 'Director'})
    writer = Column(String, info={'label': 'Writer'})
    oscar_nominee = Column(Boolean, info={'label':'Oscar Nominee'})
    oscar_winner = Column(Boolean, info={'label':'Oscar Winner'})

    def getLead(self):
        return self.lead

    def setLead(self, value):
        self.lead = value

    def getCast(self):
        return self.cast

    def setCast(self, value):
        self.cast = value

    def getDirector(self):
        return self.director

    def setDirector(self, value):
        self.director = value

    def getWriter(self):
        return self.writer

    def setWriter(self, value):
        self.writer = value

    def getOscarNominee(self):
        return self.oscar_nominee

    def setOscarNominee(self, value):
        self.oscar_nominee = value

    def getOscarWinner(self):
        return self.oscar_winner

    def setOscarWinner(self, value):
        self.oscar_winner = value


class AnimatedMovie(FeatureFilm):
    __tablename__ = 'animated_movies'
    __mapper_args__ = {'polymorphic_identity': 'animated_movie'}

    id = Column(Integer, ForeignKey('rentables.id'), ForeignKey('feature_films.id'), primary_key=True)

    animation_studio = Column(String, info={'label': 'Animation Studio'})
    original_author = Column(String, info={'label': 'Original Author'})
    has_2d = Column(Boolean, info={'label': 'Has 2D'})
    has_3d = Column(Boolean, info={'label': 'Has 3D'})
    adult_content = Column(Boolean, info={'label': 'Adult Content'})

    def getAnimationStudio(self):
        return self.animation_studio

    def setAnimationStudio(self, value):
        self.animation_studio = value

    def getOriginalAuthor(self):
        return self.original_author

    def setOriginalAuthor(self, value):
        self.original_author = value

    def getHas2D(self):
        return self.has_2d

    def setHas2D(self, value):
        self.has_2d = value

    def getHas3D(self):
        return self.has_3d

    def setHas3D(self, value):
        self.has_3d = value

    def getAdultContent(self):
        return self.adult_content

    def setAdultContent(self, value):
        self.adult_content = value


class MusicalShow(FeatureFilm):
    __tablename__ = 'musical_shows'
    __mapper_args__ = {'polymorphic_identity': 'musical_show'}

    id = Column(Integer, ForeignKey('rentables.id'), ForeignKey('feature_films.id'), primary_key=True)

    artist = Column(String, info={'label': 'Artist'})
    venue = Column(String, info={'label': 'Venue'})
    live = Column(Boolean, info={'label': 'Live'})
    acoustic = Column(Boolean, info={'label': 'Acoustic'})
    grammy_nominee = Column(Boolean, info={'label': 'Grammy Nominee'})
    grammy_winner = Column(Boolean, info={'label': 'Grammy Winner'})

    def getArtist(self):
        return self.artist

    def setArtist(self, value):
        self.artist = value

    def getVenue(self):
        return self.venue

    def setVenue(self, value):
        self.venue = value

    def getLive(self):
        return self.live

    def setLive(self, value):
        self.live = value

    def getAcoustic(self):
        return self.acoustic

    def setAcoustic(self, value):
        self.acoustic = value

    def getGrammyNominee(self):
        return self.grammy_nominee

    def setGrammyNominee(self, value):
        self.grammy_nominee = value

    def getGrammyWinner(self):
        return self.grammy_winner

    def setGrammyWinner(self, value):
        self.grammy_winner = value


class Documentary(FeatureFilm):
    __tablename__ = 'documentaries'
    __mapper_args__ = {'polymorphic_identity': 'documentary'}

    id = Column(Integer, ForeignKey('rentables.id'), ForeignKey('feature_films.id'), primary_key=True)

    director = Column(String, info={'label': 'Director'})
    narrator = Column(String, info={'label': 'Narrator'})
    locations = Column(String, info={'label': 'Locations'})
    guests = Column(String, nullable=True, info={'label': 'Guests'})
    low_budget = Column(Boolean, info={'label': 'Low Budget'})

    def getDirector(self):
        return self.director

    def setDirector(self, value):
        self.director = value

    def getNarrator(self):
        return self.narrator

    def setNarrator(self, value):
        self.narrator = value

    def getLocations(self):
        return self.locations

    def setLocations(self, value):
        self.locations = value

    def getGuests(self):
        return self.guests

    def setGuests(self, value):
        self.guests = value

    def getLowBudget(self):
        return self.low_budget

    def setLowBudget(self, value):
        self.low_budget = value

# ---

class VideoGame(Rentable):
    __tablename__ = 'video_games'
    __mapper_args__ = {'polymorphic_identity': 'video_game'}

    id = Column(Integer, ForeignKey('rentables.id'), primary_key=True)

    publisher = Column(String, info={'label': 'Publisher'})
    developer = Column(String, info={'label': 'Developer'})
    genre = Column(String, info={'label': 'Genre'})
    platform = Column(String, info={'label': 'Platform'})
    demo = Column(Boolean, info={'label': 'Demo'})
    release_year = Column(Integer, info={'label': 'Release Year'})
    single_player = Column(Boolean, info={'label': 'Single Player'})
    local_multiplayer = Column(Boolean, info={'label': 'Local Multiplayer'})
    online_multiplayer = Column(Boolean, info={'label': 'Online Multiplayer'})
    dlc_included = Column(Boolean, info={'label': 'DLC Included'})

    def getPublisher(self):
        return self.publisher

    def setPublisher(self, value):
        self.publisher = value

    def getDeveloper(self):
        return self.developer

    def setDeveloper(self, value):
        self.developer = value

    def getGenre(self):
        return self.genre

    def setGenre(self, value):
        self.genre = value

    def getPlatform(self):
        return self.platform

    def setPlatform(self, value):
        self.platform = value

    def getDemo(self):
        return self.demo

    def setDemo(self, value):
        self.demo = value

    def getReleaseYear(self):
        return self.release_year

    def setReleaseYear(self, value):
        self.release_year = value

    def getSinglePlayer(self):
        return self.single_player

    def setSinglePlayer(self, value):
        self.single_player = value

    def getLocalMultiplayer(self):
        return self.local_multiplayer

    def setLocalMultiplayer(self, value):
        self.local_multiplayer = value

    def getOnlineMultiplayer(self):
        return self.online_multiplayer

    def setOnlineMultiplayer(self, value):
        self.online_multiplayer = value

    def getDLCIncluded(self):
        return self.dlc_included

    def setDLCIncluded(self, value):
        self.dlc_included = value


class SportsEvent(Rentable):
    __tablename__ = 'sports_events'
    __mapper_args__ = {'polymorphic_identity': 'sports_event'}

    id = Column(Integer, ForeignKey('rentables.id'), primary_key=True)

    network = Column(String, info={'label': 'Network'})
    league = Column(String, info={'label': 'League'})
    championship_phase = Column(String, info={'label': 'Championship Phase'})  # finals, regular season, playoffs, etc
    location = Column(String, info={'label': 'Location'})
    periods = Column(Integer, info={'label': 'Periods'})
    period_duration_minutes = Column(Integer, info={'label': 'Period Duration Minutes'})
    home_team = Column(String, info={'label': 'Home Team'})
    away_team = Column(String, info={'label': 'Awaw Team'})
    home_team_score = Column(Integer, info={'label': 'Home Team Score'})
    away_team_score = Column(Integer, info={'label': 'Away Team Score'})

    def getNetwork(self):
        return self.network

    def setNetwork(self, value):
        self.network = value

    def getLeague(self):
        return self.league

    def setLeague(self, value):
        self.league = value

    def getChampionshipPhase(self):
        return self.championship_phase

    def setChampionshipPhase(self, value):
        self.championship_phase = value

    def getLocation(self):
        return self.location

    def setLocation(self, value):
        self.location = value

    def getPeriods(self):
        return self.periods

    def setPeriods(self, value):
        self.periods = value

    def getPeriodDurationMinutes(self):
        return self.period_duration_minutes

    def setPeriodDurationMinutes(self, value):
        self.period_duration_minutes = value

    def getHomeTeam(self):
        return self.home_team

    def setHomeTeam(self, value):
        self.home_team = value

    def getAwayTeam(self):
        return self.away_team

    def setAwayTeam(self, value):
        self.away_team = value

    def getHomeTeamScore(self):
        return self.home_team_score

    def setHomeTeamScore(self, value):
        self.home_team_score = value

    def getAwayTeamScore(self):
        return self.away_team_score

    def setAwayTeamScore(self, value):
        self.away_team_score = value
