const express = require('express');
const app = express();
const dbconnect = require('./config/database');

// load config for environment file
require('dotenv').config();

const PORT = process.env.PORT || 4000;

// Add json middleware 
app.use(express.json());

// Import routes
const routes = require('./routes/routes')

app.use('/api/v1', routes);

// Start Server
app.listen(PORT,() => console.log(`Server Started Successfully at ${PORT}`));

// for database connection 
dbconnect();

// default route
app.use('/', (req,res) => {
    res.send('This is default route');
})



