import React, { useState, useEffect } from 'react';
import axios from 'axios';

const TrafficDashboard = () => {
    const [trafficData, setTrafficData] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            const result = await axios('/api/traffic');
            setTrafficData(result.data);
        };
        fetchData();
    }, []);

    return (
        <div>
            <h1>Traffic Dashboard</h1>
            <ul>
                {trafficData.map(item => (
                    <li key={item._id}>
                        Location: {item.location}, Congestion Level: {item.congestionLevel}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default TrafficDashboard;
