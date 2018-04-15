
function getContent(){
  $.ajax({
    url: "http://" + window.location.hostname + ":5000/determine-if-leader",
    method: "GET",
    dataType: "html",
    success: function(data, textStatus, jqXHR){
      $( "#mainSection" ).html(data);
    }
  });
}
