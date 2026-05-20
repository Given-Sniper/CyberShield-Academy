from app.extensions import db


def log_activity(activity_type, user_id=None, admin_id=None, reference_type=None, reference_id=None, details=None):
    from app.models.activity import Activity

    try:
        activity = Activity(
            activity_type=activity_type,
            user_id=user_id,
            admin_id=admin_id,
            reference_type=reference_type,
            reference_id=reference_id,
            activity_details=details,
        )
        db.session.add(activity)
        db.session.commit()
        return activity
    except Exception:
        db.session.rollback()
        raise
