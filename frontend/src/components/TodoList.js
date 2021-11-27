import { Todo } from "./Todo";

const TodoList = ({ todoList, handleDelete }) => {
  return (
    <ul>
      {todoList.map((todo, index) => (
        <li key={index}>
          <Todo todo={todo} handleDelete={handleDelete} />
        </li>
      ))}
    </ul>
  );
};

export { TodoList };
