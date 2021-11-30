import { TodoList } from "../components/TodoList";

const Home = ({ todoList, handleDelete }) => {
  return (
    <main>
      <h1>This is react!</h1>
      <TodoList todoList={todoList} handleDelete={handleDelete} />
    </main>
  );
};

export { Home };
