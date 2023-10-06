$(document).ready(function () {
  const dataURL = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  $.getJSON(dataURL,
    { format: 'json' }
  )
    .done(function (data) {
      $('div#hello').text(data.hello);
    });
});
