import pygame
import math
import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox

main_label = Tk()
main_label.geometry('650x350')
main_label.title('Импульс')

Label(main_label, font='TkHeadingFont', text='Тема: "Импульс и закон сохранения импульса".\nИзучаем импульс на практике. \nВыберите количество объектов, которые хотите столкнуть').grid(row=0, columnspan=4, padx=150, pady= 10)

def click_button_simulation_collision():
    import tkinter as tk
    label_collision = tk.Tk()

    label_collision.title("Симуляция физических процессов")
    label_x = 550
    label_y = 400
    label_collision.geometry(f"{label_x}x{label_y}")

    def click_button_play():
        PLAY_COLLISION()

    def quit():
        label_collision.destroy()
        print("Close Tkinter Window")

    button_play = tk.Button(label_collision, background='lightgray', text="Запустить", command=click_button_play, height=round(0.006*label_y), width=round(0.03*label_x), justify='center')
    button_play.grid(row=0,column=0, padx=110, pady=25)

    button_exit = tk.Button(label_collision, background='lightgray', text="Выйти", command=quit, height=round(0.006*label_y), width=round(0.03*label_x), justify='center')
    button_exit.grid(row=0,column=1)  

    mass1 = tk.Entry(label_collision, background='lightgray', width=round(0.05*label_x), justify='center')
    mass2 = tk.Entry(label_collision, background='lightgray', width=round(0.05*label_x), justify='center')
    mass3 = tk.Entry(label_collision, background='lightgray', width=round(0.05*label_x), justify='center')
    mass1.grid(row=3, column=0)
    mass2.grid(row=4, column=0)
    mass3.grid(row=5, column=0)

    Label(label_collision, text = "<- Масса 1-го объекта").grid(row = 3, column=1, sticky = W)
    Label(label_collision, text = "<- Масса 2-го объекта").grid(row = 4, column=1, sticky = W)
    Label(label_collision, text = "<- Масса 3-го объекта").grid(row = 5, column=1, sticky = W)

    speed1 = tk.Entry(label_collision, background='lightgray', width=round(0.05*label_x), justify='center')
    speed2 = tk.Entry(label_collision, background='lightgray', width=round(0.05*label_x), justify='center')
    speed3 = tk.Entry(label_collision, background='lightgray', width=round(0.05*label_x), justify='center')
    speed1.grid(row=7, column=0)
    speed2.grid(row=8, column=0)
    speed3.grid(row=9, column=0)

    Label(label_collision, text = " ").grid(row = 6, column=1, sticky = W)
    Label(label_collision, text = "<- Vx 1-го объекта").grid(row = 7, column=1, sticky = W)
    Label(label_collision, text = "<- Vx 2-го объекта").grid(row = 8, column=1, sticky = W)
    Label(label_collision, text = "<- Vx 3-го объекта").grid(row = 9, column=1, sticky = W)


    def get_input():
        mass1_input = float(mass1.get())
        mass2_input = float(mass2.get())
        mass3_input = float(mass3.get())
        global mass
        mass = [mass1_input, mass2_input, mass3_input]

        speed1_input = float(speed1.get())
        speed2_input = float(speed2.get())
        speed3_input = float(speed3.get())
 
        gravity_dict = {"Земля":9.81, "Марс":3.71, "Солнце":273.8, "Венера":8.87, "Юпитер":24.79, "Нептун":11.15, "Сатурн":10.44, "Черная дыра  sgr A**":100000000000}
        global GRAVITY
        if combobox.get() in gravity_dict:
            GRAVITY = gravity_dict[combobox.get()]
        else:
            GRAVITY = float(combobox.get())
        
        global speed_x
        speed_x = [speed1_input, speed2_input, speed3_input]

    button_set_initial_conditions = tk.Button(label_collision, background='lightgray', text="Установить начальные условия", command=get_input, 
                                            height=round(0.008*label_y), width=round(0.06*label_x), justify='center')
    button_set_initial_conditions.grid(row=11,column=0, pady=20, padx=20, columnspan=2) 


    from tkinter import ttk
    list_gravity = ("Земля", "Марс", "Солнце", "Венера", "Юпитер", "Нептун", "Сатурн", "Черная дыра  sgr A**")
    combobox = ttk.Combobox (values=list_gravity,master=label_collision)
    combobox.grid(row=10, column=0, pady=20)
    Label(label_collision, text = "<--Ускорение свободного \nпадения").grid(row = 10, column=1, sticky = W)

   
    def get_info():
        import tkinter as tk
        from tkinter import Label
        from PIL import ImageTk, Image
        l = tk.Toplevel()  # Создаем новое окно
        l.geometry('960x500')

        # Загрузка изображения
        try:
            image = Image.open("osi.jpg")  # Убедитесь, что путь к изображению правильный
            image4messagebox = ImageTk.PhotoImage(image)
        except Exception as e:
            print(f"Ошибка при загрузке изображения: {e}")
            return

        # Создание метки для отображения изображения
        image2label = Label(l, image=image4messagebox)
        image2label.image = image4messagebox  # Сохраняем ссылку на изображение
        image2label.grid()
        messagebox.showinfo(title='NOTE', message='Если хотите установить разнонаправленное движение - просто задайте начальную скорость с отрицательным значением.\nОтрицательное значение в Декартовой системе координат означает обратное направление величины')
    roundedbutton = tk.Button(label_collision,  text="?", command=get_info)
    roundedbutton["border"] = "0"
    roundedbutton.grid(row=3, column=0, sticky=E)

def PLAY_COLLISION():

    # Константы
    WIDTH, HEIGHT = 1000, 900
    SPARK_COUNT = 10
    SPARK_LIFETIME = 6  # Количество кадров, в течение которых искры будут видны
    SPARK_COLOR = (100, 0, 0)  # Золотистый цвет для искр

    # Класс для искры
    class Spark:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.lifetime = SPARK_LIFETIME
            self.size = random.randint(1, 3)  # Размер искры

        def update(self):
            self.lifetime -= 1

        def draw(self, screen):
            if self.lifetime > 0:
                pygame.draw.circle(screen, SPARK_COLOR, (int(self.x), int(self.y)), self.size)

    class Ball:
        def __init__(self, x, y, radius, mass):
            self.x = x
            self.y = y
            self.radius = radius
            self.mass = mass
            self.vx = 0
            self.vy = 0
            self.sparks = []  # Список искр

        def apply_force(self, fx, fy):
            ax = fx / self.mass
            ay = fy / self.mass
            self.vx += ax
            self.vy += ay

        def update(self, dt):
            self.apply_force(0, self.mass * GRAVITY)  # Применяем силу тяжести
            self.x += self.vx * dt
            self.y += self.vy * dt

            # Проверяем столкновение с нижней границей
            if self.y + self.radius >= HEIGHT:
                self.y = HEIGHT - self.radius  # Устанавливаем шар на поверхность
                self.vy *= -0.6  # Отражаем скорость с коэффициентом восстановления

                
            if self.x + self.radius >= WIDTH:
                self.x = WIDTH - self.radius 
                self.vx *= -0.5 

            if self.x - self.radius <= 0:
                self.x = self.radius 
                self.vx *= -0.5 

            if self.y + self.radius <= 0:
                self.y = -self.radius 
                self.vx *= -0.99

            if self.y + self.radius == HEIGHT:
                self.vx *= 0.99
            

        def draw(self, screen):

            #присваиваем цвет в зависимости от массы через ргб-градиент красный-черный
            mass_min = min(mass)
            mass_max = max(mass)

            if self.mass == mass_min:
                self.color = 255
            elif mass_max > self.mass > mass_min:
                self.color = 189
            else:
                self.color = 127

            pygame.draw.circle(screen, (self.color, 0, 0), (int(self.x), int(self.y)), self.radius)

            for spark in self.sparks:
                spark.update()
                spark.draw(screen)
            self.sparks = [spark for spark in self.sparks if spark.lifetime > 0]  # Удаляем старые искры

        def check_collision(self, other):
            # Расстояние между центрами шаров
            dx = other.x - self.x
            dy = other.y - self.y
            distance = math.sqrt(dx ** 2 + dy ** 2)

            # Проверка на столкновение
            if distance < self.radius + other.radius:
                return True
            return False

        def resolve_collision(self, other):
            # Векторы нормали и тангента
            normal_x = other.x - self.x
            normal_y = other.y - self.y
            distance = math.sqrt(normal_x ** 2 + normal_y ** 2)

            # Нормализуем вектор нормали
            normal_x /= distance
            normal_y /= distance

            # Находим относительные скорости
            relative_velocity_x = other.vx - self.vx
            relative_velocity_y = other.vy - self.vy

            # Находим скорость вдоль нормали
            velocity_along_normal = (relative_velocity_x * normal_x + relative_velocity_y * normal_y)

            # Если скорости направлены друг от друга, не производим разрешение столкновения
            if velocity_along_normal > 0:
                return

            # Коэффициент восстановления (можно настроить)
            restitution = 0.85

            # Находим импульс для изменения скоростей
            impulse_magnitude = -(1 + restitution) * velocity_along_normal / (1 / self.mass + 1 / other.mass)

            # Обновляем скорости шаров
            self.vx -= impulse_magnitude * normal_x / self.mass
            self.vy -= impulse_magnitude * normal_y / self.mass

            other.vx += impulse_magnitude * normal_x / other.mass
            other.vy += impulse_magnitude * normal_y / other.mass
                    
            # Генерация искр
            for _ in range(SPARK_COUNT):
                spark_x = (self.x + other.x) / 2 + random.uniform(-20, 20)
                spark_y = (self.y + other.y) / 2 + random.uniform(-20, 20)
                self.sparks.append(Spark(spark_x, spark_y))
                other.sparks.append(Spark(spark_x, spark_y))
                
    class Simulation:
        def __init__(self):
            pygame.init()
            self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
            self.clock = pygame.time.Clock()
        

            # Создаем два шара с различными начальными условиями
            self.ball1 = Ball(500, 500, 20, mass[0])
            self.ball1.vx = speed_x[0]  # Начальная скорость первого шара

         
            self.ball2 = Ball(550, 500, 20, mass[1])
            self.ball2.vx = speed_x[1]


            self.ball3 = Ball(600, 500, 20, mass[2])
            self.ball3.vx = speed_x[2]  # Начальная скорость второго шара
            


        def run(self):
            running = True
            while running:
              
                dt = self.clock.tick(100) / 1000  # Время в секундах
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                
                # Обновляем положение шаров
                self.ball1.update(dt)
                self.ball2.update(dt)
                self.ball3.update(dt)

                # Проверяем столкновение и разрешаем его
                if self.ball1.check_collision(self.ball2):
                    self.ball1.resolve_collision(self.ball2)

                if self.ball3.check_collision(self.ball2):
                    self.ball3.resolve_collision(self.ball2)
                    
                if self.ball1.check_collision(self.ball3):
                    self.ball1.resolve_collision(self.ball3)
                    

                # Отображаем объекты на экране
                self.screen.fill((255, 255, 255))  # Очистка экрана
                self.ball1.draw(self.screen)
                self.ball2.draw(self.screen)
                self.ball3.draw(self.screen)
                pygame.display.flip()
            pygame.quit()

    sim = Simulation()
    sim.run()
#-------------------------------------------------------------------------------------------------------------------------------------------------

def click_button_simulation_falling():

    label_collision_duo = tk.Tk()

    label_collision_duo.title("Симуляция физических процессов")
    label_x = 550
    label_y = 400
    label_collision_duo.geometry(f"{label_x}x{label_y}")

    def click_button_play():
        PLAY_FALLING()

    def quit():
        label_collision_duo.destroy()
        print("Close Tkinter Window")

    button_play = tk.Button(label_collision_duo, background='lightgray', text="Запустить", command=click_button_play, height=round(0.006*label_y), width=round(0.03*label_x), justify='center')
    button_play.grid(row=0,column=0, padx=110, pady=25)

    button_exit = tk.Button(label_collision_duo, background='lightgray', text="Выйти", command=quit, height=round(0.006*label_y), width=round(0.03*label_x), justify='center')
    button_exit.grid(row=0,column=1)  

    mass1 = tk.Entry(label_collision_duo, background='lightgray', width=round(0.05*label_x), justify='center')
    mass1.grid(row=3, column=0)

    Label(label_collision_duo, text = "<- Масса 1-го объекта").grid(row = 3, column=1, sticky = W)

    speed1 = tk.Entry(label_collision_duo, background='lightgray', width=round(0.05*label_x), justify='center')
    speed1.grid(row=7, column=0)

    Label(label_collision_duo, text = " ").grid(row = 6, column=1, sticky = W)
    Label(label_collision_duo, text = "<- Vx 1-го объекта").grid(row = 7, column=1, sticky = W)


    def get_input():
        mass1_input = float(mass1.get())
        global mass
        mass = [mass1_input]

        speed1_input = float(speed1.get())
        gravity_dict = {"Земля":9.81, "Марс":3.71, "Солнце":273.8, "Венера":8.87, "Юпитер":24.79, "Нептун":11.15, "Сатурн":10.44, "Черная дыра  sgr A**":100000000000}
        global GRAVITY
        if combobox.get() in gravity_dict:
            GRAVITY = gravity_dict[combobox.get()]
        else:
            GRAVITY = float(combobox.get())
        
        global speed_x
        speed_x = [speed1_input]

    button_set_initial_conditions = tk.Button(label_collision_duo, background='lightgray', text="Задайте начальные условия", command=get_input, 
                                            height=round(0.008*label_y), width=round(0.06*label_x), justify='center')
    button_set_initial_conditions.grid(row=11,column=0, pady=20, padx=20, columnspan=2) 


    from tkinter import ttk
    list_gravity = ("Земля", "Марс", "Солнце", "Венера", "Юпитер", "Нептун", "Сатурн", "Черная дыра  sgr A**")
    combobox = ttk.Combobox (values=list_gravity,master=label_collision_duo)
    combobox.grid(row=10, column=0, pady=20)
    Label(label_collision_duo, text = "<--Ускорение свободного \nпадения").grid(row = 10, column=1, sticky = W)


    def get_info():
        import tkinter as tk
        from tkinter import Label
        from PIL import ImageTk, Image
        l = tk.Toplevel()  # Создаем новое окно
        l.geometry('960x500')

        # Загрузка изображения
        try:
            image = Image.open("osi.jpg")  # Убедитесь, что путь к изображению правильный
            image4messagebox = ImageTk.PhotoImage(image)
        except Exception as e:
            print(f"Ошибка при загрузке изображения: {e}")
            return

        # Создание метки для отображения изображения
        image2label = Label(l, image=image4messagebox)
        image2label.image = image4messagebox  # Сохраняем ссылку на изображение
        image2label.grid()
        messagebox.showinfo(title='NOTE', message='Если хотите установить разнонаправленное движение - просто задайте начальную скорость с отрицательным значением.\nОтрицательное значение в Декартовой системе координат означает обратное направление величины')

    roundedbutton = tk.Button(label_collision_duo,  text="?", command=get_info)
    roundedbutton["border"] = "0"
    roundedbutton.grid(row=3, column=0, sticky=E)


def PLAY_FALLING():

    # Константы
    WIDTH, HEIGHT = 1000, 900

    class Ball:
        def __init__(self, x, y, radius, mass):
            self.x = x
            self.y = y
            self.radius = radius
            self.mass = mass
            self.vx = 0
            self.vy = 0

        def apply_force(self, fx, fy):
            ax = fx / self.mass
            ay = fy / self.mass
            self.vx += ax
            self.vy += ay

        def update(self, dt):
            self.apply_force(0, self.mass * GRAVITY)  # Применяем силу тяжести
            self.x += self.vx * dt
            self.y += self.vy * dt

            # Проверяем столкновение с нижней границей
            if self.y + self.radius >= HEIGHT:
                self.y = HEIGHT - self.radius  # Устанавливаем шар на поверхность
                self.vy *= -0.6  # Отражаем скорость с коэффициентом восстановления

                
            if self.x + self.radius >= WIDTH:
                self.x = WIDTH - self.radius 
                self.vx *= -0.5 

            if self.x - self.radius <= 0:
                self.x = self.radius 
                self.vx *= -0.5 

            if self.y + self.radius <= 0:
                self.y = -self.radius 
                self.vx *= -0.99

            if self.y + self.radius == HEIGHT:
                self.vx *= 0.99
            

        def draw(self, screen):
            pygame.draw.circle(screen, (169, 169, 169), (int(self.x), int(self.y)), self.radius)

        def resolve_collision(self, other):
            # Векторы нормали и тангента
            normal_x = other.x - self.x
            normal_y = other.y - self.y
            distance = math.sqrt(normal_x ** 2 + normal_y ** 2)

            # Нормализуем вектор нормали
            normal_x /= distance
            normal_y /= distance

    class Simulation:
        def __init__(self):
            pygame.init()
            self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
            self.clock = pygame.time.Clock()
        
            self.ball1 = Ball(500, 500, 20, mass[0])
            self.ball1.vx = speed_x[0]  # Начальная скорость первого шара  

        def run(self):
            running = True
            while running:
              
                dt = self.clock.tick(100) / 1000  # Время в секундах
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                
                # Обновляем положение шаров
                self.ball1.update(dt)
                # Отображаем объекты на экране
                self.screen.fill((255, 255, 255))  # Очистка экрана
                self.ball1.draw(self.screen)
                pygame.display.flip()
            pygame.quit()

    sim = Simulation()
    sim.run()


#-------------------------------------------------------------------------------------------------------------------------------------------------
def click_button_simulation_collision_duo():

    label_collision_duo = tk.Tk()

    label_collision_duo.title("Симуляция физических процессов")
    label_x = 550
    label_y = 400
    label_collision_duo.geometry(f"{label_x}x{label_y}")

    def click_button_play():
        PLAY_COLLISION_DUO()

    def quit():
        label_collision_duo.destroy()
        print("Close Tkinter Window")

    button_play = tk.Button(label_collision_duo, background='lightgray', text="Запустить", command=click_button_play, height=round(0.006*label_y), width=round(0.03*label_x), justify='center')
    button_play.grid(row=0,column=0, padx=110, pady=25)

    button_exit = tk.Button(label_collision_duo, background='lightgray', text="Выйти", command=quit, height=round(0.006*label_y), width=round(0.03*label_x), justify='center')
    button_exit.grid(row=0,column=1)  

    mass1 = tk.Entry(label_collision_duo, background='lightgray', width=round(0.05*label_x), justify='center')
    mass2 = tk.Entry(label_collision_duo, background='lightgray', width=round(0.05*label_x), justify='center')
    mass1.grid(row=3, column=0)
    mass2.grid(row=4, column=0)

    Label(label_collision_duo, text = "<- Масса 1-го объекта").grid(row = 3, column=1, sticky = W)
    Label(label_collision_duo, text = "<- Масса 2-го объекта").grid(row = 4, column=1, sticky = W)

    speed1 = tk.Entry(label_collision_duo, background='lightgray', width=round(0.05*label_x), justify='center')
    speed2 = tk.Entry(label_collision_duo, background='lightgray', width=round(0.05*label_x), justify='center')
    speed1.grid(row=7, column=0)
    speed2.grid(row=8, column=0)

    Label(label_collision_duo, text = " ").grid(row = 6, column=1, sticky = W)
    Label(label_collision_duo, text = "<- Vx 1-го объекта").grid(row = 7, column=1, sticky = W)
    Label(label_collision_duo, text = "<- Vx 2-го объекта").grid(row = 8, column=1, sticky = W)


    def get_input():
        mass1_input = float(mass1.get())
        mass2_input = float(mass2.get())
        global mass
        mass = [mass1_input, mass2_input]

        speed1_input = float(speed1.get())
        speed2_input = float(speed2.get())
 
        gravity_dict = {"Земля":9.81, "Марс":3.71, "Солнце":273.8, "Венера":8.87, "Юпитер":24.79, "Нептун":11.15, "Сатурн":10.44, "Черная дыра  sgr A**":100000000000}
        global GRAVITY
        if combobox.get() in gravity_dict:
            GRAVITY = gravity_dict[combobox.get()]
        else:
            GRAVITY = float(combobox.get())
        
        global speed_x
        speed_x = [speed1_input, speed2_input]

    button_set_initial_conditions = tk.Button(label_collision_duo, background='lightgray', text="Задайте начальные условия", command=get_input, 
                                            height=round(0.008*label_y), width=round(0.06*label_x), justify='center')
    button_set_initial_conditions.grid(row=11,column=0, pady=20, padx=20, columnspan=2) 


    from tkinter import ttk
    list_gravity = ("Земля", "Марс", "Солнце", "Венера", "Юпитер", "Нептун", "Сатурн", "Черная дыра  sgr A**")
    combobox = ttk.Combobox (values=list_gravity,master=label_collision_duo)
    combobox.grid(row=10, column=0, pady=20)
    Label(label_collision_duo, text = "<--Ускорение свободного \nпадения").grid(row = 10, column=1, sticky = W)


    def get_info():
        import tkinter as tk
        from tkinter import Label
        from PIL import ImageTk, Image
        l = tk.Toplevel()  # Создаем новое окно
        l.geometry('960x500')

        # Загрузка изображения
        try:
            image = Image.open("osi.jpg")  # Убедитесь, что путь к изображению правильный
            image4messagebox = ImageTk.PhotoImage(image)
        except Exception as e:
            print(f"Ошибка при загрузке изображения: {e}")
            return

        # Создание метки для отображения изображения
        image2label = Label(l, image=image4messagebox)
        image2label.image = image4messagebox  # Сохраняем ссылку на изображение
        image2label.grid()
        messagebox.showinfo(title='NOTE', message='Если хотите установить разнонаправленное движение - просто задайте начальную скорость с отрицательным значением.\nОтрицательное значение в Декартовой системе координат означает обратное направление величины')
   
    roundedbutton = tk.Button(label_collision_duo,  text="?", command=get_info)
    roundedbutton["border"] = "0"
    roundedbutton.grid(row=3, column=0, sticky=E)

def PLAY_COLLISION_DUO():

    # Константы
    WIDTH, HEIGHT = 1000, 900
    SPARK_COUNT = 10
    SPARK_LIFETIME = 6  # Количество кадров, в течение которых искры будут видны
    SPARK_COLOR = (100, 0, 0)  # Золотистый цвет для искр

    # Класс для искры
    class Spark:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.lifetime = SPARK_LIFETIME
            self.size = random.randint(1, 3)  # Размер искры

        def update(self):
            self.lifetime -= 1

        def draw(self, screen):
            if self.lifetime > 0:
                pygame.draw.circle(screen, SPARK_COLOR, (int(self.x), int(self.y)), self.size)

    class Ball:
        def __init__(self, x, y, radius, mass):
            self.x = x
            self.y = y
            self.radius = radius
            self.mass = mass
            self.vx = 0
            self.vy = 0
            self.sparks = []  # Список искр

        def apply_force(self, fx, fy):
            ax = fx / self.mass
            ay = fy / self.mass
            self.vx += ax
            self.vy += ay

        def update(self, dt):
            self.apply_force(0, self.mass * GRAVITY)  # Применяем силу тяжести
            self.x += self.vx * dt
            self.y += self.vy * dt

            # Проверяем столкновение с нижней границей
            if self.y + self.radius >= HEIGHT:
                self.y = HEIGHT - self.radius  # Устанавливаем шар на поверхность
                self.vy *= -0.6  # Отражаем скорость с коэффициентом восстановления

                
            if self.x + self.radius >= WIDTH:
                self.x = WIDTH - self.radius 
                self.vx *= -0.5 

            if self.x - self.radius <= 0:
                self.x = self.radius 
                self.vx *= -0.5 

            if self.y + self.radius <= 0:
                self.y = -self.radius 
                self.vx *= -0.99

            if self.y + self.radius == HEIGHT:
                self.vx *= 0.99
            

        def draw(self, screen):

            #присваиваем цвет в зависимости от массы через ргб-градиент красный-черный
            mass_min = min(mass)

            if self.mass == mass_min:
                self.color = 255
            else:
                self.color = 127

            pygame.draw.circle(screen, (self.color, 0, 0), (int(self.x), int(self.y)), self.radius)

            for spark in self.sparks:
                spark.update()
                spark.draw(screen)
            self.sparks = [spark for spark in self.sparks if spark.lifetime > 0]  # Удаляем старые искры

        def check_collision(self, other):
            # Расстояние между центрами шаров
            dx = other.x - self.x
            dy = other.y - self.y
            distance = math.sqrt(dx ** 2 + dy ** 2)

            # Проверка на столкновение
            if distance < self.radius + other.radius:
                return True
            return False

        def resolve_collision(self, other):
            # Векторы нормали и тангента
            normal_x = other.x - self.x
            normal_y = other.y - self.y
            distance = math.sqrt(normal_x ** 2 + normal_y ** 2)

            # Нормализуем вектор нормали
            normal_x /= distance
            normal_y /= distance

            # Находим относительные скорости
            relative_velocity_x = other.vx - self.vx
            relative_velocity_y = other.vy - self.vy

            # Находим скорость вдоль нормали
            velocity_along_normal = (relative_velocity_x * normal_x + relative_velocity_y * normal_y)

            # Если скорости направлены друг от друга, не производим разрешение столкновения
            if velocity_along_normal > 0:
                return

            # Коэффициент восстановления (можно настроить)
            restitution = 0.85

            # Находим импульс для изменения скоростей
            impulse_magnitude = -(1 + restitution) * velocity_along_normal / (1 / self.mass + 1 / other.mass)

            # Обновляем скорости шаров
            self.vx -= impulse_magnitude * normal_x / self.mass
            self.vy -= impulse_magnitude * normal_y / self.mass

            other.vx += impulse_magnitude * normal_x / other.mass
            other.vy += impulse_magnitude * normal_y / other.mass
                    
            # Генерация искр
            for _ in range(SPARK_COUNT):
                spark_x = (self.x + other.x) / 2 + random.uniform(-20, 20)
                spark_y = (self.y + other.y) / 2 + random.uniform(-20, 20)
                self.sparks.append(Spark(spark_x, spark_y))
                other.sparks.append(Spark(spark_x, spark_y))
                
    class Simulation:
        def __init__(self):
            pygame.init()
            self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
            self.clock = pygame.time.Clock()
        

            # Создаем два шара с различными начальными условиями
            self.ball1 = Ball(500, 500, 20, mass[0])
            self.ball1.vx = speed_x[0]  # Начальная скорость первого шара

         
            self.ball2 = Ball(550, 500, 20, mass[1])
            self.ball2.vx = speed_x[1]            


        def run(self):
            running = True
            while running:
              
                dt = self.clock.tick(100) / 1000  # Время в секундах
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                
                # Обновляем положение шаров
                self.ball1.update(dt)
                self.ball2.update(dt)

                # Проверяем столкновение и разрешаем его
                if self.ball1.check_collision(self.ball2):
                    self.ball1.resolve_collision(self.ball2)
                    

                # Отображаем объекты на экране
                self.screen.fill((255, 255, 255))  # Очистка экрана
                self.ball1.draw(self.screen)
                self.ball2.draw(self.screen)
                pygame.display.flip()
            pygame.quit()

    sim = Simulation()
    sim.run()

#-------------------------------------------------------------------------------------------------------------------------------------------------



button_Simulation_collision = tk.Button(main_label, background='lightgray', text='Симуляция взаимодействия \n3 объектов', command=click_button_simulation_collision)
button_Simulation_collision.grid(row=1, column=3, sticky=NW)

button_Simulation_collision = tk.Button(main_label, background='lightgray', text='Симуляция гравитационного\nвзаимодействия 1 объекта', command=click_button_simulation_falling)
button_Simulation_collision.grid(row=1, column=1, sticky=NW)

button_Simulation_collision = tk.Button(main_label, background='lightgray', text='Симуляция взаимодействия \n2 объектов', command=click_button_simulation_collision_duo)
button_Simulation_collision.grid(row=1, column=2, sticky=NW)

Label(main_label, text='Как улететь с планеты?').grid(row=4, column=1, pady=20)
Label(main_label, text='Что такое импульс?').grid(row=3, column=1, pady=20)

from PIL import ImageTk, Image
def open_infographic_impulse():
    l = tk.Toplevel()  # Создаем новое окно
    l.geometry('960x1352')

    # Загрузка изображения
    try:
        image = Image.open("7966211.png")  # Убедитесь, что путь к изображению правильный
        image4infographic = ImageTk.PhotoImage(image)
    except Exception as e:
        print(f"Ошибка при загрузке изображения: {e}")
        return

    # Создание Canvas для прокрутки
    canvas = Canvas(l, width=1352, height=960)  # Установите высоту по вашему усмотрению
    canvas.grid(row=0, column=0)

    # Создание Scrollbar
    scrollbar = Scrollbar(l, orient="vertical", command=canvas.yview)
    scrollbar.grid(row=0, column=1, sticky='NS')

    # Привязка Scrollbar к Canvas
    canvas.configure(yscrollcommand=scrollbar.set)

    # Создание метки для отображения изображения
    image2label = Label(canvas, image=image4infographic)
    image2label.image = image4infographic  # Сохраняем ссылку на изображение

    # Добавление изображения на Canvas
    canvas.create_window(0, 0, anchor='nw', window=image2label)

    # Обновление размеров Canvas
    canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))  # Устанавливаем область прокрутки

def open_infographic_velocity():
    l = tk.Toplevel()  # Создаем новое окно
    l.geometry('960x1352')

    # Загрузка изображения
    try:
        image = Image.open("velocity.jpg")  # Убедитесь, что путь к изображению правильный
        image4infographic = ImageTk.PhotoImage(image)
    except Exception as e:
        print(f"Ошибка при загрузке изображения: {e}")
        return
    # Создание Canvas для прокрутки
    canvas = Canvas(l, width=1352, height=960)  # Установите высоту по вашему усмотрению
    canvas.grid(row=0, column=0)

    # Создание Scrollbar
    scrollbar = Scrollbar(l, orient="vertical", command=canvas.yview)
    scrollbar.grid(row=0, column=1, sticky='NS')

    # Привязка Scrollbar к Canvas
    canvas.configure(yscrollcommand=scrollbar.set)

    # Создание метки для отображения изображения
    image2label = Label(canvas, image=image4infographic)
    image2label.image = image4infographic  # Сохраняем ссылку на изображение

    # Добавление изображения на Canvas
    canvas.create_window(0, 0, anchor='nw', window=image2label)

    # Обновление размеров Canvas
    canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))  # Устанавливаем область прокрутки

# Пример кнопки для открытия инфографики
button_open_infographic = tk.Button(main_label, background='lightgray', text='--->', command=open_infographic_impulse)
button_open_infographic.grid(row=3, column=2, sticky=tk.W)

# Пример кнопки для открытия инфографики
button_open_infographic = tk.Button(main_label, background='lightgray', text='--->', command=open_infographic_velocity)
button_open_infographic.grid(row=4, column=2, sticky=tk.W)



#-------------------------------------------------------------------------------------------------------------------------------------------------
def click_button_gravity_simulation():
    import pygame
    import math
    import random

    # Константы
    WIDTH, HEIGHT = 800, 600
    FPS = 60
    G = 6.67430e-11  # Гравитационная постоянная

    # Класс для планеты
    class Planet:
        def __init__(self, x, y, mass, radius, color):
            self.x = x
            self.y = y
            self.mass = mass
            self.radius = radius
            self.color = color
            self.vx = random.uniform(-1, 1)  # Начальная скорость по оси X
            self.vy = random.uniform(-1, 1)  # Начальная скорость по оси Y

        def draw(self, screen):
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

        def update(self, planets):
            for other in planets:
                if other != self:
                    # Вычисляем силу притяжения
                    dx = other.x - self.x
                    dy = other.y - self.y
                    distance = math.sqrt(dx ** 2 + dy ** 2)

                    if distance > 0:
                        force = G * self.mass * other.mass / distance ** 2
                        ax = force * dx / (distance * self.mass)
                        ay = force * dy / (distance * self.mass)

                        self.vx += ax
                        self.vy += ay

            # Обновляем положение планеты
            self.x += self.vx
            self.y += self.vy

    # Функция для создания случайных планет
    def create_planets(num_planets):
        planets = []
        for _ in range(num_planets):
            x = random.randint(100, WIDTH - 100)
            y = random.randint(100, HEIGHT - 100)
            mass = random.uniform(1e10, 1e12)  # Масса планеты
            radius = int(mass ** (1/3)) // 1000 + 5  # Радиус планеты
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            planets.append(Planet(x, y, mass, radius, color))
        return planets

    # Основная функция
    def main():
        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Симуляция взаимодействия планет")
        clock = pygame.time.Clock()

        planets = create_planets(5)  # Создаем 5 планет

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill((0, 0, 0))  # Очистка экрана

            for planet in planets:
                planet.update(planets)
                planet.draw(screen)

            pygame.display.flip()  # Обновление экрана
            clock.tick(FPS)  # Ограничение FPS

        pygame.quit()

    if __name__ == "__main__":
        main()


button_gravity_simulation = tk.Button(main_label, background='lightgray', text='Симуляция взаимодействия\nкосмических тел (Demo)', command=click_button_gravity_simulation)
button_gravity_simulation.grid(row=2, column=1, sticky=NW, pady=30)


#-------------------------------------------------------------------------------------------------------------------------------------------------

def click_button_NASA_simulation():
    def play_comand():
        PLAY_NASA_SIMULATION()

    label_NASA_sim = Tk()
    label_x = 500
    label_y = 400

    def get_input():
        global mass_sputnik, v_sputnik, a_sputnik
        mass_sputnik = float(mass_sputnik_input.get())
        v_sputnik = float(v_sputnik_input.get())
        a_sputnik = float(a_sputnik_input.get())

    
    mass_sputnik_input = tk.Entry(label_NASA_sim, background='lightgray', width=round(0.05*label_x), justify='center')
    mass_sputnik_input.grid(row=1, column=0)
    Label(label_NASA_sim, text = "<- Масса спутника").grid(row = 1, column=1, sticky = W)

    v_sputnik_input = tk.Entry(label_NASA_sim, background='lightgray', width=round(0.05*label_x), justify='center')
    v_sputnik_input.grid(row=2, column=0)
    Label(label_NASA_sim, text = "<- Скорость спутника").grid(row = 2, column=1, sticky = W)

    a_sputnik_input = tk.Entry(label_NASA_sim, background='lightgray', width=round(0.05*label_x), justify='center')
    a_sputnik_input.grid(row=3, column=0)
    Label(label_NASA_sim, text = "<- Ускорение спутника").grid(row = 3, column=1, sticky = W)
    
    button_gravity_simulation = tk.Button(main_label, background='lightgray', text='Симуляция МКС', command=play_comand)
    button_gravity_simulation.grid(row=2, column=2, sticky=NW, pady=30)  

    button_set_initial_conditions = tk.Button(label_NASA_sim, background='lightgray', text="Задайте начальные условия", command=get_input, 
                                            height=round(0.008*label_y), width=round(0.06*label_x), justify='center')
    button_set_initial_conditions.grid(row=11,column=0, pady=20, padx=20, columnspan=2) 

    button_play = tk.Button(label_NASA_sim, background='lightgray', text="Запустить", command=play_comand, height=round(0.006*label_y), width=round(0.03*label_x), justify='center')
    button_play.grid(row=0,column=0, padx=110, pady=25)

def PLAY_NASA_SIMULATION():
    import pygame
    import math

    # Константы
    WIDTH, HEIGHT = 800, 600
    FPS = 60
    G = 6.67430e-11  # Гравитационная постоянная
    EARTH_RADIUS = 6371e3  # Радиус Земли в метрах
    FALL_DISTANCE = 100e3  # Высота, при которой объект упадет на Землю (100 км)
    SCALE = 1e6  # Масштаб для отображения (1 пиксель = 1 км)

    # Класс для спутника
    class Satellite:
        def __init__(self, mass, velocity, acceleration):
            self.mass = mass  # Масса спутника
            self.velocity = velocity  # Начальная скорость
            self.acceleration = acceleration  # Ускорение
            self.distance_from_earth = EARTH_RADIUS + 500e3  # Начальная высота (500 км)
            self.x = WIDTH // 2  # Начальная позиция по X
            self.y = HEIGHT // 2  # Начальная позиция по Y

        def update(self):
            # Вычисляем силу притяжения
            force = G * (5.972e24 * self.mass) / (self.distance_from_earth ** 2)  # Масса Земли ~ 5.972e24 кг
            acceleration_due_to_gravity = force / self.mass

            # Обновляем скорость и расстояние
            self.acceleration = acceleration_due_to_gravity
            self.velocity += self.acceleration / FPS  # Обновляем скорость
            self.distance_from_earth -= self.velocity / FPS  # Обновляем расстояние от Земли

            # Проверка на падение на Землю
            if self.distance_from_earth < EARTH_RADIUS + FALL_DISTANCE:
                self.velocity = 0  # Объект упал на Землю
                self.distance_from_earth = EARTH_RADIUS + FALL_DISTANCE  # Устанавливаем на высоту падения

        def draw(self, screen):
            # Рисуем спутник с учетом масштаба
            scaled_y = int(HEIGHT - (self.distance_from_earth - EARTH_RADIUS) / SCALE)
            pygame.draw.circle(screen, (255, 255, 0), (self.x, scaled_y), 10)

    # Функция для отображения информации
    def display_info(screen, satellite):
        font = pygame.font.Font(None, 36)
        info_text = [
            f"Расстояние от Земли: {satellite.distance_from_earth / 1000:.2f} км",
            f"Текущая скорость: {satellite.velocity:.2f} м/с",
            f"Масса спутника: {satellite.mass:.2f} кг",
            f"Ускорение: {satellite.acceleration:.2f} м/с²"
        ]
        for i, line in enumerate(info_text):
            text = font.render(line, True, (255, 255, 255))
            screen.blit(text, (10, 10 + i * 30))

    # Функция для рисования Земли
    def draw_earth(screen):
        earth_color = (0, 100, 255)  # Цвет Земли
        pygame.draw.circle(screen, earth_color, (WIDTH // 2, HEIGHT), int(EARTH_RADIUS / SCALE))  # Рисуем Землю

    # Основная функция
    def main():
        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Симуляция движения объектов на орбите Земли")
        clock = pygame.time.Clock()

        satellite = Satellite(mass_sputnik, v_sputnik, a_sputnik)  # Создаем спутник

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill((0, 0, 0))  # Очистка экрана

            # Рисуем Землю
            draw_earth(screen)

            # Обновляем и рисуем спутник
            satellite.update()
            satellite.draw(screen)

            # Отображаем информацию
            display_info(screen, satellite)

            pygame.display.flip()  # Обновление экрана
            clock.tick(FPS)  # Ограничение FPS

        pygame.quit()

    if __name__ == "__main__":
        main()


button_gravity_simulation = tk.Button(main_label, background='lightgray', text='Симуляция МКС', command=click_button_NASA_simulation)
button_gravity_simulation.grid(row=2, column=2, sticky=NW, pady=30)

#-------------------------------------------------------------------------------------------------------------------------------------------------

main_label.mainloop()