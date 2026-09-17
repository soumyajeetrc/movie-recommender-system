# 🎬 Movie Recommender System

A **Content-Based Movie Recommender System** built with Python and Streamlit.  
The application recommends movies based on the similarity between the selected movie and other movies in the dataset.

## 🚀 Live Demo

👉 **[Try the Movie Recommender System](https://movie-recommender-system-ndusfct7v7roxpqu7h9r3q.streamlit.app/)**

> https://movie-recommender-system-ndusfct7v7roxpqu7h9r3q.streamlit.app/

## 📌 Project Overview

This project provides a simple and interactive movie recommendation experience. Users select a movie from the available list, and the system returns **five similar movies** along with their posters.

The recommendation engine uses a precomputed similarity matrix and retrieves movie poster information from the **TMDB API**.

## ✨ Features

- 🎥 Select a movie from a searchable dropdown
- 🤖 Content-based movie recommendations
- 🔎 Returns the top 5 similar movies
- 🖼️ Fetches movie posters using the TMDB API
- 🌐 Interactive Streamlit web interface
- ☁️ Deployed using Streamlit Community Cloud
- 🔐 API credentials managed using Streamlit Secrets
- 📦 Large similarity model stored using Git LFS

## 🧠 How It Works

The application follows this workflow:

```text
User selects a movie
        ↓
Find the selected movie in the movie dataset
        ↓
Retrieve its similarity scores
        ↓
Rank movies by similarity
        ↓
Select the top 5 recommendations
        ↓
Fetch movie posters from TMDB
        ↓
Display recommendations in Streamlit
```

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application and user interface |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Requests | TMDB API requests |
| Pickle | Loading the preprocessed data and similarity matrix |
| TMDB API | Movie poster information |
| Git & GitHub | Version control and source code hosting |
| Git LFS | Storage of the large similarity matrix |
| Streamlit Community Cloud | Application deployment |

## 📂 Project Structure

```text
movie-recommender-system/
│
├── app.py                  # Main Streamlit application
├── movie_dict.pkl          # Preprocessed movie data
├── movies.pkl              # Movie dataset
├── similarity.pkl          # Precomputed movie similarity matrix
├── requirements.txt        # Python dependencies
├── Procfile                # Application configuration
├── setup.sh                # Setup configuration
├── .gitattributes          # Git LFS configuration
├── .gitignore              # Ignored files and secrets
└── README.md               # Project documentation
```

## ⚙️ Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/soumyajeetrc/movie-recommender-system.git
cd movie-recommender-system
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

**Windows:**

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the TMDB API key

Create:

```text
.streamlit/secrets.toml
```

Add:

```toml
TMDB_API_KEY = "YOUR_TMDB_API_KEY"
```

Never commit `secrets.toml` or expose your API key publicly.

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🔐 Security

The TMDB API key is **not stored in the GitHub repository**. For deployment, it is configured through Streamlit Community Cloud Secrets.

The local `.streamlit/secrets.toml` file is excluded through `.gitignore`.

## ☁️ Deployment

The application is deployed through **Streamlit Community Cloud** using the `main` branch of this GitHub repository.

```text
PyCharm
   ↓
Git
   ↓
GitHub
   ↓
Git LFS
   ↓
Streamlit Community Cloud
   ↓
Live Web Application
```

## 🔮 Future Improvements

- Add movie genres and release year filters
- Display movie ratings and descriptions
- Add movie search functionality
- Improve recommendation quality using additional metadata
- Add user-based or collaborative filtering
- Add recommendation explanations
- Improve the visual design and responsiveness
- Add caching to reduce repeated API requests

## 👨‍💻 Author

**Soumyajeet Roy Chowdhury**

B.Tech — Computer Science Engineering (Data Science)

GitHub:  
https://github.com/soumyajeetrc

## 📄 License

This project is intended for educational and portfolio purposes.
