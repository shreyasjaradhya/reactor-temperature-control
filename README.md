# Closed-Loop Thermal Regulation & Predictive Temperature Control for Batch Reactors

[![Language: Python](https://img.shields.io/badge/Language-Python%203.x-3776AB.svg?logo=python)]()
[![Domain: Control Systems](https://img.shields.io/badge/Domain-Industrial%20Process%20Control-blue.svg)]()
[![Context: Manipal Internship](https://img.shields.io/badge/Context-Engineering%20Internship%20Manipal-purple.svg)]()

> Dynamic simulation and closed-loop thermal regulation model for industrial batch chemical reactors exhibiting high thermal inertia, non-linear jacket heat exchange, and transport dead-time lags, comparing Bang-Bang, Anti-Windup PID, and Adaptive Predictive control strategies.

---

## 👤 Author
* **J Shreyas Aradhya** — Electronics & Communication Engineering
* **Affiliation**: NMAMIT & Engineering Internship (Manipal Batch Reactor Project)

---

## 🔬 Mathematical Process Modeling

$$\frac{dT_r}{dt} = \frac{UA}{M c_p} (T_j - T_r) + \frac{(-\Delta H) V r_A}{M c_p}$$
Where:
* $T_r$: Reactor internal temperature ($^\circ\text{C}$)
* $T_j$: Jacket coolant/heating fluid temperature ($^\circ\text{C}$)
* $UA$: Overall heat transfer coefficient ($W/K$)
* $M, c_p$: Reactor mixture mass and specific heat capacity
* $(-\Delta H) r_A$: Exothermic reaction enthalpy generation term

---

## 📁 Repository Structure
```
├── docs/
│   └── Adaptive_Ensemble_Reinforcement_Learning.pdf  # Technical research reference paper
├── src/
│   ├── reactor_control_sim.py                         # Full thermal simulation script
│   └── pid_controller.py                              # Anti-windup PID controller class
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```
