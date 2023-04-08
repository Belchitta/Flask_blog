from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

users_app = Blueprint("users_app", __name__, static_folder='../static')
USERS = {
    1: {
        'name': "Ivan Bell",
        'person_info': 'Etiam laoreet tortor in nisi laoreet, eu convallis lorem tempus. '
                       'Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. '
                       'Proin vitaeturpis a dui gravida consequat a a elit. Cras aliquet urna a ante ornare feugiat. S'
                       'ed malesuada elit leo, non blandit dui ullamcorper vel.',
    },
    2: {
        'name': "William Nesty",
        'person_info': 'Ut vel ligula vel mi iaculis varius ac malesuada dui. Phasellus mollis eros justo. '
                       'Curabitur tristique purus sagittis nisi viverra ultricies. '
                       'Nunc a ante sed erat porttitor sagittis. Nulla sagittis turpis a orci eleifend, '
                       'a blandit metus tristique. '
                       'Mauris sit amet nulla metus. Sed et lorem sit amet nulla pharetra accumsan.',
    },
    3: {
        'name': "Fridrich Zoltz",
        'person_info': 'Suspendisse posuere blandit tincidunt. Sed nec lacus mi. Suspendisse blandit congue aliquet. '
                       'Donec tempus condimentum commodo. Aenean eu diam accumsan sapien gravida malesuada. '
                       'Mauris lobortis neque in suscipit faucibus. Nam eleifend tellus in pulvinar blandit. '
                       'Sed porta leo a massa rutrum, vitae finibus tortor varius. Nam vehicula diam ex, '
                       'accumsan egestas ipsum porttitor et. '
                       'Vestibulum in enim vitae velit efficitur fringilla blandit ut lacus.',
    },
}


@users_app.route("/", endpoint="list")
def users_list():
    return render_template("users/list.html", users=USERS)


@users_app.route("/<int:user_id>/", endpoint="details")
def user_details(user_id: int):
    try:
        user_data = USERS[user_id]
    except KeyError:
        raise NotFound(f"User #{user_id} doesn't exist!")
    return render_template('users/details.html', user_id=user_id, user_data=user_data)
