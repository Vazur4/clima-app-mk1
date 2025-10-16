import axios from "axios";
import { useState } from "react";

function Search({ setWeather }) {
  const [city, setCity] = useState("");

  const handleSearch = async () => {
    const res = await axios.get(`http://127.0.0.1:5000/clima?city=${city}`);
    setWeather(res.data);
  };

  return (
    <div className="search-container">
      <input value={city} onChange={e => setCity(e.target.value)} placeholder="Ciudad"/>
      <button onClick={handleSearch}>Buscar</button>
    </div>
  );
}

export default Search;
