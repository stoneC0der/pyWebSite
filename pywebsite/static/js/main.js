$(document).ready(function() {
  login();
});

/**
 * Login the user
 */
function login() {
  $('#btnLoginIn').click(function(e) {
    e.preventDefault();
    //    alert('Ok');
    $.ajax({
      method: 'POST',
      url: '/login',
      data: $('#loginForm').serialize(),
      success: function(response) {
        console.log(response.status);
        // $('.content').html(response);
        location.replace('/admin');
      },
      error: function(error) {
        console.log(error.status);
      },
    });
  });
}
