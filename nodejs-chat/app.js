var express      = require("express"),
    app          = express(),
    http         = require("http").Server(app),
    io           = require("socket.io")(http),
    path         = require("path"),
    logger       = require("morgan"),
    jade         = require("jade"),
    cookieParser = require("cookie-parser"),
    bodyParser   = require("body-parser");

var config = require("./config.json");

app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

// 404 Handler
app.use(function(err, req, res, next) {
    res.status(err.status || 500);
    res.render('error', {
        message: err.message,
        error: err
    });
});

app.get("/", function(req, res) {
    res.render("hello", { title: "Chat Example" });
});

var messages = [];
var users = {};

io.on("connection", function(socket) {
    console.log("connection!");

    users[socket.id] = "isimsiz";
    users[0] = "ahmet";
    console.log('sss', users);
    io.sockets.emit("users", users);

    socket.emit("messages", messages);

    socket.on("message", function(message){
        messages.push({ name: socket.name, message: message });

        if(message == "/clear") {
            messages.splice(0, messages.length);
            io.sockets.emit("messages", messages);
        } else {

            io.sockets.emit("new message", { name: socket.name, message: message });
        }
    });

    socket.on("set name", function(name) {
        console.log("isim belirlendi!");
        socket.name = name;
        users[socket.id] = name;
        console.log(users);
        io.sockets.emit("users", users);
    });

    socket.on("disconnect", function() {
        delete users[socket.id];
        io.sockets.emit("users", users);
        console.log("disconnect!");
    });
});

var serverPort = process.env.PORT || config.port;
http.listen(serverPort, function(){
    console.log("Server listening on port " + serverPort);
});