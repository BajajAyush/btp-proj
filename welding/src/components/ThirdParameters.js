import React, { useState } from 'react';
import Header from './Header';

const ThirdParameter = () => {
    const [usrP, setUsrP] = useState('');
    const [varInt, setVarInt] = useState('');
    const [results, setResults] = useState([]);
    const [currentPage, setCurrentPage] = useState(0);

    const handleSubmit = async (event) => {
        event.preventDefault();

        try {
            const response = await fetch('http://localhost:5000/thirdparameters', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: new URLSearchParams({
                    usr_p: usrP,
                    var_int: varInt
                }),
            });

            if (response.ok) {
                const data = await response.json();
                setResults(data);
                setCurrentPage(0); // Reset to the first page
            } else {
                console.error('Failed to fetch data');
            }
        } catch (error) {
            console.error('Error:', error);
        }
    };

    const handleNextPage = () => {
        if (currentPage < results.length - 1) {
            setCurrentPage(currentPage + 1);
        }
    };

    const handlePreviousPage = () => {
        if (currentPage > 0) {
            setCurrentPage(currentPage - 1);
        }
    };

    return (
        <div>
            <Header />
            <div style={{
                display: 'flex',
                justifyContent: 'center',
                alignItems: 'center',
                flexDirection: 'column',
                minHeight: '100vh',
                backgroundColor: '#e3f2fd'
            }}>
                <form
                    onSubmit={handleSubmit}
                    style={{
                        maxWidth: '600px',
                        width: '100%',
                        padding: '20px',
                        background: '#bbdefb',
                        borderRadius: '8px',
                        boxShadow: '0 0 10px rgba(0, 0, 0, 0.1)',
                        display: 'flex',
                        flexDirection: 'column',
                        marginBottom: '20px'
                    }}>
                    <h1 style={{
                        textAlign: 'center',
                        marginBottom: '20px',
                        color: '#0d47a1'
                    }}>Enter Values</h1>

                    <label htmlFor="usr_p" style={{ marginBottom: '10px', fontWeight: 'bold', color: '#0d47a1' }}>
                        Enter weld bead depth (3.98 mm - 5.82 mm):
                    </label>
                    <input
                        type="number"
                        id="usr_p"
                        name="usr_p"
                        step="0.01"
                        min="3.98"
                        max="5.82"
                        required
                        value={usrP}
                        onChange={(e) => setUsrP(e.target.value)}
                        style={{
                            width: 'calc(100% - 20px)',
                            padding: '10px',
                            marginBottom: '20px',
                            border: '1px solid #64b5f6',
                            borderRadius: '4px'
                        }}
                    />

                    <label htmlFor="var_int" style={{ marginBottom: '10px', fontWeight: 'bold', color: '#0d47a1' }}>
                        Enter Acceptable Variation (1-10%):
                    </label>
                    <input
                        type="number"
                        id="var_int"
                        name="var_int"
                        step="1"
                        min="1"
                        max="10"
                        required
                        value={varInt}
                        onChange={(e) => setVarInt(e.target.value)}
                        style={{
                            width: 'calc(100% - 20px)',
                            padding: '10px',
                            marginBottom: '20px',
                            border: '1px solid #64b5f6',
                            borderRadius: '4px'
                        }}
                    />

                    <input
                        type="submit"
                        value="Submit"
                        style={{
                            backgroundColor: '#1e88e5',
                            color: 'white',
                            padding: '15px 20px',
                            border: 'none',
                            borderRadius: '4px',
                            cursor: 'pointer',
                            fontSize: '16px'
                        }}
                    />
                </form>

                {results.length > 0 && (
                    <div style={{
                        width: '100%',
                        maxWidth: '800px',
                        padding: '20px',
                        background: '#bbdefb',
                        borderRadius: '8px',
                        boxShadow: '0 0 10px rgba(0, 0, 0, 0.1)',
                        color: '#0d47a1',
                        textAlign: 'center'
                    }}>
                        <h2 style={{ marginBottom: '20px', color: '#0d47a1' }}>Processed Result</h2>
                        <div style={{
                            display: 'flex',
                            flexDirection: 'column',
                            gap: '15px',
                            padding: '10px',
                            borderRadius: '8px',
                            backgroundColor: '#e3f2fd'
                        }}>
                            <div>
                                <strong>Penetration (mm):</strong> {results[currentPage].penetration}
                            </div>
                            <div>
                                <strong>Wire Feed Rate (m/min):</strong> {results[currentPage].wire_feed_rate}
                            </div>
                            <div>
                                <strong>Arc Voltage (V):</strong> {results[currentPage].arc_voltage}
                            </div>
                            <div>
                                <strong>Contact Tube Distance (mm):</strong> {results[currentPage].contact_tube_distance}
                            </div>
                            <div>
                                <strong>Width/Height Ratio:</strong> {results[currentPage].width_height_ratio}
                            </div>
                            <div>
                                <strong>Width/Penetration Ratio:</strong> {results[currentPage].width_penetration_ratio}
                            </div>
                            <div>
                                <strong>Area of Penetration (mm²):</strong> {results[currentPage].area_of_penetration}
                            </div>
                            <div>
                                <strong>Dilution (%):</strong> {results[currentPage].dilution}
                            </div>
                            <div>
                                <strong>RHI:</strong> {results[currentPage].RHI}
                            </div>
                        </div>
                        <div style={{ marginTop: '20px', display: 'flex', justifyContent: 'space-between' }}>
                            <button
                                onClick={handlePreviousPage}
                                disabled={currentPage === 0}
                                style={{
                                    backgroundColor: currentPage === 0 ? '#ccc' : '#1e88e5',
                                    color: 'white',
                                    padding: '10px 20px',
                                    border: 'none',
                                    borderRadius: '4px',
                                    cursor: currentPage === 0 ? 'not-allowed' : 'pointer'
                                }}
                            >
                                Previous
                            </button>
                            <button
                                onClick={handleNextPage}
                                disabled={currentPage === results.length - 1}
                                style={{
                                    backgroundColor: currentPage === results.length - 1 ? '#ccc' : '#1e88e5',
                                    color: 'white',
                                    padding: '10px 20px',
                                    border: 'none',
                                    borderRadius: '4px',
                                    cursor: currentPage === results.length - 1 ? 'not-allowed' : 'pointer'
                                }}
                            >
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
