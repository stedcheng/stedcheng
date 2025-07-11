import streamlit as st
import pandas as pd

st.set_page_config(layout = 'wide')

col1, col2 = st.columns([0.8, 0.2])
with col1:
    # st.title('Sted Micah T. Cheng')
    st.markdown('''
        <h1 style='margin-top: -40px;'>Sted Micah T. Cheng</h1>
    ''', unsafe_allow_html=True)
with col2:
    st.markdown('''<div style='display: flex; gap: 10px;'>
    <a href='https://github.com/stedcheng' target='_blank'>
        <img src='https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png' alt='GitHub' width='30'>
    </a>
    <a href='https://www.linkedin.com/in/sted-micah-cheng/' target='_blank'>
        <img src='https://content.linkedin.com/content/dam/me/business/en-us/amp/xbu/linkedin-revised-brand-guidelines/in-logo/fg/brand-inlogo-download-fg-dsk-v01.png/jcr:content/renditions/brand-inlogo-download-fg-dsk-v01-2x.png' alt='LinkedIn' width='30'>
    </a>
</div>''', unsafe_allow_html=True)

date_format = st.sidebar.selectbox('Date Format', ['YYYY-MM-DD', 'MMMM YYYY', 'YYYY', 'DD MMMM YYYY', 'MMMM DD, YYYY'])

def date_formatter(option, dates):
    if not isinstance(dates, list):
        dates = [dates]
    formatted_dates = []
    for date in dates:
        date = pd.to_datetime(date)
        if option == 'MMMM DD, YYYY':
            formatted = date.strftime('%B %d, %Y')
        elif option == 'YYYY':
            formatted = date.strftime('%Y')
        elif option == 'DD MMMM YYYY':
            formatted = date.strftime('%d %B %Y')
        elif option == 'MMMM YYYY':
            formatted = date.strftime('%B %Y')
        else:
            formatted = date.strftime('%Y-%m-%d')
        formatted_dates.append(formatted)
    return formatted_dates

tab1, tab2, tab3 = st.tabs(['CV', '2', '3'])

def layout(experience_type, title, event, institution, start_date, end_date, description):
    col1, col2 = st.columns([0.8, 0.2])
    with col1:
        if experience_type in ['Work', 'Education']:
            st.write(f'**{title}** at {institution}')
        elif experience_type == 'Certification':
            st.write(f'**{title}**, issued by {institution}')
        elif experience_type == 'Examination':
            st.write(f'Passer of **{title}**, issued by {institution}')
        elif experience_type == 'Project':
            st.write(f'**{title}**')
        elif experience_type == 'Achievement':
            st.write(f'**{title}**, *{event}*, issued by {institution}')
    with col2:
        if end_date == None:
            formatted_dates = date_formatter(date_format, [start_date])
            st.write(f'{formatted_dates[0]}')
        elif end_date == 'Present':
            formatted_dates = date_formatter(date_format, [start_date, pd.to_datetime('today').strftime('%Y-%m-%d')])
            st.write(f'{formatted_dates[0]} – Present')
        else:
            formatted_dates = date_formatter(date_format, [start_date, end_date])
            st.write(f'{formatted_dates[0]} – {formatted_dates[1]}')
    st.write(description)

with tab1:
    st.header('Work Experience')

    layout('Work', 'Education Innovation Fellowship Intern', None, 'Eskwelabs', '2025-01-17', '2025-03-28',
           '''- Consolidated and created insights based on evaluation data from 10+ iterations of a product management bootcamp
- Automated report creation from 30+ evaluation questions in 4 minutes using Python, ChatGPT & Google Slides API
- Developed a dashboard with Streamlit to assign 400+ facilitators to seminars, based on schedules, skills, & ratings''')

    layout('Work', 'Power BI Developer - Metrics Dashboard Intern', None, 'MSCI', '2024-06-03', '2024-08-08',
           '''- Extracted incident management, client requests, and project tracker data from cloud softwares ServiceNow, Salesforce, and Jira
- Created and automated charts and **dashboards** in Power BI based on metrics used in the team's monthly progress updates, replacing manual processes for internal improvement
- Collaborated in the documentation process of the database columns used in charting
- Demonstrated dashboard usage and explained its benefits to MSCI Manila, together with a cointern''')

    layout('Work', 'Freelance Math Expert', 'Photomath', None, '2021-07-13', '2022-06-13',
           '''- Crafted solutions to grade school and high school math problems
- Created illustrations to enhance understanding of math concepts''')

    st.header('Education')

    layout('Education', 'Master in Data Science', None, 'Ateneo de Manila University', '2025-06-09', 'Present',
           '''- Coursework: Data Visualization, Advanced Time Series and Forecasting''')

    layout('Education', 'Bachelor of Science in Applied Mathematics with Specialization in Data Science',
           None, 'Ateneo de Manila University', '2021-08-26', '2025-05-24',
           '''- Director’s List Scholar: Php 50,000 semestral grant given by the Ateneo Office of Admission and Aid to 200 students per batch
- GPA 3.89/4.00 (Summa Cum Laude)
- Program Awardee
- First Dean's Lister (3.7+) every semester
- Coursework:
  - Mathematics: Advanced Calculus, Linear Algebra, Probability Theory, Numerical Analysis, Operations Research, Ordinary Differential Equations,
  Statistical Theory, Theory of Interest, Time Series and Forecasting
  - Data Science: Artificial Intelligence, Business Intelligence, Databases, Probabilistic Machine Learning, Simulation and Modeling, Text Analysis
  - Economics: Data Science for Economists, Microeconomic Theory, Macroeconomic Theory, International Finance''')

    st.header('Certifications')
    
    layout('Certification', 'Data Analyst Associate', None, 'Datacamp', '2025-01-13', None, 
           '''- Certification
- More details to follow''')

    layout('Certification', 'Associate Data Analyst in SQL', None, 'Datacamp', '2025-01-06', None,
           '''- Series of courses dealing with...
- More details to follow''')

    layout('Certification', 'Data Analyst in Python', None, 'Datacamp', '2024-12-28', None,
           '''- Series of courses dealing with...
- More details to follow''')

    layout('Examination', 'Traditional Life Insurance', None, 'Sun Life', '2025-01-06', None, '')


    st.header('Projects')

    layout('Project', 'Bayesian Network Implementation on Nutritional Data to Predict the Nutrient Adequacy of Filipino Schoolchildren',
           None, None, '2024-08-07', '2025-05-24', '''- For the course *Undergraduate Thesis in Applied Mathematics* (MATH 199.11/199.12)
- Applied Bayesian networks using GeNIe on a nutrition dataset containing demographic, food consumption, and nutrient adequacy variables, and made contextualized recommendations for dietary interventions based on numerical relationships between nodes''')

    layout('Project', 'Rage, Regret, and Repentance: A Psycho-linguistic Analysis of Inmates\' Last Statements',
           None, None, '2024-08-07', '2024-12-07', '''- Final project for the course *Data Analytics for Text Analysis* (PSYC 80.18i)
- Performed clustering by demographics, using Latent Dirichlet Allocation, on a dataset of Texas inmates' last words''')

    layout('Project', 'Unveiling the Enablers: Analyzing the Persistence of Dynasties in Local Philippine Politics',
           None, None, '2024-08-07', '2024-12-07', '''- Final project for the course *Data Science for Economists* (ECON 185.78i)
- Utilized OLS and geospatial regression to predict Philippine political dynastic index based on economic factors''')

    layout('Project', 'Enlistment Tool for Ateneans', None, None, '2022-01-23', '2024-07-04',
           '''- Identified the lack of innovation in the enlistment portal and continually thinking of ideas to better serve students
- Scheduler: Allowed 600+ students to search for classes quickly by systematically removing conflicting classes
- Syllabus Viewer: Automated via Python a pattern in course syllabi links, helping 1000+ students choose electives and professors
- Schedule Checker for Classrooms and Professors: Integrated schedule tables to inform students of classes handled by a certain professor or taken in a certain room''')

    layout('Project', 'Developing Product Placement Strategies for e-Commerce Using Clickstream Data', None, None, '2024-01-15', '2024-05-18',
           '''- Final project for the course *Business Intelligence* (CSCI 113)
- Performed k-means and hierarchical clustering on a clothing store’s online clickstream dataset in UCI, and utilized understanding on customer behavior for screen-clicking location to create recommendations''')

    layout('Project', 'Cyberbullying Detection in Tweets using Machine Learning Algorithms and Convolutional Neural Networks', None, None, '2023-08-09', '2023-12-12',
           '''- Final project for the course *Predictive Modeling for Text* (MATH 103.1)
- Used natural language preprocessing techniques and convolutional neural networks to classify cyberbullying tweets''')

    layout('Project', 'TENTATIVE NAME', None, None, '2023-08-09', '2023-12-12',
           '''- Final project for the course *Artificial Intelligence* (CSCI 111)
- Performed feature engineering, k-nearest neighbors, and random forest on UCI's Seoul Bike Sharing dataset''')

    layout('Project', 'Brand Marketing Strategies and the Competition Between Two Clothing Brands', None, None, '2023-01-16', '2023-05-20',
           '''- Final project for the course *Computer Simulation and Modeling* (CSCI 115)
- Developed an agent-based model with AgentPy about effects of brand marketing strategies on consumer behavior''')

    layout('Project', 'How was Your Order? Querying Transaction Data from a Generated Database based on a Food Delivery App Use Case', None, None, '2022-08-15', '2022-12-10',
           '''- Final project for the course *Contemporary Databases* (CSCI 112)
- Used MongoDB to analyze a food delivery company’s database, containing restaurants, customers, riders, menu items; derived insights for future action''')

    st.header('Achievements')

    layout('Achievement', 'Finalist', 'Ateneo Socio-Civic Engagement for National Development (ASCEND) Awards', 'ASCEND Committee',
           '2025-06-13', None, ('- Member of one of the finalists of the ASCEND Awards'
                                'for the NSTP project entitled "Higit Pa sa Titik: A Literacy Tutorial and Enhancement Program for Primary Students from STMTOPSI'))

    layout('Achievement', '5th Place', 'Search for Collegiate Math Whizz', 'Mathematical Society of the Philippines - NCR', '2025-05-16', None,
           '- Bested more than 50 participants from different universities, reached the final round')

    layout('Achievement', 'Nominee', 'Outstanding Student Research Award', 'Ateneo de Manila University - School of Science and Engineering',
           '2025-05-09', None, ('- Member of one of the 21 teams admitted to the final round of the Outstanding Student Research Award, a sub-event of the annual School of Science and Engineering Week, '
                                'for the undergraduate thesis entitled *Bayesian Network Implementation on Nutritional Data to Predict the Nutrient Adequacy of Filipino Schoolchildren*'))





    


    
