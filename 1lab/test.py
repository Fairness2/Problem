from neuronweb import NeuronNetwork

nn = NeuronNetwork()
# инициализируем нейрон
nn.add_neuron("A")
#print("Жопа")
#обучаем нейрон
for i in range(1,4):
    img_file = open("learning/A%s.png" % (i), "rb")
    nn.learning(img_file, "A")
    img_file.close()

nn.add_neuron("T")
for i in range(1,4):
    img_file = open("learning/T%s.png" % (i), "rb")
    nn.learning(img_file, "T")
    img_file.close()

#проверяем на значение
print("A")
for i in range(1,7):
    img_file = open("learning/A%s.png" % (i), "rb")
    result = nn.prediction(img_file)
    img_file.close()
    print(result)

print("T")
for i in range(1,5):
    img_file = open("learning/T%s.png" % (i), "rb")
    result = nn.prediction(img_file)
    img_file.close()
    print(result)
