const mongoose = require('mongoose');

require('dotenv').config();

const dbconnect = () => {
    mongoose.connect(process.env.DATABASE_URL,{
        useNewUrlParser: true,
        useUnifiedTopology: true,
    }).then(() => {
        console.log("Database connection successfully");
    }).catch((error) => {
        console.log("Some issues occur in database connection");
        console.error(error.message);
        process.exit();
    })
}

module.exports = dbconnect;