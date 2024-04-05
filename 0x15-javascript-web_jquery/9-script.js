$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    success: function (result) {
      $('DIV#hello').text(result.hello);
    }
  });
});
