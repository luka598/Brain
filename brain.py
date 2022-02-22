from networkx.algorithms.components.strongly_connected import condensation
from visual import GraphVisualization

class neuron():
	def __init__(self, id) -> None:
		self.id = id
		self.input_neurons = []
		self.value = 0
		return

	def tick(self):
		if len(self.input_neurons) == 0:
			return self.value
		values = []
		for input_neuron in self.input_neurons:
			values.append(input_neuron.value)
		self.value = sum(values)/len(self.input_neurons)

	def no_inputs(self):
		return len(self.input_neurons) == 0

class brain():
	def __init__(self) -> None:
		self.input_neurons = []
		self.neurons = []
		self.output_neurons = []
		self.last_id = -1
		return

	def add_neuron(self, neuron_type="normal"):
		self.last_id += 1
		new_neuron = neuron(self.last_id)
		if neuron_type == "input":
			self.input_neurons.append(new_neuron)
		elif neuron_type == "normal":
			self.neurons.append(new_neuron)
		elif neuron_type == "output":
			self.output_neurons.append(new_neuron)
		return new_neuron

	def connect_neurons(self, connection):
		connection = list(connection)
		all_neurons = self.input_neurons + self.neurons + self.output_neurons
		assert connection[0] in all_neurons, "Connection[0] not a valid neuron"
		assert connection[1] in all_neurons, "Connection[1] not a valid neuron"
		assert connection[0] not in self.output_neurons, "Can't connect output neuron as input"
		assert connection[1] not in self.input_neurons, "Can't add input to input neuron"
		connection[1].input_neurons.append(connection[0])

	def tick(self):
		for neuron in self.neurons:
			neuron.tick()
		for neuron in self.output_neurons:
			neuron.tick()

	def visualise(self):
		G = GraphVisualization()
		for neuron in self.neurons:
			for input_neuron in neuron.input_neurons:
				G.add_edge((input_neuron.id, neuron.id), alpha=input_neuron.value, color="lime")
		for neuron in self.output_neurons:
			for input_neuron in neuron.input_neurons:
				G.add_edge((input_neuron.id, neuron.id), alpha=input_neuron.value, color="lime")
		for neuron in self.input_neurons:
			G.add_node(neuron.id, "orange")
		for neuron in self.neurons:
			G.add_node(neuron.id, "blue")
		for neuron in self.output_neurons:
			G.add_node(neuron.id, "green")
		G.visualize()
		return

b=brain()
inn0 = b.add_neuron("input")
inn1 = b.add_neuron("input")
nn0 = b.add_neuron("normal")
nn1 = b.add_neuron("normal")
onn = b.add_neuron("output")
b.connect_neurons((inn0, nn0))
b.connect_neurons((inn1, nn0))
b.connect_neurons((nn0, nn1))
b.connect_neurons((nn1, nn0))
b.connect_neurons((nn0, onn))

inn0.value = 1
for i in range(10):
	b.tick()
	print(onn.value)

inn1.value = 1
for i in range(10):
	b.tick()
	print(onn.value)

