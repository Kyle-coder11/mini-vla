def choose_action(target_x, image_x):
    image_center_x = image_x / 2
    tolerance = 50

    left_boundary = image_center_x - tolerance
    right_boundary = image_center_x +tolerance
    
    # if image_center_x + tolerance < target_x :
    if target_x > right_boundary:
        return "Turn Right"
    # elif image_center_x - tolerance > target_x:
    elif target_x < left_boundary:
        return "Turn Left"
    else:
        return "move forward"
    
action = choose_action(100, 640)
print(action)
