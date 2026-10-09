from flask import Flask, render_template, request
import boto3
import pymysql
import os
from werkzeug.utils import secure_filename
from uuid import uuid4

app = Flask(__name__)

app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024

bucket_name = "joseph-student-app-files-2026"

db = pymysql.connect(
    host="studentdb1.cn2ueesgyvcd.eu-north-1.rds.amazonaws.com",
    port=3306,
    user="admin",
    password=os.environ.get("DB_PASSWORD"),
    database="studentdb",
    connect_timeout=10
)

s3 = boto3.client("s3")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    name = request.form["name"]
    email = request.form["email"]
    course = request.form["course"]

    photo = request.files.get("photo")

    if not photo or not photo.filename:
        return "Please select a photo.", 400

    filename = secure_filename(photo.filename)

    if not filename:
        return "Invalid photo filename.", 400

    object_key = f"students/{uuid4().hex}_{filename}"

    s3.upload_fileobj(
        photo,
        bucket_name,
        object_key
    )

    photo_url = (
        f"https://{bucket_name}.s3.eu-north-1.amazonaws.com/"
        f"{object_key}"
    )

    try:
        with db.cursor() as cursor:
            sql = """
            INSERT INTO students
            (name, email, course, photo_url)
            VALUES (%s, %s, %s, %s)
            """

            cursor.execute(
                sql,
                (name, email, course, photo_url)
            )

        db.commit()

    except Exception:
        db.rollback()
        raise

    return "Student Registered Successfully"


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
