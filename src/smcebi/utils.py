from room.models import Room
from employee.models import Employee

def remove_data():
    Room.objects.all().delete()
    Employee.objects.all().delete()



def assign_employee_to_room(verbose=False):
    try:
        verbose = bool(int(verbose))
    except Exception:
        verbose = False

    for employee in Employee.objects.all():
        emp_room = Room.objects.filter(geom__intersects=employee.geom).first()
        if verbose:
            print('Assigned {emp} to {room}'.format(
                emp=str(employee),
                room=str(emp_room)
            ))
        employee.room = emp_room
        employee.save()
