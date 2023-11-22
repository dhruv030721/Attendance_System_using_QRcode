const express = require('express');
const router = express.Router();

const {Attendance} = require('../controller/Attendance');

router.post('/Attendance', Attendance);

module.exports = router;