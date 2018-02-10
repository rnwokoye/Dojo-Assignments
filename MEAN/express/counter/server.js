var express = require('express');
var app = express();
var session = require('express-session');

// to require body parser
var bodyParser = require('body-parser');

// app.HTTP_VERB('URL', function(req, res){}); 

app.use(express.static(__dirname + "/static"));

app.use(session({
    secret: 'codingdojoDCKey',
    proxy: true,
    resave: false,
    saveUninitialized: true
}));

//use body-parser
app.use(bodyParser.urlencoded({extended: true}));


app.set('views', __dirname + '/views');

app.set('view engine', 'ejs');


app.get('/', function(req, res){
    if (session.count == undefined){
        session.count = 1; 
    }
    else {
        session.count ++; 
    }
    res.render('index', {'count' : session.count});
});

app.post('/add2', function(req, res){
    session.count += 1;
    res.redirect('/');
});

app.post('/reset', function(req, res){
    session.count = 0; 
    res.redirect('/');
});

app.listen(8000, function(){
    console.log('listening on port 8000');
});