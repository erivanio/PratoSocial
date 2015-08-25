from apps.website.models import SocialNetwork


def statics(request):
    try:
        social_networks = SocialNetwork.objects.all()[0]
        return {'social': social_networks}
    except:
        return {}

