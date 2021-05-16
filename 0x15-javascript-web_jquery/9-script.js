$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    cache: false,
    success: function (response) {
      $('#hello').text(response.hello);
    }
  });
});
