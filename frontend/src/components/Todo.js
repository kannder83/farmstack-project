const Todo = ({ todo, handleDelete }) => {
  return (
    <form>
      <input type="text" defaultValue={todo.title} readOnly={true} />
      <input type="text" defaultValue={todo.description} readOnly={true} />
      <input
        type="submit"
        value="update"
        onClick={(e) => {
          e.preventDefault();
        }}
      />
      <input
        type="submit"
        value="delete"
        onClick={(e) => {
          e.preventDefault();
          handleDelete(todo.id);
        }}
      />
    </form>
  );
};

export { Todo };
