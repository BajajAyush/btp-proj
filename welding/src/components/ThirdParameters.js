import React, { useState } from 'react';

const ThirdParameter = () => {
    const [usrP, setUsrP] = useState('');
    const [varInt, setVarInt] = useState('');
    const [results, setResults] = useState([]);
    const [error, setError] = useState(null);

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
            } else {
                console.error('Failed to fetch data');
            }
        } catch (error) {
            console.error('Error:', error);
        }
    };

    return (
        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh', backgroundColor: '#f4f4f4' }}>
            <form onSubmit={handleSubmit} style={{
                maxWidth: '600px',
                width: '100%',
                padding: '20px',
                background: 'white',
                borderRadius: '8px',
                boxShadow: '0 0 10px rgba(0, 0, 0, 0.1)',
                display: 'flex',
                flexDirection: 'column'
            }}>
                <h1 style={{ textAlign: 'center', marginBottom: '20px' }}>Enter Third Parameters</h1>

                <label htmlFor="usr_p" style={{ marginBottom: '10px', fontWeight: 'bold' }}>Enter penetration range (3.98 mm - 5.82 mm):</label>
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
                    style={{ width: 'calc(100% - 20px)', padding: '10px', marginBottom: '20px', border: '1px solid #ccc', borderRadius: '4px' }}
                />

                <label htmlFor="var_int" style={{ marginBottom: '10px', fontWeight: 'bold' }}>Enter Acceptable Variation (1-10%):</label>
                <input
                    type="number"
                    id="var_int"
                    name="var_int"
                    step="0.01"
                    min="1"
                    max="10"
                    required
                    value={varInt}
                    onChange={(e) => setVarInt(e.target.value)}
                    style={{ width: 'calc(100% - 20px)', padding: '10px', marginBottom: '20px', border: '1px solid #ccc', borderRadius: '4px' }}
                />

                <input
                    type="submit"
                    value="Submit"
                    style={{
                        backgroundColor: '#4CAF50',
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
                <div style={{ marginTop: '20px', maxWidth: '600px', width: '100%', padding: '20px', background: 'white', borderRadius: '8px', boxShadow: '0 0 10px rgba(0, 0, 0, 0.1)' }}>
                    <h2 style={{ textAlign: 'center', marginBottom: '20px' }}>Processed Results</h2>
                    <ul>
                        {results.map((result, index) => (
                            <li key={index}>
                                <strong>Penetration:</strong> {result.penetration} <br />
                                <strong>Wire Feed Rate:</strong> {result.wire_feed_rate} <br />
                                <strong>Arc Voltage:</strong> {result.arc_voltage} <br />
                                <strong>Contact Tube Distance:</strong> {result.contact_tube_distance} <br />
                                <strong>Width/Height Ratio:</strong> {result.width_height_ratio} <br />
                                <strong>Width/Penetration Ratio:</strong> {result.width_penetration_ratio} <br />
                                <strong>Area of Penetration:</strong> {result.area_of_penetration} <br />
                                <strong>Dilution:</strong> {result.dilution} <br />
                                <strong>RHI:</strong> {result.RHI} <br />
                            </li>
                        ))}
                    </ul>
                </div>
            )}
        </div>
    );
};

export default ThirdParameter;
