let mongoose = require('mongoose');

mongoose.model('Question', new mongoose.Schema({
   content: {
       type:String,
       required:[true, "Must be at least 10 characters"],
       minlength:10,
       maxlength:255
   },description:{ type:String, default: "" },
    _answers:[{ type: mongoose.Schema.Types.ObjectId, ref: 'Answer' }],
    _user: { type: mongoose.Schema.Types.ObjectId, ref: 'User'}
}, {timestamps:true}));
