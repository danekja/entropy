$(function () {
    "use strict";
  
    // for better performance - to avoid searching in DOM
    var content = $('#content');
    var input = $('#input');
    var status = $('#status');
  
    // my color assigned by the server
    var myColor = false;
    // my name sent to the server
    var myName = false;
  
    // if user is running mozilla then use it's built-in WebSocket
    window.WebSocket = window.WebSocket || window.MozWebSocket;
  
    // if browser doesn't support WebSocket, just show
    // some notification and exit
    if (!window.WebSocket) {
      content.html($('<p>',
        { text:'Sorry, but your browser doesn\'t support WebSocket.'}
      ));
      input.hide();
      $('span').hide();
      return;
    }
  
    // open connection
    var connection = new WebSocket('ws://127.0.0.1:1337');


    
    /**
     * Send message when user presses Enter key
     */
    input.keydown(function(e) {
      if (e.keyCode === 13) {
        var msg = $(this).val();
        if (!msg) {
          return;
        }
        // send the message as an ordinary text
        connection.send(msg);
        $(this).val('');
  
        // we know that the first message sent from a user their name
        if (myName === false) {
          myName = msg;
        }
      }
    });
  
    /**
     * This method is optional. If the server wasn't able to
     * respond to the in 3 seconds then show some error message 
     * to notify the user that something is wrong.
     */
    setInterval(function() {
      if (connection.readyState !== 1) {
        status.text('Error');
        input.attr('disabled', 'disabled').val(
            'Unable to communicate with the WebSocket server.');
      }
    }, 3000);
  
    /**
     * Add message to the chat window
     */
    function addMessage(author, message, dt) {
      content.prepend('<p><span>'
          + author + '</span> @ ' + (dt.getHours() < 10 ? '0'
          + dt.getHours() : dt.getHours()) + ':'
          + (dt.getMinutes() < 10
            ? '0' + dt.getMinutes() : dt.getMinutes())
          + ': ' + message + '</p>');
    }
  });