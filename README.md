# AI-based Drop-out Prediction and Counseling System

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=for-the-badge&logo=tailwind-css&logoColor=white)
![Chart.js](https://img.shields.io/badge/Chart.js-F64F59?style=for-the-badge&logo=chartdotjs&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)


## Description

This system employs AI to identify students who are at risk of dropping out by examining information such as grades, attendance, and behavior. Teachers and counselors can provide early intervention and focused support by identifying at-risk students on a dashboard, increasing student success and retention.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Tech Stack / Key Dependencies](#tech-stack--key-dependencies)
- [File Structure Overview](#file-structure-overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage / Getting Started](#usage--getting-started)
- [Demo](#demo)
- [License](#license)


<!-- TODO: Add screenshots if applicable -->

## Features

*   **AI-Powered Prediction:** Predicts student drop-out risk based on academic and behavioral data.
*   **Early Intervention:** Enables timely intervention and support for at-risk students.
*   **Dashboard Visualization:** Presents at-risk students in an easily accessible dashboard.
*   **Data-Driven Insights:** Leverages student data to improve retention rates.

## Tech Stack / Key Dependencies

*   Python
*   HTML
*   Flask (likely, based on `app.py` and `templates` dir)
*   scikit-learn (likely, based on `dropout_model.pkl`, `encoders.pkl`, `scaler.pkl`, `train_model.py`)
*   pandas (likely, based on usage with data and `student_dataset_5000.csv`)

## File Structure Overview

```text
.
├── .gitignore
├── LICENSE
├── app.py
├── dropout_model.pkl
├── encoders.pkl
├── requirements.txt
├── scaler.pkl
├── student_dataset_5000.csv
├── templates
│   └── ... (HTML templates likely reside here)
└── train_model.py
```

## Prerequisites

*   Python 3.6+
*   pip package installer

## Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/girish-indurkar/AI-based-drop-out-prediction-and-counseling-system
    cd AI-based-drop-out-prediction-and-counseling-system
    ```

2.  Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage / Getting Started

1.  Run the Flask application:

    ```bash
    python app.py
    ```

2.  Access the dashboard in your web browser.

<!-- TODO: Add details about building the project (if applicable) -->
<!-- TODO: Add details about running tests (if applicable) -->

## Demo

<img width="1920" height="1020" alt="Screenshot 2025-09-22 184947" src="https://github.com/user-attachments/assets/f03ce58e-9326-4664-866c-5370d27df8c0" />
<img width="1920" height="1020" alt="Screenshot 2025-09-22 185001" src="https://github.com/user-attachments/assets/f66454fc-912e-4f8a-b45d-9939284c16e6" />
<img width="1920" height="1020" alt="Screenshot 2025-09-22 185030" src="https://github.com/user-attachments/assets/846d26fb-9a6e-4b1d-9fed-536ea56f36de" />


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

Distributed under the MIT License. See `LICENSE` file for more information.

