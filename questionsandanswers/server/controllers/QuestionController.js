const mongoose = require('mongoose');
const Question = mongoose.model('Question');
const User = mongoose.model('User');

class QuestionController {

    createQuestion(request, response) {
        request.body._user = request.session.user_id;                               
        User.findOne({ _id: request.session.user_id }, (err, user) => {
            var question = new Question(request.body);                              
            user._questions.push(question);
            user.save((err) => {

                question.save((err) => {                                              
                    if (err) {
                        console.log("Error: " + err);
                        response.json(err);                                              
                    } else {
                        console.log("Success! Question created.");
                        response.json(question);                                        
                    }
                });
            });
        });
    }

    findAll(request,response){
        Question.find({})
        .populate({
            path:"_answers",
            model:'Answer',
            
            populate:({
        path:"_user",
        model:"User"
            })
        })
        .exec(
            (err,questions)=>{
                if(err){
                    console.log("Error: " + err);
                    response.json(err);
                }else{
                    console.log("Success! Questions found.");
                    response.json(questions);
                }
            }
        )
   }

    findById(request,response){
        Question.findOne({_id:request.params.question_id})
        .populate({ path:"_answers", model:'Answer', options: {sort:{"likes": "descending"}}, 
            populate:({
                path:"_user",
                model:"User"
            })
        })
        .exec(
            (err,question)=>{
                if(err){
                    console.log("Error: " + err);
                    response.json(err);
                }else{
                    response.json(question);
                }
            }
        )   
    }
}

module.exports = new QuestionController();