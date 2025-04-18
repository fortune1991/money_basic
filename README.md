# Money Pots  

## Video Demo:  
<https://www.youtube.com/watch?v=9nUeLk2rJWc&ab_channel=MichaelFortune>  

## Description:  
Money Pots is a budgeting calculator designed for travelers. It allows users to divide their savings into "Vaults" and "Pots" to better manage their funds. A detailed explanation of its functionality is provided upon execution.  

The program's user interface (UI) is inspired by text-based adventure games, prompting users to input data through a series of interactive questions.  

## OOP and Design Principles  
One of the key goals of this project was to gain a deeper understanding of Object-Oriented Programming (OOP). The core elements—**User, Pot, Vault, and Transactions**—are implemented as class objects. These classes include instance and class methods that calculate updated values for Vaults and Pots.  

A key feature of the program is that users can create as many Vaults or Pots as they like. The **step-by-step instantiation** of these objects ensures they are linked correctly based on user input. **Error handling** was also carefully considered as part of the approach.  

At this stage, the primary development focus was ensuring that these objects interact within the expected hierarchy. As the program evolved, I also identified opportunities to consolidate reusable code into functions, improving the clarity and efficiency of the `main()` function.  

## Code Structure  
The codebase is organized into three main files:  

- **`project.py`** – Contains the main function along with three additional user-defined functions. 
- **`project_classes.py`** – Houses all class definitions and associated methods.  
- **`project_functions.py`** – Includes supplementary user-defined methods. This separation enhances code maintainability.

## Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/fortune1991/money_basic.git
   cd money_basic

2. **Run the application**:
    ```bash
    python3 project.py

## Future Development  
Currently, the program is implemented in its simplest form, primarily modeling interactions between transactions, pots, and vaults. Some additional data, such as transaction dates, is collected but not yet integrated into the logic.  

The next phase of development aims to expand its functionality into **budget forecasting and financial modeling**. To achieve this, a database will be introduced—initially using **CSV files** and later transitioning to **SQL**.  

Further to the database integration, I plan to develop the project as below:  

1. **Additional features** provided for "Forecasting", to predict future expenditure and it's impact on budgets 
2. Use **Grafana** to provide realtime analytics from the database
3. Devoloping the programme as a **RESTFUL API** using the Flask framework. This will be deployed and hosted on AWS.
4. Developing a **web application** for broader accessibility, using the Flask Framework. This will be deployed and hosted on AWS.
 
Through these iterations, I hope to explore different disciplines in computer science and continue my learning journey beyond CS50.  



