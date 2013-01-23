//Backbone.emulateHTTP = true; // Use _method parameter rather than using DELETE and PUT methods
//Backbone.emulateJSON = true; // Send data to server via parameter rather than via request content

var Deploy = Backbone.Model.extend({
  initialize: function() {
    this.on('all', function(e) { console.log(this.get('number') + " event: " + e); });
  },
  defaults: {
    number: 'undefined',
    url: 'undefined'
  },
  urlRoot: "js/mockdata/buildlist.txt"
  /*url: function() {
    var base = this.urlRoot || (this.collection && this.collection.url) || "/";
    if (this.isNew()) return base;
      return base + "?id=" + encodeURIComponent(this.id);
  }*/
});

/*
var deploy = new Deploy({id:1});
deploy.fetch(); // fetch model from DB with id = 1
 
deploy = new Deploy({number:"Joe Zim", url:23});
deploy.save(); // create and save a new model on the server, also get id back and set it
 
deploy = new Deploy({id:1, number:"Joe Zim", url:23});
deploy.save(); // update the model on the server (it has an id set, therefore it is on the server already)
deploy.destroy(): // delete the model from the server
*/
var Deploys = Backbone.Collection.extend({
  initialize: function() {
    this.on('all', function(e) { console.log("Deploy event: " + e); });
  },
  model: Deploy,
  parse: function(response){
    return response.builds;
  },
  url: "js/mockdata/buildlist.txt"
});

var deploys = new Deploys();
deploys.fetch({success: function() {
  //alert(JSON.stringify(deploys.at(1)))
}}); 
//fetch({success: function(){view.render();}});

//alert(JSON.stringify(deploys.at(1)));
//deploys.create({number:"Joe Zim", url:23}); // Create model, add to Collection and add to DB
//deploys.create({id:6, number:"Chuck Norris", url:72}); // Update model: add to Collection, update DB