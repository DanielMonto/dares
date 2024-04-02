import random

list_index=[1,2,3,4]
colors=[
    'Violeta',
    'Amarillo',
    'Rojo',
    'Naranja',
    'Verde',
    'Azul',
    'Amarillo verdoso',
    'Rojo anaranjado',
    'Azul violeta',
    'Amarillo anaranjado',
    'Rojo violeta',
    'Azul verdoso'
]
tasks_raining=[
    'Leer un libro con una taza de té caliente',
    'Ver una película acogedora en casa',
    'Hacer manualidades o proyectos artísticos',
    'Cocinar una receta nueva y reconfortante',
    'Escuchar música relajante',
    'Escribir en un diario o comenzar a escribir una historia',
    'Disfrutar de un juego de mesa con amigos o familiares',
    'Hacer una sesión de yoga o ejercicios en casa',
    'Explorar nuevas playlists de música',
    'Planificar y organizar tus metas y proyectos futuros'
]
countrys_travellables=[
    'Japón',
    'Italia',
    'Nueva Zelanda',
    'Canadá',
    'Australia',
    'Noruega',
    'Costa Rica',
    'Grecia',
    'Vietnam',
    'Sudáfrica'
]
christmas_tasks=[
    'Decorar el árbol de Navidad',
    'Hornear galletas o pasteles festivos',
    'Hacer una maratón de películas navideñas',
    'Visitar mercados navideños',
    'Hacer tarjetas de Navidad a mano',
    'Realizar un intercambio de regalos',
    'Participar en una obra de caridad o voluntariado',
    'Hacer un muñeco de nieve o tener una guerra de bolas de nieve',
    'Asistir a un espectáculo de luces festivas',
    'Disfrutar de una cena especial en familia o con amigos'
]
animals_kinds=[
    'Rana',
    'Loro',
    'Perro',
    'Tiburon',
    'Cocodrilo',
    'Mariposa'
]
list_houses=['Gryffindor', 'Slytherin', 'Hufflepuff', 'Ravenclaw']
houses_points={hn:0 for hn in list_houses}

def choser_hat():
    while True:
        questions_answers={
            'Cual de estos colores te gusta?':random.sample(colors,4),
            'Que haces mientras llueve?':random.sample(tasks_raining,4),
            'A que pais te gustaria viajar?':random.sample(countrys_travellables,4),
            'Que prefieres hacer en navidad?':random.sample(christmas_tasks,4),
            'Que animal te gusta mas?':random.sample(animals_kinds,4)
        }
        for index,(question,answers) in enumerate(questions_answers.items()):
            rd_li=random.sample(list_index,4)
            rd_hl=random.sample(list_houses,4)
            house_asignation={ih:house for ih,house in zip(rd_li,rd_hl)}
            while True:
                print(f'Pregunta {index+1}:\n{question}')
                for i,ans in enumerate(answers):
                    print(f'{i+1}. {ans}')
                try:
                    ans_chosed=int(input('dame tu respuesta [1 - 4]:'))
                    if ans_chosed<1 or ans_chosed>4:
                        print('elige un numero [1 - 4]')
                        continue
                    house_name=house_asignation[ans_chosed]
                    houses_points[house_name]+=1
                    print(f'se te agrego un punto a al casa {house_name}')
                    break
                except ValueError:
                    print('elige un numero [1 - 4]')
        max_value=max(houses_points.values())
        max_values=[v for v in houses_points if houses_points[v]==max_value]
        if len(max_values)>1:
            print(f'hay 2 o mas casa con puntos iguales:\n{houses_points} \n')
        else:
            print(f'tu casa es {max_values[0]}')
        want_continue=input('deseas hacer otra vez el test? [si o no]')
        if want_continue!='si':
            break
    
choser_hat()