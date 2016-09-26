import pottery
import kiln

if __name__ == "__main__":
    cup = pottery.Pottery("cup", 250)
    bowl = pottery.Pottery("bowl", 400)
    plate_red = pottery.Pottery("red plate", 500, input_description="red round plate")
    plate_blue = pottery.Pottery("blue plate", 500, input_description="blue square plate")

    kiln = kiln.Kiln()
    
    print("Starting with empty kiln.")

    kiln.add_pottery([cup, bowl])

    print("Added cup and bowl:")
    kiln.list_contents()
    kiln.list_contents(state="unbaked")
    kiln.list_contents(state="baked")

    print("Changing temperature to 300:")
    kiln.change_temperature(300)

    kiln.list_contents()
    kiln.list_contents(state="unbaked")
    kiln.list_contents(state="baked")

    print("Changing temperature to 450:")
    kiln.change_temperature(450)

    kiln.list_contents()
    kiln.list_contents(state="unbaked")
    kiln.list_contents(state="baked")

    print("Changing temperature to 550 and adding red plate:") 
    kiln.change_temperature(550)
    kiln.add_pottery([plate_red])

    kiln.list_contents()
    kiln.list_contents(state="unbaked")
    kiln.list_contents(state="baked")

    print("Adding blue plate:")
    kiln.add_pottery([plate_blue])

    kiln.list_contents()
    kiln.list_contents(state="unbaked")
    kiln.list_contents(state="baked")

