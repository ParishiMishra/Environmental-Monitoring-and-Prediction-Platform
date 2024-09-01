import React, { useState } from 'react';
import axios from 'axios';

const LandslidePrediction = () => {
    const [data, setData] = useState({ rainfall: '', soil_moisture: '', slope: '', land_use: '' });
    const [result, setResult] = useState(null);

    const handleChange = (e) => {
        setData({ ...data, [e.target.name]: e.target.value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post('http://localhost:8000/api/predict/landslide/', data)
            .then(response => setResult(response.data.landslide_probability))
            .catch(error => console.error(error));
    };

    return (
        <div>
            <h2>Landslide Prediction</h2>
            <form onSubmit={handleSubmit}>
                <input type="text" name="rainfall" placeholder="Rainfall" onChange={handleChange} />
                <input type="text" name="soil_moisture" placeholder="Soil Moisture" onChange={handleChange} />
                <input type="text" name="slope" placeholder="Slope" onChange={handleChange} />
                <input type="text" name="land_use" placeholder="Land Use" onChange={handleChange} />
                <button type="submit">Predict</button>
            </form>
            {result && <p>Landslide Probability: {result}</p>}
        </div>
    );
};

export default LandslidePrediction;
