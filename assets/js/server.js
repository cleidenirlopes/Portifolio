const express = require('express');
const nodemailer = require('nodemailer');
const bodyParser = require('body-parser');
const app = express();

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.post('/send-message', (req, res) => {
    const { name, email, subject, message } = req.body;

    let transporter = nodemailer.createTransport({
        service: 'outlook',
        auth: {
            user: 'cleidenirlopes@outlook.com',
            pass: 'upufyvtmkwfbtnjy'
        }
    });

    let mailOptions = {
        from: email,
        to: 'cleidenirlopes@outlook.com',
        subject: subject,
        text: `Message from ${name} (${email}):\n\n${message}`
    };

    transporter.sendMail(mailOptions, (error, info) => {
        if (error) {
            console.log(error);
            return res.status(500).send('Error sending email');
        }
        console.log('Email sent: ' + info.response);
        res.status(200).send('Message sent');
    });
});

app.listen(3000, () => console.log('Server running on port 3000'));
