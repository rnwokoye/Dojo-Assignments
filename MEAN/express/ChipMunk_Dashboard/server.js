var express = require('express'),
    path = require('path'),
    session = require('express-session'),
    bodyParser = require('body-parser'),
    mongoose = require('mongoose'),
    app = express(),
    port = 8000;

mongoose.connect('mongodb://localhost/chipmunks'); 
var ChipmunkSchema = new mongoose.Schema({
    //mongoose db entry with validation.
    name: { type: String, required: true, minlength: 3},
    age: { type: Number, required: true, min: 1, max: 10}, 
    color: { type: String, required: true, minlength: 2 }
},
{timestamps: true});
var Chipmunk = mongoose.model('Chipmunk', ChipmunkSchema);


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
    Chipmunk.find({}, function(error, chipmunks){
        return res.render('index', {'chipmunks': chipmunks });
    })     
});

app.get('/chipmunks/new', function(req, res){

    return res.render('new_chipmunk'); 
})

app.post('/chipmunks', function(req, res){
    var chipmunk = new Chipmunk(req.body); 
    chipmunk.save(function(err){
        if(err){
            console.log("there are errors")
            res.render('new_chipmunk', {errors: chipmunk.errors });
        }else {
            return res.redirect('/'); 
        }
    })
})
app.get('/chipmunks/:id', function(req, res){
    // find records matching "id"
    Chipmunk.findById({_id: req.params.id}, function(err, chipmunk){
        if(err){
            console.log(err);
            res.redirect('/' + req.params.id);
        }
        return res.render('findChipmunk', {chipmunk: chipmunk});
    });
});

app.get('/chipmunks/edit/:id', function(req, res){
    Chipmunk.findById({_id: req.params.id}, function(err, chipmunk){
        if(err){
            res.render('editChipmunk');
        }
        res.render('editChipmunk', {chipmunk: chipmunk});
    });
});
app.post('/chipmunks/:id', function(req, res){
    Chipmunk.findByIdAndUpdate(req.params.id, {$set: req.body}, {new:true }, function(err, chipmunk){
        chipmunk.name = req.body.name;
        chipmunk.age = req.body.age;
        chipmunk.color = req.body.color;
        chipmunk.save(function(err){
            console.log("after save" +req.body);
            if(err){
                console.log(error);
                res.render('/', {errors: chipmunk.errors});
            }else{
                res.redirect('/');
            }
        });
    });
});
app.get('/chipmunks/destroy/:id', function(req, res){
    Chipmunk.findByIdAndRemove(req.params.id, function(err, chipmunk){
        if(err){
            console.log(error);
            res.redirect('/', {errors: chipmunk.errors});
        }else{
            res.redirect('/');
        }
    });
})
app.listen(port, function(){
    console.log(`listening on port ${port}`);
});
