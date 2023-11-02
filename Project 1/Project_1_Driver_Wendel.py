"""
Motor_driver.py

Leland Wendel
July 3, 2023

Description: This program imports the motor class and uses
it in an interactive menu.

Tests: I tested each menu function to ensure the program worked properly.
Invalid input has been handled for each function.
"""

import Project_1_Wendel


engine = """

         _....---------...._
       .'              A    '.
     .'      _.--. .--._      '.
  __/     .-'.-._E |_.-.'-.     \__
 .--      |_.'   .-.   '._E      --.
 |       ::||:.-/   \-.:||:U    B  |
 '--..__ U:||:'-\ F /-':||:: __..--'
  )     '-.||    `-'    ||.-'     (
 |'._  G   H|.         .|D   C  _.'|
 |   '-._ _||_\       /_||_ _.-'   |
 |_______'----''.___.''----'_______|
 '--.    | _______________ |    .--'
    |.--.||-------M-1-----||.--.|     A - valve cover
    ||  |||-----M-2-------|||  ||     B - Head
    ||  |||===M=3=========|||  ||     C - Fuel/Intake port
    ||  |||      .-.      |||  ||     D - Intake valve
    ||  |||     ( L )     |||  ||     E - Rocker Arms
    || J|||      `-'   K  ||| J||     F - Cam shaft
    ||  |||      ___      |||  ||     G - Exhaust port
    ||  |||   _.'   '._   |||  ||     H - Exhaust valve
    ||  |||_.' |  |  | '._|||  ||     I - Engine block
    ||  ||     |  |  |     ||  ||     J - Water jacket
    ||  ||     |  |  |     ||  ||     K - Piston
    |'--'|     |  N  |     |'--'|     L - Wrist pin
   .' .--'     |  |  |     '--. '.    M - Rings
   |  |        |  |  |        |  |     M1 - Compression ring
   I  |        |  |  |        |  I     M2 - Compression ring
   |  |        |  |  |        |  |     M3 - Oil ring
   |  |     ___'.---.'___     |  |    N - Piston/connecting rod
   |  |    | .' .---. '. O    |  |    O - Rod cap
   |  |    || .'     '. ||    |  |    P - Rod bearings
   |  |    || |   P   | ||    |  |    Q - Crank Shaft journals
 _.'__|    '| '.     .' |'    |__'._  R - Crank Shaft
'---. |     |   `---'   |     | .---' S - Oil pan
    | |    /     ___     \    | |     T - Oil sump
    | |   /   .'     '.   \   | |     U - Valve springs
    |S|  /   /         \   \  |S|
    | |  |   |    Q    | R |  | |
    | |  |   \         /   |  | |
     \ \  '.  '. ___ .'  .'  / /
      \ \   '-._______.-'   / /
       `.`. T           T .'.'
         `.`-._________.-'.'
           `-._________.-'

"""


def cylinders_input():
    """
    User chooses the amount of cylinders. Input must match a value in cylinder
    options variable.
    """
    cylinder_options = [2, 4, 6, 8, 10, 12]
    cylinders = int(
        input(
            "\nWe offer motors with 2, 4, 6, 8, 10, or 12 cylinder options.\n"
            "How many cylinders would you like your motor to have? "
        )
    )
    while cylinders not in cylinder_options:
        print("\nWe do not offer that option.")
        cylinders = int(input("Enter a valid number of cylinders: "))
    else:
        return cylinders


def liters_input():
    """
    User inputs the displacement in liters. The displacement must be greater
    than 0.4 L and less than 10.1 L.
    """
    liters = float(
        input("\nEnter your desired engine displacement in liters (0.5 - 10): "))
    while liters < 0.5 or liters > 10:
        print("We do not offer that option.")
        liters = float(
            input("Enter your desired engine displacement in liters (0.5 - 10): : "))
    else:
        return liters


def aspiration_input():
    """
    User chooses 1 of 3 options for engine aspiration. Invalid input handled in
    the loop.
    """
    aspiration = str(input(
        "\nWould you like to add a turbo or supercharger to your motor? (type Y or N): "))

    while aspiration.upper() == "Y":
        choice = int(
            input("Enter 1 for a Turbocharger or 2 for a Supercharger: "))
        if choice == 1:
            aspiration = "Turbocharged"
            break
        elif choice == 2:
            aspiration = "Supercharged"
            break
    else:
        aspiration = "Naturally Aspirated"
    return aspiration


def code_input():
    """
    User chooses an engine code. Possible issue, engine codes entered twice
    will be written over.
    """
    code = str(
        input("\nEnter a 3 to 5 digit code containing letters and numbers.\nThis will represent the motor's codename: ")
    )
    while len(code) < 3 or len(code) > 5:
        code = str(input("Please enter a 3 to 5 digit code: "))
    return code


def new_motor():
    """
    This function creates an invoice and calculates the simulated output and
    cost. Files are named based on the engine code.
    """
    cylinders = cylinders_input()
    liters = liters_input()
    aspiration = aspiration_input()
    code = code_input()

    print("\nCongratulations, you've designed a motor!")

    new_order = Project_1_Wendel.Motor(cylinders, liters, aspiration, code)

    motor_redline = new_order.get_redline()
    motor_cost = new_order.get_cost()
    motor_power = new_order.get_horsepower()

    print(
        f"Your new motor '{new_order.code}' is expected to produce {motor_power} horsepower @ {motor_redline} RPMs.")

    with open(new_order.code, "w") as f:
        line_one = "Wendel Motorworks Inc."
        address = "1600 Pennsylvania Avenue NW"
        address2 = "Washington DC, 20500"
        phone = "Phone: 1.888.624.8140"

        f.write(line_one + "\n")
        f.write(address + "\n")
        f.write(address2 + "\n")
        f.write(phone + "\n")
        f.write("\n\tINVOICE\n")
        f.write(f"\nEngine Code: {new_order.code}\n")
        f.write(f"Liters: {new_order.liters}\n")
        f.write(f"Cylinders: {new_order.cylinders}\n")
        f.write(f"Aspiration: {new_order.aspiration}\n")
        f.write(f"Horsepower: {motor_power}\n")
        f.write(f"Redline: {motor_redline}\n")
        f.write(f"\nTotal Cost: {motor_cost}\n")
    f.close()

    print("\nA file containing this invoice has been saved to your current directory.\n")


def get_invoice():
    """
    This is a search function for previous invoices. Errors are handled with
    try and except and the loop can be exited by inputting 'return'.
    """
    while True:
        try:
            inv_lookup = input(
                "\nEnter a valid engine code in the current directory or type 'return' to exit to the main menu: "
            )
            print("-----------------------------------------------------------------")
            print()
            if inv_lookup == "return":
                break
            with open(inv_lookup, "r") as f:
                for line in f:
                    print(line, end="")
            print("")
            break
        except FileNotFoundError:
            print("Oops! Invoice not found.")


def main_menu():
    """
    This is the main function.
    """
    while True:
        print(
            "------------------------------------------------------------------------"
            "\n\t\tWelcome to Wendel Motorworks!\n"
            "\nThis program will allow you to design a motor to your exact\n"
            "specifications and test potential power output. When you are happy\n"
            "with the simulated results, our experts will get to work handcrafting \n"
            "your unique design. Expect orders to ship 70 days after they are placed.\n"
            "Average arrival time is 2 weeks, but actual time may vary.\n"
            "------------------------------------------------------------------------\n"
        )
        print("Please make a selection:")
        print("\n\t[1] Build a Motor")
        print("\t[2] Invoice Search")
        print("\t[3] Cylinder Cross Section Diagram")
        print("\t[4] Exit")

        menu_input = int(input("\n\t--> "))

        if menu_input == 1:
            new_motor()
        elif menu_input == 2:
            get_invoice()
        elif menu_input == 3:
            print(engine)
        elif menu_input == 4:
            print("\nThank you for choosing Wendel Motorworks!\n")
            exit()
        else:
            print("Please select a valid option.")


main_menu()
