    
$.ajax({
    type:  "GET",
    url: "https://swapi-api.hbtn.io/api/films/?format=json",
    cache: false,
    success: function (response) {
        response.results.map((movie) => {
            $("#list_movies").append(`<li>${movie.title}</li>`)
        })
    }
});
