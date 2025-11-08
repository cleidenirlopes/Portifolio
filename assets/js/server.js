const express = require('express');
const nodemailer = require('nodemailer');
const bodyParser = require('body-parser');
const path = require('path');
const livereload = require('livereload');
const connectLivereload = require('connect-livereload');

const app = express();

// Live Reload Server
const liveReloadServer = livereload.createServer();
liveReloadServer.watch(path.join(__dirname, '../../'));

// Inject livereload script into pages
app.use(connectLivereload());

// Serve static files from the root directory
app.use(express.static(path.join(__dirname, '../../')));

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

// Serve the main page
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, '../../index.html'));
});

// Serve any other HTML files
app.get('/:page.html', (req, res) => {
    res.sendFile(path.join(__dirname, '../../', req.params.page + '.html'));
});

app.listen(3000, () => {
    console.log('Server running on port 3000');
    console.log('Open http://localhost:3000 in your browser');
});
