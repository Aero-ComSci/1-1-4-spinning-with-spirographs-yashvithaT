def generate_flowers(user_input):
    flower_types = ["dandelion", "sunflower", "tulip", "daisy", "lily"]
    tokens = user_input.lower().split()
    
    if len(tokens) < 3 or len(tokens) % 3 != 0:
        print("Invalid input format. Please use 'number flower_type color' format.")
        return
    
    flowers = []
    
    i = 0
    while i < len(tokens):
        try:
            number_of_flowers = int(tokens[i])
        except ValueError:
            print("Invalid number: {tokens[i]}")
            return
        
        flower_type = tokens[i + 1]
        color = tokens[i + 2]
        
        if flower_type not in flower_types:
            print("Invalid flower type: {flower_type}. Available types are: {', '.join(flower_types)}.")
            return
        
        flowers.append((number_of_flowers, flower_type, color))
        i += 3

