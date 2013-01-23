function jsonToUL(data) {    
  if (typeof(data) == 'object') {        
    var ul = $('<ul>');
    for (var i in data) {            
      ul.append($('<li>').text(i).append(jsonToUL(data[i])));
    }        
      return ul;
  } else {       
    var textNode = document.createTextNode(' => ' + data);
    return textNode;
  }
}