function Results({ data }) {
  return (
    <div>
      <h2>{data.name}</h2>
      <p>Temperatura: {data.main.temp} °C</p>
      <p>Humedad: {data.main.humidity} %</p>
      <p>Clima: {data.weather[0].description}</p>
    </div>
  );
}

export default Results;
