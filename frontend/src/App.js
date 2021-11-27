import axios from "axios";
import { useState, useEffect } from "react";
import { TodoList } from "./components/TodoList";

function App() {
  const URL = "http://localhost:8000/api/todo";
  const [todoList, setTodoList] = useState([{}]);

  useEffect(() => {
    const loadTodo = async () =>
      await axios.get(URL).then((res) => {
        setTodoList(res.data);
      });

    loadTodo();
  }, []);

  const handleDelete = async (id) => {
    await axios.delete(`${URL}/${id}`).then((res) => {
      console.log(res);
    });
  };

  return (
    <div className="App">
      <h1>This is react!</h1>
      <TodoList todoList={todoList} handleDelete={handleDelete} />
    </div>
  );
}

export default App;
