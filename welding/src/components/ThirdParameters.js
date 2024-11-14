import React, { useState } from 'react';
import Header from './Header';

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
        <div>
            <Header />
            <div style={{
                display: 'flex',
                justifyContent: 'center',
                alignItems: 'center',
                flexDirection: 'column',
                minHeight: '100vh',
                backgroundColor: '#e3f2fd' // Light blue background for consistency
            }}>
                <form
                    onSubmit={handleSubmit}
                    style={{
                        maxWidth: '600px',
                        width: '100%',
                        padding: '20px',
                        background: '#bbdefb', // Light blue form background
                        borderRadius: '8px',
                        boxShadow: '0 0 10px rgba(0, 0, 0, 0.1)',
                        display: 'flex',
                        flexDirection: 'column',
                        marginBottom: '20px'
                    }}>
                    <h1 style={{
                        textAlign: 'center',
                        marginBottom: '20px',
                        color: '#0d47a1' // Dark blue heading
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
                        step="0.01"
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
                            backgroundColor: '#1e88e5', // Darker blue for button
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
                        background: '#bbdefb', // Light blue background for results table
                        borderRadius: '8px',
                        boxShadow: '0 0 10px rgba(0, 0, 0, 0.1)',
                        color: '#0d47a1'
                    }}>
                        <h2 style={{ textAlign: 'center', marginBottom: '20px', color: '#0d47a1' }}>Processed Results</h2>
                        <table style={{
                            width: '100%',
                            borderCollapse: 'collapse',
                            textAlign: 'left',
                            backgroundColor: '#e3f2fd' // Lighter blue for table background
                        }}>
                            <thead>
                                <tr>
                                    <th style={{
                                        borderBottom: '2px solid #90caf9',
                                        paddingBottom: '10px',
                                        color: '#0d47a1'
                                    }}>Parameter</th>
                                    <th style={{
                                        borderBottom: '2px solid #90caf9',
                                        paddingBottom: '10px',
                                        color: '#0d47a1'
                                    }}>Value</th>
                                </tr>
                            </thead>
                            <tbody>
                                {results.map((result, index) => (
                                    <React.Fragment key={index}>
                                        <tr>
                                            <td style={{
                                                padding: '10px 0',
                                                borderBottom: '1px solid #bbdefb',
                                                color: '#0d47a1'
                                            }}><strong>Penetration (mm):</strong></td>
                                            <td style={{ padding: '10px 0', borderBottom: '1px solid #bbdefb' }}>{result.penetration}</td>
                                        </tr>
                                        {/* Add additional rows as needed for each parameter */}
                                    </React.Fragment>
                                ))}
                            </tbody>
                        </table>
                    </div>
                )}
            </div>
        </div>
    );
};

export default ThirdParameter;
