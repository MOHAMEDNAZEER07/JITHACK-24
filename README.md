```markdown
# Farmer's Delight - Empowering Farmers with Technology

**Farmer's Delight** is a comprehensive web platform designed to assist farmers in making informed decisions for their agricultural endeavors. By leveraging machine learning, real-time data, and expert knowledge, the platform provides three core features: crop recommendations, vegetable price prediction, and a plant care assistant. This innovative solution aims to improve farm productivity, optimize market prices, and provide quick plant care guidance, all tailored to the needs of modern farmers.

## Key Features

### 🌾 **Crop Recommendation System**
- Utilizes a **Random Forest regression model** to recommend suitable crops based on environmental factors such as temperature, season, and disaster occurrences.
- The model analyzes historical data to suggest the most profitable crops, enabling farmers to plan their crops better and increase yields.

### 💰 **Vegetable Price Prediction**
- Predicts the prices of various vegetables based on features like season, month, temperature, and past market data.
- Helps farmers make informed decisions about when to harvest and sell crops to maximize profitability and reduce losses.

### 🌱 **Plant Doctor**
- A plant care assistant where farmers can submit queries regarding plant diseases, symptoms, and care.
- Provides expert guidance through an AI-powered system based on pre-trained models, helping farmers address plant health issues promptly.

### 🖥️ **User-Friendly Interface**
- The platform is designed to be intuitive and accessible for farmers with minimal technical knowledge, featuring an easy-to-navigate interface powered by **Bootstrap 5.3.2**.
- Real-time predictions and crop recommendations are just a few clicks away, making it easy for farmers to use the platform in their daily routines.

## Technologies Used

- **Backend:**
  - **Django 5.0.6**: A robust and scalable web framework that powers the server-side logic and business rules of the platform.
  - **Django-Heroku**: For seamless deployment to **Heroku**, ensuring scalability and high availability in the cloud.
  - **Scikit-learn**: Implements machine learning algorithms for vegetable price prediction and crop recommendation.
  - **Joblib**: Efficiently handles the saving and loading of machine learning models.
  - **Gunicorn**: A WSGI server used for serving the Django application in production environments.

- **Frontend:**
  - **HTML** and **CSS**: Used for structuring and styling the platform’s web pages.
  - **Bootstrap 5.3.2**: Provides a responsive and mobile-friendly design.
  - **JavaScript**: Handles user interactions, such as form validation and button actions.

- **Database:**
  - **PostgreSQL**: Stores essential data such as vegetable prices, crop recommendations, and user queries.
  - **Psycopg2**: Allows Python to interface with the PostgreSQL database.

- **Cloud Deployment:**
  - **Heroku**: Hosted on Heroku for fast deployment and scalable cloud infrastructure.

## Installation & Setup

### Prerequisites:
- Python 3.x
- PostgreSQL installed locally or use a cloud service like Heroku for the database.

### Steps to Run Locally:
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/farmers-delight.git
   cd farmers-delight
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up PostgreSQL Database**:
   - Create a new database on PostgreSQL.
   - Update the `DATABASES` setting in `settings.py` with your database credentials.

5. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

7. Open your browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000) to access the platform.


## Contributing

We welcome contributions to enhance the platform! If you have ideas for new features or improvements, feel free to fork the repository and submit a pull request. Before contributing, make sure to:
- Ensure your code adheres to the style and architecture of the project.
- Test your changes thoroughly.
- Submit a detailed description of the changes made.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Django**: A high-level Python web framework that makes rapid development easy.
- **Scikit-learn**: For providing powerful tools to build machine learning models for agricultural predictions.
- **Bootstrap**: For an elegant, responsive design that works across devices.
- **Heroku**: For seamless deployment of web applications in the cloud.

---

**Farmer's Delight** is revolutionizing the agricultural sector by empowering farmers with data-driven insights, allowing them to make smarter decisions, optimize their crops, and improve their livelihoods. Join us on our mission to transform the way farmers interact with technology!
```
