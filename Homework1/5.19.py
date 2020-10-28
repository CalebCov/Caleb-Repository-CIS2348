#Caleb Covington
#1606086
print("""Davy's auto shop services
Oil change -- $35
Tire rotation -- $19
Car wash -- $7
Car wax -- $12
""")

select_first = input("Select first service:\n")
select_second = input("Select second service:\n")

first_service_cost = int(0)
second_service_cost = int(0)

print("\nDavy's auto shop invoice\n")

if select_first.lower() == 'oil change':
    first_service_cost = 35
    print(f'Service 1: {select_first}, ${first_service_cost}'.format(select_first=select_first,first_service_cost=first_service_cost))
elif select_first.lower() == 'tire rotation':
    first_service_cost = 19
    print(f'Service 1: {select_first}, ${first_service_cost}'.format(select_first=select_first,first_service_cost=first_service_cost))
elif select_first.lower() == 'car wash':
    first_service_cost = 7
    print(f'Service 1: {select_first}, ${first_service_cost}'.format(select_first=select_first,first_service_cost=first_service_cost))
elif select_first.lower() == "car wax":
    first_service_cost = 12
    print(f'Service 1: {select_first}, ${first_service_cost}'.format(select_first=select_first,first_service_cost=first_service_cost))
else:
    print('Service 1: No service')

if select_second.lower() == 'oil change':
    second_service_cost = 35
    print(f'Service 2: {select_second}, ${second_service_cost}'.format(select_second=select_second,second_service_cost=second_service_cost))
elif select_second.lower() == 'tire rotation':
    second_service_cost = 19
    print(f'Service 2: {select_second}, ${second_service_cost}'.format(select_second=select_second,second_service_cost=second_service_cost))
elif select_second.lower() == 'car wash':
    second_service_cost = 7
    print(f'Service 2: {select_second}, ${second_service_cost}'.format(select_second=select_second,second_service_cost=second_service_cost))
elif select_second.lower() == "car wax":
    second_service_cost = 12
    print(f'Service 2: {select_second}, ${second_service_cost}'.format(select_second=select_second,second_service_cost=second_service_cost))
else:
    print('Service 2: No service')

total_cost = first_service_cost + second_service_cost
print(f'\nTotal: ${total_cost}'.format(total_cost=total_cost))
