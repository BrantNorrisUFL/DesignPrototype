#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Prototype code for Graphene-based NEMS simulator
# Brant Norris

#Note: Uncomment the "pip install" commands if your local (client-side) installation and environment does not already have the necessary tools and packages installed


# In[2]:


#pip install qiskit


# In[3]:


#pip install QuTiP


# In[4]:


#pip install numpy


# In[5]:


#pip install ipywidgets


# In[6]:


#pip install Ipython


# In[7]:


#pip install matplotlib


# In[8]:


#pip install pylatexenc


# In[9]:


#pip install voila


# In[10]:


#pip install qiskit


# In[11]:


#pip install QuTiP


# In[12]:


#pip install numpy


# In[13]:


#pip install latex


# In[14]:


import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator
from qiskit import *
from qiskit.visualization import plot_histogram
from qiskit.tools.monitor import job_monitor
from qutip import *
import matplotlib.pyplot as plt
import ipywidgets as widgets
import IPython
from IPython.display import display, clear_output
from ipywidgets import VBox
from ipywidgets import HBox
from ipywidgets import *


# In[ ]:





# In[15]:


file = open("GrapheneQubit.png", 'rb');


# In[16]:


qubit_file = file.read();


# In[17]:


image_qubit = widgets.Image(value=qubit_file,format='png',width='300')


# In[18]:


label_qubit = widgets.Label(value='Graphene NEMS Qubit',style={'description_width':'initial'})


# In[19]:


vbox_qubit = widgets.VBox([image_qubit, label_qubit])


# In[20]:


qubit_image = widgets.Image(value = qubit_file, format='png', width='300',height='400')


# In[ ]:





# In[ ]:





# In[21]:


gate_select = widgets.Dropdown(options=[('X'),('Y'),('Z')], value='X', description='Gate type:',disabled=False)


# In[22]:


run_button = widgets.Button(description='Run Simulation',tooltip='Run',style={'description_width': 'initial'},disabled=False)


# In[23]:


initial_state = widgets.Dropdown(options=[('0', 0),('1', 1)], value=0, description='Initial state:',disabled=False)


# In[24]:


widget_output = widgets.Output()


# In[25]:


def run_sim(event):
    with widget_output:
        clear_output()
        print("Results: ")
        print(f"Initial state: {initial_state.value}")
        print(f"Gate type: {gate_select.value}")
        circuit = QuantumCircuit(1,1)
        if initial_state.value == 0:
            circuit.initialize(0)
        elif initial_state.value == 1:
            circuit.initialize(1)
        if gate_select.value == 'X':
            circuit.x(0)
        elif gate_select.value == 'Y':
            circuit.y(0)
        elif gate_select.value == 'Z':
            circuit.z(0)
        display(circuit.draw('mpl'))
        #U = Operator(circuit) 
        #display(U.data)
        meas = QuantumCircuit(1,1)
        meas.measure(0,0)
        backend = BasicAer.get_backend('qasm_simulator')
        measurement_circuit = circuit.compose(meas)
        result = backend.run(transpile(measurement_circuit,backend), shots=1000).result()
        counts = result.get_counts(circuit)
        print(counts)
        display(plot_histogram(counts))
        
      
        


# In[ ]:





# In[26]:


run_button.on_click(run_sim)


# In[27]:


vbox_sim = widgets.VBox([run_button, widget_output])


# In[28]:


title = widgets.HTML(value="<h1>Graphene-based NEMS Simulator</h1>")


# In[29]:


vbox_button = widgets.VBox([run_button, widget_output])


# In[30]:


vbox_output = widgets.VBox([title, initial_state, gate_select, vbox_button])


# In[31]:


front_end = widgets.HBox([vbox_qubit, vbox_output])


# In[32]:


display(front_end)


# In[ ]:





# In[ ]:





# In[ ]:




