import functools

from flask import flash, g, redirect, url_for


def login_required(view):
    """
    This decorator returns a new view function that wraps 
    the original view it’s applied to. The new function checks 
    if a user is loaded and redirects to the login page otherwise. 
    If a user is loaded the original view is called and continues 
    normally. You’ll use this decorator when writing the blog views.
    """
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        flash("Необходима авторизация!")
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view