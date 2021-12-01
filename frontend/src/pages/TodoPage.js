import { useParams } from "react-router";

const TodoPage = ({ handleDelete, todoList }) => {
  const { id } = useParams();
  const findTodo = todoList.find((todo) => todo.id === id);
  return (
    <main>
      {findTodo && (
        <>
          <h1>{findTodo.title}</h1>
          <h2>{findTodo.description}</h2>
          <button onClick={(e) => handleDelete(findTodo.id)}>Complete</button>
        </>
      )}
      {!findTodo && (
        <>
          <p>No information</p>
        </>
      )}
    </main>
  );
};

export { TodoPage };
