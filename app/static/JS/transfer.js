function thankYou(){
  $.ajax({
    url: "http://" + window.location.hostname + ":5000/thankYou",
    method: "GET",
    dataType: "html",
    success: function(data, textStatus, jqXHR){
      $( "#mainSection" ).html(data);
    }
  });
}
