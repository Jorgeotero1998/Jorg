# Sentinel-Log Framework v2.0 🛡️⚡
### Python Automation Engineer | Cybersecurity & SOC Analyst

## 📖 Project Overview
Sentinel-Log is a high-performance telemetry simulation and forensic auditing engine. This repository demonstrates the integration of **Automated Security Operations (SecOps)** with large-scale data integrity challenges. 

The system simulates an EDR-like environment, generating high-frequency system heartbeats and audit trails to test log ingestion and repository scalability.

## 🛡️ Key Focus Areas
* **Threat Detection & Telemetry:** Real-time simulation of system events and security logs.
* **Forensic Auditing:** Structured event logging designed for SIEM-ready environments.
* **Git-Based Data Persistence:** Utilizing the Git index as a high-frequency event database.

## 🛠️ Technical Stack
* **Python (Expert):** Core engine for log generation and system monitoring.
* **Security Ops:** Simulation of SOC workflows and forensic traceability.
* **Infrastructure:** Scalable Git architecture for handling 15,000+ atomic commits.

## 🧠 Engineering Challenges & Learning Outcomes
* **Scalability & I/O Performance:** We pushed the Git index to its limits, managing over 15k commits. This taught us deep lessons about **File System Race Conditions** in Windows and index-locking mechanisms.
* **Data Integrity:** Developing mechanisms to ensure that every "heartbeat" is uniquely traceable andforensically sound across a long-term timeline.
* **Automation Excellence:** Building a seamless pipeline that converts raw system events into structured, documented history without manual overhead.

---
*Developed by Jorge Otero - Specializing in Automation and Digital Security.*
