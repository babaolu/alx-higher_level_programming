$.ajax({
  type: 'GET',
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  success: function (result) {
    $.each(result.films, function (i, film) {
      $.ajax({
        type: 'GET',
        url: film,
        success: function (movie) {
          $('UL#list_movies').append('<li>' + movie.title + '</li>');
        }
      });
    });
  }
});
