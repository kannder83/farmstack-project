import { TodoList } from "../components/TodoList";
import { Link } from "react-router-dom";

const Home = ({ todoList, handleDelete }) => {
  return (
    <main>
      <h1>This is react!</h1>
      <TodoList todoList={todoList} handleDelete={handleDelete} />
      <Link to="/post">
        <p>Add New Task</p>
      </Link>
    </main>
  );
};

export { Home };
