function printHello () {
  const userInput = $('#language_code').val();
  if (userInput) {
    const dataURL = 'https://hellosalut.stefanbohacek.dev/?lang=' + userInput;
    $.getJSON(dataURL,
      { format: 'json' }
    )
      .done(function (data) {
        $('div#hello').text(data.hello);
      });
  }
}

$(document).ready(function () {
  // Button clicked
  $('#btn_translate').on('click', function () {
    printHello();
  });
});
