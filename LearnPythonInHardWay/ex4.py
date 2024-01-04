cars = 100  # 有100辆车
space_in_a_car = 4  # 每辆车可以坐4个人
drivers = 30  # 运行的车辆数，即一共有30个司机
passengers = 90  # 一共有90个乘客
cars_not_driven = cars - drivers  # 空车数=总车数-运行车辆数
cars_driven = drivers  # 在运行的车辆数=司机数
carpool_capacity = cars_driven * space_in_a_car  # 最大可载人数，加上司机
average_passengers_per_car = passengers / cars_driven  # 平均每辆车乘客数

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
