# Logistics-Analysis-Platform

##  Project Overview
The **Logistics Analysis Platform** is an end-to-end data analytics and visualization tool designed to transform fragmented supply chain and shipment records into actionable route-level operational intelligence. 

Logistics networks often struggle with invisible bottlenecks, inconsistent delivery lead times, and unoptimized transit modes. This platform reconstructs origin-to-destination shipping corridors, benchmarks transit performance against geographical distance, and pinpoints congestion-prone delivery regions.

##  Key Problems Solved
* **Route Reconstruction & Efficiency Scoring:** Normalizes delivery lead times across factory-to-customer corridors to rank top- and bottom-performing lanes.
* **Geographic Bottleneck Detection:** Identifies destination states and transit corridors experiencing high lead-time variability and chronic delivery delays.
* **Ship Mode Tradeoff Analysis:** Evaluates delivery speed vs. cost tradeoffs across shipping tiers to identify SLA breaches and misallocated expedited freight.
* **Interactive Decision Support:** Provides an interactive dashboard with origin-destination spatial mapping, dynamic SLA threshold filtering, and route drill-downs.

##  Tech Stack
* **Language:** Python
* **Data Processing & Analysis:** Pandas, NumPy
* **Visualization & Mapping:** Plotly, Pydeck / GeoPandas
* **Interactive Dashboard:** Streamlit
