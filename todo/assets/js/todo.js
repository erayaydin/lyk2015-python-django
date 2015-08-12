var TODO = function () {
    this.todos = [];
};

TODO.prototype.init = function() {
    this.todos = $.parseJSON(localStorage.getItem("todos"));
};

TODO.prototype.addTodo = function(todo) {
    var id = this.todos.push(todo);

    localStorage.setItem("todos", JSON.stringify(this.todos));

    return id;
};

TODO.prototype.removeTodo = function(key) {
    this.todos.splice(key, 1);

    localStorage.setItem("todos", JSON.stringify(this.todos));
};

TODO.prototype.getTodo = function(key) {
    return this.todos[key];
};

TODO.prototype.todos = function() {
    return this.todos;
};