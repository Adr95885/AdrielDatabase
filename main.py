from flask import Flask, request, jsonify
from database import init_db, add_task, get_tasks
import logging

app = Flask(__name__)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

# Initialize database
init_db()



@app.route("/")
def home():
    logger.info("Home endpoint accessed")
    return "Task API is running"


@app.route("/tasks", methods=["GET"])
def tasks():
    logger.info("GET /tasks requested")
    return jsonify(get_tasks())


@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    logger.info(f"POST /tasks received: {data}")

    add_task(data["name"])

    logger.info(f"Task saved to database: {data['name']}")

    return {"message": "Task added"}

if __name__ == "__main__":
    logger.info("Starting Flask server...")
    app.run(host="0.0.0.0", port=5000)