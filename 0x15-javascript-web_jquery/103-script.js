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
  // ENTER key pressed
  $('input#language_code').keydown(function (event) {
    if (event.which === 13) {
      event.preventDefault();
      printHello();
    }
  });

  // Button clicked
  $('#btn_translate').on('click', function () {
    printHello();
  });
});
