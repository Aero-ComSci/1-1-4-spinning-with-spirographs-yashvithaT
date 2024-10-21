def generate_flowers(user_input):
    #initializes list of flower types
    flower_types = ["dandelion", "sunflower", "tulip", "daisy", "lily"]
    #converts input into lowercase and tokenzies by splitting into individual words based on spaces
    tokens = user_input.lower().split()
    #ensures input is correctly formatted
    if len(tokens) < 3 or len(tokens) % 3 != 0:
        print("Invalid input format. Please use 'number flower_type color' format.")
        return
    #initialize empty list
    flowers = []
    
    i = 0
    while i < len(tokens):
        try:
            #convert token to integer for flower number
            number_of_flowers = int(tokens[i])
        except ValueError:
            #error protocol
            print("Invalid number: {tokens[i]}")
            return
        #assigns next tokens
        flower_type = tokens[i + 1]
        color = tokens[i + 2]
        
        if flower_type not in flower_types:
            print("Invalid flower type: {flower_type}. Available types are: {', '.join(flower_types)}.")
            return
        
        flowers.append((number_of_flowers, flower_type, color))
        i += 3

