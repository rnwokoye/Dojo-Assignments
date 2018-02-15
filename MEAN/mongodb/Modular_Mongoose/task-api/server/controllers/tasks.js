const mongoose = require('mongoose');
const Task = mongoose.model('Task');

class TasksController {
    index(req, res){
        Task.find({}, (err, tasks) => {
            if(err){
                //no more "console errors"
                return res.json(err); 
            }
            return res.json(tasks); 
        })
    }
    create(req, res){
        Task.create(req.body, (err, task) => {
            if(err){
                return res.json(err);
            }
            return res.json(task);
        })
    }
    show(req, res){
        Task.findById(req.params.id,  (err, task) => {
            if(err){
                return res.json({error: '404 -task not found'});
            }
            return res.json(task);
        })
    }
    update(req, res) {
        // remember to check and study the "$" $sign modifiers. "set, pull, push, "
        Task.findByIdAndUpdate(req.params.id, {$set: req.body}, {new: true}, (err, task) =>{
            if(err){
                return res.json(err);
            }
            return res.json(task); 
        })
    }
    destroy(req, res){
        Task.findByIdAndRemove(req.params.id, (err, task) =>{
            if(err){
                return res.json(err);
            }
            return res.json({
                'success': 'successfully deleted task'
            });
        })
    }
}

//get all tasks method: index route:  /task, type: get
//create a task method: create, route: /tasks type: post
// get a single task from the db method: show, route:/tasks/:id, type: get
//update task by ID method: update, route: /tasks/:id, type: put/patch
//Delete task by id method: destroy, route: /tasks/:id, type: delete





module.exports = new TasksController(); 