# QGen by Muhammad Noman Baig DS017/2024-25
## 🤖 Chat with your SQL database 📊.
## Accurate Text-to-SQL Generation via LLMs using RAG 🔄

<img width="1392" alt="Screenshot 2023-06-23 at 3 49 45 PM" src="./assets/vanna_demo.gif">

# Install

```bash
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

# Configure
Modify the `setup_vanna` function in [vanna_calls.py](./vanna_calls.py) to use your desired Vanna setup.

You can configure secrets in `.streamlit/secrets.toml` and access them in your app using `st.secrets.get(...)`.

# Run

```bash
streamlit run app.py
```


## License
[MIT](https://choosealicense.com/licenses/mit/)
