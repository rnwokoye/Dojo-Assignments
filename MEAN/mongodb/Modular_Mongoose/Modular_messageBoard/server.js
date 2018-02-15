var express = require('express'),
    path = require('path'),
    session = require('express-session'),
    bodyParser = require('body-parser'),
    mongoose = require('mongoose'),
    app = express(),
    port = 8000;


app.use(express.static( path.join(__dirname, "./client/static") ));
app.use(bodyParser.urlencoded({extended: true}));
app.set('views', path.join(__dirname, './client/views'));
app.set('view engine', 'ejs');


require("./server/config/mongoose.js");
require("./server/config/routes.js")(app);



app.listen(port, function(){
    console.log(`listening on port ${port}`);
});
