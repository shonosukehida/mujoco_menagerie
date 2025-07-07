
#サイズは全て半サイズ
############################
camera_center = [0.515, 0]
dx = 0.2
dy = 0.2

top_bottom_x_size = 1
top_bottom_y_size = dy 

left_right_x_size = dx 
left_right_y_size = 1
############################

bottom_bar_pos = [camera_center[0] - dx - top_bottom_x_size, 0]
top_bar_pos = [camera_center[0] + dx + top_bottom_x_size, 0]

right_bar_pos = [0, -dy - left_right_y_size]
left_bar_pos = [0, dy + left_right_y_size]


inner_x_range = [bottom_bar_pos[0] + top_bottom_x_size, top_bar_pos[0] - top_bottom_x_size]
inner_y_range = [right_bar_pos[1] + left_right_y_size, left_bar_pos[1] - left_right_y_size]



print('position')
print('-'*100)
print('bottom_bar:', bottom_bar_pos)
print('top_bar:', top_bar_pos)

print('right_bar: ', right_bar_pos) 
print('left_bar: ', left_bar_pos)
print('-'*100)

print('size')
print('top_bottom_bar(x,y):', top_bottom_x_size,',',top_bottom_y_size)
print('right_left_bar(x,y):', left_right_x_size, ',',left_right_y_size)
print('inner_range')
print('x:', inner_x_range, 'diff:', abs(inner_x_range[1] - inner_x_range[0]) / 2)
print('y:', inner_y_range, 'diff:', abs(inner_y_range[1] - inner_y_range[0]) / 2)
print('-'*100)

