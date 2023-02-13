import numpy as np
import random
import math

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

class UnitV1_NN:
    def __init__(self):
        self.weights_input = [[random.uniform(-1, 1) for i in range(23)] for i in range(23)]
        self.weights_hidden = [[random.uniform(-1, 1) for i in range(23)] for i in range(32)]
        self.weights_output = [[random.uniform(-1, 1) for i in range(32)] for i in range(3)]
        ### [[random for i in range(OUTPUTS LAST LAYER)] for i in range(NEURONS AT LAYERS)]

    def think(self, posx, posy, oldangle, oscilator, closests, border_top, border_down, border_left, border_right, oscilator1, oscilator2, score):
        ### INPUT LAYER

        input_layer_weights = []

        #print(posx, posy, oldangle, oscilator, [i for i in closests])

        for i in self.weights_input:
            input_layer_weights.append([
                posx * i[0],
                posy * i[1],
                oldangle * i[2],
                oscilator * i[3],
                closests[0][0] * i[4],  # closest cell #1
                closests[0][1] * i[5],
                closests[0][2] * i[6],
                closests[1][0] * i[7],  # closest cell #2
                closests[1][1] * i[8],
                closests[1][2] * i[9],
                closests[2][0] * i[10], # closest cell #3
                closests[2][1] * i[11],
                closests[2][2] * i[12],
                closests[3][0] * i[13], # closest cell #4
                closests[3][1] * i[14],
                closests[3][2] * i[15],
                border_top * i[16],
                border_down * i[17],
                border_left * i[18],
                border_right * i [19],
                oscilator1 * i[20],
                oscilator2 * i[21],
                score * i[22],
            ])


        input_layer_sums = []
        for i in input_layer_weights:
            input_layer_sums.append(sum(i)) # aqui se podria aplicar una funcion de activacion

        #print(input_layer_sums)

        ### HIDDEN LAYER
        hidden_layer_weights = []

        for i in self.weights_hidden:
            result = []
            for j, z in zip(input_layer_sums, i):       ### for input neuron sum * weight correspondiente
                result.append(j * z)

            hidden_layer_weights.append(result)

        hidden_layer_sums = []

        for i in hidden_layer_weights:
            hidden_layer_sums.append(sum(i)) # aqui se podria aplicar una funcion de activacion

        #print(hidden_layer_sums)
        #print(len(hidden_layer_sums))
        #print()

        ### HIDDEN LAYER

        output_layer_weights = []

        for i in self.weights_output:
            result = []
            for j, z in zip(hidden_layer_sums, i):
                result.append(j * z)

            output_layer_weights.append(result)

        output_layer_sums = []

        cont = 0
        for i in output_layer_weights:
            if cont == 0:
                output_layer_sums.append(sigmoid(sum(i))) # aqui se utiliza la funcion de activacion tanh
            elif cont == 1:
                output_layer_sums.append(np.tanh(sum(i)))
            elif cont == 2:
                output_layer_sums.append(sigmoid(sum(i)))
            cont += 1
       #print(output_layer_sums)

        return output_layer_sums




#t = Unit_NN()
#for i in t.weights_input:
#    print(i)

#t.think(1, 2, 3, 4)