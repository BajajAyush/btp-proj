import React, { useState } from 'react';
import './Parameters.css'; // CSS for improved styling
import Header from "./Header";

function Parameters() {
    const [formData, setFormData] = useState({
        wire_feed_rate: '',
        arc_voltage: '',
        nozzle_distance: '',
        electrode_inclination: '',
        welding_speed: '',
        gas_flow_rate: ''
    });

    const [result, setResult] = useState(null);

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();

        fetch('http://localhost:5000/parameters', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: new URLSearchParams(formData).toString()
        })
        .then(response => response.json())
        .then(data => setResult(data))
        .catch(error => console.error('Error:', error));
    };

    const resetForm = () => {
        setFormData({
            wire_feed_rate: '',
            arc_voltage: '',
            nozzle_distance: '',
            electrode_inclination: '',
            welding_speed: '',
            gas_flow_rate: ''
        });
        setResult(null);
    };

    // Function to format numbers to 3 decimal places
    const formatNumber = (number) => {
        return parseFloat(number).toFixed(2);
    };

    return (
        <div>
            <Header/>
            <div className="parameters-container">
                {!result ? (
                    <>
                        <h2>Enter Welding Parameters</h2>
                        <form onSubmit={handleSubmit} className="form-grid">
                            <div className="form-group">
                                <label htmlFor="wire_feed_rate">
                                    Wire Feed Rate (W) (6.1 to 7.6 m/min):
                                </label>
                                <input
                                    type="number"
                                    id="wire_feed_rate"
                                    name="wire_feed_rate"
                                    step="0.1"
                                    min="6.1"
                                    max="7.6"
                                    value={formData.wire_feed_rate}
                                    onChange={handleChange}
                                    required
                                />
                            </div>
                            <div className="form-group">
                                <label htmlFor="arc_voltage">
                                    Arc Voltage (V) (24.0 to 29.0 Volts):
                                </label>
                                <input
                                    type="number"
                                    id="arc_voltage"
                                    name="arc_voltage"
                                    step="0.1"
                                    min="24.0"
                                    max="29.0"
                                    value={formData.arc_voltage}
                                    onChange={handleChange}
                                    required
                                />
                            </div>
                            <div className="form-group">
                                <label htmlFor="nozzle_distance">
                                    Nozzle to Plate Distance (N) (15.0 to 20.0 mm):
                                </label>
                                <input
                                    type="number"
                                    id="nozzle_distance"
                                    name="nozzle_distance"
                                    step="0.1"
                                    min="15.0"
                                    max="20.0"
                                    value={formData.nozzle_distance}
                                    onChange={handleChange}
                                    required
                                />
                            </div>
                            <div className="form-group">
                                <label htmlFor="electrode_inclination">
                                    Electrode Inclination (A) (80.0 to 100.0 degrees):
                                </label>
                                <input
                                    type="number"
                                    id="electrode_inclination"
                                    name="electrode_inclination"
                                    step="0.1"
                                    min="80.0"
                                    max="100.0"
                                    value={formData.electrode_inclination}
                                    onChange={handleChange}
                                    required
                                />
                            </div>
                            <div className="form-group">
                                <label htmlFor="welding_speed">
                                    Welding Speed (S) (25.0 to 40.0 cm/min):
                                </label>
                                <input
                                    type="number"
                                    id="welding_speed"
                                    name="welding_speed"
                                    step="0.1"
                                    min="25.0"
                                    max="40.0"
                                    value={formData.welding_speed}
                                    onChange={handleChange}
                                    required
                                />
                            </div>
                            <div className="form-group">
                                <label htmlFor="gas_flow_rate">
                                    Gas Flow Rate (G) (18.0 to 33.0 Litres/min):
                                </label>
                                <input
                                    type="number"
                                    id="gas_flow_rate"
                                    name="gas_flow_rate"
                                    step="0.1"
                                    min="18.0"
                                    max="33.0"
                                    value={formData.gas_flow_rate}
                                    onChange={handleChange}
                                    required
                                />
                            </div>
                            <input type="submit" value="Submit" className="submit-btn" />
                        </form>
                    </>
                ) : (
                    <div className="result-container">
                        <h2>Processed Parameters</h2>
                        <div className="result-grid">
                            <div className="result-item"><strong>Height (mm):</strong> {formatNumber(result.height)}</div>
                            <div className="result-item"><strong>P (mm):</strong> {formatNumber(result.p)}</div>
                            <div className="result-item"><strong>Width (mm):</strong> {formatNumber(result.width)}</div>
                            <div className="result-item"><strong>Width/Height Ratio:</strong> {formatNumber(result.wh)}</div>
                            <div className="result-item"><strong>Width/P Ratio:</strong> {formatNumber(result.wp)}</div>
                            <div className="result-item"><strong>Mind:</strong> {formatNumber(result.mind)}</div>
                            <div className="result-item"><strong>HPL:</strong> {formatNumber(result.rhi2)}</div>
                            <div className="result-item"><strong>AP (mm²):</strong> {formatNumber(result.ap)}</div>
                        </div>
                        <button onClick={resetForm} className="new-values-btn">Enter New Values</button>
                    </div>
                )}
            </div>
        </div>
    );
}

export default Parameters;
