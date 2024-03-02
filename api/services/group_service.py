from sqlalchemy import text

from api.db import db

def create_new_group(
    group_name: str,
    group_description: str | None,
):
    new_group = {
        "group_name": group_name,
        "group_description": group_description if group_description else ""
    }
    sql = text(
        """
        INSERT INTO groups (group_name, group_description)
        VALUES (:group_name, :group_description)
        """
    )

    db.session.execute(sql, new_group)
    db.session.commit()

    return True, "Added group succesfully"