document.addEventListener("DOMContentLoaded"), function() {
    const tasklist = document.getElementById("task-list")
    const newTaskInput = document.getElementById("new-Task")
    const addTaskButton = document.getElementById("add-Task")

    addTaskButton.addEventListener("click", function() {
        const tasktext = newTaskInput.ariaValueMax.trim ();
        if (tasktext !== "") {
            addTaskButton(tasktext);
            newTaskInput.value = "";
        }
  } )}

  newTaskInput.addEventListener("keyup", function(event) {
    if (event.key === "Enter") {
        addTaskButton.click();
    } } );

    function addTask(tasktext) {
        const taskItem = document.createElement("li");
        taskItem.textContent = tasktext;

        const deleteButton = Document.createElement("button");
        deleteButton.textContent = "delete";
        deleteButton.classlist.add("delete-Button");

        deleteButton.addEventListener("click", function() {
  } )};
    taskItem.appenchild(deleteButton);

    taskItem.addEventListener("click", function() {
        taskItem.classlist.toggle("completed");
    }   );

    tasklist.appenChild(taskItem); {

    };