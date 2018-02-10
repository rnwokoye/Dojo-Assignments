var express = require('express');
var app = express();
var session = require('express-session');

// to require body parser
var bodyParser = require('body-parser');

// app.HTTP_VERB('URL', function(req, res){}); 

console.log(__dirname);
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


app.get('/testing', function(req, res){
    res.send('<h1>Hello Express</h1>');
});

//route to process new user form data
app.post('/success', function(req, res){

    //store form info into session
    session.form_info = req.body;

    //this console logs the post data 
    console.log("POST DATA \n\n", req.body)
    //code to add user to db goes here.
    // this shows about session
    req.session.name = req.body.name;
    req.session.email = req.body.email;
    console.log(req.session.name);

    //redirect the user to index
    res.redirect('/success')
});
app.get('/success', function(req, res){

    // console.log(session.name);
    context = {
        'first_name': session.form_info.name,
        'email': session.form_info.email
    }
    res.render('success', context);
});

app.get("user/:id", function(req, res){
    //this gets the form data onto our url as a get request, using req.params.id
    console.log('The user id requested is: ', req.params.id);

    res.send("You request the user with id: " + req.params.id);
});

app.get('/', function(req, res){
    // console.log("***************************")
    // console.log(req);
    res.render('index', {title: "my Express project"});

});
app.get("/users", function(req, res){
    var users_array = [
        {name: "Michael", email: "michael@codingdojo.com"}, 
        {name: "Jay", email: "jay@codingdojo.com"}, 
        {name: "Brendan", email: "brendan@codingdojo.com"}, 
        {name: "Andrew", email: "andrew@codingdojo.com"}
    ];
    res.render('users', {users: users_array})
})
app.listen(8000, function(){
    console.log('listening on port 8000');
});