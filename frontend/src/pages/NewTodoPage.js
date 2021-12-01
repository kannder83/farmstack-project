const NewTodoPage = ({
  handleSubmit,
  todoBody,
  todoTitle,
  setTodoBody,
  setTodoTitle,
}) => {
  return (
    <main>
      <h2>New Todo</h2>
      <form onSubmit={handleSubmit}>
        <label htmlFor="todoTitle">Title:</label>
        <input
          id="todoTitle"
          type="text"
          required
          value={todoTitle}
          onChange={(e) => setTodoTitle(e.target.value)}
        />
        <label htmlFor="todoBody">Post:</label>
        <textarea
          id="todoBody"
          required
          value={todoBody}
          onChange={(e) => setTodoBody(e.target.value)}
        />
        <input type="submit" value="Create" />
      </form>
    </main>
  );
};

export { NewTodoPage };
