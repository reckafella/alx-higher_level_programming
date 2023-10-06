$(document).ready(function () {
  const dataURL = 'https://swapi-api.alx-tools.com/api/films/?format=json';

  $.getJSON(dataURL,
    { format: 'json' }
  )
    .done(function (data) {
      for (let index = 0; index < data.results.length; index++) {
        $('ul#list_movies').append('<li>' + data.results[index].title + '</li>');
      }
    });
});
