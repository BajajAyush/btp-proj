import React, { useState } from 'react';

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

    return (
        <div>
            <h2>Enter Parameters</h2>
            <form onSubmit={handleSubmit}>
                <label htmlFor="wire_feed_rate">Wire Feed Rate (W) (6.1 to 7.6 m/min):</label>
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

                <label htmlFor="arc_voltage">Arc Voltage (V) (24.0 to 29.0 Volts):</label>
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

                <label htmlFor="nozzle_distance">Nozzle to Plate Distance (N) (15.0 to 20.0 mm):</label>
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

                <label htmlFor="electrode_inclination">Electrode Inclination (A) (80.0 to 100.0 degrees):</label>
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

                <label htmlFor="welding_speed">Welding Speed (S) (25.0 to 40.0 cm/min):</label>
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

                <label htmlFor="gas_flow_rate">Gas Flow Rate (G) (18.0 to 33.0 Litres/min):</label>
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

                <input type="submit" value="Submit" />
            </form>

            {result && (
                <div>
                    <h2>Processed Parameters</h2>
                    <ul>
                        <li>Height: {result.height}</li>
                        <li>P: {result.p}</li>
                        <li>Width: {result.width}</li>
                        <li>Width/Height Ratio: {result.wh}</li>
                        <li>Width/P Ratio: {result.wp}</li>
                        <li>Mind: {result.mind}</li>
                        <li>RHI2: {result.rhi2}</li>
                        <li>AP: {result.ap}</li>
                    </ul>
                </div>
            )}
        </div>
    );
}

export default Parameters;
