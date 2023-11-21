def celsius_to_kelvin(temperature):
    return temperature + 273.15

if __name__ == '__main__':
    with open("input.txt", "r") as file:
        lines = file.readlines()
        temperatures = []
        for line in lines:
            temperature = float(line.strip())
            temperatures.append(temperature)
        print(lines)
        print(temperatures)

