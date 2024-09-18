import React, { useEffect, useState } from 'react';
import './Calculate.css'; // Import CSS for styling

function Calculate() {
    const [results, setResults] = useState([]);

    useEffect(() => {
        fetch('http://localhost:5000/calculate', {
            method: 'GET'
        })
        .then(response => response.json())
        .then(data => setResults(data))
        .catch(error => console.error('Error:', error));
    }, []);

    return (
        <div className="container">
            <h1 className="heading">Optimization Results</h1>
            <div className="table-wrapper">
                <table className="results-table">
                    <thead>
                        <tr>
                            <th>Penetration</th>
                            <th>Wire Feed Rate</th>
                            <th>Arc Voltage</th>
                            <th>Contact Tube To</th>
                            <th>Plate Distance</th>
                            <th>Angle</th>
                            <th>Welding Speed</th>
                            <th>Gas Flow Rate</th>
                            <th>RHI</th>
                            <th>Area of Penetration</th>
                        </tr>
                    </thead>
                    <tbody>
                        {results.map((result, index) => (
                            <tr key={index}>
                                <td>{result.penetration}</td>
                                <td>{result.wire_feed_rate}</td>
                                <td>{result.arc_voltage}</td>
                                <td>{result.contact_tube_to}</td>
                                <td>{result.plate_distance}</td>
                                <td>{result.angle}</td>
                                <td>{result.welding_speed}</td>
                                <td>{result.gas_flow_rate}</td>
                                <td>{result.rhi}</td>
                                <td>{result.area_of_penetration}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
}

export default Calculate;
