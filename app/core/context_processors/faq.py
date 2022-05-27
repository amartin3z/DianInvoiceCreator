from app.core.models import SatFaq


def faq(request, *args, **kwargs):

    sat_faq_obj = SatFaq.objects.filter(can_show=True)
    result = {'faqs': sat_faq_obj}
    return result