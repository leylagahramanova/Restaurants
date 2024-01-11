from django.shortcuts import render

from .models import Restaurant1
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import EmptyTables
def restaurant1(request):
    reservations = Restaurant1.objects.prefetch_related('empty_tables')
    return render(request, 'resta1.html', {'reservations': reservations})

def delete_table(request):
    if request.method == 'POST':
        table_id = request.POST.get('table_id')
        selected_date = request.POST.get('date')
        selected_time_slot = request.POST.get('time_slot')
        selected_inside_table = request.POST.get('inside_table')
        selected_outside_table = request.POST.get('outside_table')

        try:
            # Ensure that the values are not empty and are valid numbers
            selected_inside_table = int(selected_inside_table)
            selected_outside_table = int(selected_outside_table)

            # Retrieve the table based on the selected parameters
            table = get_object_or_404(
                EmptyTables,
                restaurant__date=selected_date,
                time_slot=selected_time_slot,
                num_empty_tables_inside=selected_inside_table,
                num_empty_tables_outside=selected_outside_table
            )

            # Delete the table record
            table.delete()

            return JsonResponse({'message': 'Table deleted successfully'})
        except ValueError:
            return JsonResponse({'error': 'Invalid values for inside_table or outside_table'})
        except EmptyTables.DoesNotExist:
            return JsonResponse({'error': 'Table does not exist'})
    else:
        return JsonResponse({'error': 'Invalid request method'})