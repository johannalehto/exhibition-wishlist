from flask import flash, request
from sqlalchemy import text
from datetime import datetime

from api.db import db


def add_user_to_exhibition(user_id, exhibition_id):
    new_join = {
        "user_id": user_id,
        "exhibition_id": exhibition_id
    }
    sql = text(
        """
        INSERT INTO users_exhibitions (user_id, exhibition_id)
        VALUES (:user_id, :exhibition_id)
        """
    )
    db.session.execute(sql, new_join)
    db.session.commit()

def remove_user_from_exhibition(user_id, exhibition_id):
    sql = text(
        """
        DELETE FROM users_exhibitions
        WHERE user_id = :user_id AND exhibition_id = :exhibition_id
        """
    )
    db.session.execute(sql, {"user_id": user_id, "exhibition_id": exhibition_id})
    db.session.commit()

def get_days_left(exhibition_end_date):
    today = datetime.now().date()
    delta = exhibition_end_date - today
    return delta.days


def get_museums() -> list:
    sql = text("SELECT museum_name FROM museums ORDER BY museum_name")
    result = db.session.execute(sql)
    museums = result.fetchall()
    return [museum[0] for museum in museums]

def get_attendees(query_exhibition_id) -> list | None:
    sql = text(
        """
        SELECT u.id, u.username, u.first_name, u.profile_picture_url
        FROM users u
        JOIN users_exhibitions ue ON u.id = ue.user_id
        JOIN exhibitions e ON ue.exhibition_id = e.id
        WHERE e.id = :query_exhibition_id;
        """
    )

    result = db.session.execute(sql, {"query_exhibition_id": query_exhibition_id})
    all_attendees = result.fetchall()
    return all_attendees

def get_exhibitions():
    sql = text(
        """
        SELECT e.id, e.exhibition_name, e.start_date, e.end_date, m.museum_name
        FROM exhibitions e
        JOIN museums m ON e.museum_id = m.id
    """
    )
    result = db.session.execute(sql)
    all_exhibitions_from_db = result.fetchall()

    all_exhibitions = []
    for db_exhibition in all_exhibitions_from_db:
        exhibition = db_exhibition._asdict()

        exhibition['days_left'] = get_days_left(exhibition['end_date'])
        exhibition['attendees'] = get_attendees(exhibition['id'])


        all_exhibitions.append(exhibition)

    return all_exhibitions


def handle_museum(museum_name: str) -> int:
    sql = text("SELECT id FROM museums WHERE museum_name = :museum_name")
    result = db.session.execute(sql, {"museum_name": museum_name})
    existing_museum_id = result.fetchone()

    if existing_museum_id:
        return existing_museum_id[0]
    else:
        sql = text(
            "INSERT INTO museums (museum_name) VALUES (:museum_name) RETURNING id"
        )
        result = db.session.execute(sql, {"museum_name": museum_name})
        new_museum_id = result.fetchone()
        db.session.commit()
        return new_museum_id[0]


def check_missing_fields():
    required_fields = ["exhibition_name", "museum_name", "start_date", "end_date"]

    missing_fields = [
        field.replace("_", " ").capitalize()
        for field in required_fields
        if not request.form.get(field, "").strip()
    ]
    if missing_fields:
        flash(f'Please fill in: {", ".join(missing_fields)}')
        return True
    return False


def create_new_exhibition(
    exhibition_name,
    museum_name,
    start_date,
    end_date,
):

    museum_id = handle_museum(museum_name)

    new_exhibition = {
        "exhibition_name": exhibition_name,
        "museum_id": museum_id,
        "start_date": start_date,
        "end_date": end_date,
    }
    sql = text(
        """
        INSERT INTO exhibitions (exhibition_name, museum_id, start_date, end_date)
        VALUES (:exhibition_name, :museum_id, :start_date, :end_date)
        """
    )

    db.session.execute(sql, new_exhibition)
    db.session.commit()

    return True, "Added exhibition succesfully"
