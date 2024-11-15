import React, { useEffect, useState } from 'react';
import './Calculate.css'; // Import CSS for styling
import Header from "./Header";

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

    // Helper function to format numbers to 2 decimal places
    const formatNumber = (number) => {
        return parseFloat(number).toFixed(2);
    };

    return (
        <div>
            <Header/>
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
                                    <td>{formatNumber(result.penetration)}</td>
                                    <td>{formatNumber(result.wire_feed_rate)}</td>
                                    <td>{formatNumber(result.arc_voltage)}</td>
                                    <td>{formatNumber(result.contact_tube_to)}</td>
                                    <td>{formatNumber(result.plate_distance)}</td>
                                    <td>{formatNumber(result.angle)}</td>
                                    <td>{formatNumber(result.welding_speed)}</td>
                                    <td>{formatNumber(result.gas_flow_rate)}</td>
                                    <td>{formatNumber(result.rhi)}</td>
                                    <td>{formatNumber(result.area_of_penetration)}</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    );
}

export default Calculate;
