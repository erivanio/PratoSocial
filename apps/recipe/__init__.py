from apps.recipe.models import CommentWithPic
from apps.recipe.forms import CommentFormWithPic

def get_model():
    return CommentWithPic

def get_form():
    return CommentFormWithPic