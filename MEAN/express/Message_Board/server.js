var express = require('express'),
    path = require('path'),
    session = require('express-session'),
    bodyParser = require('body-parser'),
    mongoose = require('mongoose'),
    app = express(),
    port = 8000;

mongoose.connect('mongodb://localhost/message_board'); 
mongoose.Promise = global.Promise;

var Schema = mongoose.Schema; 

var MessageSchema = new mongoose.Schema({
    name: {type: String, required: [true, "Name is required!"]},
    message: {type: String, required: [true, "Message is required!!"]},
    comments: [{type: Schema.Types.ObjectId, ref: "Comment"}]
}, {usePushEach: true, timestamps: true});

var CommentSchema = new mongoose.Schema({
    name: {type: String, required: [true, "Name is required"]},
    _message: {type: Schema.Types.ObjectId, ref: "Message"},
    comment: {type: String, required: true }
}, {usePushEach: true, timestamps: true});

mongoose.model('Message', MessageSchema);
mongoose.model('Comment', CommentSchema);

var Message = mongoose.model('Message');
var Comment = mongoose.model('Comment');



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
    Message.find({})
    .populate('comments')
    .exec(function(err, messages){
        console.log(messages)
        res.render('index', {messages: messages});
    });
});
app.post('/message', function(req, res){
    var message = new Message(req.body);
    message.save(function(err){
        console.log(req.body);
        if(err){
            console.log('error');
            res.redirect('/');
        }else {
            res.redirect('/');
        }
    });
});
app.post('/message/:id', function(req, res){
    Message.findOne({_id: req.params.id}, function(err, message){
        var comment = new Comment(req.body);
        comment._message = message._id;

        comment.save(function(err){
        console.log('here comment' + comment.comment);
            message.comments.push(comment);
            console.log('first comment' + comment);
            message.save(function(err){
                if(err){
                    console.log("error");
                }else {
                    res.redirect('/');
                }
            });  
        });
    });
});



app.listen(port, function(){
    console.log(`listening on port ${port}`);
});

