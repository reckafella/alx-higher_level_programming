const dataURL = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

$.getJSON(dataURL,
  { format: 'json' }
)
  .done(function (data) {
    $('div#character').text(data.name);
  });
