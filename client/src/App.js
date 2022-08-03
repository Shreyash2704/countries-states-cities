import './App.css';
import Content from './components/Content';
import Navbar from './components/Navbar';

function App() {
  return (
    <div className="App">
      <Navbar />
     <div className="container">
         <Content />
      </div>  
      
      
     
      <header className="App-header">
        Hello World
      </header>
    </div>
  );
}

export default App;
