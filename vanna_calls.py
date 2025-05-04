import streamlit as st
from vanna.remote import VannaDefault

@st.cache_resource(ttl=3600)
def setup_vanna():
    vn = VannaDefault(
        api_key=st.secrets["vn-a742f15f67254df584aa8260e350d666"],
        model="chinook"
    )

    # Use raw GitHub link (important: raw file, not blob view)
    vn.connect_to_sqlite("https://raw.githubusercontent.com/nomanbaig98/QGen/main/Chinook.sqlite")

    # Train with some example Q&A pairs
    training_examples = [
        {
            "question": "What are the top 5 artists by number of albums?",
            "sql": "SELECT Artist.Name, COUNT(*) AS AlbumCount FROM Album JOIN Artist ON Album.ArtistId = Artist.ArtistId GROUP BY Artist.Name ORDER BY AlbumCount DESC LIMIT 5;"
        },
        {
            "question": "List all album titles.",
            "sql": "SELECT Title FROM Album;"
        },
        {
            "question": "Which customers are from Brazil?",
            "sql": "SELECT FirstName, LastName FROM Customer WHERE Country = 'Brazil';"
        },
        {
            "question": "Show the total number of invoices.",
            "sql": "SELECT COUNT(*) FROM Invoice;"
        },
        {
            "question": "What is the total sales amount?",
            "sql": "SELECT SUM(Total) AS TotalSales FROM Invoice;"
        },
        {
            "question": "What is the average invoice total?",
            "sql": "SELECT AVG(Total) AS AverageTotal FROM Invoice;"
        },
        {
            "question": "List all tracks in the 'Rock' genre.",
            "sql": "SELECT Name FROM Track JOIN Genre ON Track.GenreId = Genre.GenreId WHERE Genre.Name = 'Rock';"
        }
    ]

    vn.train(question_sql_pairs=training_examples)
    return vn

@st.cache_data(show_spinner="Generating sample questions ...")
def generate_questions_cached():
    vn = setup_vanna()
    try:
        return vn.generate_questions()
    except Exception as e:
        st.warning("Could not generate suggested questions. Check training or DB.")
        return []

@st.cache_data(show_spinner="Generating SQL query ...")
def generate_sql_cached(question: str):
    vn = setup_vanna()
    return vn.generate_sql(question=question, allow_llm_to_see_data=True)

@st.cache_data(show_spinner="Checking for valid SQL ...")
def is_sql_valid_cached(sql: str):
    vn = setup_vanna()
    return vn.is_sql_valid(sql=sql)

@st.cache_data(show_spinner="Running SQL query ...")
def run_sql_cached(sql: str):
    vn = setup_vanna()
    return vn.run_sql(sql=sql)

@st.cache_data(show_spinner="Checking if we should generate a chart ...")
def should_generate_chart_cached(question, sql, df):
    vn = setup_vanna()
    return vn.should_generate_chart(df=df)

@st.cache_data(show_spinner="Generating Plotly code ...")
def generate_plotly_code_cached(question, sql, df):
    vn = setup_vanna()
    return vn.generate_plotly_code(question=question, sql=sql, df=df)

@st.cache_data(show_spinner="Running Plotly code ...")
def generate_plot_cached(code, df):
    vn = setup_vanna()
    return vn.get_plotly_figure(plotly_code=code, df=df)

@st.cache_data(show_spinner="Generating followup questions ...")
def generate_followup_cached(question, sql, df):
    vn = setup_vanna()
    return vn.generate_followup_questions(question=question, sql=sql, df=df)

@st.cache_data(show_spinner="Generating summary ...")
def generate_summary_cached(question, df):
    vn = setup_vanna()
    return vn.generate_summary(question=question, df=df)
