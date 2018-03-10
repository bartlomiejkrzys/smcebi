#!/bin/bash
project_path=/code/smcebi

echo "INFO: Loading rooms from .shp file"

echo "from room.load import main; main($VERBOSE)" | python $project_path/manage.py shell
echo "from employee.load import main; main($VERBOSE)" | python $project_path/manage.py shell

echo "INFO: Assigning employees to rooms."

echo "from utils import assign_employee_to_room; assign_employee_to_room($VERBOSE)" | python $project_path/manage.py shell
