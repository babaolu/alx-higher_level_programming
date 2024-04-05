$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const lang = $('INPUT#language_code').val();
    $.ajax({
      type: 'GET',
      url: 'https://hellosalut.stefanbohacek.dev/?lang=' + lang,
      success: function (result) {
        $('DIV#hello').text(result.hello);
      }
    });
  });
});
