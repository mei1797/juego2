import random
import textwrap
import time
import turtle 

def print_bold(msg):
    print("\033[1m"+msg+"\033[0m")

def print_linea_punteada(width=72):
    print('-'*width)

def ocupar_chozas():
    ocupantes = ['enemigo','Bulbej']
    chozas = []
    while len(chozas) < 5: 
        eleccion_aleatoria = random.choice(ocupantes)
        chozas.append(eleccion_aleatoria)
    return chozas

def mostrar_mision():
    print("los personajes son:...")
    print("1 = Freya   2 = Thor")
    jugador = int(input("elige un personaje:  "))
    if jugador == 1:
        print("Freya guia de las valkirias")
    if jugador == 2:
        print("Thor dios del trueno")
    print("\033[1m"+ "Guerra de Dioses" + "\033[0m")
    msg = ("Al inicio de los timepos los dioses Aesir y Vanir vivian en armonia,pero una Vanir"
          "llamada Bulbej.comocida por su gran poder,solia visitar a los Aeris pero estas siempre"
          "eran breves y poco agradables.Los Aesir cansado arremetieron,pero esta se alzo intacta. "
          "Este suceso produjo un gran enojo en los Vanir, puesto que uno de los suyos habia sido"
          "atacado.Para poder recompensar su falta,le propusieron un trato a los Aesir estos deberian"
          "pagra un agran multa o bien ser reconocidos como sus igules."
          "Los Aesir no queriendo compartir ninguno de sus privilegios,negaron ambas peticiones y los "
          "Vanir por lo tanto le declararon la guerra.")

    print(textwrap.fill(msg, width = 72))
    print("Para poder entrar el codigo debes adivinar")
    print(" ")
    time.sleep(0.5)
    print("Comienza a adivinar")
    print("\033[1m"+"Pista:"+"\033[0m")
    print("Procedentes de las frías regiones de Escandinavia")
    time.sleep(0.5)
    palabra = 'vikingo'
    tupalabra = ' '
    vidas = 5

    while vidas > 0:

        fallas=0
        for letra in palabra:
            if letra in tupalabra:
                print(letra,end="")
            else:
                print("-",end="")
                fallas+=1
        if fallas==0:
            print("Felicidades adivinaste la contraseña,"
                "ahora podras entrar al Asgrad")
            print("\033[1m"+"Misión:"+"\033[0m")
            print("Busca a Bulbej,ella se encuentra"
                "en una de estas casa ¡Encuentrala!")
        
            break

        tuletra=input("Introduce una letra: ")
        tupalabra+=tuletra

        if tuletra not in palabra:
            vidas-=1
            print("Equivocacion")
            print("tu tienes  " ,+vidas," vidas") 
            print("\033[1m"+"Pista:"+"\033[0m") 
            print("Tienen cuernos en sus cascos")
        tuletra=input("Introduce una letra: ")
        tupalabra+=tuletra

        if tuletra not in palabra:
            vidas-=1
            print("Equivocacion")
            print("tu tienes  " ,+vidas," vidas") 
            print("\033[1m"+"Pista:"+"\033[0m")
            print("Son pueblos guerreros")
        if vidas == 0:
            print("Perdiste!")
    else:
        print("vuelve a intentarlo")
    print("\033[1m"+"Misión:"+"\033[0m")
    print("Encuentra a Bulbej")
    print("\033[1m"+"NOTA:"+"\033[0m")
    print("¡Cuidado! Hay enemigos rondando la zona")
    print_linea_punteada()

def mostrar_salud(medidor_salud, bold):
    if bold:
        print_bold("Salud jugador:")
        print_bold("%d"%(medidor_salud['jugador']))
        print_bold("Salud Enemigo:")
        print_bold("%d"%(medidor_salud['enemigo']))
    else:
        print("Salud jugador:")
        print("%d"%(medidor_salud['jugador']))
        print("Salud Enemigo:")
        print("%d"%(medidor_salud['enemigo']))


def procesar_decision_usuario():
    msg = "\033[1m" + "Elige una choza, introduce un número entre 1 y 5: " + "\033[0m"
    decision_usuario = input("\n"+msg)
    idx = int(decision_usuario)
    return idx

def reset_medidor_salud(medidor_salud):
    medidor_salud['jugador']=40
    medidor_salud['enemigo']=30

def atacar(medidor_salud):
    lista_golpes = 4*['jugador']+6*['enemigo']
    unidad_herida = random.choice(lista_golpes)
    puntos_vida = medidor_salud[unidad_herida]
    herida = random.randint(10,15)
    medidor_salud[unidad_herida] = max(puntos_vida- herida,0)
    print("¡Ataque!")
    mostrar_salud(medidor_salud,bold=False)

def revelar_ocupantes(idx, chozas):
    msg=""
    print("Revelando los ocupantes...")
    for i in range(len(chozas)):
        ocupantes_info = "<%d:%s>"%(i+1, chozas[i])
        if i+1 == idx:
            ocupantes_info = "\033[1m" + ocupantes_info + "\033[0m"
        msg += ocupantes_info + " "
    print("\t" + msg)
    print_linea_punteada()

#En la siguiente función se establece un sistema de combate iterativo
def play_game(medidor_salud):
    chozas = ocupar_chozas()
    idx = procesar_decision_usuario()
    revelar_ocupantes(idx, chozas)

    if chozas[idx-2] != 'Bulbej':
        print_bold("Has terminado tu mision")
        print("Deberas vencer a Jörmungandr para ganar"
            "¿Eres lo suficente valiente para vencerla?"
            ", que los dioses te acompañen")
        posponer = 0.1
        #marcador 
        score = 0
        high_score = 0
        # ventana 
        wn = turtle.Screen()
        wn.title("snake")
        wn.bgcolor("black")
        wn.setup(width = 600, height = 600)
        wn.tracer(0)
        #cabeza de serpiente 
        cabeza = turtle.Turtle()
        cabeza.speed(0)
        cabeza.shape("square")
        cabeza.color("pink")
        cabeza.penup()
        cabeza.goto(0,0)
        cabeza.direction = "stop"
        #comidita 
        comidita = turtle.Turtle()
        comidita.speed(0)
        comidita.shape("circle")
        comidita.color("green")
        comidita.penup()
        comidita.goto(0,100)
        comidita.direction = "stop"
        #cuerpo
        segmentos = [] 
        # texto 
        texto = turtle.Turtle()
        texto.speed(0)
        texto.color("white")
        texto.penup()
        texto.hideturtle()
        texto.goto(0,260)
        texto.write("Score: 0         High Score: 0" , align=  "center", font = ("courier" ,24, "normal"))
        #funcioness
        def arriba():
            cabeza.direction = "Up"
        def abajo():
            cabeza.direction = "Down"
        def izquierda():
            cabeza.direction = "Left"
        def derecha():
            cabeza.direction = "Right"

        def mov():
            if cabeza.direction == "Up":
                y = cabeza.ycor()
                cabeza.sety(y + 20)
            if cabeza.direction == "Down":
                y = cabeza.ycor()
                cabeza.sety(y - 20)
            if cabeza.direction == "Left":
                x = cabeza.xcor()
                cabeza.setx(x - 20)
            if cabeza.direction == "Right":
                x = cabeza.xcor()
                cabeza.setx(x + 20) 
        #teclado 
        wn.listen()
        wn.onkey(arriba, "Up")
        wn.onkey(abajo, "Down")
        wn.onkey(izquierda, "Left")
        wn.onkey(derecha, "Right")
        while True:
            wn.update()
            if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor()  < -280:
                time.sleep(1)
                cabeza.goto(0,0)
                cabeza.direction = "stop"
                #esconder cuerpito
                for segmento in segmentos:
                    segmento.goto(90000,90000)
                #liempiar segmentos
                    segmentos.clear() 
                #resetaer marcador
                score = 0
                texto.clear()
                texto.write("Score:{}        High Score: {}".format(score, high_score), 
                align= "center", font = ("courier" ,24, "normal")) 
                
            if cabeza.distance(comidita) < 20:
                x = random.randint(-280,280)
                y = random.randint(-280,280)
                comidita.goto(x,y)

                nuevo_segmento = turtle.Turtle()
                nuevo_segmento.speed(0)
                nuevo_segmento.shape("circle")
                nuevo_segmento.color("green")
                nuevo_segmento.penup()
                segmentos.append(nuevo_segmento)

                score += 10  
            if score  > high_score:
                high_score = score
                texto.clear()
                texto.write("Score:{}        High Score: {}".format(score, high_score), 
                align=  "center", font = ("courier" ,24, "normal")) 
            if score == 60:
                texto.clear()
                texto.write("Ganaste pero no es el final...".format(texto), 
                align=  "center", font = ("courier" ,24, "normal"))
                texto.goto(0,0)
                cabeza.direction = "stop"

            

            #mover cuerpo
            totalSeg = len(segmentos)
            for index in range(totalSeg -1, 0, -1):
                x = segmentos[index -1].xcor()
                y = segmentos[index -1].ycor()
                segmentos[index].goto(x,y)
            if totalSeg  > 0:
                x = cabeza.xcor()
                y = cabeza.ycor()
                segmentos[0].goto(x,y)
            mov()
            time.sleep(posponer)

    if chozas[idx-1] != 'enemigo':
        print_bold("¡Enhorabuena! ¡Has GANADO!")
    else:
        print_bold('¡Enemigo encontrado!')
        mostrar_salud(medidor_salud, bold=True)
        continuar_ataque = True

        while continuar_ataque:
            continuar_ataque = input("...continuar con el ataque? Si(1)/No(0)")
            if continuar_ataque == 0:
                print_bold("Huyendo con el siguiente estado de salud...")
                mostrar_salud(medidor_salud, bold=True)
                print_bold("¡Game Over!")
                break

            atacar(medidor_salud)

            if medidor_salud['enemigo'] <=0:
                print_bold("¡Has derrotado a tu enemigo!")
                break
            if medidor_salud['jugador'] <=0:
                print_bold("Has muerto ...")
                break

#Funcion para hacer funcionar el programa principal que queremos ejecutar
def run_application():
    seguir_jugando = 1
    medidor_salud = {}
    reset_medidor_salud(medidor_salud)
    mostrar_mision()

    while seguir_jugando == 1:
        reset_medidor_salud(medidor_salud)
        play_game(medidor_salud)
        seguir_jugando = input("¿Quieres jugar de nuevo? Si(1)/No(0):")

if __name__ == '__main__':
    run_application()