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
    
    res.render('index');

});

app.post('/process', function(req, res){

    session.formData = req.body;
    console.log(req.body);
    res.redirect('/result');
});
app.get('/result', function(req, res){

    context = {
        "name": session.formData.your_name,
        "location": session.formData.dojo_location,
        "lang": session.formData.favorite_lang,
        "comment": session.formData.comments
    }
    res.render('result', context);
})

app.listen(8000, function(){
    console.log('listening on port 8000');
});