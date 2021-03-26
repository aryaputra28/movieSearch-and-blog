$(document).ready(function () {
    popularMovies();
    $("button").click(function (e) { 
        var pencarian = $("#searchArea").val();
        console.log("SINI = " + pencarian);
        searchMovie(pencarian);
    });
});

searchMovie = (search_value) => {
    $.ajax({
        type: "GET",
        url: 'http://www.omdbapi.com/?apikey=55bd88dc&t=' + search_value,
        data: "json",
        success: function (data) {
            $('#choosenMovie').empty()
            var title = data.Title;
            var release_date = data.Released;
            var genre = data.Genre;
            var director = data.Director;
            var img = data.Poster;
            var result = '<div class="d-flex bookCard" style="padding: 15px; background-color: #3E4D5E; border-radius:20px"><img src=' 
            + img + ' style="margin: 0 30px 0 0"><div style="color: white;"><h3 >'+title+'</h3><h6>' 
            + release_date+ '</h6> <p>' + genre + '</p><p>' + director + '</p> <i onclick="loveFunction(this)" class="far fa-heart"></i> </div>'
            $("#choosenMovie").append(result);
                
        }
    });
}

function popularMovies() {
    $.ajax({
        type: "GET",
        url: 'https://api.themoviedb.org/3/movie/popular?api_key=22c4a45d5b066700924b98bbe6fa507f&language=en-US&page=1',
        data: "json",
        success: function (data) {
            for (var i = 0 ; i < data.results.length ; i++) {
                console.log(data.results[i].original_title);
                
                var title = data.results[i].original_title;
                var release_date = data.results[i].release_date;
                var img = "https://image.tmdb.org/t/p/w500" + data.results[i].backdrop_path
                var overview = data.results[i].overview
                var vote = data.results[i].vote_average;
                var result = '<div class="d-flex bookCard" style="padding: 15px; background-color: #3E4D5E; border-radius:20px; margin-top:10px"><img src=' 
                + img + ' style="margin: 0 30px 0 0"><div style="color: white;"><h3 >'
                + title +'</h3><h6>' + release_date+ '</h6> <p>' + overview + '</p><p>' + vote + '</p> </div>'
                $("#popularMovies").append(result);

            }
        }
    });
}

function loveFunction(x) {
    x.classList.toggle("fas fa-heart")
}