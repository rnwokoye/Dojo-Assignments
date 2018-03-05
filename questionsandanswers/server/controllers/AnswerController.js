const mongoose = require('mongoose');
const Answer = mongoose.model('Answer');
const Question = mongoose.model('Question');

class AnswerController {

   
    createAnswer(req, res) {     
        req.body._user = req.session.user_id;
        Question.findOne({ _id: req.params.question_id }, (err, question) => {

    
            let answer = new Answer(req.body);
            answer._question = question._id;
            question._answers.push(answer);
            question.save((err) => {
                answer.save((err) => {
                    if (err) {
                        console.log("Error: " + err);
                        res.json(err);
                    } else {
                        console.log("Success!");
                        res.json(answer);
                    }
                })
            })
        })
    }

  
    findAll(req, res) {
        Answer.find({}).exec((err, answers) => {
            if (err) {
                console.log("Error: " + err);
                res.json(err);
            } else {
                console.log("Success, ans");
                res.json(answers);
            }
        })
    }

   
    findById(req, res) {
        Answer.findOne({ _id: req.params.id }, (err, answer) => {
            if (err) {
                console.log("Error: " + err);
                res.json(err);
            } else {
                res.json(answer);
            }
        });
    }

   
    likeAnswer(req, res) {
        
        Answer.findOne({ _id: req.params.id }, (error, answer) => {
            if (error) {
                console.log("Error: " + error);
            } else {
                answer.likes++;
                answer.save(answer, (error, updatedAnswer) => {
                    if (error) {
                        console.log("Error: " + error);
                        return res.json(error);
                    } else {
                        return res.json(updatedAnswer);
                    }
                })
            }
        })
    }

    findAllByQuestionId(req, res) {
        Question.findOne({ _id: req.params.id })
            .populate({
                path: "_answers",
                model: "Answer"
            })
            .exec((err, specificAnswers) => {
                if (err) {
                    console.log("Error: " + err);
                    res.json(err);
                } else {
                    res.json(specificAnswers);
                }
            })
    }
}

module.exports = new AnswerController();