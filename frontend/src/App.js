import axios from "axios";
import { Header } from "./components/Header";
import { Footer } from "./components/Footer";
import { Home } from "./pages/Home";
import { TodoPage } from "./pages/TodoPage";
import { NewTodoPage } from "./pages/NewTodoPage";
import { About } from "./pages/About";
import { useState, useEffect } from "react";
import { Routes, Route, useNavigate } from "react-router-dom";

function App() {
  const URL = "http://localhost:8000/api/todo";
  const [todoList, setTodoList] = useState([{}]);
  const [todoTitle, setTodoTitle] = useState("");
  const [todoBody, setTodoBody] = useState("");
  const history = useNavigate();

  const loadTodo = async () =>
    await axios.get(URL).then((res) => {
      setTodoList(res.data);
    });

  const handleDelete = async (id) => {
    await axios.delete(`${URL}/${id}`);
    await loadTodo();
    history("/");
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const newTodo = {
      title: todoTitle,
      description: todoBody,
    };
    try {
      await axios.post(URL, newTodo);
    } catch (err) {
      console.log(err);
    }
    setTodoTitle("");
    setTodoBody("");
    loadTodo();
    history("/");
  };

  useEffect(() => {
    loadTodo();
  }, []);

  return (
    <div className="App">
      <Header />
      <Routes>
        <Route
          path="/"
          element={<Home handleDelete={handleDelete} todoList={todoList} />}
        />
        <Route
          path="home"
          element={<Home handleDelete={handleDelete} todoList={todoList} />}
        />
        <Route path="about" element={<About />} />
        <Route
          path="post"
          element={
            <NewTodoPage
              todoTitle={todoTitle}
              todoBody={todoBody}
              setTodoTitle={setTodoTitle}
              setTodoBody={setTodoBody}
              handleSubmit={handleSubmit}
            />
          }
        />
        <Route
          path="post/:id"
          element={<TodoPage handleDelete={handleDelete} todoList={todoList} />}
        />
        <Route path="*" element={<p>nothing</p>} />
      </Routes>

      <Footer />
    </div>
  );
}

export default App;
