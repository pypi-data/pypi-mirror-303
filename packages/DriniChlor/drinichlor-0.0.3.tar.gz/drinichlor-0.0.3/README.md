# Engineering Tool for Water Quality Monitoring

This project is an engineering tool developed in Python using the Tkinter and Matplotlib libraries to create a graphical interface for monitoring and analyzing chlorine, temperature, dissolved oxygen (DO), and turbidity (NTU) in water. The system simulates measurements and analyzes the necessary chlorine level for disinfecting water, depending on measured values for DO, temperature, and NTU.

## Main Components

### Sensor Class
- Represents a sensor that reads randomly generated values for the main variables (e.g., chlorine, DO, temperature).
- Contains methods to calculate the chlorine level based on:
  - DO level
  - Temperature
  - The difference in NTU between the inlet and outlet.

### EngineeringTool Class
- Contains the graphical interface where the user can manually enter values for NTU and temperature.
- The use of graphs allows for the visualization of the read data, along with predictions and differences between various chlorine levels.

## Graphs and Analysis
- The tool creates graphs that show the relationships between chlorine and DO, temperature, as well as NTU, illustrating the differences and averages of chlorine levels.
- Predictions of future chlorine levels are based on historical data collected by the sensor.

This tool can be used to simulate and analyze the effectiveness of water disinfection with chlorine, based on important parameters such as temperature and dissolved oxygen. Its functionality offers an experimental approach that can be useful for research laboratories or scientific studies related to water quality and disinfection.

## Installation

1. Ensure that Python and the Tkinter and Matplotlib libraries are installed on your system.
2. Download or clone this repository to your computer.
3. Run the file `engineering_tool.py`.

```bash
python engineering_tool.py
