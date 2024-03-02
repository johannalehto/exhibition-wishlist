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

def add_user_to_group(user_id: int, group_id: int):
    new_join = {"user_id": user_id, "group_id": group_id}
    sql = text(
        """
        INSERT INTO groups_users (user_id, group_id)
        VALUES (:user_id, :group_id)
        """
    )
    db.session.execute(sql, new_join)
    db.session.commit()


def remove_user_from_group(user_id: int, group_id: int):
    sql = text(
        """
        DELETE FROM groups_users
        WHERE user_id = :user_id AND group_id = :group_id
        """
    )
    db.session.execute(
        sql, {"user_id": user_id, "group_id": group_id}
    )
    db.session.commit()

def get_groups_by_user_id(query_user_id) -> list:
    sql = text(
        """
        SELECT g.id, g.group_name, g.group_description
        FROM groups g
        JOIN groups_users gu ON g.id = gu.group_id
        JOIN users u ON gu.user_id = u.id
        WHERE u.id = :query_user_id;
        """
    )

    result = db.session.execute(
        sql, {"query_user_id": query_user_id}
    )
    groups_by_user_id = result.fetchall()
    return groups_by_user_id

def get_group_members(query_group_id: int) -> list:
    sql = text(
        """
        SELECT u.id, u.username, u.first_name, u.profile_picture_url
        FROM users u
        JOIN groups_users gu ON gu.user_id = u.id
        JOIN groups g ON g.id = gu.group_id
        WHERE g.id = :query_group_id;
        """
    )

    result = db.session.execute(
        sql, {"query_group_id": query_group_id}
    )
    group_members = result.fetchall()
    return group_members

def get_all_groups_by_user(user_id: int) -> list:
    groups_by_user_id_from_db = get_groups_by_user_id(user_id)
    all_groups_by_user = []
    for group_db in groups_by_user_id_from_db:
        group = group_db._asdict()
        group["members"] = get_group_members(group["id"])
        all_groups_by_user.append(group)
    return all_groups_by_user

def get_all_groups(query_user_id: int) -> list:
    # gets all the groups user is not a member of
    sql = text(
        """
        SELECT g.id, g.group_name, g.group_description
        FROM groups g
        WHERE NOT EXISTS (
            SELECT 1
            FROM groups_users gu
            WHERE gu.group_id = g.id AND gu.user_id = :query_user_id
            )
        """
    )

    result = db.session.execute(
        sql, {"query_user_id": query_user_id}
    )
    all_groups = result.fetchall()
    return all_groups

