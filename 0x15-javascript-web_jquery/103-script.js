$(document).ready(function () {
  $('INPUT#btn_translate').click(translate);
  $('INPUT#language_code').keypress(function (event) {
    if (event.which === 13) translate();
  });
});

function translate () {
  const lang = $('INPUT#language_code').val();
  $.ajax({
    type: 'GET',
    url: 'https://hellosalut.stefanbohacek.dev/?lang=' + lang,
    success: function (result) {
      $('DIV#hello').text(result.hello);
    }
  });
}
