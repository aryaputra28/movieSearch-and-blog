var likes = new Map()
let bookmarked = new Map()

$(document).ready(function () {
    searchMovie("Avengers");
    $(".searchButton").click(function (e) { 
        var pencarian = $("#searchArea").val();
        searchMovie(pencarian);
    });
    $(".likedButton").click(function (e){   
        var lovedMovie = $("#liked").text();
        for (var i = 0 ; i < lovedMovie.length ; i++) {
            lovedMovie = lovedMovie.replace(' ', '%20');
        }
        likedMovie(lovedMovie, likes);
    })
    $(".bookmarkButton").click(function (e) { 
        var bookmarkMovie = $("#liked").text();
        for (var i = 0 ; i < bookmarkMovie.length ; i++) {
            bookmarkMovie = bookmarkMovie.replace(' ', '%20');
        }
        bookedMovie(bookmarkMovie);
    });
});


searchMovie = (search_value) => {
    $.ajax({
        type: "GET",
        url: 'http://www.omdbapi.com/?apikey=55bd88dc&t=' + search_value,
        data: "json",
        success: function (data) {
            $('#choosenMovie').empty()  
            if(data.Response == "True") {
                var title = data.Title;
                var year = data.Year;
                var img = data.Poster;
                var plot = data.Plot;
                var result = '<div class="card" style="width: 18rem;"><img class="card-img-top" src="'+ img+ 
                '" alt="Card image cap"><div class="card-body"><h3 id=liked><b>'+title+'</b></h3><h5><b>'+year+'</b></h5><p class="card-text">'+plot+
                '</p></div></div>'
                $("#choosenMovie").append(result);
            } else {
                $("#choosenMovie").append("<h2>Movie not found</h2>");
            }
                
        }
    });
}

function likedMovie(search_value) {
    $.ajax({
        type: "GET",
        url: 'http://www.omdbapi.com/?apikey=55bd88dc&t=' + search_value,
        data: "json",
        success: function (data) {
            likes.set(data.Title, data);
            returnLikes();
        }
    });
}

function bookedMovie(search_value) {
    $.ajax({
        type: "GET",
        url: 'http://www.omdbapi.com/?apikey=55bd88dc&t=' + search_value,
        data: "json",
        success: function (data) {
            bookmarked.set(data.Title, data);
            returnBook();
        }
    });
}

function returnLikes() {
    console.log("masuk");
    console.log(likes);
    $(".likesClass").empty();
    for (const [key, value] of likes.entries()) {
        var title = value.Title;
        var year = value.Year;
        var plot = value.Plot.substr(0,100)+"...";
        var img = value.Poster;
        var result = '<div class="card col-lg-3 col-md-6 col-sm-12 col-12" style="width: 5rem; margin-top:10px"> <img src="' +img +
        '"class="card-img-top" style="border-radius: 5px; margin-top:5px"><div class="card-body"><h5 class="card-title"><b>' +title + 
        '</b></h5><h6><b>' +year + '</b></h6><p class="card-text">' +plot +'</p></div></div>'
        $(".likesClass").append(result);
    }
}

function returnBook() {
    console.log("masuk");
    console.log(bookmarked);
    $(".bookmarksClass").empty();
    for (const [key, value] of bookmarked.entries()) {
        var title = value.Title;
        var year = value.Year;
        var plot = value.Plot.substr(0,100)+"...";
        var img = value.Poster;
        var result = '<div class="card col-lg-3 col-md-6 col-sm-12 col-12" style="width: 5rem; margin-top:10px"> <img src="' +img +
        '"class="card-img-top" style="border-radius: 5px; margin-top:5px"><div class="card-body"><h5 class="card-title"><b>' +title + 
        '</b></h5><h6><b>' +year + '</b></h6><p class="card-text">' +plot +'</p></div></div>'
        $(".bookmarksClass").append(result  );
    }
}
// function popularMovies() {
//     $.ajax({
//         type: "GET",
//         url: 'https://api.themoviedb.org/3/movie/popular?api_key=22c4a45d5b066700924b98bbe6fa507f&language=en-US&page=1',
//         data: "json",
//         success: function (data) {
//             for (var i = 0 ; i < data.results.length ; i++) {
//                 // console.log(data.results[i].original_title);
                
//                 var title = data.results[i].original_title;
//                 var release_date = data.results[i].release_date;
//                 var img = "https://image.tmdb.org/t/p/w500" + data.results[i].backdrop_path
//                 var overview = data.results[i].overview
//                 var vote = data.results[i].vote_average;
//                 var result = '<div class="d-flex bookCard" style="padding: 15px; background-color: #FFB231; border-radius:20px; margin-top:10px"><img src=' 
//                 + img + ' style="margin: 0 30px 0 0"><div style="color: white;"><h3 >'
//                 + title +'</h3><h6>' + release_date+ '</h6> <p>' + overview + '</p><p>' + vote + '</p></div>'
//                 $("#popularMovies").append(result);

//             }
//         }
//     });
// }

