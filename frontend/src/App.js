import axios from "axios";
import { Header } from "./components/Header";
import { Footer } from "./components/Footer";
import { Home } from "./pages/Home";
import { TodoPage } from "./pages/TodoPage";
import { About } from "./pages/About";
import { useState, useEffect } from "react";
import { Routes, Route } from "react-router-dom";

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
      <Header />
      <Routes>
        <Route
          path="/"
          element={<Home handleDelete={handleDelete} todoList={todoList} />}
        />
        <Route path="about" element={<About />} />
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
