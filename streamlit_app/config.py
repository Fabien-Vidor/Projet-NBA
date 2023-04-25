"""

Config file for Streamlit App

"""

from member import Member


TITLE = "Projet NBA"

TEAM_MEMBERS = [
    Member(
        name="Leo Ferretti",
        linkedin_url="https://www.linkedin.com/in/leo-ferretti-18042724b",
        github_url="https://github.com/LeoF57/",
    ),
    Member(
        name="Florian Lluch",
        linkedin_url="https://www.linkedin.com/in/florian-lluch/",
        github_url="https://github.com/Lluchi/",
    ),
    Member(
        name="Alex Randrianantoandro",
        linkedin_url="https://www.linkedin.com/in/alex-randrianantoandro-8935ab179/",
        github_url="https://github.com/AlexRandria",
    ),
    Member(
        name="Fabien Vidor",
        linkedin_url="https://www.linkedin.com/in/fabien-vidor/",
        github_url="https://github.com/Fabien-Vidor/",
    ),
]

PROMOTION = "Promotion Bootcamp Data Scientist - February 2023"
