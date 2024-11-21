import React, { useState } from 'react';
import './ThirdParameter.css';
import Header from './Header';
import CustomSwitch from './CustomSwitch';

const ThirdParameter = () => {
    const [usrP, setUsrP] = useState('');
    const [varInt, setVarInt] = useState('');
    const [results, setResults] = useState([]);
    const [results_univ, setResults_univ] = useState([]);
    const [univ,setUniv] = useState(false);
    const [currentPage, setCurrentPage] = useState(1);
    const resultsPerPage = 5; // Number of rows to display per page

    const handleSubmit = async (event) => {
        event.preventDefault();
        if (univ === false){
        try {
            const response = await fetch('http://localhost:5000/thirdparameters', {
                method: 'POST',
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                body: new URLSearchParams({ usr_p: usrP, var_int: varInt }),
            });

            if (response.ok) {
                const data = await response.json();
                setResults(data);
                setResults_univ([]);
                setCurrentPage(1); // Reset to the first page
            } else {
                console.error('Failed to fetch data');
            }
        } catch (error) {
            console.error('Error:', error);
        }}
        else if (univ === true){
            try {
                const response = await fetch('http://localhost:5000/thirdparametersuniv', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                    body: new URLSearchParams({ usr_p: usrP, var_int: varInt }),
                });
    
                if (response.ok) {
                    const data = await response.json();
                    setResults_univ(data);
                    setResults([])
                    setCurrentPage(1); // Reset to the first page
                } else {
                    console.error('Failed to fetch data');
                }
            } catch (error) {
                console.error('Error:', error);
            }
        }
    };

    // Pagination logic
    const indexOfLastResult = currentPage * resultsPerPage;
    const indexOfFirstResult = indexOfLastResult - resultsPerPage;
    const currentResults = results.slice(indexOfFirstResult, indexOfLastResult);

    const totalPages = Math.ceil(results.length/ resultsPerPage);

    
    const currentResults_univ = results_univ.slice(indexOfFirstResult, indexOfLastResult);
    const totalPages_univ = Math.ceil(results_univ.length / resultsPerPage);

    const goToNextPage = () => {
        if (currentPage < totalPages) setCurrentPage(currentPage + 1);
    };

    const goToPreviousPage = () => {
        if (currentPage > 1) setCurrentPage(currentPage - 1);
    };
    const onSelectSwitch = index => {
        if (index === 1) setUniv(false)
        else if (index === 2) setUniv(true)
      };

    return (
        <div>
            <Header />
            <div className="container">
                <h1 className="heading">Welding Parameter Optimizer</h1>
                <CustomSwitch
                        selectionMode={1}
                        roundCorner={true}
                        option1={'Factorial Method'}
                        option2={'Dimensional Method'}
                        onSelectSwitch={onSelectSwitch}
                        selectionColor={'#61dafb'}
                />
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
                                        <th>HPL</th>
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
                )}{ results_univ.length > 0 && (
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
                                        <th>Welding Speed (cm/min)</th>
                                        <th>Gas Flow Rate (l/min)</th>
                                        <th>Width/Height Ratio</th>
                                        <th>Width/Penetration Ratio</th>
                                        <th>Dilution (%)</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {currentResults_univ.map((result, index) => (
                                        <tr key={index}>
                                            <td>{result.penetration}</td>
                                            <td>{result.wire_feed_rate}</td>
                                            <td>{result.arc_voltage}</td>
                                            <td>{result.contact_tube_distance}</td>
                                            <td>{result.welding_speed}</td>
                                            <td>{result.shield_gas}</td>
                                            <td>{result.width_height_ratio}</td>
                                            <td>{result.width_penetration_ratio}</td>
                                            <td>{result.dilution}</td>
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
                                Page {currentPage} of {totalPages_univ}
                            </span>
                            <button onClick={goToNextPage} disabled={currentPage === totalPages_univ}>
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
