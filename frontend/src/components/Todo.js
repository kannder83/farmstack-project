const Todo = ({ todo, handleDelete }) => {
  return (
    <article>
      <h2>{todo.title}</h2>
      <h3>{todo.description}</h3>
    </article>
  );
};

export { Todo };
