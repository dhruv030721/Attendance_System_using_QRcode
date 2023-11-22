const Student = require('../model/Student-Model');

exports.Attendance = async(req, res) => {
    try{
        
    const {data} = req.body;
    const Entrydata = JSON.parse(data);
    const { name , enrollment_no, branch } = Entrydata;
    const entry = await Student.create({name, enrollment_no, branch});

    res.status(200).json(
        {
            success: true,
            data: entry ,
            message: "Attendance marked successfully",
        }
    );
    }catch(error){
        console.error(error);
        res.status(500).json({
            success: true,
            data: "Internal Server Error",
            message: error.message,
        })
    }

}   