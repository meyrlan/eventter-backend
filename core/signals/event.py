from django.db.models.signals import post_save
from django.dispatch import receiver
from core.models import Event


@receiver(post_save, sender=Event, dispatch_uid="add_owner_to_attendees")
def add_owner_to_attendees(sender, instance, created, **kwargs):
    return
    # TODO:
    # print('adkjhsadakhj')
    # event = instance
    # print(event.owner.id)
    # print(event.attendees.all())
    # owner_in_attendees_count = event.attendees.filter(id=event.owner.id).count()
    # print('1')
    # if owner_in_attendees_count == 1:
    #     print('2')
    #     return
    # if owner_in_attendees_count > 1:
    #     print('3')
    #     event.attendees.filter(id=event.owner.id).delete()
    #     event.attendees.add(event.owner)
    #     event.save()
    # if owner_in_attendees_count == 0:
    #     print('4')
    #     event.attendees.add(event.owner)
    #     event.save()
