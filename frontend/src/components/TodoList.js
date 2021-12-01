import { Todo } from "./Todo";
import { Link } from "react-router-dom";

const TodoList = ({ todoList, handleDelete }) => {
  return (
    <ul>
      {todoList.map((todo, index) => (
        <li key={index}>
          <Link to={`/post/${todo.id}`}>
            <Todo todo={todo} handleDelete={handleDelete} />
          </Link>
        </li>
      ))}
    </ul>
  );
};

export { TodoList };
