const mongoose = require('mongoose');

const student = mongoose.Schema({
    name:{
        type: String,
        required: true,
        maxLength: 50,
    },
    enrollment_no:{
        type: String,
        required: true,
        maxLength: 12,
    },
    branch: {
        type: String,
        required: true,
        maxLength: 10,
    },
    time: {
        type: Date,
        default: Date.now(),
    }
})

module.exports = mongoose.model('Student',student);