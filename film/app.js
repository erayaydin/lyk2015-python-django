/**
 * Movie Model
 *
 * @param name
 * @param year
 * @param characters
 * @param director
 * @constructor
 */

var Movie = function(name, year, characters, director) {
    this.name       = name;
    this.year       = year;
    this.director   = director;
    this.characters = characters;

    this.watched = false;
};

Movie.prototype.getName = function() {
    return this.name;
};

Movie.prototype.setName = function(name) {
    this.name = name;
};

Movie.prototype.getYear = function() {
    return this.year;
};

Movie.prototype.setYear = function(year) {
    this.year = year;
};

Movie.prototype.getDirector = function() {
    return this.director;
};

Movie.prototype.setDirector = function(director) {
    this.director = director;
};

Movie.prototype.getWatched = function() {
    return this.watched;
};

Movie.prototype.setWatched = function(status) {
    this.watched = status;
};

/**
 * Character Model
 *
 * @param name
 * @param actor
 * @constructor
 */

var Character = function(name, actor) {
    this.name  = name;
    this.actor = actor;
};

Character.prototype.getName = function() {
    return this.name;
};

Character.prototype.setName = function(name) {
    this.name = name;
};

Character.prototype.getActor = function() {
    return this.actor;
};

Character.prototype.setActor = function(actor) {
    this.actor = actor;
};

/**
 * Actor Model
 *
 * @param firstname
 * @param surname
 * @param country
 * @param birthday
 * @constructor
 */

var Actor = function(firstname, surname, country, birthday) {
    this.firstname = firstname;
    this.surname   = surname;
    this.country   = country;
    this.birthday  = birthday;
};

Actor.prototype.getFirstname = function() {
    return this.firstname;
};

Actor.prototype.setFirstname = function(firstname) {
    this.firstname = firstname;
};

Actor.prototype.getSurname = function() {
    return this.surname;
};

Actor.prototype.setSurname = function(surname) {
    this.surname = surname;
};

Actor.prototype.getCountry = function() {
    return this.country;
};

Actor.prototype.setCountry = function(country) {
    this.country = country;
};

Actor.prototype.getBirthday = function() {
    return this.birthday;
};

Actor.prototype.setBirthday = function(birthday) {
    this.birthday = birthday;
};

/**
 * Director Model
 *
 * @param firstname
 * @param surname
 * @param country
 * @param birthday
 * @constructor
 */

var Director = function(firstname, surname, country, birthday) {
    this.firstname = firstname;
    this.surname   = surname;
    this.country   = country;
    this.birthday  = birthday;
};

Director.prototype.getFirstname = function() {
    return this.firstname;
};

Director.prototype.setFirstname = function(firstname) {
    this.firstname = firstname;
};

Director.prototype.getSurname = function() {
    return this.surname;
};

Director.prototype.setSurname = function(surname) {
    this.surname = surname;
};

Director.prototype.getCountry = function() {
    return this.country;
};

Director.prototype.setCountry = function(country) {
    this.country = country;
};

Director.prototype.getBirthday = function() {
    return this.birthday;
};

Director.prototype.setBirthday = function(birthday) {
    this.birthday = birthday;
};

/**
 * Category Model
 *
 * @param name
 * @constructor
 */
var Category = function(name) {
    this.name = name;
};

Category.prototype.getName = function() {
    return this.name;
};

Category.prototype.setName = function(name) {
    this.name = name;
};

/**
 * MovieList Model
 *
 * @constructor
 */
var MovieList = function() {
    this.movies = [];
};

MovieList.prototype.addMovie = function(movie) {
    this.movies.push(movie);
};

MovieList.prototype.getMovies = function() {
    return this.movies;
};

MovieList.prototype.watchedMovies = function() {
    var watched = [];

    for(i=0;i<this.movies.length;i++) {
        if(this.movies[i].watched) {
            watched.push(this.movies[i]);
        }
    }

    return watched;
};

MovieList.prototype.notWatchedMovies = function() {
    var notWatched = [];

    for(i=0;i<=this.movies.length;i++) {
        if(this.movies[i].watched) {
            notWatched.push(this.movies[i]);
        }
    }

    return notWatched;
};

/** CONTENT **/
var francisfordcoppola = new Director("Francis Ford", "Coppola", "Italia", 1939);
var christophernolan   = new Director("Christopher", "Nolan", "UK", 1970);

var marlonbrando  = new Actor("Marlon", "Brando", "USA", 1924);
var alpacino      = new Actor("Al", "Pacino", "USA", 1940);
var jamescaan     = new Actor("James", "Caan", "USA", 1940);
var christianbale = new Actor("Christian", "Bale", "UK", 1974);
var heathledger   = new Actor("Heath", "Ledger", "Australia", 1979);
var aaroneckhart  = new Actor("Aaron", "Eckhart", "USA", 1968);

var godfather = new Movie("The Godfather", 1972, [
    {
        name: "Don Vito Corleone",
        actor: marlonbrando
    },
    {
        name: "Michael Corleone",
        actor: alpacino
    },
    {
        name: "Sonny Corleone",
        actor: jamescaan
    }
], francisfordcoppola);
var thedarkknight = new Movie("The Dark Knight", 2008, [
    {
        name: "Bruce Wayne",
        actor: christianbale
    },
    {
        name: "Joker",
        actor: heathledger
    },
    {
        name: "Harvey Dent",
        actor: aaroneckhart
    }
], christophernolan);
/** CONTENT END **/

var movielist = new MovieList();
movielist.addMovie(godfather);
movielist.addMovie(thedarkknight);

godfather.watched = true;
//thedarkknight.watched = true;
console.log(movielist.watchedMovies());