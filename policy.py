def choose_action(target_x, image_x):
    image_center_x = image_x / 2
    tolerance = 50

    if image_center_x + tolerance < target_x :
        return "Turn Right"
    elif image_center_x - tolerance > target_x:
        return "Turn Left"
    else:
        return "move forward"
    
action = choose_action(100, 640)
print(action)
