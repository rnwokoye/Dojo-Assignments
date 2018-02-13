var express = require('express'),
    path = require('path'),
    session = require('express-session'),
    bodyParser = require('body-parser'),
    mongoose = require('mongoose'),
    app = express(),
    port = 8000;

mongoose.connect('mongodb://localhost/basic_mongoose'); 
var QuoteSchema = new mongoose.Schema({
    //mongoose db entry with validation.
    name: { type: String, required: true, minlength: 3},
    quote: { type: String, min: 5, max: 350}, 
},
{timestamps: true});
var Quote = mongoose.model('Quote', QuoteSchema);


app.use(express.static( path.join(__dirname, "/static") ));
app.use(bodyParser.urlencoded({extended: true}));
app.use(session({
    secret: 'secretpassword',
    proxy: true,
    resave: false,
    saveUninitialized: true
}));

app.set('views',path.join(__dirname, '/views'));
app.set('view engine', 'ejs');


app.get('/', function(req, res){
    
        return res.render('index');
});

app.get('/quotes', function(req, res){

    Quote.find({}, function(error, quotes){
        return res.render('quotes', {'quotes': quotes} )
    });
});

app.post('/quotes', function(req, res){
    console.log("POST DATA", req.body)
    //create a new Quote with the name and age. Note no quotes for the "value" pair.
    // var Quote = new Quote({name: req.body.name, age: req.body.age}); 
    var quote = new Quote(req.body); 
    //save Quote to db
    quote.save(function(err){
        // if error console.log it
        if(err){
            console.log("something went wrong");
            console.log(quote.errors);
            res.render('index', {errors: quote.errors });
        }else {//console.log the result
            console.log('sucessfuly added quote'); 
            res.redirect('/quotes');
        }
    })
    
});

app.listen(port, function(){
    console.log(`listening on port ${port}`);
});
