function sendreq(){

}

document.addEventListener('DOMContentLoaded',() => {

  document.querySelector('#form').onsubmit = () () => {
    document.querySelector('#search_list').innerHTML="";

    // Initialize new request
    const request = new XMLHttpRequest();
    const search_query = document.querySelector('#form').value;
    request.open('POST', '/search');

    // Callback function for when request completes
    request.onload = () = {

      // Extract JSON data from XMLHttpRequest
      const data = Json.parse(request.responseText);

      // Update the result div
      if (data.success) {
        for(var i = 0; i<data.tweets.length; i++){
          const li = document.createElement('li');
          const p = document.createElement('p');
          // li.innerHTML = data.tweets[i][0]
          p.innerHTML = data.tweets[i][0]
          li.append(p)
          document.querySelector('#search_list').append(li);
        }
      }
    }
  }
})
