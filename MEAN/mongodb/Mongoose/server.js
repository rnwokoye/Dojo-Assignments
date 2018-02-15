var express = require('express'),
    path = require('path'),
    session = require('express-session'),
    bodyParser = require('body-parser'),
    mongoose = require('mongoose'),
    app = express(),
    port = 8000;

mongoose.connect('mongodb://localhost/basic_mongoose'); 
var UserSchema = new mongoose.Schema({
    //mongoose db entry with validation.
    name: { type: String, required: true, minlength: 3},
    age: { type: Number, min: 1, max: 150}, 
    email: { type: String, required: true }
},
{timestamps: true});
var User = mongoose.model('User', UserSchema);


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
    User.find({}, function(err, users){
        return res.render('index', {'users': users});
    });
});

app.get('/findusers', function(req, res){
    // find records matching "Richard"
    User.find({name: "Richard"}, function(err, users){
        return res.render('findUsers', {"users": users});
    })

    // User.findOne({}, function(err, user){
    //     //run code to find "one" user
    // })

    // User.remove({}, function(err){
    //     // run code to delete all users
    // })

    // User.remove({_id: 'insert record unique id here'}, function(err){
    //     //run code to delete one user maching search criteria above. 
    // })

    // User.update({name: "Richard"}, {name: 'Last_name'}, function(err){
    //     //code to update a matching user record. 
    // })
    // User.find({name: 'Richard'}, function(err, user){
    //     user.name = 'Rich'
    //     user.save(function(err){
    //         // message if save was successfull.
    //         //check out http://mongoosejs.com/docs/index.html
    //     })
    // })
})
app.post('/users', function(req, res){
    console.log("POST DATA", req.body)
    //create a new user with the name and age. Note no quotes for the "value" pair.
    // var user = new User({name: req.body.name, age: req.body.age}); 
    var user = new User(req.body); 
    //save user to db
    user.save(function(err){
        // if error console.log it
        if(err){
            console.log("something went wrong");
            console.log(err);
            // res.redirect('index', {errors: user.errors });
        }else {//console.log the result
            console.log('sucessfuly added user'); 
            res.redirect('/');
        }
    })
    
});

app.listen(port, function(){
    console.log(`listening on port ${port}`);
});
