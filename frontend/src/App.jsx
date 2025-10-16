import { useState } from "react";
import Search from "./Search";
import Results from "./Result.jsx";
import './app.css';

function App() {
  const [weather, setWeather] = useState(null);

  return (
    <div>
      <Search setWeather={setWeather} />
      {weather && <Results data={weather} />}
    </div>
  );
}

export default App;
