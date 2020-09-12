import math

# Dictionary of paint colors and cost per gallon
paint_colors = {
   'red': 35,
   'blue': 25,
   'green': 23
}
gallon_of_paint = 350
wall_height = int(input('Enter wall height (feet):\n'))
wall_width = int(input('Enter wall width (feet):\n'))
wall_area = wall_width * wall_height
paint_amount = float(wall_area / gallon_of_paint)
cans_needed = math.ceil(paint_amount)

print('Wall area:', wall_area,'square feet')
print('Paint needed:','{:.2f}'.format(paint_amount),'gallons')
print('Cans needed:', cans_needed,'can(s)\n')

cost_of_paint=0

paint_color = input('Choose a color to paint the wall:\n')
if paint_color.lower() == 'red':
    cost_of_paint = paint_colors['red']*cans_needed
elif paint_color.lower() == 'blue':
    cost_of_paint = paint_colors['blue']*cans_needed
else:
    cost_of_paint = paint_colors['green']*cans_needed
#print('Cost of purchasing',paint_color,'paint: $',cost_of_paint)
print('Cost of purchasing {paint_color} paint: ${cost_of_paint}'.format(paint_color = paint_color, cost_of_paint = cost_of_paint))