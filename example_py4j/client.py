from py4j.java_gateway import JavaGateway

# Подключаемся к Java-серверу
gateway = JavaGateway()

# Получаем доступ к объекту MathServer
math_server = gateway.entry_point

# Вызываем метод сложения
result = math_server.add(10, 20)

print(f"Результат сложения: {result}")

# Закрываем соединение
gateway.close()









