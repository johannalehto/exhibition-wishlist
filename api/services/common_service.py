from flask import flash, request

def check_missing_fields(required_fields: list) -> bool:
    missing_fields = [
        field.replace("_", " ").capitalize()
        for field in required_fields
        if not request.form.get(field, "").strip()
    ]
    if missing_fields:
        flash(f'Please fill in: {", ".join(missing_fields)}')
        return True
    return False
