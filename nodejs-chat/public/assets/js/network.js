var socket = io.connect("http://10.64.108.78:3000");

var name = prompt("İsminiz:");

socket.emit("set name", name);

$("#messages").html("");

socket.on("messages", function (messages) {
    $("#messages").html("");
    $.each(messages, function(i, message) {
        var mess = "<div class='well'><p><span class='text-success'>" + message.name + " : </span><span class='text-muted'>" + message.message + "</span></p></div>";
        $("#messages").append(mess);
    });
    reloadScroll();
});

socket.on("new message", function (message) {
    var mess = "<div class='well'><p><span class='text-success'>" + message.name + " : </span><span class='text-muted'>" + message.message + "</span></p></div>";
    $("#messages").append(mess);
    reloadScroll();
});

socket.on("users", function(users) {
    console.log("User geldi!");
    console.log(users);
    $("#users").html("");

    $.each(users, function(i, user) {
        var user = "<span class='label label-primary'>"+user+"</span> ";
        $("#users").append(user);
    });
});

function reloadScroll() {
    $("#messages").animate({
        "scrollTop": $("#messages")[0].scrollHeight
    }, "slow");

    $('#messages .well p span.text-muted').emoticonize();
}

$("#sendForm").submit(function(){
    var message = $("#sendForm input[name='message']").val();

    var message = $("<div/>").html(message).text();

    $("#sendForm button").attr("disabled");
    socket.emit("message", message);
    $("#sendForm input[name='message']").val("");
    $("#sendForm button").removeAttr("disabled");

    return false;
});