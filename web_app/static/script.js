$(document).ready(function () {

  // API STATUS
  $.getJSON('http://0.0.0.0/status/')
    .done(function (data) {
      console.log('FLASK CONNECTED');
      window.alert('FLASK CONNECTED');
    })
    .fail(function (data) {
      console.log('FLASK NOT REACHABLE');
      window.alert('FLASK NOT REACHABLE');
    });

});
