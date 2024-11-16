import React, { useState } from 'react';
import './ThirdParameter.css';
import Header from './Header';

const ThirdParameter = () => {
    const [usrP, setUsrP] = useState('');
    const [varInt, setVarInt] = useState('');
    const [results, setResults] = useState([]);
    const [currentPage, setCurrentPage] = useState(1);
    const resultsPerPage = 5; // Number of rows to display per page

    const handleSubmit = async (event) => {
        event.preventDefault();

        try {
            const response = await fetch('http://localhost:5000/thirdparameters', {
                method: 'POST',
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                body: new URLSearchParams({ usr_p: usrP, var_int: varInt }),
            });

            if (response.ok) {
                const data = await response.json();
                setResults(data);
                setCurrentPage(1); // Reset to the first page
            } else {
                console.error('Failed to fetch data');
            }
        } catch (error) {
            console.error('Error:', error);
        }
    };

    // Pagination logic
    const indexOfLastResult = currentPage * resultsPerPage;
    const indexOfFirstResult = indexOfLastResult - resultsPerPage;
    const currentResults = results.slice(indexOfFirstResult, indexOfLastResult);

    const totalPages = Math.ceil(results.length / resultsPerPage);

    const goToNextPage = () => {
        if (currentPage < totalPages) setCurrentPage(currentPage + 1);
    };

    const goToPreviousPage = () => {
        if (currentPage > 1) setCurrentPage(currentPage - 1);
    };

    return (
        <div>
            <Header />
            <div className="container">
                <h1 className="heading">Welding Parameter Optimizer</h1>
                <form className="parameters-container" onSubmit={handleSubmit}>
                    <label htmlFor="usr_p">Weld Bead Depth (3.98 - 5.82 mm):</label>
                    <input
                        type="number"
                        id="usr_p"
                        value={usrP}
                        onChange={(e) => setUsrP(e.target.value)}
                        min="3.98"
                        max="5.82"
                        step="0.01"
                        required
                    />

                    <label htmlFor="var_int">Acceptable Variation (1-10%):</label>
                    <input
                        type="number"
                        id="var_int"
                        value={varInt}
                        onChange={(e) => setVarInt(e.target.value)}
                        min="1"
                        max="10"
                        step="1"
                        required
                    />

                    <button type="submit">Submit</button>
                </form>

                {results.length > 0 && (
                    <div className="result-container">
                        <h2>Results</h2>
                        <div className="table-container">
                            <table>
                                <thead>
                                    <tr>
                                        <th>Penetration (mm)</th>
                                        <th>Wire Feed Rate (m/min)</th>
                                        <th>Arc Voltage (V)</th>
                                        <th>Contact Tube Distance (mm)</th>
                                        <th>Width/Height Ratio</th>
                                        <th>Width/Penetration Ratio</th>
                                        <th>Area of Penetration (mm²)</th>
                                        <th>Dilution (%)</th>
                                        <th>RHI</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {currentResults.map((result, index) => (
                                        <tr key={index}>
                                            <td>{result.penetration}</td>
                                            <td>{result.wire_feed_rate}</td>
                                            <td>{result.arc_voltage}</td>
                                            <td>{result.contact_tube_distance}</td>
                                            <td>{result.width_height_ratio}</td>
                                            <td>{result.width_penetration_ratio}</td>
                                            <td>{result.area_of_penetration}</td>
                                            <td>{result.dilution}</td>
                                            <td>{result.RHI}</td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                        </div>
                        <div className="pagination">
                            <button onClick={goToPreviousPage} disabled={currentPage === 1}>
                                Previous
                            </button>
                            <span>
                                Page {currentPage} of {totalPages}
                            </span>
                            <button onClick={goToNextPage} disabled={currentPage === totalPages}>
                                Next
                            </button>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export default ThirdParameter;
